# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Slot, Signal, Property

class MainWindow(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.zs_re = 0
        self.zs_im = 0
        self.zl_re = 0
        self.zl_im = 0
        self.f = 0
        self.q = 0
        self.typeOfImpedance = ""
        self.circuitType = ""
        self.f_unit = "Hz"

    @Property(bool)
    def checkFilled(self):
        # Kiem tra dinh dang dau vao va ep kieu
        try:
            self.zs_re = float(self.zs_re)
            self.zs_im = float(self.zs_im)
            self.zl_re = float(self.zl_re)
            self.zl_im = float(self.zl_im)
            self.f = float(self.f)
            self.q = float(self.q)
        except Exception as e:
            return False
        # Kiem tra f khac 0 va type da duoc chon
        # Kiem tra co 1 trong 2 phan thuc va phan ao
        # Kiem tra neu la L section thi khong can phai q khac 0
        if (self.zs_re or self.zs_im) and (self.zl_re or self.zl_im) and self.f and (self.typeOfImpedance == "L Section" or self.q != 0) and self.typeOfImpedance and self.circuitType:
            return True
        return False

    @Property(list)
    def setData(self):
        # zs_re, zs_im, zl_re, zl_im, f, q, typeOfImpedance, circuitType, f_unit
        data = [self.zs_re, self.zs_im, self.zl_re, self.zl_im, self.f, self.q, self.typeOfImpedance, self.circuitType, self.f_unit]
        return data

    @Slot(str, str, str, str, str, str, str)
    def getParameter(self, zs_re, zs_im, zl_re, zl_im, f, q, f_unit):
        self.zs_re = zs_re
        self.zs_im = zs_im
        self.zl_re = zl_re
        self.zl_im = zl_im
        self.f = f
        self.q = q
        self.f_unit = f_unit


    @Slot(str)
    def getCircuitType(self, name):
        self.circuitType = name

    @Slot(str)
    def getTypeOfImpedance(self, name):
        self.typeOfImpedance = name

    @Slot()
    def calculate(self):
        pass

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # get context
    main = MainWindow()
    engine.rootContext().setContextProperty("backend", main)

    # load qml file
    qml_file = Path(__file__).resolve().parent / "main.qml"
    engine.load(str(qml_file))
    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
