from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from main import get_coords, get_picture
from PIL import Image
import sys


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.MAP_FILE = 'map.jpg'
        self.coords = 'Австралия'
        self.SPN = 25
        self.SIZE = 450
        self.SCREEN_SIZE = [self.SIZE, self.SIZE]
        self.x = 0
        self.y = 0

        self.initUI()

    def initUI(self):
        self.setGeometry(self.SIZE, self.SIZE, *self.SCREEN_SIZE)
        self.setWindowTitle('Отображение картинки')
        self.lay = QVBoxLayout(self)

        self.x, self.y = get_coords(self.coords)
        get_picture(self.SPN, self.x, self.y, self.MAP_FILE)
        # Изображение
        self.pixmap = QPixmap(self.MAP_FILE)
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет
        self.image = QLabel(self)
        self.image.setPixmap(self.pixmap)
        self.image.resize(self.SIZE, self.SIZE)
        self.lay.addWidget(self.image)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.SPN -= 1
            self.rel()

        if event.key() == Qt.Key_PageDown:
            self.SPN += 1
            self.rel()

    def rel(self):
        get_picture(self.SPN, self.x, self.y, self.MAP_FILE)
        change_size(self.MAP_FILE, self.SIZE)
        self.pixmap = QPixmap(self.MAP_FILE)
        self.image.setPixmap(self.pixmap)


def change_size(mp, size):
    Image.open(mp).resize((size, size)).save(mp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
