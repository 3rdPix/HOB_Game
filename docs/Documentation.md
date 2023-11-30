# Documentation for the HOB language
> [Main](README.md)

## Comments
Comments in HOB are placed after `//`.
## Terminal of execution
Commands can be executed in the local machine or in the server's terminal. To specify where it should be ran we must declare the token:
 - `§` for the local machine
 - `<<` for the remote machine

One of these tokens must be included at the beggining of every starting line.
Note that running a command in the remote machine, means the script will executed exactly as it is in the far terminal. This means, if we have locally stored variables, they will not be accesible directly from the other machine unless we specify with the `§` token. This token works as an escape token for our script.

## Time of execution
It is possible to run commands instantly or later whenever a specified event is triggered. It is always necessary to specify when the command should be ran, it is inserted at the end of the command.
 - `#` to run immediately
 - `##` ro tun later. The event should be specified after the token.

## Variables
The possible variable types are:

 - **String**: As in any other language, strings are an array of characters. They should be instanced inside double quotes `" "`.
 - **Number**: No distinction between integer, float, or double here. Numbers should be instanced inside parenthesis `()`, and use a comma for decimals. For instance: `(13,2)`.
 - **General Object**: Represents any entity of the environment. Objects here act as structs with their own variables and methods.
 - **Events**: Used to allocate commands that will be ran whenever the instance occurs.

This is how we could create the different types:

**String**
```
§ name_of_variable>"some_string" #
```
**Number**
```
§ name_of_variable>(12345,6789) #
```
**General Object**

This structure is a bit more complex, but let's say we want to refer to a local file *example.txt*. What we do is declare the variable to be a general object via `OOP`, this will execute the internal method for instancing an object (it will internally turn the argument given to a referable object). In this case, we want to create a variable of a file, so we need to use the `fG` (file get) function from the local machine.
```
§ name_of_variable>OOP -§**fG --"example.txt" #
```
**Event**

There are many types of events, each of which its associated with another type of variable. Event variables are used to allocate commands to be ran whenever the slot is activated. The next is an example of how you would create a variable event to recognize when a certain value is changed.
```
§ number_variable>(15) #
§ event_variable>§**Ev -number_variable -alter #
§ echo number_variable ## event_variable
```
In this segment we created the number variable with a value of 15, then created the event variable associating it to the alter process of the number variable. Finally we allocated the command `echo` to the event variable. This will print the value of `number_variable` whenever its value changes.

Note that the set of available events is associated with the environment in which the command is executed, this is because the `Ev` function is a method of the local machine `§` in this case. The *flag* `-alter` is used to specify what is the trigger.

## Ghost variables
Sometimes we need to initialize a variable without a value. A similar concept is seen in the **C/C++** languages when doing exactly the same:

**C**
```
int some_number;
char some_character;
struct Some* some_structure;
```
Here to initialize a variable without a value we do it with `@`:

**HOB**
```
§ @some_variable
```
Note that the expression does not require to be specified of a time for execution. This is because it just creates a container associated with the name of the variable, it also does not save any type before being specified a value. If we want to assign a value for this container we do it as follows:
```
§ some_varible@(15,7)
```
For a number value, but it could be a string too:
```
§ @my_variable
§ my_variable@"some_string"
```

Ghost variables are mostly used in the later execution of commands, before having access to specific events. For instance, let's say we do not have access to the server yet, but for when we do, we need to detect a remote event that has yet to occur, and execute commands accordingly.

To achieve this, we first create the command we want to be run when the event is triggered. Let's just print *"event occurred"* whenever the value *number of users* in the server changes.
```
§ echo "event ocurred" ## @server_event
```
`server_event` is something we do not have access just yet because it is a remote event. We want that, as soon as we connect to the server, the variable gets assigned the event value. To do this, let's assume we already had created a `connected` event variable that triggers when we are inside the server. With this, we assign:
```
§ server_event@<<**Ev -<<*number_of_users -<<*alter ## connected
```
With only two lines we created a series of triggers and events. The first event will be `connected`, when this happens the command `§ server_event@<<**Ev -number_of_users -alter` will be executed, linking the `server_event` variable to the change of value of `number_of_users` (a server-side variable). Later, if `number_of_users` changes, `server_event` will be triggered and will run the command `echo "event ocurred"` in the local machine.

It is important to note that `number_of_users` is a remote variable hence it needs to be obtained from the `<<` token, as does the `Ev` method and the `alter` flag. Even though our local machine has definitions for these expressions, they might not be the same as to those from the server, therefore, it is needed to use the server's functions and flags.

Also note that the assignment of the variable `server_event` is not done immediately, because before we access the server we can't access its methods or variables.

## Code example
Let's wrap all this and create an example code. This program should automate the process of sending a file to every new user that gets connected to the server. We can build this before we are connected to the server, or when we already gained access to it, here are the two blocks:

**Before**
```
// create the server connection event
§ server_connected_event>§**Ev -<< -alter #

// first send the file from our local machine to the server
§ fD -fG --the_file.txt -<<*IP ## server_connected

// create the new user event in the remote server
<< new_user_event>§**Ev -number_of_users -increase ## server_connected

// associate the distribution of the file for a new user
<< fD -fG --the_file.txt -last_user*IP ## new_user_event
```

**After**
```
// send the file to the server
§ fD -fG --the_file.txt -<<*IP #

// create the new user event
<< new_user_event>§**Ev -number_of_users -increase #

// allocate the command in the event
<< fD -fG --the_file.txt -last_user*IP ## new_user_event
```

As in any other languages, there are many ways in which we can achieve this, these two blocks are just an example of how to approach it.