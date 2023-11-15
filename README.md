# Hackers of Blysis
[![Static Badge](https://img.shields.io/github/issues/3rdPix/HOB_Game.svg)](https://github.com/3rdPix/HOB_Game/issues)
[![Static Badge](https://img.shields.io/github/issues-closed/3rdPix/HOB_Game.svg)](https://github.com/3rdPix/HOB_Game/issues)
![Static Badge](https://img.shields.io/badge/Documentation-incomplete-red)
![Static Badge](https://img.shields.io/badge/Project-HOB_developing-cyan?logo=github&link=https%3A%2F%2Fgithub.com%2Fusers%2F3rdPix%2Fprojects%2F3)
![Static Badge](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

> A game about hacking with its own programming language

## Background 🖥️
I'm sure you are familiar with the guy with a hoodie, staring at a black screen with green letters, writing dozens of lines of code to say "We're In" after a couple seconds. How some television series portrait the hacking experience as something exciting, intense, and battle-like against the defenses of *whatever software or server* they are trying to gain access to.
Well, this game aims to make that child dream come true. You are given the mission to get access to Blysis, the central server of a futuristic world where everything is connected, every person, every action, every sale, every emotion, everything is registered inside this giant server called Blysis. As an underground person, the resistance requests your help to get access to the server. In this game you will have different levels of complexity while trying to achieve your mission. Not only will you have to hack the defenses of the most advanced, modern, and secured server in this world, but you will also need to be very cautelous with *how* you do it as it might get the attention of civilians, or the Blaegis, a special unit dedicated to the protection and preservation of Blysis. If they find out about you, they will start attacking you back, while repairing every defense of the server, making it even more difficult to enter.

## Developing stages
[![Static Badge](https://img.shields.io/badge/Py-Qt6-brightgreen?labelColor=blue)](https://pypi.org/project/PyQt6/)
[![Static Badge](https://img.shields.io/badge/PEP8-darkblue?logo=python&logoColor=white)](https://pep8.org/)
[![Static Badge](https://img.shields.io/badge/Qt-Documentation-darkblue?labelColor=brightgreen)](https://doc.qt.io/qtforpython-6/)


Since I am developing this as I explore and extend my knowledge around the PyQt framework and all its capabilities, the stages will be very segmented between build-up functionality of the app and gaming features. The flow of the game should follow the next diagram.

<div align="center">
    <img src="other/window_flow.png" alt="Window Flow Chart" />
    <p><em>In this chart, purple bidirectional arrows mean a strict connection, i.e. if window <b>A</b> is accessed through window <b>B</b>, it can only go back to window <b>B</b> and not any of the other windows for which <b>A</b> has connections.</em></p>
</div>
As per usual, this chart might be modified if new windows or panels are added to complete features of the game. Note that the <i>Game Window</i> has sub windows and panels, but those are related to the gameplay itself, not the app management. Also, for any sub window of this <i>Game Window</i>, all connections from its parent are preserved.
The stages of development follow the path a user would take in the app; first the main window, options window, about panel, then new game, game window, and load game. In all of these, a minimum amount of frontend is needed to start adding features and functionality to the game. However, I do not intend to fulfill the minimum only. As mentioned earlier, this is a project to learn the full extent of the Qt framework, therefore, a lot of frontend will be created before moving to the next part.


<img align="left" width="40" height="40" src="https://pypi.org/static/images/logo-small.2a411bc6.svg" alt="Modularization concept">

## Modularization and directory

The app is extensively modularized. This means that parameters, settings, style definitions, and paths are separated from the constructor module. This is a non-extensive list of how the directory works.
* <img align="left" width="20" height="20" src="other/json_icon.png" alt="JSON file"> `paths.json`: As its name suggests, contains the relative paths of all the source files in the directory, including images, sounds, style definitions, and parameters of different windows.
* <img align="left" width="20" height="20" src="other/css.png" alt="JSON file"> `*.qss`: Files with custom style sheets applied to QWidgets. These can found in the frontend folder.
* <img align="left" width="20" height="20" src="other/json_icon.png" alt="JSON file"> (window)`parameters.json`: Files with different window parameters. These are related to the visual representation of the windows. Can also be found in the frontend folder.

Additionaly, module files are also segmented into different needs. For instance, `main_menu_signals.py` contains the `MainMenuSignals` class which is inherited by `MainMenuWindow` found in `main_menu.py`. This is to organize classes according to its contents and keep files below a certain number of lines, maintaining its readibility.