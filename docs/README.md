# HobL Documentation
![Static Badge](https://img.shields.io/badge/Documentation-incomplete-red)
![Static Badge](https://img.shields.io/badge/Version-0.0.1-purple)

    1. [Introduction to the language](Documentation.md)
    2. [Variables](Variables.md)
    3. [Functions](Functions.md)
    4. [Events](Events.md)


## What is it?

Hackers of Blysis' programming language (HobL) is a script-like command-driven syntax type that is used to interact with the game and solve the problems that it proposes. It is the core mechanic of the game that sustains the hacking experience by providing the player an environment where he can experiment with different code attacks without the need to worry about the troubles a real programming language would arise. This is the language that needs to be used to gain access to Blysis, and it is the language in which the server works.

HobL is the approach taken to obtain different advantages regarding level design and learning curve of the hacking experience in HOB, which include:

 - By providing a specialized unique language, experienced coders have no significant advantage over other players when solving the puzzles the game offers.
 - Creates a learning curve that, although may be steep at the beginning, the later rewards the player gets by researching design patterns and better techniques to approach a determined puzzle make up for that slow start.
 - Weird looking lines with a bunch of unusual characters are embedded in popular culture as to be hacker-related and provides a more exciting experience.

HobL aims to be in the middle of a proper programming language and the cinema/tv-series portrayed image of a hacker code. Thus, it has to look crazy for the unexperienced eye, but rather readable for a player.

Just like in many other games (chess, to mention one), memorizing structures and dedicating a bit of time to learn the mechanic is rewarded with better performing. Despite this, HobL is not obligatory, as the game offers a block game mode where you can do all of HobL without necessarily writing code but using the in-game user interface instead.

## What it's not?

A programming language. It cannot compile, nor is related to any executing environment, nor has the basic tools most programming languages work with. This is purely to be written within the game and make things work inside an instance of the game.

## What it looks like?

As mentioned, HobL is a script-like command-driven language that is intented to work as a terminal, it is structured in a way that most of the funcionalities that it offers can be written in a single line. However, more complex methods and flows can be written in multiple independent lines; the way HobL handles this is using time of execution options and events.

Let's take at what the language looks like comparing these two blocks of code:

**Python**
```
try:
    print('fire')
except error:
    a_certain_object.tick()
```

**HobL**
```
§ echo "fire" ¬ a_certain_object**tick #
```

These two blocks have the same behavior, although they differ in some requirements to be executed; they follow the same principles and handle things in the same way. To be specific, the code tries to print *"fire"* into the console and if it fails (for any reason) it calls the method `tick` from the object `a_certain_object`.

| **Python** | **HobL** |
|:-------:|:------:|
| `print` | `echo` |
| `try/except` | `¬` |
| `a_certain_object.tick()` | `a_certain_object**tick` |

Two special tokens appear in the HobL block, these are `§` used to specify the terminal in which the command should be executed, and `#` that determines when to execute the command. More information about this can be found in the detailed description in [General Rules](Documentation.md) document.

Here's another example that retrieves a file from the server, compared to the **Bash** environment:

**Bash**
```
ssh username@server_ip_address
find / -name example.txt
scp username@server_ip_address:/path/to/example.txt /local/directory
```

**HobL**
```
<< fD -fS --example.txt -<<*IP #
```

In these two blocks we are sending a file from the server to our local machine. The only comparable methods here are the `find` from **Bash** and `fS` from **HobL**, both of them search for a file in the machine (the server machine in this case). It is important to mention that in the **HobL** block we assume we have already hacked the server and are in parallel status.

These are some special characters and tokens used in **HobL**: `§`, `<<`, `¬`, `#`, `"`, `*`, `()`, `-`, `>`, `@`.

## But.. why?

**HobL** allows me to create an experience that portraits the visuals of the code from cinema and tv series while also being somewhat close to what real coding feels like. This is a game, so concepts do not need to be accurate to a developer, they need to be appealing to the player.

Every feature in the language has a reason not just from a development point of view, but from a concept logic point of view too. For example I can mention that time of execution is a thing because sometimes when hacking you a series of commands to be ran as fast as possible and as soon as an event occurs (like when a user plugs a USB-stick a lot commands are run).

## End note

The game is still in early stages of development, so many changes are expected. Any ideas or suggestions should be posted in the [Issues](https://github.com/3rdPix/HOB_Game/issues). The language itself is still in a definition stage, which means some relationships might be deprecated.