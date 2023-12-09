from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout
from PyQt6.QtCore import Qt
import sys

from button import QAliveButton

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = QWidget()

    my_button = QAliveButton(text='something')


    main_window.show()
    sys.exit(app.exec())