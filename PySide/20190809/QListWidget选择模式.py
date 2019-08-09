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


class MultList_widgets_win(QtWidgets.QDialog):

    def __init__(self, parent=maya_main_weindow()):
        super(MultList_widgets_win, self).__init__(parent)

        self.setWindowTitle(u'多选QListWidget_窗口测试')
        self.setMinimumSize(300, 80)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.list_widgets = QtWidgets.QListWidget()
        self.list_widgets.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)  # ContiguousSelection,MultiSelection(选择模式切换)
        self.list_widgets.addItems([u'元素1', u'元素2', u'元素3', u'元素4', u'元素5', u'元素6'])

        self.AAA_btn = QtWidgets.QPushButton(u'关闭')

    def create_layout(self):
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.AAA_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(2, 2, 2, 2)  # 设置边框间距
        main_layout.setSpacing(2)  # 设置控件间距

        main_layout.addWidget(self.list_widgets)
        main_layout.addLayout(button_layout)

    def create_connections(self):

        self.list_widgets.itemClicked.connect(self.print_select_yuansu)

    def print_select_yuansu(self):
        items = self.list_widgets.selectedItems()

        select_labels = []
        for item in items:
            select_labels.append(item.text())

        print(u'选择的元素为：{}'.format(select_labels))

if __name__ == "__main__":
    try:
        ui.close()
        ui.deleteLater()
    except:
        pass
    ui = MultList_widgets_win()
    ui.show()
