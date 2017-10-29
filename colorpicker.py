import sys
from PyQt5.QtWidgets import QApplication, QWidget


class ColorPickerWindow(QWidget):

    def __init__(self):
        super(ColorPickerWindow, self).__init__()
        self.init_UI()
    
    def init_UI(self):
        # Set window dimensions to 600px by 400px
        self.resize(600, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cpw = ColorPickerWindow()
    cpw.show()
    app.exec_()
