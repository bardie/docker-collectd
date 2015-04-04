#!/usr/bin/env python
 
import random
import json
import docker
import sys

cli=docker.Client(base_url='unix://var/run/docker.sock')
 
types = ["gauge-cpu0"]
types = {"network": NetworkStats,
         "blkio_stats": BlkioStats,
         "cpu_stats": CpuStats,
         "memory_stats": MemoryStats}
 
for h in cli.containers():
    if not h["Status"].startswith("Up"):
        continue
    stats = json.loads(cli.stats(h["Id"]).next())
    for k, v in stats.items():
        if types.get(k):
            r = random.randrange(0, 100, 1)
            print("PUTVAL %s/%s/%s N:%s" % (h, 'docker-cpu', t, r))

