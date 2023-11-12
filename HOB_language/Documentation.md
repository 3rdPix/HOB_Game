# Documentation for the HOB language
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
`§ name_of_variable>"some_string" #`
**Number**
`§ name_of_variable>(12345,6789) #`
**General Object**
This structure is a bit more complex, but let's say we want to refer to a local file *example.txt*. What we do is declare the variable to be a general object via `OOP`, this will execute the internal method for instancing an object (it will internally turn the argument given to a referable object). In this case, we want to create a variable of a file, so we need to use the `fG` (file get) function from the local machine.
`§ name_of_variable>OOP -§**fG --"example.txt" #`
**Event**
