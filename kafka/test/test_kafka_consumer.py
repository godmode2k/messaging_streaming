#!/usr/bin/python3
# -*- coding: utf-8 -*-



# -----------------------------------------------------------------
# Purpose: Kafka test
# Author: Ho-Jung Kim (godmode2k@hotmail.com)
# Filename: test_kafka_consumer.py
# Date: Since April 14, 2021
#
#
# Reference:
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



from include.kafka import *
import datetime



def main():
    topic = "test1_topic"
    data = { "test1_topic": "test1_topic_data" }
    data2 = [ "test1", "test2", "test3" ]


    # New Topic
    #new_topic = CNewTopic( topic )
    #print()


    # Consumer
    consumer = CConsumer( topic )
    consumer.test_fetch( topic )
    print()

    #start_datetime = datetime.datetime( 2021, 1, 1, 0, 0, 0 )
    start_datetime = datetime.datetime.today().replace(hour = 0, minute = 0, second = 0, microsecond = 0)
    days = 1
    consumer.datetime_add_days( start_datetime, days )
    print()

    start_datetime = datetime.datetime( 2021, 4, 16, 0, 0, 0 )
    end_datetime = datetime.datetime( 2021, 4, 17, 0, 0, 0 )
    days = 1
    #consumer.fetch_datetime( topic, start_datetime, end_datetime, None )
    #consumer.fetch_datetime( topic, start_datetime, None, days )
    print()


    # Producer
    #producer = CProducer( topic )
    #producer.test( topic, data )
    #print()



if __name__ == "__main__":
    main()
