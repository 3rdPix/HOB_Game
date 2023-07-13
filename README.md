# HOB_Game
## Introduction 🖥️
I'm sure you are familiar with the guy with a hoodie, staring at a black screen with green letters, writing dozens of lines of code to say "We're In" after a couple seconds. How some television series portrait the hacking experience as something exciting, intense, and battle-like against the defenses of *whatever software or server* they are trying to gain access to.
Well, this game aims to make that child dream come true. You are given the mission to get access to Blysis, the central server of a futuristic world where everything is connected, every person, every action, every sale, every emotion, everything is registered inside this giant server called Blysis. As an underground person, the resistance requests your help to get access to the server. In this game you will have different levels of complexity while trying to achieve your mission. Not only will you have to hack the defenses of the most advanced, modern, and secured server in this world, but you will also need to be very cautelous with *how* you do it as it might get the attention of civilians, or the Blaegis, a special unit dedicated to the protection and preservation of Blysis. If they find out about you, they will start attacking you back, while repairing every defense of the server, making it even more difficult to enter.

<img align="left" width="50" height="50" src="https://doc.qt.io/qtforpython-5/_static/pysidelogo.png" alt="PyQt icon">

## Developing stages

Since I am developing this as I explore and extend my knowledge around the PyQt framework and all its capabilities, the stages will be very segmented between build-up functionality of the app and gaming features. The flow of the game should follow the next diagram.
<div align="center">
    <img src="other/window_flow.png" alt="Window Flow Chart" />
    <p><em>In this chart, purple bidirectional arrows mean a strict connection, i.e. if window **A** is accessed through window **B**, it can only go back to window **B** and not any of the other windows for which **A** has connections.</em></p>
</div>
As per usual, this chart might be modified if new windows or panels are added to complete features of the game. Note that the *Game Window* has sub windows and panels, but those are related to the gameplay itself, not the app management. Also, for any sub window of this *Game Window*, all connections from its parent are preserved.
