#!/bin/bash

# 创建network
network1=$(docker network create --subnet=172.18.0.0/24 net_mysql)
network2=$(docker network create --subnet=172.19.0.0/24 net_redis)
eval "set network result ${network1},${network2}"

# 创建volume
volume1=$(docker volume create --name volume_mysql)
eval "set volume result ${volume1}"