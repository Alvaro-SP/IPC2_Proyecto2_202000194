
from ventana import *

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SMARTWATCH_WINDOW = QtWidgets.QMainWindow()
    ui = Ui_SMARTWATCH_WINDOW()
    ui.setupUi(SMARTWATCH_WINDOW)
    SMARTWATCH_WINDOW.show()
    sys.exit(app.exec_())
