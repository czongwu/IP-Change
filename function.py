# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox, QApplication
from PyQt5.QtCore import QSettings, QTimer
from view import Ui_MainWindow
import os


class Function(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

    # 路径历史记录保存方法
    def DirRecord(self):
        setting = QSettings("./lib/config.ini", QSettings.IniFormat)
        setting.setValue("FilePath_1", self.FileDir_1.text())
        setting.setValue("FilePath_2", self.FileDir_2.text())
        setting.setValue("FilePath_3", self.FileDir_3.text())
        setting.setValue("FilePath_4", self.FileDir_4.text())
        setting.setValue("FilePath_5", self.FileDir_5.text())
        setting.setValue("FilePath_6", self.FileDir_6.text())
        setting.setValue("FilePath_7", self.FileDir_7.text())
        setting.setValue("FilePath_8", self.FileDir_8.text())
        setting.setValue("FilePath_9", self.FileDir_9.text())
        setting.setValue("FilePath_10", self.FileDir_10.text())
        setting.setValue("ServerName", self.NameEdit.text())
        # setting.setValue("IPAddress", self.IpChangeEdit.text())

    # 初始化窗口信息
    def init_view_info(self):
        setting = QSettings("./lib/config.ini", QSettings.IniFormat)
        self.FileDir_1.setText(setting.value("FilePath_1"))
        self.FileDir_2.setText(setting.value("FilePath_2"))
        self.FileDir_3.setText(setting.value("FilePath_3"))
        self.FileDir_4.setText(setting.value("FilePath_4"))
        self.FileDir_5.setText(setting.value("FilePath_5"))
        self.FileDir_6.setText(setting.value("FilePath_6"))
        self.FileDir_7.setText(setting.value("FilePath_7"))
        self.FileDir_8.setText(setting.value("FilePath_8"))
        self.FileDir_9.setText(setting.value("FilePath_9"))
        self.FileDir_10.setText(setting.value("FilePath_10"))
        self.NameEdit.setText(setting.value("ServerName"))
        # self.IpChangeEdit.setText(setting.value("IPAddress"))

    # 文件路径选择方法
    def SelectFile_1(self):
        FileDialog = QFileDialog()
        FileDir, ok = FileDialog.getOpenFileName(self, '选择文件', "D:/")
        if ok:
            self.FileDir_1.setText(FileDir)

    # 同上
    def SelectFile_2(self):
        FileDialog = QFileDialog()
        FileDir, ok = FileDialog.getOpenFileName(self, '选择文件', "D:/")
        if ok:
            self.FileDir_2.setText(FileDir)

    # 同上
    def SelectFile_3(self):
        FileDialog = QFileDialog()
        FileDir, ok = FileDialog.getOpenFileName(self, '选择文件', "D:/")
        if ok:
            self.FileDir_3.setText(FileDir)

    # 同上
    def SelectFile_4(self):
        FileDialog = QFileDialog()
        FileDir, ok = FileDialog.getOpenFileName(self, '选择文件', "D:/")
        if ok:
            self.FileDir_4.setText(FileDir)

    # 同上
    def SelectFile_5(self):
        FileDialog = QFileDialog()
        FileDir, ok = FileDialog.getOpenFileName(self, '选择文件', "D:/")
        if ok:
            self.FileDir_5.setText(FileDir)

    # 同上
    def SelectFile_6(self):
        FileDialog = QFileDialog()
        FileDir, ok = FileDialog.getOpenFileName(self, '选择文件', "D:/")
        if ok:
            self.FileDir_6.setText(FileDir)

    # 同上
    def SelectFile_7(self):
        FileDialog = QFileDialog()
        FileDir, ok = FileDialog.getOpenFileName(self, '选择文件', "D:/")
        if ok:
            self.FileDir_7.setText(FileDir)

    # 同上
    def SelectFile_8(self):
        FileDialog = QFileDialog()
        FileDir, ok = FileDialog.getOpenFileName(self, '选择文件', "D:/")
        if ok:
            self.FileDir_8.setText(FileDir)

    # 同上
    def SelectFile_9(self):
        FileDialog = QFileDialog()
        FileDir, ok = FileDialog.getOpenFileName(self, '选择文件', "D:/")
        if ok:
            self.FileDir_9.setText(FileDir)

    # 同上
    def SelectFile_10(self):
        FileDialog = QFileDialog()
        FileDir, ok = FileDialog.getOpenFileName(self, '选择文件', "D:/")
        if ok:
            self.FileDir_10.setText(FileDir)

    # 文件内容修改方法
    def setup_txt(self, files):
        file = files
        new_file = '%s.new' % (file)
        f_new = open(new_file, mode='w', encoding='GB2312')
        with open(file, mode='r', encoding='GB2312') as f:
            old_str = f.readlines()
            old_server = old_str[2]
            old_LogServerIp = old_str[31]
            content = old_str[6]
            # print(content)
            serverName = self.NameEdit.text()
            ip = self.IpChangeEdit.text()
            New_serverName = 'ServerName={}\n'.format(serverName)
            new_content = 'DBAddr={}\n'.format(ip)
            logServerIp = 'LogServerAddr={}\n'.format(ip)
            for line in old_str:
                if old_server in line:
                    line = line.replace(old_server, New_serverName, 1)
                elif content in line:
                    line = line.replace(content, new_content, 1)
                elif old_LogServerIp in line:
                    line = line.replace(old_LogServerIp, logServerIp, 1)
                f_new.write(line)
            f.close()
            f_new.close()
            os.remove(file)
            os.rename(new_file, file)

    # 同上
    def DBServer_ini(self, files):
        file = files
        new_file = '%s.new' % (file)
        f_new = open(new_file, mode='w', encoding='GB2312')
        with open(file, mode='r', encoding='GB2312') as f:
            old_str = f.readlines()
            old_serverName = old_str[2]
            old_LoginGateIp = old_str[27]
            old_GameGate_1 = old_str[58]
            old_GameGate_2 = old_str[59]
            old_GameServer_1 = old_str[66]
            serverName = self.NameEdit.text()
            ip = self.IpChangeEdit.text()
            New_serverName = 'ServerName={}\n'.format(serverName)
            New_LoginGateIp = 'IP={}\n'.format(ip)
            New_GameGate_1 = 'GameGate1={}:7100\n'.format(ip)
            New_GameGate_2 = 'GameGate2={}:7101\n'.format(ip)
            New_GameServer_1 = 'GameServer1={}\n'.format(ip)
            for line in old_str:
                if old_serverName in line:
                    line = line.replace(old_serverName, New_serverName, 1)
                elif old_LoginGateIp in line:
                    line = line.replace(old_LoginGateIp, New_LoginGateIp, 1)
                elif old_GameGate_1 in line:
                    line = line.replace(old_GameGate_1, New_GameGate_1, 1)
                elif old_GameGate_2 in line:
                    line = line.replace(old_GameGate_2, New_GameGate_2, 1)
                elif old_GameServer_1 in line:
                    line = line.replace(old_GameServer_1, New_GameServer_1, 1)
                f_new.write(line)
            f.close()
            f_new.close()
            os.remove(file)
            os.rename(new_file, file)

    # 同上
    def LoginGate_ini(self, files):
        file = files
        new_file = '%s.new' % (file)
        f_new = open(new_file, mode='w', encoding='GB2312')
        with open(file, mode='r', encoding='GB2312') as f:
            old_str = f.readlines()
            old_IPAddress1 = old_str[9]
            old_group1DBS = old_str[17]
            old_group1name = old_str[18]
            old_group1Desc = old_str[19]
            serverName = self.NameEdit.text()
            ip = self.IpChangeEdit.text()
            New_IPAddress1 = 'IPAddress1={}\n'.format(ip)
            New_group1DBS = 'group1DBS={}\n'.format(serverName)
            New_group1name = 'group1name={}\n'.format(serverName)
            New_group1Desc = 'group1Desc={}\n'.format(serverName)
            for line in old_str:
                if old_IPAddress1 in line:
                    line = line.replace(old_IPAddress1, New_IPAddress1, 1)
                elif old_group1DBS in line:
                    line = line.replace(old_group1DBS, New_group1DBS, 1)
                elif old_group1name in line:
                    line = line.replace(old_group1name, New_group1name, 1)
                elif old_group1Desc in line:
                    line = line.replace(old_group1Desc, New_group1Desc, 1)
                f_new.write(line)
            f.close()
            f_new.close()
            os.remove(file)
            os.rename(new_file, file)

    # 同上
    def MirGate_ini(self, files):
        file = files
        new_file = '%s.new' % (file)
        f_new = open(new_file, mode='w', encoding='utf-8')
        with open(file, mode='r', encoding='utf-8') as f:
            old_str = f.readlines()
            old_DBServerIP = old_str[2]
            old_LogServerIP = old_str[4]
            ip = self.IpChangeEdit.text()
            New_DBServerIP = 'DBServerIP={}\n'.format(ip)
            New_LogServerIP = 'LogServerIP={}\n'.format(ip)
            for line in old_str:
                if old_DBServerIP in line:
                    line = line.replace(old_DBServerIP, New_DBServerIP, 1)
                elif old_LogServerIP in line:
                    line = line.replace(old_LogServerIP, New_LogServerIP, 1)
                f_new.write(line)
            f.close()
            f_new.close()
            os.remove(file)
            os.rename(new_file, file)

    # 同上
    def Project_manifest(self, files):
        file = files
        new_file = '%s.new' % (file)
        f_new = open(new_file, mode='w', encoding='utf-8')
        with open(file, mode='r', encoding='utf-8') as f:
            old_str = f.readlines()
            old_packageUrl = old_str[9191]
            old_remoteManifestUrl = old_str[9192]
            old_remoteVersionUrl = old_str[9193]
            old_serverUrl = old_str[9194]
            # print(old_packageUrl, old_remoteManifestUrl, old_remoteVersionUrl, old_serverUrl)
            ip = self.IpChangeEdit.text()
            New_packageUrl = ' "packageUrl": "http://{}/assets/", \n'.format(ip)
            New_remoteManifestUrl = ' "remoteManifestUrl": "http://{}/project.manifest", \n'.format(ip)
            New_remoteVersionUrl = ' "remoteVersionUrl": "http://{}/version.manifest", \n'.format(ip)
            New_serverUrl = ' "serverUrl": "http://{}/", \n'.format(ip)

            for line in old_str:
                if old_packageUrl in line:
                    line = line.replace(old_packageUrl, New_packageUrl, 1)
                elif old_remoteManifestUrl in line:
                    line = line.replace(old_remoteManifestUrl, New_remoteManifestUrl, 1)
                elif old_remoteVersionUrl in line:
                    line = line.replace(old_remoteVersionUrl, New_remoteVersionUrl, 1)
                elif old_serverUrl in line:
                    line = line.replace(old_serverUrl, New_serverUrl, 1)
                f_new.write(line)
            f.close()
            f_new.close()
            os.remove(file)
            os.rename(new_file, file)

    # 同上
    def serverlist_json(self, files):
        file = files
        new_file = '%s.new' % (file)
        f_new = open(new_file, mode='w', encoding='utf-8')
        with open(file, mode='r', encoding='utf-8') as f:
            old_str = f.readlines()
            old_content = old_str[0]
            ServerName = self.NameEdit.text()
            ip = self.IpChangeEdit.text()

            New_content = '{"kaifubiao":1,"shopurl":"http://www.860fupay.com/B98BA6DDC868A7F9B5A9A580F85E2680CD21030A474742DE"' \
                          ',"notice":"\\u003cb\\u003e\\u003cparam size\\u003d25 textcolor\\u003d255|0|0  /\\u003e\\u003ct \\n%s公告:' \
                          '\\n /\\u003e\\u003c/b\\u003e\\u003cb\\u003e\\u003cparam size\\u003d20 textcolor\\u003d255|222|173 /\\u003e\\u003ct\\n目前游戏已正式开放，' \
                          '所有玩家可以通过微信：sihai1688188为本游戏提供BUG和修改意见，确认采纳后会根据玩家提供的信息给予不同的奖励。\\n ' \
                          ' /\\u003e\\u003c/b\\u003e","verinfo":[{"verid":"%s","vername":"%s","verindex":1,"clientver":180}],' \
                          '"servers":[{"verid":"%s","serverinfo":"[区服: %s ]","zoneid":2,"zonename":"%s","zoneip":"%s:7000",' \
                          '"area":180,"suggest":1,"heat":2,"ConfigName":"config176.zip","ConfigVer":"2020022512"},' \
                          '{"verid":"%s","serverinfo":"[区服: %s ]","zoneid":2,"zonename":"%s","zoneip":"%s:7000",' \
                          '"area":180,"suggest":1,"heat":2,"ConfigName":"config176.zip","ConfigVer":"2020022512"}]}' % \
                          (ServerName, ServerName, ServerName, ServerName, ServerName, ServerName, ip, ServerName,
                           ServerName, ServerName, ip)

            for line in old_str:
                if old_content in line:
                    line = line.replace(old_content, New_content, 1)

                f_new.write(line)
            f.close()
            f_new.close()
            os.remove(file)
            os.rename(new_file, file)

    # 同上
    def serverlist_lua(self, files):
        file = files
        new_file = '%s.new' % (file)
        f_new = open(new_file, mode='w', encoding='utf-8')
        with open(file, mode='r', encoding='utf-8') as f:
            old_str = f.readlines()
            old_content = old_str[21]
            ServerName = self.NameEdit.text()
            ip = self.IpChangeEdit.text()
            New_content = '    return \'{"serverlist":{"kaifubiao":1,"servers":[{"isactive":1,"serverid":"1997dw","rank1":1,"rank2":1,"serverip":"%s:8088",' \
                          '"servername":"%s","desc":"火热测试中"}],"imglist":[{"pos":"1","url":"http://www.sihai168.xyz/gg/1.png"},{"pos":"2","url":"http://www.sihai168.xyz/gg/2.png"},' \
                          '{"pos":"3","url":"http://www.sihai168.xyz/gg/3.png"}],"notice":"<b><param size=20 textcolor=255|222|173 /><t \\n\\n欢迎使用来到 \\n\\n\\n要了解更多详情请访问我们的站点： />' \
                          '</b><b><param size=20 urlcolor=255|222|173 urltext=%s urladdr=http://www.sihai168.xyz /></b>"}}\' \n ' % (
                              ip, ServerName, ServerName)

            for line in old_str:
                if old_content in line:
                    line = line.replace(old_content, New_content, 1)

                f_new.write(line)
            f.close()
            f_new.close()
            os.remove(file)
            os.rename(new_file, file)

    # 同上
    def version_manifest(self, files):
        file = files
        new_file = '%s.new' % (file)
        f_new = open(new_file, mode='w', encoding='utf-8')
        with open(file, mode='r', encoding='utf-8') as f:
            old_str = f.readlines()
            old_packageUrl = old_str[1]
            old_remoteManifestUrl = old_str[2]
            old_remoteVersionUrl = old_str[3]
            old_serverUrl = old_str[4]
            # print(old_packageUrl, old_remoteManifestUrl, old_remoteVersionUrl, old_serverUrl)
            ip = self.IpChangeEdit.text()
            New_packageUrl = ' "packageUrl": "http://{}/assets/", \n'.format(ip)
            New_remoteManifestUrl = ' "remoteManifestUrl": "http://{}/project.manifest", \n'.format(ip)
            New_remoteVersionUrl = ' "remoteVersionUrl": "http://{}/version.manifest", \n'.format(ip)
            New_serverUrl = ' "serverUrl": "http://{}/", \n'.format(ip)

            for line in old_str:
                if old_packageUrl in line:
                    line = line.replace(old_packageUrl, New_packageUrl, 1)
                elif old_remoteManifestUrl in line:
                    line = line.replace(old_remoteManifestUrl, New_remoteManifestUrl, 1)
                elif old_remoteVersionUrl in line:
                    line = line.replace(old_remoteVersionUrl, New_remoteVersionUrl, 1)
                elif old_serverUrl in line:
                    line = line.replace(old_serverUrl, New_serverUrl, 1)
                f_new.write(line)
            f.close()
            f_new.close()
            os.remove(file)
            os.rename(new_file, file)

    # 文件路径生成列表
    def file_list(self):
        file_1 = self.FileDir_1.text()
        file_2 = self.FileDir_2.text()
        file_3 = self.FileDir_3.text()
        file_4 = self.FileDir_4.text()
        file_5 = self.FileDir_5.text()
        file_6 = self.FileDir_6.text()
        file_7 = self.FileDir_7.text()
        file_8 = self.FileDir_8.text()
        file_9 = self.FileDir_9.text()
        file_10 = self.FileDir_10.text()
        files = [file_1, file_2, file_3, file_4, file_5, file_6, file_7, file_8, file_9, file_10]
        return files

    # 循环列表批量修改文件
    def change_Function(self):
        files = self.file_list()
        try:
            for file in files:
                if '!Setup.txt' in file:
                    print(file)
                    self.setup_txt(file)
                elif 'DBService.ini' in file:
                    print(file)
                    self.DBServer_ini(file)
                elif 'LoginGate.ini' in file:
                    print(file)
                    self.LoginGate_ini(file)
                elif 'MirGate.ini' in file:
                    print(file)
                    self.MirGate_ini(file)
                elif 'project.manifest' in file:
                    print(file)
                    self.Project_manifest(file)
                elif 'serverlist.json' in file:
                    print(file)
                    self.serverlist_json(file)
                elif 'serverlist.lua' in file:
                    print(file)
                    self.serverlist_lua(file)
                elif 'version.manifest' in file:
                    print(file)
                    self.version_manifest(file)
        except:
            msg_3 = '请检查文件路径或者文件名是否正确！！！'
            self.msg_box(msg_3)

    # 清空所有文本框类容
    def clear_all(self):
        self.FileDir_1.setText('')
        self.FileDir_2.setText('')
        self.FileDir_3.setText('')
        self.FileDir_4.setText('')
        self.FileDir_5.setText('')
        self.FileDir_6.setText('')
        self.FileDir_7.setText('')
        self.FileDir_8.setText('')
        self.FileDir_9.setText('')
        self.FileDir_10.setText('')
        # self.NameEdit.setText('')
        self.IpChangeEdit.setText('')

    # 提示信息弹窗
    def msg_box(self, msg):
        msg_box = QMessageBox()
        msg_box.question(self, '批量修改工具', msg, msg_box.Ok)

    # IP修改方法
    def ChangeBtn(self):
        self.DirRecord()
        if (self.NameEdit.text() and self.IpChangeEdit.text()) != '':
            self.change_Function()

        elif (self.NameEdit.text() == '') and (self.IpChangeEdit.text() == ''):
            msg1 = '哥，都是空滴，改不了呢！！！'
            self.msg_box(msg1)

        elif (self.NameEdit.text() == '') or (self.IpChangeEdit.text() == ''):
            msg2 = '哥，服务器名或IP有一个没填呀！！！'
            self.msg_box(msg2)
