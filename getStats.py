#!/usr/bin/python3

import datetime
from scapy.all import *

## Obtain frame times
fDict = {}
fCount = 1
rdr = PcapReader('mpTraffic.pcap')
for r in rdr:
    fDict.update({fCount: float(r.time)})
    fCount += 1

## Notate log
with open('flowTester.log') as iFile:
    fLog = iFile.read().splitlines()

## Time from start to finish
span = len(fDict)
eTime = fDict.get(span)
eOut = datetime.fromtimestamp(int(eTime)).strftime("%Y-%m-%d %H:%M")
sTime = fDict.get(1)
sOut = datetime.fromtimestamp(int(sTime)).strftime("%Y-%m-%d %H:%M")
tTime = eTime - sTime


## qty show
print('\npcap length:')
print(span)
## Time compares
print('\npcap timing:')
print(sOut)
print(eOut)

## tX statistics
print ('\ntx statistics:')
print(fLog[2])

print('\nrx statistics:')
print('{0}\n'.format(tTime))

## Delta
ff = float(fLog[2])
f = abs(ff)
tt = float(tTime)
t = abs(tt)
pMax = max(f, t)
if pMax == f:
    dt = f - t
    val = 'tx higher'
else:
    dt = t - f
    val = 'rx higher'
print('tx -v- rx:')
print('{0} - {1}\n'.format(str(dt), val))

print('tx interval:')
print(fLog[3])

print('\nrx average/sec:')
rAvg = tTime / span
print(str(rAvg) + '\n')

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
print('txInt -v- rxAvg:')
print('{0} - {1}\n'.format(str(dt), rVal))
