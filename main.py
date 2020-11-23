import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageDraw
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        new_image = Image.new('RGB', (150, 150), (240, 240, 240))
        x = 75
        y = 75
        radius = random.randint(10, 75)
        draw = ImageDraw.Draw(new_image)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(255, 255, 0), width=1)
        new_image.save('ellipse.jpeg')
        self.pixmap = QPixmap('ellipse.jpeg')
        self.label.setPixmap(self.pixmap)
        radius = random.randint(10, 75)
        draw = ImageDraw.Draw(new_image)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(255, 255, 0), width=1)
        new_image.save('ellipse.jpeg')
        self.pixmap = QPixmap('ellipse.jpeg')
        self.label_2.setPixmap(self.pixmap)
        radius = random.randint(10, 75)
        draw = ImageDraw.Draw(new_image)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(255, 255, 0), width=1)
        new_image.save('ellipse.jpeg')
        self.pixmap = QPixmap('ellipse.jpeg')
        self.label_3.setPixmap(self.pixmap)
        radius = random.randint(10, 75)
        draw = ImageDraw.Draw(new_image)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(255, 255, 0), width=1)
        new_image.save('ellipse.jpeg')
        self.pixmap = QPixmap('ellipse.jpeg')
        self.label_4.setPixmap(self.pixmap)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
