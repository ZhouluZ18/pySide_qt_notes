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
        self.setMinimumHeight(120)
# 去除右上角help按钮
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        self.lineedit = QtWidgets.QLineEdit()
        self.checkbox01 = QtWidgets.QCheckBox('xuanxiang 01')
        self.checkbox02 = QtWidgets.QCheckBox('xuanxiang 02')
        self.ok_button = QtWidgets.QPushButton('OK')
        self.cancel_button = QtWidgets.QPushButton('cancel')

    def create_layout(self):
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow('name:', self.lineedit)
        form_layout.addRow('hidden:', self.checkbox01)
        form_layout.addRow('locked:', self.checkbox02)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)


if __name__ == "__main__":
    try:
        ui.close()
    except:
        pass
    ui = TestDialog()
    ui.show()
