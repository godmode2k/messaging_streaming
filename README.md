# Messaging and Streaming Test


Summary
----------
>


Environment
----------
> build all and tested on GNU/Linux

    GNU/Linux: Ubuntu 20.04_x64 LTS
    Python: v3.8.5
    Go: go1.16.2 linux/amd64
    Docker, Docker-compose: latest
    Kafka: kafka-python, docker wurstmeister/kafka, wurstmeister/zookeeper
    Spark: apache/zeppelin
    Redis: docker redis(sentinel)


Kafka
----------
```sh
$ pip3 install kafka-python

$ git clone https://github.com/wurstmeister/kafka-docker.git
$ cd kafka-docker
$ sudo docker-compose up -d
```


Spark
----------
```sh
$ sudo docker pull apache/zeppelin
```


Redis, Redis-Sentinel
----------
```sh
$ sudo docker pull redis
$ git clone https://github.com/vhf/redis-sentinel-docker-example.git
$ cd redis-sentinel-docker-example
$ sudo docker-compose up -d
```


