### 自动化搭建高可用的docker生产环境
* 为什么编写这个脚本
  >  实现脚本快速搭建一个高可用高负载的生产环境，简化运维部署脚本

* 集群环境介绍
  > 1. mysql_docker : 基于PXC方案的mysql集群部署方案
  > 2. redis_docker : 基于redisCluster的集群部署方案
  > 3. web_docker   : 创建nginx + vue的集群部署方案
  > 4. backup_docker: 创建python的集群化部署方案
  
* 部署方案整体架构
> <img width=”300px” src=”tupiandizhi” />

* 网段划分
> * mysql  集群网段 172.18.0.0/16 -> 192.168.99.150(虚拟成一个主机网口)
> * redis  集群网段 172.19.0.0/16 -> 192.168.100.150(虚拟成一个主机网口)
> * backup 集群网段 localhost:6501(外部能够访问直接映射到宿主机端口)
> * web    集群网段 localhost:6001(外部能够访问直接映射到宿主机端口)

* 脚本使用方法
    1. 支持直接输入主机IP，智能的将各个IP分配到特定的系统上