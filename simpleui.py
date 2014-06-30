#! /usr/bin/env python
# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

application = QApplication(sys.argv)




# QWidget - базовый класс для всех объектов интерфейса
# пользователя; если использовать для виджета конструктор
# без родителя, такой виджет станет окном
widget = QWidget()
size = 600
widget.resize(size, size)  # изменить размеры виджета
widget.setWindowTitle("Drawing")  # установить заголовок
point = QPoint(0,0)
widget.x = 10
widget.y = 10
widget.label = QLabel(widget)
widget.label.resize(size,size)
widget.show()  # отобразить окно на экране
#rect = QRect(10,10,100,100)
#paint = QPaintEvent(rect)
#widget.paintEvent(paint)
widget.setAttribute(Qt.WA_PaintOutsidePaintEvent, True)
#pd = QPaintDevice()
brush = QBrush(QColor(200,90,90))
pen = QPen(QColor(200,90,90))
pixmap = QPixmap(size,size)
pixmap.fill(Qt.white)
painter = QPainter()
house = QImage()
reader = QImageReader()
house = reader.read()
painter.begin(pixmap)
painter.setBrush(brush)
painter.setPen(pen)
print house.load("/home/keder/house.png")
painter.drawRect(0,0,50,50)
painter.drawImage(50,50,house)
painter.end()
painter.begin(pixmap)
painter.setBrush(brush)
painter.setPen(pen)
print house.load("/home/keder/house.png")
painter.drawRect(100,100,50,50)
painter.drawImage(150,150,house)
painter.end()
widget.label.setPixmap(pixmap)
widget.update()
sys.exit(application.exec_())
