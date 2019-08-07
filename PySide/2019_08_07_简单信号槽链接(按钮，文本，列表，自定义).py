import maya.OpenMayaUI as omui
import pymel.core as pm
from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance


def maya_main_weindow():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class TestUi(QtWidgets.QDialog):

    test_signal = QtCore.Signal()  # 自定义信号

    def __init__(self, parent=maya_main_weindow()):
        super(TestUi, self).__init__(parent)

    def create(self):
        '''
        create the ui
        '''
        self.setWindowTitle('TestUi')
        self.setWindowFlags(QtCore.Qt.Tool)

        self.create_controls()
        self.create_layout()
        self.create_connections()

    def create_controls(self):
        self.push_button = QtWidgets.QPushButton('btn01')
        self.check_box_01 = QtWidgets.QCheckBox('check_box01')
        self.check_box_02 = QtWidgets.QCheckBox('check_box02')
        self.line_edit = QtWidgets.QLineEdit('line_edit')
        self.list_wdg = QtWidgets.QListWidget()
        self.list_wdg.addItems(['item_01',
                                'item_02',
                                'item_03',
                                'item_04'])
        self.list_wdg.setCurrentRow(0)
        self.list_wdg.setMaximumHeight(60)

    def create_layout(self):
        check_box_layout = QtWidgets.QHBoxLayout()
        check_box_layout.setContentsMargins(2, 2, 2, 2)
        check_box_layout.addWidget(self.check_box_01)
        check_box_layout.addWidget(self.check_box_02)

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setContentsMargins(6, 6, 6, 6)

        main_layout.addWidget(self.push_button)
        main_layout.addLayout(check_box_layout)

        main_layout.addWidget(self.line_edit)
        main_layout.addWidget(self.list_wdg)
        main_layout.addStretch()

        self.setLayout(main_layout)

    def create_connections(self):

        self.push_button.clicked.connect(self.on_button_pressed)
        self.check_box_01.toggled.connect(self.on_check_box_toggled)
        self.check_box_02.toggled. connect(self.on_check_box_toggled)
        # self.line_edit.textChanged.connect(self.on_text_changed)
        self.line_edit.editingFinished.connect(self.on_text_changed)
        self.list_wdg.currentItemChanged.connect(self.on_selection_changed)
        self.test_signal.connect(self.on_test_signal_emitted)

    def on_button_pressed(self):
        print('Button_pressed')

        if self.line_edit.text() == 'text_xinhao':
            self.test_signal.emit()

    def on_check_box_toggled(self):
        # print('chebox_toggled')
        sender = self.sender()  # 消息发送者，消息反馈
        print('{} toggled'. format(sender.text()))

    def on_text_changed(self):
        print('test_changed')

    def on_selection_changed(self, current, previous):
        print('selection_changed')
        print('current item: {}'.format(current.text()))  # 反馈上一个选择物体名
        print('previous item: {}'.format(previous.text()))  # 当前物体名

    def on_test_signal_emitted(self):
        print ('siggnal_received')


if __name__ == "__main__":
    test_ui = TestUi()
    try:
        test_ui.close()
    except:
        pass
    test_ui = TestUi()
    test_ui.create()
    test_ui.show()
