#!/usr/bin/env python
 
import random
import json
import docker
import sys
 
hosts = ["docker-nginx1", "docker-nginx2"]
types = ["gauge-cpu0"]
 
for h in hosts:
    for t in types:
        r = random.randrange(0, 100, 1)
        print("PUTVAL %s/%s/%s N:%s" % (h, 'docker-cpu', t, r))


cli=docker.Client(base_url='unix://var/run/docker.sock')
stats=cli.stats(sys.argv[1])
print json.dumps(json.loads(next(stats).rstrip('\n')),indent=4)
