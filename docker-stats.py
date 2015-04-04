#!/usr/bin/env python
 
import random
 
hosts = ["docker-nginx1", "docker-nginx2"]
types = ["gauge-cpu0"]
 
for h in hosts:
    for t in types:
        r = random.randrange(0, 100, 1)
        print("PUTVAL %s/%s/%s N:%s" % (h, 'docker-cpu', t, r))
