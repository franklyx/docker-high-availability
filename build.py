#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/12/14 9:04 PM 
# @Author : Lyx 
# @Site : 自动化创建高可用集群环境脚本
# @File : build.py

# 提供命令安装docker以及docker_compose

# build_file > docker_file > docker_compose > docker
# 脚本分成自动创建和自定义创建两种模式

MYSQL_DOCKER_NUM = 4
REDIS_DOCKER_NUM = 3
WEB_DOCKER_NUM = 4
BACKUP_DOCKER_NUM = 4
