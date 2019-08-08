import maya.OpenMayaUI as omui
from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance


def maya_main_weindow():
    main_window_ptr = omui.MQtUtil.mainWindow()  # 获取maya主窗口
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


def hello_world():
    label = QtWidgets.QLabel("Hello World!", parent=maya_main_weindow())  # 窗口p给maya主窗口
    label.setWindowFlags(QtCore.Qt.Tool)
    label.show()


if __name__ == "__main__":
    hello_world()
