from PyQt6.QtWidgets import QFrame, QLabel, QGridLayout, QPushButton
from PyQt6.QtCore import pyqtSignal, QPropertyAnimation
from PyQt6.QtGui import QPixmap
from typing import overload

class QAliveButton(QPushButton):

    __lightPixmap: QPixmap = None
    __backgroundPixmap: QPixmap = None

    __startGeometry: tuple
    __finalGeometry: tuple
    __sizeAnimation: bool = False
    __backgroundAnimation: bool = False
    __lightAnimation: bool = False

    @overload
    def __init__(self, **kwargs) -> None: ...

    @overload
    def __init__(self, text: str, **kwargs) -> None: ...

    @overload
    def __init__(self, text: str, light_animation: str, **kwargs) -> None: ...

    @overload
    def __init__(self, text: str, background_animation: str, **kwargs) -> None: ...
    
    @overload
    def __init__(self, text: str, light_animation: str, background_animation: str,
                 **kwargs) -> None: ...
    
    def __init__(self, text: str=None, light_animation: str=None,
                 background_animation: str=None, **kwargs) -> None:
        super().__init__(text, **kwargs)
        if light_animation:
            self.__lightPixmap = QPixmap(light_animation)
            self.__initLightAnimation()
        if background_animation: 
            self.__backgroundPixmap = QPixmap(background_animation)
            self.__initBackgroundAnimation()
        self.__initSizeAnimation()

    def __initSizeAnimation(self) -> None:
        self.__sizeIncrease: QPropertyAnimation = QPropertyAnimation(
            self, b'geometry')
        self.__sizeDecrease: QPropertyAnimation = QPropertyAnimation(
            self, b'geometry')
        
    def __initBackgroundAnimation(self) -> None:
        self.__backgroundLabel: QLabel = QLabel(parent=self)
        self.__backgroundLabel.setPixmap(self.__backgroundPixmap)
        self.__backgroundIncrease: QPropertyAnimation = QPropertyAnimation(
            self.__backgroundLabel, b'geometry')
        self.__backgroundDecrease: QPropertyAnimation = QPropertyAnimation(
            self.__backgroundLabel, b'geometry')
        
    def __initLightAnimation(self) -> None:
        self.__lightLabel: QLabel = QLabel(parent=self)
        self.__lightLabel.setPixmap(self.__lightPixmap)
        self.__lightIncrease: QPropertyAnimation = QPropertyAnimation(
            self.__lightLabel, b'x')
        self.__lightDecrease: QPropertyAnimation = QPropertyAnimation(
            self.__lightLabel, b'x')
        
    def setAnimations(self, size: bool, light: bool, background: bool) -> None:

        # geometry
        x, y, w, h = self.geometry().getRect()
        fw, fh = w * 1.1, h * 1.1
        fx, fy = x - (fw - w) / 2, y - (fh - h) / 2
        self.__startGeometry = x, y, w, h
        self.__finalGeometry = fx, fy, fw, fh

        # size animation
        if size:
            self.__sizeAnimation = size
            self.__sizeIncrease.setStartValue(self.__startGeometry)
            self.__sizeIncrease.setEndValue(self.__finalGeometry)
            self.__sizeDecrease.setStartValue(self.__finalGeometry)
            self.__sizeDecrease.setEndValue(self.__startGeometry)
        else: self.__sizeAnimation = size

        # background animation
        if background and self.__backgroundPixmap:
            self.__backgroundAnimation = background
            self.__backgroundIncrease.setStartValue(x, y, 0, h)
            self.__backgroundIncrease.setEndValue(fx, fy, fw, fh)
            self.__backgroundDecrease.setStartValue(fx, fy, fw, fh)
            self.__backgroundDecrease.setEndValue(x, y, 0, h)
        elif background and not self.__backgroundPixmap:
            raise Exception('No background provided')
        else: self.__backgroundAnimation = background
        
        # light animation
        if light and self.__lightAnimation:
            self.__lightAnimation = light
            self.__lightIncrease.setStartValue(x)
            self.__lightIncrease.setEndValue(fx + fw)
            self.__lightDecrease.setStartValue(fx + fw)
            self.__lightDecrease.setEndValue(x)
        elif light and not self.__lightAnimation:
            raise Exception('No light provided')
        else: self.__lightAnimation = light

    def setDuration(self, msec: int) -> None:
        self.__sizeIncrease.setDuration(msec)
        self.__sizeDecrease.setDuration(msec)
        self.__backgroundIncrease.setDuration(msec)
        self.__backgroundDecrease.setDuration(msec)
        self.__lightIncrease.setDuration(msec)
        self.__lightDecrease.setDuration(msec)

    def enterEvent(self, event) -> None:
        if self.__sizeAnimation: self.__sizeIncrease.start()
        if self.__lightAnimation: self.__lightIncrease.start()
        if self.__backgroundAnimation: self.__backgroundIncrease.start()
        return super().enterEvent(event)

    def leaveEvent(self, event) -> None:
        if self.__sizeAnimation: self.__sizeDecrease.start()
        if self.__lightAnimation: self.__lightDecrease.start()
        if self.__backgroundAnimation: self.__backgroundDecrease.start()
        return super().leaveEvent(event)
    