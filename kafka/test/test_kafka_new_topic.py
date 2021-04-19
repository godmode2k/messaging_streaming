#!/usr/bin/python3
# -*- coding: utf-8 -*-



# -----------------------------------------------------------------
# Purpose: Kafka test
# Author: Ho-Jung Kim (godmode2k@hotmail.com)
# Filename: test_kafka_new_topic.py
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



def main():
    topic = "test1_topic1"
    data = { "test1_topic": "test1_topic_data" }
    data2 = [ "test1", "test2", "test3" ]


    # New Topic
    new_topic = CNewTopic( topic )


    # Consumer
    #consumer = CConsumer( topic )
    #consumer.test_fetch( topic )


    # Producer
    #producer = CProducer( topic )
    #producer.test( topic, data )



if __name__ == "__main__":
    main()
