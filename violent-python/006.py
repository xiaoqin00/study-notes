#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by xiaoqin00 on 2017/7/15

#端口及服务扫描，改进多线程
import optparse
from socket import *
from threading import *
screenLock=Semaphore(value=1)
def connScan(tgtHost,tgtPort):
    print 'test'
    try:
        connSkt=socket(AF_INET,SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send('voilentPython\r\n')
        results=connSkt.recv(100)
        screenLock.acquire()
        print '[+]%d /tcp open'%tgtPort
        print '[+]'+str(results)
    except:
        screenLock.acquire()
        print '[-]%d /tcp closed'%tgtPort
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtHost,tgtPorts):
    try:
        tgtIP=gethostbyname(tgtHost)
    except:
        print "[-]cannot resolve '%s':unknown host"%tgtHost
        return
    try:
        tgtName=gethostbyaddr(tgtIP)
        print '\n [+]scan results for :'+tgtName[0]
    except:
        print '\n[+]scan results for :'+tgtIP
    setdefaulttimeout(1)
    for tgtport in tgtPorts:
        t=Thread(target=connScan,args=(tgtHost,int(tgtport)))
        t.start()

def main():
    parser=optparse.OptionParser("usage %prog -H <target Host> -p <target port>")
    parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
    parser.add_option('-p',dest='tgtPort',type='string',help='specify target port[s]')
    (options,args)=parser.parse_args()
    tgtHost=options.tgtHost
    tgtPorts=str(options.tgtPort).split(',')
    if (tgtHost==None)|(tgtPorts[0]==None):
        print parser.usage
        exit(0)
    portScan(tgtHost,tgtPorts)

if __name__ == '__main__':
    main()