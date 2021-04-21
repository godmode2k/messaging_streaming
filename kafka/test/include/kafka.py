#!/usr/bin/python3
# -*- coding: utf-8 -*-



# -----------------------------------------------------------------
# Purpose: Kafka test
# Author: Ho-Jung Kim (godmode2k@hotmail.com)
# Filename: kafka.py
# Date: Since April 14, 2021
#
#
# Reference:
# - https://kafka-python.readthedocs.io/en/master/usage.html
# - https://hellbreak.medium.com/how-a-kafka-consumer-can-start-reading-messages-from-a-different-offset-and-get-back-to-the-start-eee28dc19428
# - https://stackoverflow.com/questions/26021541/how-to-programmatically-create-a-topic-in-apache-kafka-using-python/55524560
#
# $ pip3 install kafka-python
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



from kafka import KafkaConsumer, KafkaProducer, TopicPartition
from kafka.admin import KafkaAdminClient, NewTopic
import json
import datetime



#g_KAFKA_HOST = "localhost:9092"
g_KAFKA_HOST = "192.168.0.6:9092"



class CNewTopic:
    def __init__(self, topic):
        admin_client = KafkaAdminClient(
            bootstrap_servers = g_KAFKA_HOST,
            client_id = "test"
        )

        topic_list = []
        topic_list.append( NewTopic(name = topic, num_partitions = 1, replication_factor = 1) )
        admin_client.create_topics( new_topics = topic_list, validate_only = False )



class CConsumer:
    def __init__(self, topic):
        self.topic = topic
        self.partition = 0
        self.offset = 0

        #self.consumer = self.create()
        #self.topic_partition = TopicPartition( self.topic, self.partition )

    def create(self):
        consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers = [g_KAFKA_HOST],
            auto_offset_reset = "earliest",
            enable_auto_commit = True,
            consumer_timeout_ms = 1000
        )

        #consumer.assign( [self.topic_partition] )
        #consumer.seek( self.topic_partition, self.offset )
        ##consumer.commit()

        # beginning at
        #consumer.seek_to_beginning( self.topic_partition )
        # or
        # recent offset
        #consumer.seek_to_end( self.topic_partition )

        return consumer

    def close(self):
        self.consumer.close()

    def fetch(self):
        count = 0
        for message in self.consumer:
            value = json.loads( message.value.decode( "utf-8") )
            #print( f'message = { message }' )
            print( f'[{count}] message = { value }' )

            #self.consumer.commitSync()
            count += 1

    def datetime_add_days(self, start_datetime, days):
        start_datetime_str = start_datetime.strftime( "%Y-%m-%d" )
        end_datetime = datetime.datetime.strptime(start_datetime_str, "%Y-%m-%d") + datetime.timedelta( days = days )
        print( f'start_datetime = { start_datetime }, timestamp = { start_datetime.timestamp() }' )
        print( f'end_datetime = { end_datetime }, timestamp = { end_datetime.timestamp() }' )

        return end_datetime

    def fetch_datetime(self, topic, start_datetime = None, end_datetime = None, days = None):
        if end_datetime == None:
            end_datetime = self.datetime_add_days( start_datetime, days )

        consumer = KafkaConsumer(
            topic,
            bootstrap_servers = [g_KAFKA_HOST],
            auto_offset_reset = "earliest",
            enable_auto_commit = True,
            consumer_timeout_ms = 1000
        )
        consumer.poll( 0 )

        tp = TopicPartition( topic, 0 )

        if start_datetime != None:
            if end_datetime == None:
                end_datetime = self.datetime_add_days( start_datetime, days )

            _start = consumer.offsets_for_times( {tp: start_datetime.timestamp() * 1000} ) # timestamp: ms
            _end = consumer.offsets_for_times( {tp: end_datetime.timestamp() * 1000} ) # timestamp: ms

            consumer.seek( tp, _start[tp].offset )


        print( f'datetime = { start_datetime } ~ { end_datetime }' )

        count = 0
        for message in consumer:
            if start_datetime != None:
                if _end != None and _end[tp] != None and message.offsets >= _end[tp].offset:
                    break;

            value = json.loads( message.value.decode( "utf-8") )
            #print( f'message = { message }' )
            print( f'[{count}] message ({message.timestamp}, {message.offset} = { value }' )
            count += 1

        if start_datetime != None:
            consumer.close()

    def test_fetch(self, topic):
        print( "CConsumer::test_test()" )
        print( f'topic = { topic }' )

        consumer = KafkaConsumer(
            topic,
            bootstrap_servers = [g_KAFKA_HOST],
            auto_offset_reset = "earliest",
            enable_auto_commit = True,
            consumer_timeout_ms = 1000
        )

        count = 0
        for message in consumer:
            value = json.loads( message.value.decode( "utf-8") )
            #print( f'message = { message }' )
            print( f'[{count}] message ({message.timestamp}, {message.offset} = { value }' )
            count += 1

        consumer.close()



class CProducer:
    def __init__(self, topic):
        self.topic = topic
        #self.producer = self.create()

    def create(self):
        producer = KafkaProducer(
            bootstrap_servers = [g_KAFKA_HOST]
        )

        return producer

    def close(self):
        self.producer.close()

    def send(self, data):
        self.send( self.topic, data )

    def send(self, topic, data):
        self.producer.send( topic, value = json.dumps(data).encode("utf-8") )
        self.producer.flush()

    def test(self, topic, data):
        print( "CProducer::test()" )
        print( f'topic = { topic }' )
        print( f'data = { data }' )

        producer = KafkaProducer(
            bootstrap_servers = [g_KAFKA_HOST]
        )

        producer.send( topic, value = json.dumps(data).encode("utf-8") )
        producer.flush()




