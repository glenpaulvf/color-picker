import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class ColorPickerWindow(QWidget):

    def __init__(self):
        super(ColorPickerWindow, self).__init__()
        self.init_UI()
    
    def init_UI(self):
        # Set window dimensions to 600px by 400px
        self.resize(600, 400)
        
        # Set window background color to white
        pal = self.palette()
        pal.setColor(self.backgroundRole(), Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)
        
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.draw_viewer(painter)
        painter.end()
    
    def draw_viewer(self, painter):
        painter.setPen(Qt.black)
        painter.setBrush(Qt.white)
        painter.drawRect(10, 10, 50, 50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cpw = ColorPickerWindow()
    cpw.show()
    app.exec_()
