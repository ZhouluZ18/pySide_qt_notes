# -*- coding: UTF-8 -*-
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


class color_select_test(QtWidgets.QDialog):

    def __init__(self, parent=maya_main_weindow()):
        super(color_select_test, self).__init__(parent)

        self.setWindowTitle('color_select_test')
        self.setMinimumSize(300, 80)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.my_directory = cmds.internalVar(userPrefDir=True)
        self.my_color = QtGui.QColor(255, 0, 0)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):

        self.AAA_btn = QtWidgets.QPushButton('color')

    def create_layout(self):

        button_layout = QtWidgets.QHBoxLayout()

        button_layout.addWidget(self.AAA_btn)

        main_layout = QtWidgets.QVBoxLayout(self)

        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.AAA_btn.clicked.connect(self.show_color_select)

    def show_color_select(self):
        self.my_color = QtWidgets.QColorDialog.getColor(self.my_color, self)
        print ('red:{} green:{} bule:{}'.format(self.my_color.red(),
                                                self.my_color.green(),
                                                self.my_color.blue()))

if __name__ == "__main__":
    try:
        ui.close()
        ui.deleteLater()
    except:
        pass
    ui = color_select_test()
    ui.show()
