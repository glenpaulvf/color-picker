import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class ColorPickerWindow(QWidget):

    def __init__(self):
        super(ColorPickerWindow, self).__init__()
        
        # Window properties
        self.width = 600
        self.height = 400
        
        self.init_UI()
    
    def init_UI(self):
        # Set window dimensions to 600px by 400px
        self.resize(self.width, self.height)
        
        # Set window background color to white
        pal = self.palette()
        pal.setColor(self.backgroundRole(), Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        # Initialize color viewer        
        viewer = ColorViewer(self)
        viewer.resize(50, 50) # force viewer dimensions to 50px square
        
        
class ColorViewer(QWidget):
        
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.draw_viewer(painter)
        painter.end()
    
    def draw_viewer(self, painter):
        painter.setPen(Qt.black)
        painter.setBrush(Qt.red)
        painter.drawRect(10, 10, 50, 50)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.press_pos = event.globalPos()
            self.move_pos = event.globalPos()

        super(ColorViewer, self).mousePressEvent(event)
    
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # Adjust offset from clicked point to origin of widget
            curr_pos = self.mapToGlobal(self.pos())
            global_pos = event.globalPos()
            offset = global_pos - self.move_pos
            new_pos = self.mapFromGlobal(curr_pos + offset)
            self.move(new_pos)
            self.move_pos = global_pos

        super(ColorViewer, self).mouseMoveEvent(event)
    
    def mouseReleaseEvent(self, event):
        super(ColorViewer, self).mouseReleaseEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cv = ColorPickerWindow()
    cv.show()
    app.exec_()
