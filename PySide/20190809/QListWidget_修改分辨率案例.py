'''# -*- coding: UTF-8 -*-'''
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
import maya.OpenMaya as om
import pymel.core as pm
import maya.cmds as cmds


def maya_main_weindow():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class List_widgets_win(QtWidgets.QDialog):

    FENGBIANLVLIST = [
                        ['1920x1080 (1080p)', 1920.0, 1080.0],
                        ['1280x720 (720p)', 1280.0, 720.0],
                        ['960x540 (540p)', 960.0, 540.0],
                        ['640x480', 640.0, 480.0],
                        ['320x240', 320.0, 240.0]
                        ]

    def __init__(self, parent=maya_main_weindow()):
        super(List_widgets_win, self).__init__(parent)

        self.setWindowTitle(u'QListWidget_窗口测试')
        self.setMinimumSize(300, 80)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.list_widgets = QtWidgets.QListWidget()
        # self.list_widgets.addItems(['1920*1080 (1080p)', '1280*720 (720p)', '960*540 (540p)'])
        for fenbianlv in self.FENGBIANLVLIST:
            my_item = QtWidgets.QListWidgetItem(fenbianlv[0])
            my_item.setData(QtCore.Qt.UserRole, [fenbianlv[1], fenbianlv[2]])
            self.list_widgets.addItem(my_item)

        self.close_btn = QtWidgets.QPushButton('close')

    def create_layout(self):

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.close_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)  # 设置边框间距
        main_layout.setSpacing(2)  # 设置控件间距

        main_layout.addWidget(self.list_widgets)
        main_layout.addLayout(button_layout)

    def create_connections(self):

        self.list_widgets.itemClicked.connect(self.set_fenbianlv)

    def set_fenbianlv(self, item):
        FBL = item.data(QtCore.Qt.UserRole)
        print(u'分辨率为：{}'.format(item.text()))
        cmds.setAttr('defaultResolution.width', FBL[0])
        cmds.setAttr('defaultResolution.height', FBL[1])
        cmds.setAttr('defaultResolution.deviceAspectRatio', FBL[0]/FBL[1])

if __name__ == "__main__":
    try:
        ui.close()
        ui.deleteLater()
    except:
        pass
    ui = List_widgets_win()
    ui.show()
