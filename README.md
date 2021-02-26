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
In order to make this a universal benchmark technique, examples are needed.  To kickstart the concept, [frameTracer](https://github.com/stryngs/802Eleven/blob/master/frameTracer.py "frameTracer") has been included in this repo.
```
frameTracer.py -i wlan1mon -x aa:bb:cc:dd:ee:ff -y ae:b5:87:b7:9a:09 -v
```

Running the above and locked onto the channel in question; run frameTracer.  Switch back and forth between sender and sniffer.  When receiver is complete; crtl + c frameTracer:
```
^C
 [!] Saving 8508 frames --> mpTraffic.pcap
```

When frameTracer finishes the pcap, compare away.  As this project rolls forward, those concepts will be discussed
