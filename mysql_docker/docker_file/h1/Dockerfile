FROM haproxy

ENV MYSQL_ROOT_PASSWORD=abc123123 \
    CLUSTER_NAME=PXC \
    XTRABACKUP_PASSWORD=abc123123
COPY ./haproxy.cfg /usr/local/etc/haproxy