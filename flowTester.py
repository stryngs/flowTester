#!/usr/bin/python3

import argparse
import os
import time
from timeit import default_timer as timer
from scapy.all import *
from scapy.sendrecv import __gen_send as gs

def main(qty, spd, nic, r):
    try:
        ## Timestamps and frame loading
        
        
        """
        Add a PcapReader loop to a [] and see the delta
        """
        
        fStart = time.time()
        frameStream = rdpcap('testflow.pcap', count = qty)
        fStop = time.time()

        ## Lazy stopwatch
        timeStart = time.time()

        ## Fire teh missiles
        with open('flowstats.log', 'w') as oFile:
            s = conf.L2socket(iface = nic)
            for frame in frameStream:
                sTime = time.time()
                gs(s, frame, verbose = False)
                eTime = time.time()
                tSpent = eTime - sTime
                tSent = sTime + ((eTime - sTime) / 2)
                oFile.write('{0} - {1} - {2} - {3}\n'.format(sTime, eTime, tSpent, tSent))
                time.sleep(spd)
        
        #sendp(frameStream[0:qty], iface = nic, inter = spd, verbose = 0)

        ## Received poor usage stats on both sendpfast and tcpreplay from the console -- not recommended for injection testing
        #results = sendpfast(frameStream[0:10], pps = 1000, file_cache = True, iface = 'wlan0mon')

        ## How fast
        oSpeed = time.time() - timeStart

        out = '~ {0} packets sent\n~ Packets loaded in {1}\n~ Ran in {2}\n'.format(qty, fStop - fStart, oSpeed)
        l =  '{0}\n{1}\n{2}\n{3}\n'.format(qty, fStop - fStart, oSpeed, spd)
        with open('flowtester.log', 'w') as oFile:
                  oFile.write(l)

        if r is not None:
            return out, frameStream
        else:
            return out
    except Exception as E:
        print(E)

if __name__ == '__main__':

    ## ARGUMENT PARSING
    parser = argparse.ArgumentParser(description = 'flowTester - Metrics for the unmeasured')
    parser.add_argument('-i',
                        help = 'Interface to inject on')
    parser.add_argument('-q',
                        help = 'Quantity of packets from testflow.pcap to run - Between 1 - 10000 - defaults to 10000')
    parser.add_argument('-r',
                        help = 'Return the loaded packets for further study within an IDE',
                        action = 'store_true')
    parser.add_argument('-s',
                        help = 'Time (in s) between two packets (default .001) - Results not valid if set to 0; must have a speed')

    ## Launch
    args = parser.parse_args()
    if args.q is not None:
        qty = int(args.q)
    else:
        qty = 10000
    if args.s is not None:
        spd = float(args.s)
    else:
        spd = .001
    if args.i is None:
        nic = 'wlan0mon'

    ## stdout and such
    print('\nflowTester ~ Metrics for the unmeasured\n\n')
    print('-i (interface)                == {0}'.format(nic))
    print('-q (quantity)                 == {0}'.format(qty))
    print('-r (return pcap as an object) == {0}'.format(args.r))
    print('-s (speed between packets     == {0}\n'.format(spd))
    print('Running ~ BE PATIENT ~ lower quantity for less packets to transmit if desired\n')

    ## Run
    if args.r is not None:
        out, pList = main(qty, spd, nic, args.r)
    else:
        out = main(qty, spd, nic, args.r)

    ## closeout
    print(out)
