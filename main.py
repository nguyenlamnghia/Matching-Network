# This Python file uses the following encoding: utf-8
import sys
from pathlib import Path

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtCore import QObject, Slot, Signal, Property

class MainWindow(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.zin = 0
        self.zl = 0
        self.f = 0
        self.q = 0
        self.typeOfImpedance = ""
        self.circuitType = ""

    @Property(bool)
    def checkFilled(self):
        try:
            self.zin = int(self.zin)
            self.zl = int(self.zl)
            self.f = int(self.f)
            self.q = int(self.q)
        except Exception as e:
            return False
        if self.zin and self.zl and self.f and self.q and self.typeOfImpedance and self.circuitType:
            return True
        return False

    @Property(list)
    def setData(self):
        data = [self.zin, self.zl, self.f, self.q, self.typeOfImpedance, self.circuitType]
        return data

    @Slot(str, str, str, str)
    def getParameter(self, zin, zl, f, q):
        self.zin = zin
        self.zl = zl
        self.f = f
        self.q = q

    @Slot(str)
    def getCircuitType(self, name):
        self.circuitType = name

    @Slot(str)
    def getTypeOfImpedance(self, name):
        self.typeOfImpedance = name

    @Slot()
    def calculate(self):
        print(self.zin+self.zl)

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
