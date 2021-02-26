#!/usr/bin/python3

import argparse
import os
import time
from scapy.all import *

def main(qty, spd, nic, r):
    try:
        ## Timestamps and frame loading
        fLoad = time.time()
        frameStream = rdpcap('testflow.pcap')
        fStop = time.time()

        ## Lazy stopwatch
        timeStart = time.time()

        ## Fire teh missiles ~~~~~> Need to study byt3bl33d3r techniques for gofasters (https://byt3bl33d3r.github.io/mad-max-scapy-improving-scapys-packet-sending-performance.html)
        sendp(frameStream[0:qty], iface = nic, inter = spd, verbose = 0)

        ## Received poor usage stats on both sendpfast and tcpreplay from the console -- not recommended for injection testing
        #results = sendpfast(frameStream[0:10], pps = 1000, file_cache = True, iface = 'wlan0mon')

        ## How fast
        oSpeed = time.time() - timeStart

        a = '~ Loaded in {0}'.format(fStop - fLoad)
        b = '~ Ran in {0}'.format(oSpeed)
        print(a)
        print(b)
        with open('flowTester.log', 'w') as oFile:
                  oFile.write(a + '\n' + b + '\n')

        if r is not None:
            return a, b, frameStream
        else:
            return a, b
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
        a, b, pList = main(qty, spd, nic, args.r)
    else:
        a, b = main(qty, spd, nic, args.r)

    ## closeout
    print(a)
    print(b + '\n')
