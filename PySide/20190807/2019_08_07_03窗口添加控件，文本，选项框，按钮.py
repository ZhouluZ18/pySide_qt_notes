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

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.lineedit = QtWidgets.QLineEdit()
        self.checkbox01 = QtWidgets.QCheckBox('xuanxiang 01')
        self.checkbox02 = QtWidgets.QCheckBox('xuanxiang 02')
        self.button01 = QtWidgets.QPushButton('button 01')
        self.button02 = QtWidgets.QPushButton('button 02')

    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.lineedit)
        main_layout.addWidget(self.checkbox01)
        main_layout.addWidget(self.checkbox02)
        main_layout.addWidget(self.button01)
        main_layout.addWidget(self.button02)

if __name__ == "__main__":
    ui = TestDialog()
    ui.show()
