# -*- coding:utf-8 -*-
# 一键批量修改图片RGB颜色软件V1.0
# 作者：陶小桃Blog
# 日期：2023-11-27
# 博客主页：https://www.52txr.cn
# 邮箱：to52txr@163.com

import os
import sys

import cv2
import numpy as np
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QColorDialog

import json
from MAINWIDOWS import Ui_MainWindow  # PyQt 界面样式
import resource_rc  # 资源文件

class MainWindow(QMainWindow):
    # 初始化主交互界面
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # 初始化界面
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint)  # 窗口尺寸固定，禁止最大化按钮

        # 存储按钮的原始颜色
        self.color_dict = {
                           'color1qian': (255, 255, 255), 'color1hou': (255, 255, 255),
                           'color2qian': (255, 255, 255), 'color2hou': (255, 255, 255),
                           'color3qian': (255, 255, 255), 'color3hou': (255, 255, 255),
                           'color4qian': (255, 255, 255), 'color4hou': (255, 255, 255),
                           'color5qian': (255, 255, 255), 'color5hou': (255, 255, 255),
                           'color6qian': (255, 255, 255), 'color6hou': (255, 255, 255),
                           'color7qian': (255, 255, 255), 'color7hou': (255, 255, 255),
                           'color8qian': (255, 255, 255), 'color8hou': (255, 255, 255)
                           }

    def ChooseInputDir(self):
        # 选择输入的文件夹
        self.InputDir = QFileDialog.getExistingDirectory(self, "选择原图文件夹", "./")
        self.ui.inputpath.setText(self.InputDir)
        print(self.InputDir)
        if self.InputDir == "":
            QMessageBox.warning(self, "警告", "请选择需要修改图片的文件夹！")
            return 0

    def ChooseOutDir(self):
        # 选择PNG文件夹
        self.OutDir = QFileDialog.getExistingDirectory(self, "选择图片输出文件夹", "./")
        self.ui.outputpath.setText(self.OutDir)
        print(self.OutDir)
        if self.OutDir == "":
            QMessageBox.warning(self, "警告", "请选择输出文件夹！")
            return 0

        # 判断文件夹是否为空
        # 建议使用一个空文件夹来存储PNG文件
        def is_folder_empty(folder_path):
            return len(os.listdir(folder_path)) == 0

        is_empty = is_folder_empty(self.OutDir)
        print(is_empty)
        if not is_empty:
            QMessageBox.warning(self, "警告", "强烈建议选择一个空文件夹来存储修改后的图片！")
            return 0
        elif self.OutDir == self.InputDir:
            QMessageBox.warning(self, "警告", "请原图文件夹与输出文件夹不要选择同一个文件夹！养成良好的作业习惯~")
            return 0
        else:
            pass

# 取色器
    def GetColor(self, button):
        color = QColorDialog.getColor()
        # 获取按钮的名称
        button_name = button.objectName()
        # print(button_name)
        if color.isValid():
            # print(f'Selected color name: {color.name()}')
            print(f'RGB values: ({color.red()}, {color.green()}, {color.blue()})')
            rgb_values = (color.red(), color.green(), color.blue())
            button.setStyleSheet(f'background-color: rgb{rgb_values}')
            self.color_dict[button_name] = rgb_values
            print(self.color_dict)
            # return color.red(), color.green(), color.blue()

    def ModifyRGBs(self):
        for im_name in os.listdir(self.InputDir):
            im = cv2.imread(self.InputDir + "/" + im_name)
            im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            for key, value in self.color_dict.items():
                if key.endswith('qian'):
                    hou_key = key.replace('qian', 'hou')
                    print(hou_key)
                    print(self.color_dict[hou_key])
                    im[np.all(im == value, axis=-1)] = (self.color_dict[hou_key][2], self.color_dict[hou_key][1], self.color_dict[hou_key][0])
                    cv2.imwrite(self.OutDir + "/" + im_name, im)
                    print(self.OutDir + "/" + im_name)
                    print(self.color_dict)
                else:
                    pass

    def ResetRGBs(self):
        self.ui.color1qian.setStyleSheet("background-color: rgb(255,255,255);")
        self.ui.color1hou.setStyleSheet("background-color: rgb(255,255,255);")
        self.ui.color2qian.setStyleSheet("background-color: rgb(255,255,255);")
        self.ui.color2hou.setStyleSheet("background-color: rgb(255,255,255);")
        self.ui.color3qian.setStyleSheet("background-color: rgb(255,255,255);")
        self.ui.color3hou.setStyleSheet("background-color: rgb(255,255,255);")
        self.ui.color4qian.setStyleSheet("background-color: rgb(255,255,255);")
        self.ui.color4hou.setStyleSheet("background-color: rgb(255,255,255);")
        self.ui.color5qian.setStyleSheet("background-color: rgb(255,255,255);")
        self.ui.color5hou.setStyleSheet("background-color: rgb(255,255,255);")
        self.ui.color6qian.setStyleSheet("background-color: rgb(255,255,255);")
        self.ui.color6hou.setStyleSheet("background-color: rgb(255,255,255);")
        self.ui.color7qian.setStyleSheet("background-color: rgb(255,255,255);")
        self.ui.color7hou.setStyleSheet("background-color: rgb(255,255,255);")
        self.ui.color8qian.setStyleSheet("background-color: rgb(255,255,255);")
        self.ui.color8hou.setStyleSheet("background-color: rgb(255,255,255);")

    def Run(self):
        try:
            self.ModifyRGBs()
            QMessageBox.information(self, "提示", "修改完成！")
        except:
            QMessageBox.warning(self, "警告", "出现错误！")

if __name__ == '__main__':
    ### 加载 UI 界面
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)  # 添加高分辨率缩放支持
    app = QApplication(sys.argv)
    MainInterface = MainWindow()
    MainInterface.show()
    sys.exit(app.exec_())
