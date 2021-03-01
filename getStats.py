#!/usr/bin/python3

import datetime
from scapy.all import *

# RX work
## Obtain frame times from pcap
fDict = {}
fCount = 1
rdr = PcapReader('mpTraffic.pcap')
with open('rx.stats', 'w') as oFile:
    for r in rdr:
        fDict.update({fCount: float(r.time)})
        oFile.write('{0} - {1}\n'.format(fCount, float(r.time)))
        fCount += 1

## Time from start to finish
span = len(fDict)
eTime = fDict.get(span)
sTime = fDict.get(1)
eOut = datetime.fromtimestamp(int(eTime)).strftime("%Y-%m-%d %H:%M")
sOut = datetime.fromtimestamp(int(sTime)).strftime("%Y-%m-%d %H:%M")
tTime = eTime - sTime

## Avg
rAvg = tTime / span


# TX work
## Notate log
with open('flowtester.log') as iFile:
    fLog = iFile.read().splitlines()


# Compare work
## Delta
ff = float(fLog[2])
f = abs(ff)
tt = float(tTime)
t = abs(tt)
pMax = max(f, t)
if pMax == f:
    dt = f - t
    val = 'tx higher value'
else:
    dt = t - f
    val = 'rx higher value'

## tx interval v rxAvg
spd = float(fLog[3])
aSpd = abs(spd)
rSpd = abs(rAvg)
rMax = max(aSpd, rSpd)
if rMax == aSpd:
    dt = aSpd - rSpd
    rVal = 'tx higher'
else:
    dt = rSpd - aSpd
    rVal = 'rx higher'

## tx rough v rxAvg
rts = float(fLog[2]) / float(fLog[0])
aRts = abs(rts)
rMax = max(aRts, rSpd)
if rMax == aRts:
    adt = aRts - rSpd
    arVal = 'tx higher value'
else:
    adt = rSpd - aRts
    arVal = 'rx higher value'

# Output
## qty show
print('\n~~~ RX Statistics ~~~')
print('pcap length:')
print(' {0}'.format(span))

## time
print('\nTotal time to receive:')
print(' {0}'.format(tTime))

## avg
print('\nrx average/sec:')
print(' {0}'.format(str(rAvg)))
print ('~~~~~~~~~~~~~~~~~~~~~~\n')

## tx statistics
print('~~~ TX Statistics ~~~')
print('Quantity sent:')
print(' {0}'.format(fLog[0]))
print ('\nTotal time to send:')
print(' {0}\n'.format(fLog[2]))
print('Send interval:')
print(' {0}\n'.format(fLog[3]))
print('Average time per send:')
print(' {0}'.format(rts))
print ('~~~~~~~~~~~~~~~~~~~~~~\n')

## compares
print('~~~ Comparisons ~~~')
print('tx speed -v- rx speed:')
print(' {0}\n {1}\n'.format(str(dt), val))

print('tx interval -v- rx avg:')
print(' {0}\n {1}\n'.format(str(dt), rVal))

print('tx avg -v- rx avg:')
print(' {0}\n {1}'.format(str(adt), arVal))
print ('~~~~~~~~~~~~~~~~~~~~~~\n')

