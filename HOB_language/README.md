# HOB Language
## what is it?
To fully experience the game, the player must feel like his actions mean something, and in a game about hacking; writing code is a must. However, we do not want the player to actually write a program, having to take care of all the details, errors and logic behind making a code work. Therefore, the idea of having a *programming language* exclusively for the game does not sound crazy. This way we achieve various things
 - No developers have an advantage by knowing how to code beforehand, nor it matters the language they have experience at.
 - The game has a learning curve, a steep one maybe. The player can feel how learning some keywords, knowing how to optimally group the expressions, and memorizing structures can help in the game outcome. Just like in chess, learning about strategies and such can make you a better player, here, learning the game language will make the player have a better performance.
 - Weird looking lines, a bunch of code with strange letters is embedded in pop culture as to be **hacky** and exciting. Hence, the language should portrait a balance between looking crazy for someone without context, but quite readable for the player even if he is new.
## what it's not
A programming language. It cannot compile, nor is related to any executing environment, nor has the basic tools most programming languages work with. This is purely to be written within the game and make things work inside an instance of the game.
## What it looks like?
HOB is a game of actions, rather than writing files of code it is intented to be closer to a terminal, therefore, single-line commands will be the general case scenario. This does not mean variables can't be created, with their own values and even object instances. Let's take a look at these lines

**Python**
```
try:
    print('fire')
except error:
    a_certain_object.tick()
```
**HOB**
```
§ echo "fire" ¬ a_certain_object**tick #
```
As mentioned early, HOB is not a language but it can be understand as such to recognize some structures. In this scenario, through **Python** we are trying to print the word *fire*, if an error occurs, we call the function tick of the object.

It does exactly the same in *HOB*, first the `§` states the local machine, something that is meant to be ran locally. The `echo` token is to print something in the console. Followed by the *fire* word inside `" "`. The `¬` token asks if the previous command was succesfully executed. If it fails, executes the function `tick` from the object, this is achieved through the `**` indicator. And finally, ends the line with `#`, indicating that this is meant to be executed immediately.

Another example is to try a function on the server
**Bash**
```
ssh username@server_ip_address
find / -name example.txt
scp username@server_ip_address:/path/to/file /local/directory
```
**HOB**
If we have yet to be "in"
```
§ server_object**fD -server_object**fS --example.txt -§*IP ##
```
Or if we gained access to the server beforehand
```
<< fD -fS --example.txt -§*IP #
```
Here we are retrieving the file `example.txt` from the server. Of course, it is completely different from that example in **Bash**, the idea is to share the thought process behind it.

In the first line we assume we have not hacked the server yet, and therefore we do not have access to administrator commands. We run the `fD` (file distribution) function from our generalized `server_object`, and declare as the arguments
1. The file, which we do not know where is it, so we have to find it through the `fS` (file search) function. To this function we give the argument `example.txt`.
2. Our direction to which the file should be sent. This is done by `§*IP`. Accessing the variable (`*`) `IP` from local (`§`).

The second line we are "in", and can run commands directly into the server's terminal.