#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by xiaoqin00 on 2017/7/17

#ssh 僵尸客户端

import optparse
from pexpect import pxssh

class Client:
    def __init__(self,host,user,password):
        self.host=host
        self.user=user
        self.password=password
        self.session=self.connect()
    def connect(self):
        try:
            s=pxssh.pxssh()
            s.login(self.host,self.user,self.password)
            return s
        except Exception,e:
            print e
            print '[-]Error Connecting'
    def send_command(self,cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

def botnetCommand(command):
    for client in botNet:
        output=client.send_command(command)
        print '[*]output from '+client.host
        print '[+]'+output+'\n'
def addClient(host,user,password):
    client=Client(host,user,password)
    botNet.append(client)
botNet=[]
addClient('10.10.10.10','root','toor')
addClient('10.10.10.20','root','toor')
botnetCommand('uname -v')
botnetCommand('cat /etc/issue')