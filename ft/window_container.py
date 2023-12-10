from PyQt6.QtWidgets import QStackedWidget, QWidget


class WindowHandler(QStackedWidget):

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

    def setWindows(self, *args) -> None:
        [self.addWidget(element) for element in args]

    def show(self) -> None:
        return super().show()
    
    def moveTo(self, window: int) -> None:
        self.setCurrentIndex(window)

    def showMainMenu(self) -> None:
        self.moveTo(0)

    def showOptionsMenu(self) -> None:
        self.moveTo(1)