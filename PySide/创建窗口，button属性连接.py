import maya.OpenMayaUI as omui
import pymel.core as pm
from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance


def maya_main_weindow():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class PrimitiveUi(QtWidgets.QDialog):

    def __init__(self, parent=maya_main_weindow()):
        super(PrimitiveUi, self).__init__(parent)

        self.setWindowTitle('Primitives')
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.create_layout()
        self.create_connections()

    def create_layout(self):
        self.cube_btn = QtWidgets.QPushButton('Cube')
        self.Sphere_btn = QtWidgets.QPushButton('Sphere')
        self.Cone_btn = QtWidgets.QPushButton('Cone')
        self.Cylinder_btn = QtWidgets.QPushButton('Cylinder')

        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setContentsMargins(2, 2, 2, 2)
        main_layout.setSpacing(2)

        main_layout.addWidget(self.cube_btn)
        main_layout.addWidget(self.Sphere_btn)
        main_layout.addWidget(self.Cone_btn)
        main_layout.addWidget(self.Cylinder_btn)
        main_layout.addStretch()

        self.setLayout(main_layout)

    def create_connections(self):
        self.cube_btn.clicked.connect(PrimitiveUi.make_cube)
        self.Sphere_btn.clicked.connect(PrimitiveUi.make_sphere)
        self.Cone_btn.clicked.connect(PrimitiveUi.make_cone)
        self.Cylinder_btn.clicked.connect(PrimitiveUi.make_cylinder)

    @classmethod
    def make_cube(cls):
        pm.polyCube()

    @classmethod
    def make_sphere(cls):
        pm.polySphere()

    @classmethod
    def make_cone(cls):
        pm.polyCone()

    @classmethod
    def make_cylinder(cls):
        pm.polyCylinder()

if __name__ == "__main__":

    try:
        ui.close()
    except:
        pass
    ui = PrimitiveUi()
    ui.show()
