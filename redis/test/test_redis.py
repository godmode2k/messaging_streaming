#!/usr/bin/python3
# -*- coding: utf-8 -*-



# -----------------------------------------------------------------
# Purpose: Redis test
# Author: Ho-Jung Kim (godmode2k@hotmail.com)
# Filename: test_redis.py
# Date: Since April 13, 2021
#
#
# Reference:
# - https://github.com/andymccurdy/redis-py
# - https://github.com/andymccurdy/redis-py/blob/master/redis/sentinel.py
#
# $ pip3 install redis
# $ pip3 install hiredis
#
#
# License:
#
# *
# * Copyright (C) 2021 Ho-Jung Kim (godmode2k@hotmail.com)
# *
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# *      http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
# * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# * See the License for the specific language governing permissions and
# * limitations under the License.
# *
# -----------------------------------------------------------------
# Note:
# -----------------------------------------------------------------
#
# -----------------------------------------------------------------



import json

# Redis [
import redis

# Sentinel
from redis.sentinel import Sentinel

# Hiredis
#import hiredis
#DefaultParser = HiredisParser
# Redis ]



def main():
    rd = redis.Redis( host = 'localhost', port = 6379, db = 0, password = None, socket_timeout = None )
    #rd = redis.StrictRedis( host = 'localhost', port = 6379, db = 0, password = None, socket_timeout = None )


    key = "test1"
    value = "test1_val"
    rd.set( key, value )
    result = rd.get( key )
    print( "result =\n" )
    print( f'{ key } = { result }\n' )


    # mset
    data = { "test2": "test2_val", "test3": "test3_val", "test4": "test4_val" }
    rd.mset( data )
    result = rd.get( "test2" )
    print( "result =\n" )
    print( f'{ key } = { result }\n' )


    # value: JSON data
    key = "test1_sub"
    value = { "test1_sub1": "test1_sub1_value", "test1_sub1": "test1_sub1_value", "test1_sub1": "test1_sub1_value" }
    value = json.dumps( value, ensure_ascii = False).encode( "utf-8" )
    rd.set( key, value )
    result = rd.get( key )
    result = result.decode( "utf-8" )
    result = dict( json.loads(result) )
    print( "result =\n" )
    print( f'{ key } = { result }\n' )


    rd.close()



    # Sentinel
    sentinel = Sentinel( [('localhost', 26379)], socket_timeout = 0.1 )
    master = sentinel.master_for( 'my_redis_master', socket_timeout = 0.1 )
    key = "master_test1"
    value = "master_test1_val"
    master.set( key, value )
    result = master.get( key )
    print( "result (master) =\n" )
    print( f'{ key } = { result }\n' )
    slave = sentinel.slave_for( 'my_redis_master', socket_timeout = 0.1 )
    result = slave.get( key )
    print( "result (slave) =\n" )
    print( f'{ key } = { result }\n' )

    sentinel.close()



    # Hiredis
    #




if __name__ == "__main__":
    main()
