> [Main page](README.md)

# Generalized Objects

Objects are the basic unit of abstraction to work in HobL. They are used to change values of variables, to read files, modify its contents, write new files, send files, create events. They are also used to access some otherwise unreferrable properties of the terminal, and many other things.

Except from already general objects, almost anything can be turned into a general object, this will create a duplicate of the object where all its properties are public, allowing you to read, modify, and refer them. For instance, to get the length of a string we do it as follows:
```
// Create the string
§ my_string>"HobL is really fun!!" #

// Create a generalized object from the string
§ crazy_object>OOP -my_string #

// Now we can access some properties of the string
§ echo crazy_object*len #
```
The output would like this:
```
[LOG] 21
```
Note that this code will not work:
```
§ echo my_string*len #
```
Would give:
```
[ERROR] my_string is not an object
```
We provide another example where we modify the value of a number by generalizing it:
```
// Create the number
§ my_number>(1714) #
§ super_object>OOP -my_number #

// We have access to some functions of a generalized number
§ super_object**increase #
§ echo super_object #

§ super_object>(super_object + 1) #
§ echo super_object #

§ super_object**square #
§ echo super_object #
```
The output will look like this:
```
[LOG] 1715
[LOG] 1716
[LOG] 2944656
```
In the above scenario, the variable `my_number` stays the same, it is the generalized object that receives the changes.

## List of objects
We showed that generalized objects have some properties and methods associated with it. This is a list of all the properties and methods related to its origin type.

### Number objects
#### Properties
|Name|Description|
|:---:|:--------:|
|value|The numeric value of the object|
|size| The memory size of the object|
#### Methods
|Name|Description|
|:--:|:---------:|
|increase| Adds 1 to the numeric value|
|decrease| Adds -1 to the numeric value|
|square| Squares the number|
|half| Divides the number by 2|

### String objects
#### Properties
|Name|Description|
|:--:|:---------:|
|value| The text that the variable contains|
|len| The length of the string|
|size| The memory size of the object|
|weigth| The sum of the UNICODE index of all the characters|
#### Methods
|Name|Description|
|:--:|:---------:|
|low| Formats the string to lowercase|
|upr| Formats the string to uppercase|

### Files
Files are objects created through the `fG` function and should be initialized like this:
```
§ file_object>OOP -fG --"path/to/file" #
```
#### Properties
|Name|Description|
|:---:|:--------:|
|size| The memory size of the object|
|value| The contents of the object|
|name| The name of the file|
|path| The path to the file|
|fsize| The memory size of the file|