import sys
from PyQt5.QtWidgets import QApplication, QWidget, QColorDialog
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
    
    # Viewer properties
    viewer_color = Qt.red
        
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        self.draw_viewer(painter)
        painter.end()
    
    def draw_viewer(self, painter):
        painter.setPen(Qt.black)
        painter.setBrush(ColorViewer.viewer_color)
        painter.drawRect(10, 10, 50, 50)

    def mousePressEvent(self, event):
        self.press_pos = event.globalPos()
        self.move_pos = event.globalPos()

        super(ColorViewer, self).mousePressEvent(event)
    
    def mouseMoveEvent(self, event):
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
        
    def mouseDoubleClickEvent(self, event):
        color_dialog = QColorDialog()
        #color_dialog.move(self.x(), self.y())
        new_color = color_dialog.getColor()
        if new_color.isValid():
            ColorViewer.viewer_color = new_color
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cv = ColorPickerWindow()
    cv.show()
    app.exec_()
