#!/usr/bin/env python
# -*- coding:utf8 -*-
# coding=utf-8
# coding=gbk

import os
import time
import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

def get_ip_dir(list):
    list01 = []
    time01 = time.strftime('%Y%m%d', time.localtime())[2:]
    for dir in list:
        # dir01 = dir.split('\\')[-1]
        dir01 = dir.split('/')[-1]
        dir02 = dir01.split('.')
        if len(dir02) == 4:
            list01.append(dir)
        elif dir01 == time01:
            list01.append(dir)
    return list01

def get_dir_file(path):
    list = []
    for cur_path, cur_dirs, cur_files in os.walk(path):
        for dir in cur_dirs:
            list.append(os.path.join(cur_path, dir))

    for cur_path, cur_dirs, cur_files in os.walk(path):
        for file in cur_files:
            list.append(os.path.join(cur_path, file))
    return list

def file_path(path):
    list = []
    for cur_path, cur_dirs, cur_files in os.walk(path):
        for file in cur_files:
            list.append(os.path.join(cur_path, file))
    return list

def folder_path(path): 
    list = []
    for cur_path, cur_dirs, cur_files in os.walk(path):
        for dir in cur_dirs:
            list.append(os.path.join(cur_path, dir))
    
    return get_ip_dir(list)

def cunchu_rizhi(jilu):
    path = os.path.split(os.path.realpath(__file__))[0] 
    lists = file_path(path)
    
    if path + '/rizhi.txt' not in lists:
        with open(path+'/rizhi.txt', 'w+t', encoding='Utf-8') as f:
            f.write(jilu)
        f.close()
    else:
        with open(path+'/rizhi.txt', 'a+t', encoding='Utf-8') as f:
            f.write(jilu)
        f.close()

def backup_excute(dirname1,dirname2): 
    os.system('xcopy %s %s /s' % (dirname1, dirname2))

def backup_file(name):
    path = os.path.split(os.path.realpath(__file__))[0]
    lists = folder_path(path)
    path += name
    if path not in lists:
        os.makedirs(path)
    else:
        pass

def sendEmail(add_jilu):
    host_server = 'smtp.qq.com'  # qq??????smtp?????????
    sender_qq = 'xxxx@qq.com'  # ???????????????
    pwd = '?????????'
    receiver = ['xxxx@qq.com']  # ???????????????
    # receiver = 'xxxxxx@qq.com'
    mail_title = '??????cobaltstrike?????????????????????'  # ??????????????????????????????????????????
    mail_content = add_jilu  # ??????????????????
    # ???????????????????????????
    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title, 'utf-8')
    msg["From"] = sender_qq
    # msg["To"] = Header("????????????",'utf-8')
    msg['To'] = ";".join(receiver)
    # ??????????????????
    msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))

    smtp = SMTP_SSL(host_server)  # ssl??????

    
    smtp.login(sender_qq, pwd)

    smtp.sendmail(sender_qq, receiver, msg.as_string())
    
    smtp.quit()

def add_file(lists, filelist):
    jilu = ''
    for i in range(len(lists)):
        if lists[i] not in filelist:
            # print(os.path.split(lists[i])[-1])
            lists[i] = os.path.split(lists[i])[-1]
            # newtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            jilu01 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            jilu01 += ' ??????????????????????????????????????????cs?????????????????????????????????:'
            jilu01 += lists[i]
            jilu01 += '\n'
            jilu += jilu01
    return jilu

monitor_dir = input('???????????????????????????:')
filelist = folder_path(monitor_dir)
while True:
    time.sleep(1)
    # lists = get_dir_file(monitor_dir) #?????????????????????
    lists = folder_path(monitor_dir)
    if len(lists) > len(filelist):
        print("????????????????????????/??????")
        add_jilu = add_file(lists, filelist)
        print(add_jilu)
        sendEmail(add_jilu)
        cunchu_rizhi(add_jilu)
    filelist = lists





































