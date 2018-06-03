#!/bin/bash

yum install tomcat8 -y
service tomcat8 start
echo "Enter the port Number you want tomcat to run on"
read PORTi
/sbin/iptables -t nat -I PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port $PORT
/sbin/service iptables save
/etc/init.d/iptables restart
