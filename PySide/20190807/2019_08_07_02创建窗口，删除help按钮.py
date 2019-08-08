from PySide2 import QtCore
from PySide2 import QtWidgets
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance


def maya_main_weindow():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class TestDialog(QtWidgets.QDialog):

    def __init__(self, parent=maya_main_weindow()):
        super(TestDialog, self).__init__(parent)

        self.setWindowTitle('test_win')
        self.setMinimumWidth(200)
        self.setMinimumHeight(200)
# 去除右上角help按钮
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

if __name__ == "__main__":
    ui = TestDialog()
    ui.show()
