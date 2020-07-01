# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QMessageBox, QApplication
from PyQt5.QtCore import QSettings, QTimer
from view import Ui_MainWindow
import os, re


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

    # 服务器名和IP地址获取
    def SettingUp(self):
        files = self.file_list()
        setup = files[0]
        if "!Setup.txt" in setup:
            with open(setup, mode='r', encoding='GB2312') as setup_F:
                all_str = setup_F.readlines()
                old_serverName = ((all_str[2])[11:]).strip()
                old_ipAddress = ((all_str[6])[7:]).strip()
                setup_content = [old_serverName, old_ipAddress]
            setup_F.close()
            return setup_content
        elif setup == "":
            self.msg_box("哥哥，第一个框框不能空到！！！")
        else:
            self.msg_box("哥哥，第一个框框一定要放“ !Setup.txt ”！！！")

    # 文件内容修改方法
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

    def File_Change(self, files, New_serverName, New_IpAddress):
        setup = self.SettingUp()
        old_ServerName = setup[0]
        old_IpAddress = setup[1]
        file = files
        new_file = "%s.new" % (file)
        if "serverlist" in file:
            f_new = open(new_file, mode='w', encoding='utf-8')
        else:
            f_new = open(new_file, mode='w', encoding='GB2312')
        with open(file, mode='r', encoding='GB2312') as old_file:
            old_str = old_file.readlines()
            for content in old_str:
                pattern_1 = re.compile(old_ServerName)
                content = re.sub(pattern_1, New_serverName, content)
                new_str = [content]
                for new_content in new_str:
                    pattern_2 = re.compile(old_IpAddress)
                    new_text = re.sub(pattern_2, New_IpAddress, new_content)
                    # print(new_text)
                    f_new.write(new_text)
            f_new.close()
            old_file.close()

    def MirGate_ini(self, files, New_IpAddress):
        setup = self.SettingUp()
        old_IpAddress = setup[1]
        file = files
        new_file = "%s.new" % (file)
        f_new = open(new_file, mode='w', encoding='utf-8')
        with open(file, mode='r', encoding='GB2312') as old_file:
            old_str = old_file.readlines()
            for content in old_str:
                pattern_1 = re.compile(old_IpAddress)
                content = re.sub(pattern_1, New_IpAddress, content)
                f_new.write(content)
            f_new.close()
            old_file.close()

    def All_File_Change(self):
        files = self.file_list()
        New_serverName = (self.NameEdit.text()).strip()
        New_IpAddress = (self.IpChangeEdit.text()).strip()
        for file in files:
            if "DBService.ini" in file:
                self.File_Change(file, New_serverName, New_IpAddress)
            elif "LoginGate.ini" in file:
                self.File_Change(file, New_serverName, New_IpAddress)
            elif "serverlist.json" in file:
                self.File_Change(file, New_serverName, New_IpAddress)
            elif "serverlist.lua" in file:
                self.File_Change(file, New_serverName, New_IpAddress)
            elif "MirGate.ini" in file:
                self.MirGate_ini(file, New_IpAddress)
            elif "project.manifest" in file:
                self.Project_manifest(file)
            elif "version.manifest" in file:
                self.version_manifest(file)
            elif "Setup.txt" in file:
                self.File_Change(file, New_serverName, New_IpAddress)


    # IP修改方法
    def ChangeBtn(self):
        self.DirRecord()
        if (self.NameEdit.text() and self.IpChangeEdit.text()) != '':
            self.All_File_Change()
            self.IpChangeBtn.setText("修改成功")

        elif (self.NameEdit.text() == '') and (self.IpChangeEdit.text() == ''):
            msg1 = '哥哥，都是空滴，改不了呢！！！'
            self.msg_box(msg1)

        elif (self.NameEdit.text() == '') or (self.IpChangeEdit.text() == ''):
            msg2 = '哥哥，服务器名或IP有一个没填呀！！！'
            self.msg_box(msg2)
