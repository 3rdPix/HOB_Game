# Functions
> [Main page](README.md)

Functions are callable methods associated to a terminal, whether it is the local machine or the remote server. Most methods need arguments of a certain type. Arguments can be specified after calling the function with `-` token. All arguments are positional. Token functions do not need the `-` indicator. For instance to print something into the console function `echo` should be used.

```
// Since echo is a token, indicator - is not needed
§ echo "this text will be printed" #
§ echo -"this will also work" #
```
For other functions arguments need to specified. Assigning the contents of the file *some_file.txt* to a variable:
```
// Using specifier "-" to indicate argument of function fG
§ some_variable>fG -"some_file.txt" #
```
## Concatenation
When calling a method, sub methods can be concatenated as arguments of the prior function. To specify arguments to the second level specifier token should be used twice, or three times for a third level, and so on. 
```
// We assume some_file.txt is not in the main directory, thus it needs to be searched
// We search for it using fS function that returns the path to the file
§ some_variable>fG -fS --"some_file.txt" #
```
Arguments should be specified immediately after the function is called. If sub level methods are called, their arguments should be specified first with the corresponding specifier tokens.

Suppose we want to call `method1` requiring 2 arguments, we want to give as the first argument the output of `method2` that requires 3 arguments, and as the second argument the output of `method3` that requires 1 argument.

The lexical should be written like:
```
method1 -method2 --arg1_2 --arg2_2 --arg3_2 -method3 --arg1_2
```
Note that this is the same as specifying the arguments in BFS order.
## Available functions

This is a full table of general available functions.

 | Function | Description |
 |:------------:|:------------:|
 | `fG -string` | File get function receives a string with the path to the file and returns the contents of the file. |
 | `fS -string` | File search functions receives a string with the name of a file and search for it in the directory. |
 | `fD -object -string` | File distribution receives a file in the form of a generalized object and sends it to the IP in string. This method ensures that the file is created in the remote machine. |
 | `echo` | Token to print string into console. |
 | `Ev -positional_args -flag` | The event function creates a generalized object for events that can be asigned to variables. It needs one or more argument depending on the flag (See [Events](Events.md)). |
 | `OOP -any` | Creates a generalized object from the argument. Generalized objects can be modified and are use in a wide variety of other functions. (See [OOP](OOP.md)) |
 |`dOOP -any`| Takes a generalized object and degeneralizes it, accepts flags. |
 | `Syncro -any -any -optional_flag` | Syncroes two objects. Syncroed objects share values at all times. Whenever one changes value, the other will be updated. It is possible to indicate a flag *first* if the first argument takes priority, or *second* if the second argument takes priority. Object with priority will be set constant. If a non priority object changes value it is denied and returns to the constant value of prioritized object. If the arguments are not the same type, the function will interpret a random comparable internal property. For instance, the length of a string would be compared to the value of an integer. |
 | `Dsyncro -any -any` | Given two syncroed objects, it disabled the syncronicity of the objects. |
 | `Telefrag -syncro_object` | Given a flagged syncro, it alternates the prioritized object of the syncro. |

 