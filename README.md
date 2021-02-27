# General concept
There are a ton of sniffing programs in the wild.  They all do neat and interesting things.  Some are broad and some very narrow in their purpose.

flowTester has been built with the concept of envisioning what to measure.

What works in a given situation may not work fast enough in other situations.  When it comes to sniffing a frame or packet, so many variables are in play that it can be hard at times to pick out what code is really faster in that sense.

Sometimes your driver may never even see the frame.

flowTester takes that into consideration and helps you to score it.

Within testflow.pcap you will find only two MAC addresses:
* BSSID : aa:bb:cc:dd:ee:ff
* STA   : ae:b5:87:b7:9a:09

# Expected output
flowTester.py is used by a separate machine and not the machine you are benchmarking on.

```
flowTester ~ Metrics for the unmeasured


-i (interface)                == wlan0mon
-q (quantity)                 == 10
-r (return pcap as an object) == False
-s (speed between packets     == 0.001

Running ~ BE PATIENT ~ lower quantity for less packets to transmit if desired

~ 1000 packets sent
~ Packets loaded in 6.501736402511597
~ Ran in 10.78224492073059
```

# Scoring a metric
In order to make this a universal benchmark technique, examples are needed.  To kickstart the concept, [frameTracer](https://github.com/stryngs/802Eleven/blob/master/frameTracer.py "frameTracer") has been included in this repo.  Where QTY is the value set in -q for flowTester
```
frameTracer.py -i wlan1mon -x aa:bb:cc:dd:ee:ff -y ae:b5:87:b7:9a:09 -v -c QTY
```

When frameTracer finishes the pcap, copy the pcap from the rx node to the tx node and then:
```
python3 ./getStats.py
```

Resultant output should look as such:
```
pcap length:
1000

pcap timing:
2021-02-27 03:24
2021-02-27 03:25

tx statistics:
11.591093301773071

rx statistics:
9.51879096031189

tx -v- rx:
2.0723023414611816 - tx higher

tx interval:
0.001

rx average/sec:
0.00951879096031189

txInt -v- rxAvg:
0.00851879096031189 - rx higher
```

