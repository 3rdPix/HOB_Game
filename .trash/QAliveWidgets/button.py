from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QFrame, QLabel, QPushButton, QWidget, QAbstractButton
from PyQt6.QtCore import pyqtSignal, QPropertyAnimation, QRectF, Qt, QSizeF, QRectF
from PyQt6.QtGui import QPixmap, QIcon
from typing import overload, Optional


class QAliveButton(QPushButton):

    __backgroundPixmap: QPixmap = None
    __backgroundLabel: QLabel = None

    __doSizeAnimation: bool = True
    __doBackgroundAnimation: bool = False

    __startingSize: QSizeF
    __endingSize: QSizeF

    def __init__(self, backgroundIm: Optional[str | QPixmap] = None,
                 text: Optional[str] = None,
                 parent: Optional[QWidget] = None) -> None:
        
        # Handle args
        if text: super().__init__(text, parent)
        else: super().__init__(parent)
        if isinstance(backgroundIm, str):
            self.__backgroundPixmap = QPixmap(backgroundIm)
            self.__doBackgroundAnimation = True
        elif isinstance(backgroundIm, QPixmap):
            self.__backgroundPixmap = backgroundIm
            self.__doBackgroundAnimation = True
    
        self.__initSizeAnimation()
        self.__initBackgroundAnimation()

    def __initSizeAnimation(self) -> None:
        self.__sizeIncrease: QPropertyAnimation = QPropertyAnimation(
            self, b'geometry')
        self.__sizeDecrease: QPropertyAnimation = QPropertyAnimation(
            self, b'geometry')
        
    def __initBackgroundAnimation(self) -> None:
        self.__backgroundLabel = QLabel(parent=self)
        if isinstance(self.__backgroundPixmap, QPixmap):
            self.__backgroundLabel.setPixmap(self.__backgroundPixmap)
        self.__backgroundLabel.setScaledContents(True)
        self.__backgroundLabel.setGeometry(QRectF(0, 0, 0, self.height()))
        self.__backgroundIncrease: QPropertyAnimation = QPropertyAnimation(
            self.__backgroundLabel, b'size')
        self.__backgroundDecrease: QPropertyAnimation = QPropertyAnimation(
            self.__backgroundLabel, b'size')
        
    def __startingSize_getter(self) -> QSizeF:
        return self.__startingSize
    
    def __startingSize_setter(self, newSize: QSizeF) -> None:
        self.__startingSize = newSize
        self.__endingSize = QSizeF(newSize.width() * 1.2,
                                   newSize.height() * 1.2)
        # Increase
        self.__sizeIncrease.setStartValue(self.__startingSize)
        self.__sizeIncrease.setEndValue(self.__endingSize)
        self.__backgroundIncrease.setStartValue(
            QSizeF(0, self.__startingSize.height()))
        self.__backgroundIncrease.setEndValue(self.__endingSize)

        # Decrease
        self.__sizeDecrease.setStartValue(self.__endingSize)
        self.__sizeDecrease.setEndValue(self.__startingSize)
        self.__backgroundDecrease.setStartValue(self.__endingSize)
        self.__backgroundDecrease.setEndValue(self.__startingSize)
        
    _startingSize = property(__startingSize_getter, __startingSize_setter)

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        self._startingSize = event.size()
        return super().resizeEvent(event)