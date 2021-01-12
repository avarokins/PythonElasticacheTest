from __future__ import print_function
import time
import uuid
import sys
import socket
from pymemcache.client.hash import HashClient
from elasticache_pyclient import MemcacheClient

# ElastiCache setup
mc = MemcacheClient('clusterforlambdatest.xstzul.cfg.use1.cache.amazonaws.com:11211')


'''
Adds a key to a memcached client hosted by ElastiCache, then fetches the same entry
'''
def lambda_handler(event, context):

  #Put the UUID to the cache.
  mc.set('foo', 'bar')

  #Get item (UUID) from the cache.
  uuid_obtained = mc.get('foo')

  if uuid_obtained == 'bar':
    # this print should go to the CloudWatch Logs and Lambda console.
    print ('Success: Fetched value ' + uuid_obtained + ' from memcached.')
  else:
    raise Exception('Value is not the same as we put :(')

  return 'Fetched value from memcache: ' + uuid_obtained
