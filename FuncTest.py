# -*- coding: utf-8 -*-

import os
import base64

# file_1 = './file/version.manifest'
# file_2 = './file/!Setup.txt'
# files = [file_1, file_2]
# print(files)


# def version_manifest(files):
#     file = files
#     new_file = '%s.new' % (file)
#     f_new = open(new_file, mode='w', encoding='utf-8')
#     with open(file, mode='r', encoding='utf-8') as f:
#         old_str = f.readlines()
#         old_packageUrl = old_str[1]
#         old_remoteManifestUrl = old_str[2]
#         old_remoteVersionUrl = old_str[3]
#         old_serverUrl = old_str[4]
#         # print(old_packageUrl, old_remoteManifestUrl, old_remoteVersionUrl, old_serverUrl)
#         ip = '118.24.123.118'
#         New_packageUrl = ' "packageUrl": "http://{}/assets/", \n'.format(ip)
#         New_remoteManifestUrl = ' "remoteManifestUrl": "http://{}/project.manifest", \n'.format(ip)
#         New_remoteVersionUrl = ' "remoteVersionUrl": "http://{}/version.manifest", \n'.format(ip)
#         New_serverUrl = ' "serverUrl": "http://{}/", \n'.format(ip)
#
#         for line in old_str:
#             if old_packageUrl in line:
#                 line = line.replace(old_packageUrl, New_packageUrl, 1)
#             elif old_remoteManifestUrl in line:
#                 line = line.replace(old_remoteManifestUrl, New_remoteManifestUrl, 1)
#             elif old_remoteVersionUrl in line:
#                 line = line.replace(old_remoteVersionUrl, New_remoteVersionUrl, 1)
#             elif old_serverUrl in line:
#                 line = line.replace(old_serverUrl, New_serverUrl, 1)
#             f_new.write(line)
#         f.close()
#         f_new.close()
#
#
# def setup_txt(files):
#     file = files
#     new_file = '%s.new' % (file)
#     f_new = open(new_file, mode='w', encoding='GB2312')
#     with open(file, mode='r', encoding='GB2312') as f:
#         old_str = f.readlines()
#         old_server = old_str[2]
#         old_LogServerIp = old_str[31]
#         content = old_str[6]
#         # print(content)
#         serverName = '五湖传奇'
#         ip = '118.24.123.118'
#         New_serverName = 'ServerName={}\n'.format(serverName)
#         new_content = 'DBAddr={}\n'.format(ip)
#         logServerIp = 'LogServerAddr={}\n'.format(ip)
#         for line in old_str:
#             if old_server in line:
#                 line = line.replace(old_server, New_serverName, 1)
#             elif content in line:
#                 line = line.replace(content, new_content, 1)
#             elif old_LogServerIp in line:
#                 line = line.replace(old_LogServerIp, logServerIp, 1)
#             f_new.write(line)
#         f.close()
#         f_new.close()
#
# open_icon = open('./res/img/long60x60.png', mode='rb')
# b64str = base64.b64encode(open_icon.read())
#
# open_icon.close()
#
# write_data = 'image = %s' % b64str
# f = open('chuanqi.py', mode='w+')
# f.write(write_data)
# f.close()

import re

file = './Desktop/!Setup.txt'
file2 = './Desktop/DBService.ini'
file3 = "%s.new" % (file2)
new_file = open(file3, mode='w', encoding='GB2312')
with open(file, mode='r', encoding='GB2312') as f:
    all_str = f.readlines()
    name = ((all_str[2])[11:]).strip()
    ipAddress = ((all_str[6])[7:]).strip()
    print(name, ipAddress)
    new_name = '宝毅传奇'
    new_ipAddress = '227.233.149.199'
    with open(file2, mode='r', encoding='GB2312') as old_file:
        old_str = old_file.readlines()
        for content in old_str:
            pattern_1 = re.compile(name)
            content = re.sub(pattern_1, new_name, content)
            new_str = [content]
            for new_content in new_str:
                pattern_2 = re.compile(ipAddress)
                new_text = re.sub(pattern_2, new_ipAddress, new_content)
                # print(new_text)
                new_file.write(new_text)


# for line in old_str:
#     if name in line:
#         line = re.sub(name, new_name, line)
#     elif ipAddress in line:
#         line = re.sub(ipAddress, new_ipAddress, line)
#     new_file.write(line)
old_file.close()
new_file.close()
f.close()
# old_str = "GameGate1=132.232.47.246:7100"
# ip = r'132.232.47.246'
# new_ip = '112.25.138.222'
# pattern = re.compile(ip)
# print(pattern.findall(old_str))
# newip = re.sub(ip, new_ip, old_str)
# print(newip)
