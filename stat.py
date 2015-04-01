#!/usr/bin/env python

import json
import docker
import sys

cli=docker.Client(base_url='unix://var/run/docker.sock')
stats=cli.stats(sys.argv[1])
print json.dumps(json.loads(next(stats).rstrip('\n')),indent=4)
