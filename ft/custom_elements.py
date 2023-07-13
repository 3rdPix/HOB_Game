import typing
from PyQt5 import QtCore, QtWidgets, QtGui, QtMultimedia
from PyQt5.QtWidgets import QWidget


class AnimatedButton(QtWidgets.QPushButton):

    def __init__(self, hover_se: str, font, click_se, **kwargs) -> None:
        super().__init__(**kwargs)
        self.hover_se: QtMultimedia.QSound = QtMultimedia.QSound(hover_se)
        self.click_se: QtMultimedia.QSound = QtMultimedia.QSound(click_se)
        self.setFont(QtGui.QFont(font))
        self.setObjectName('HudButton')
        self.setMaximumWidth(int((self.parent().width() * 3) / 4))

    def mousePressEvent(self, QMouseEvent) -> None:
        self.click_se.play()
        return super().mousePressEvent(QMouseEvent)

    def enterEvent(self, Qevent) -> None:
        self.hover_se.play()
        return super().enterEvent(Qevent)
    
class TransitionLabel(QtWidgets.QFrame):

    def __init__(self, im_1: QtGui.QPixmap, im_2: QtGui.QPixmap,
                 max_opacity: float, **kwargs) -> None:
        super().__init__(**kwargs)

        # Create both labels with images
        self._image1: QtWidgets.QLabel = QtWidgets.QLabel(self)
        self._image1.setPixmap(im_1)
        self._image1.setScaledContents(True)

        self._image2: QtWidgets.QLabel = QtWidgets.QLabel(self)
        self._image2.setPixmap(im_2)
        self._image2.setScaledContents(True)

        # Set up opacity effects
        self._opacity1: QtWidgets.QGraphicsOpacityEffect = \
            QtWidgets.QGraphicsOpacityEffect(self._image1)
        self._opacity1.setOpacity(max_opacity)
        self._image1.setGraphicsEffect(self._opacity1)
        
        self._opacity2: QtWidgets.QGraphicsOpacityEffect = \
            QtWidgets.QGraphicsOpacityEffect(self._image2)
        self._opacity2.setOpacity(0.0)
        self._image2.setGraphicsEffect(self._opacity2)

        # Create transitions
        self._opacity1_upwards: QtCore.QPropertyAnimation = \
            QtCore.QPropertyAnimation(self._opacity1, b'opacity')
        self._opacity1_upwards.setStartValue(0.0)
        self._opacity1_upwards.setEndValue(max_opacity)
        
        self._opacity1_downwards: QtCore.QPropertyAnimation = \
            QtCore.QPropertyAnimation(self._opacity1, b'opacity')
        self._opacity1_downwards.setStartValue(max_opacity)
        self._opacity1_downwards.setEndValue(0.0)

        self._opacity2_upwards: QtCore.QPropertyAnimation = \
            QtCore.QPropertyAnimation(self._opacity2, b'opacity')
        self._opacity2_upwards.setStartValue(0.0)
        self._opacity2_upwards.setEndValue(max_opacity)

        self._opacity2_downwards: QtCore.QPropertyAnimation = \
            QtCore.QPropertyAnimation(self._opacity2, b'opacity')
        self._opacity2_downwards.setStartValue(max_opacity)
        self._opacity2_downwards.setEndValue(0.0)

        # Status
        self._first_stage: bool = True

    def set_duration(self, msec: int) -> None:
        self._opacity1_upwards.setDuration(msec)
        self._opacity1_downwards.setDuration(msec)
        self._opacity2_upwards.setDuration(msec)
        self._opacity2_downwards.setDuration(msec)

    def transition(self) -> None:
        if self._first_stage:
            self._opacity1_downwards.start()
            self._opacity2_upwards.start()
            self._first_stage: bool = not self._first_stage
        else:
            self._opacity1_upwards.start()
            self._opacity2_downwards.start()
            self._first_stage: bool = not self._first_stage

    def resizeEvent(self, QResizeEvent) -> None:
        self._image1.resize(self.size())
        self._image2.resize(self.size())
        return super().resizeEvent(QResizeEvent)