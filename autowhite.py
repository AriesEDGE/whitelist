import config
import logs
import os


def init():
    os.system("iptables -F")
    os.system("iptables -I INPUT -p TCP --dport "+ str(config.port) +" -j DROP")
    os.system("iptables -I INPUT -p UDP --dport "+ str(config.port) +" -j DROP")


def add(ip):
        os.system("iptables -I INPUT -s "+ip+" -p TCP --dport "+ str(config.port) +" -j ACCEPT")
        os.system("iptables -I INPUT -s "+ip+" -p UDP --dport "+ str(config.port) +" -j ACCEPT")
        print(ip+"已添加到白名单")
        logs.add(ip)