from ft.custom_elements import AnimatedButton, TransitionLabel
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia
from ft.main_menu_signals import MainMenuSignals
from math import cos, sin
from os.path import join
from json import load


class MainMenuWindow(MainMenuSignals):

    """
    Upper class methods
    """
    def __init__(self, directory: dict) -> None:
        super().__init__()

        # Get parameters
        with open(join(*directory.get('parameters'))) as data:
            self.parameters: dict = load(data)

        # Save directory
        self.directory: dict = directory

        self.init_UI()
        self.connect_events()

    def show(self) -> None:
        self.gradient_timer.start()
        self.music_player.play()
        return super().show()
    
    def hide(self) -> None:
        self.gradient_timer.stop()
        self.music_player.pause()
        return super().hide()
        
    def paintEvent(self, paintEvent) -> None:
        painter: QtGui.QPainter = QtGui.QPainter(self)
        painter.fillRect(QtCore.QRectF(self.rect()), self.gradient)
        return super().paintEvent(paintEvent)
    
    def resizeEvent(self, QResizeEvent) -> None:
        self.background_label.resize(self.size())
        return super().resizeEvent(QResizeEvent)

    def keyPressEvent(self, event) -> None:
        if event.text() == 'm': self.full_screen()
        elif event.text() == 't': self.background_label.transition()
        return super().keyPressEvent(event)

    """
    Game screen
    """
    def init_UI(self) -> None:

        # window -> icon, flag and size
        self.setWindowIcon(QtGui.QIcon(join(
            *self.directory.get('window_icon'))))
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.resize(self.parameters.get('window_width'),
                    self.parameters.get('window_heigth'))

        # background
        self.gradient: QtGui.QLinearGradient = QtGui.QLinearGradient()
        self.gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        self.gradient.setColorAt(
            0, QtGui.QColor(*self.parameters.get('gradient_color_1')))
        self.gradient.setColorAt(
            1, QtGui.QColor(*self.parameters.get('gradient_color_2')))
        self.g_angle: int = 0
        
        self.gradient_timer: QtCore.QTimer = QtCore.QTimer(self)
        self.gradient_timer.setInterval(
            self.parameters.get('gradient_rotation_tick'))
        self.gradient_timer.timeout.connect(self.update_gradient)
        
        self.normal_image: QtGui.QPixmap = QtGui.QPixmap(join(
            *self.directory.get('normal_background_image')))
        self.fullscreen_image: QtGui.QPixmap = QtGui.QPixmap(join(
            *self.directory.get('fullscreen_background_image')))

        self.background_label: TransitionLabel = TransitionLabel(
            self.normal_image, self.fullscreen_image,
            self.parameters.get('background_image_opacity'), parent=self)
        self.background_label.set_duration(
            self.parameters.get('background_transition_duration'))
        self.background_label.resize(self.size())

        # buttons
        custom_font_id = QtGui.QFontDatabase.addApplicationFont(join(
            *self.directory.get('menu_font')))
        font_family: QtGui.QFontDatabase = \
            QtGui.QFontDatabase.applicationFontFamilies(custom_font_id)[0]
        button_hover_se: str = join(*self.directory.get('button_hover_se'))
        button_click_se: str = join(*self.directory.get('button_click_se'))
       
        self.newgame_button = AnimatedButton(button_hover_se, font_family,
                                             button_click_se,
                                            text='start new game', parent=self)
        self.loadgame_button = AnimatedButton(button_hover_se, font_family,
                                             button_click_se,
                                            text='load game', parent=self)
        self.options_button = AnimatedButton(button_hover_se, font_family,
                                             button_click_se,
                                            text='options', parent=self)
        self.about_button = AnimatedButton(button_hover_se, font_family,
                                           button_click_se,
                                           text='about', parent=self)
        self.exit_button = AnimatedButton(button_hover_se, font_family,
                                          button_click_se,
                                            text='exit', parent=self)
        
        # buttons layout
        vertical_layout = QtWidgets.QVBoxLayout()
        vertical_layout.addStretch()
        vertical_layout.addWidget(self.newgame_button)
        vertical_layout.addWidget(self.loadgame_button)
        vertical_layout.addWidget(self.options_button)
        vertical_layout.addWidget(self.about_button)
        vertical_layout.addWidget(self.exit_button)
        vertical_layout.addStretch()

        horizontal_layout = QtWidgets.QHBoxLayout(self)
        horizontal_layout.addStretch(1)
        horizontal_layout.addLayout(vertical_layout, 3)
        horizontal_layout.addStretch(1)

        # apply stylesheet
        with open(join(*self.directory.get('qss'))) as qss:
            self.setStyleSheet(qss.read())

        # music. Could be adapted to include more songs
        self.song: QtMultimedia.QMediaContent = QtMultimedia.QMediaContent(
            QtCore.QUrl.fromLocalFile(join(
            *self.directory.get('background_song'))))
        self.playlist: QtMultimedia.QMediaPlaylist = \
            QtMultimedia.QMediaPlaylist()
        self.playlist.addMedia(self.song)
        self.playlist.setPlaybackMode(QtMultimedia.QMediaPlaylist.Loop)
        self.music_player: QtMultimedia.QMediaPlayer = \
            QtMultimedia.QMediaPlayer()
        self.music_player.setPlaylist(self.playlist)
        self.music_player.setVolume(15)

        self.setFocus()

    def update_gradient(self) -> None:
        self.g_angle += 1
        deg_to_rad: float = 0.01745329
        start = QtCore.QPointF(0.5 + 0.5 * cos(self.g_angle * deg_to_rad),
                               0.5 + 0.5 * sin(self.g_angle * deg_to_rad))
        f_stop = QtCore.QPointF(0.5 + 0.5 * \
                                cos((self.g_angle + 180) * deg_to_rad),
                                0.5 + 0.5 * \
                                sin((self.g_angle + 180) * deg_to_rad))
        self.gradient.setStart(start)
        self.gradient.setFinalStop(f_stop)
        self.update()

    """
    Events
    """
    def connect_events(self) -> None:
        self.exit_button.clicked.connect(
            exit)
        
    """
    Calls
    """
    def full_screen(self) -> None:
        if not self.isFullScreen():
            self.background_label.transition()
            self.showFullScreen()
        else:
            self.background_label.transition()
            self.showNormal()