# Variables in HobL
> [Main page](README.md)
There are four types of variables in HobL. Each variable needs to be linked to a name in order to be referenced later. It is also possible to create ghost variables that hold a name to be referenced with no value nor type.

Values are stored in the machine they are created and cannot be referenced between terminals before entering the parallel status with the desired terminal.

In general, variable names are limited in their syntax; they can only contain upper and lowercase letters of the English alphabet, underscores, and numbers. No spacing is allowed in the name of a variable.

Here are some examples of valid and non-valid names:
```
§ @valid_name
§ @aNoThEr_Valid_namE
§ @32nd_valid_name
§ @not a valid name
§ @ this;name-doesn't work
```

Variables is misleading name, because when a variable is assign, it cannot obtain new values. This means that it is not possible to re-write the content of a variable and save it in the same name. It is possible, however, to pass a stashed version of the variable into a generalized object and modify its properties through OOP's methods.
## Numbers

This is the most basic form of a variable used to store numeric values with no distinction between integer or decimal number. They are initialized by declaring the variable name followed by the assignment token and the number enclosed in parentheses. Decimal numbers use a comma as indicator.

This is an example of how to initialize different numbers:
```
§ my_first_number>(1) #
§ my_second_number>(1000) #
§ my_third_number>(3,14159265) #
```

Mathematical operations can be written inside the definition of the number variable.
```
§ my_calculus_number>(3+3-2) #
§ echo my_calculus_number # // This will print 4
```
## Strings

Text chains are called strings and can be saved in a variable to be referenced later. Strings can contain any [UNICODE](https://home.unicode.org/) character. They need to be initialized between double quotes.

This is an example of how to initialize different strings:
```
§ my_first_string>"some text" #
§ my_second_string>" yet another text 😬" #
§ my_third_string>"注册新账号" #
```

## OOP

General object is a special kind of variable that can act as a container or entering link for different non-value instances. Almost anything can be turned into a generalized object and if done, the instance stashes its properties inside an OOP container. The object can then be referenced later with the name of the variable.

Turn things into generalized objects if they need to be referenced later to read or alter its properties.

To generalize into an object, you must call the `OOP` method of the machine that holds the variable and pass the variable as the argument of the function. This will return the container of the stashed object and allocate it in the declared variable name.
### Generalizing a number or string variable

If we have a constant value number variable that we need to use and modify, it is not possible to do it directly with the variable. We need to generalize first. Then we can use the generalize object to modify the value of the number, but this will only affect the object container. If later we want to save the final value of the number, we must do so with the `dOOP` method.

```
// A number variable that cannot be modified on its own
§ my_number_variable>(1714) #

// We turn it into an object
§ generalized_number>OOP -my_number_variable #

// We can modify the value now
§ generalized_number>(generalized_number+1) #

// But this will only affect the object
§ echo my_number_variable #     // This will print 1714
§ echo generalized_number #     // This will print 1715

// We can save the new value using dOOP with the -do flag
§ dOOP -generalized_number -do #

§ echo my_number_variable #     // This will now print 1715
```

The same principle applies to strings.
```
// A string variable that cannot be modified on its own
§ my_string_variable>"my text" #

// We turn it into an object
§ generalized_string>OOP -my_string_variable #

// We can modify the value now
§ generalized_string>"my longer text" #

// But this will only affect the object
§ echo my_string_variable #     // This will print "my text"
§ echo generalized_string #     // This will print "my longer text"

// We can save the new value using dOOP with the -do flag
§ dOOP -generalized_string -do #

§ echo my_string_variable #     // This will now print "my longer text"
```

Further detail of the flags associated with the methods along with a detailed explanation of the functions can be found in [Functions](Functions.md).

## Event variables

Another special yet important type of variable, it is used to create flows between executions of different commands. They are needed to trigger commands associated with `##` token.

To create an event variable the `Ev` method of the respective terminal must be used. The type of event that triggers the variable depends on the type of variable to which it is linked.

When writing commands to an event variable, the instructions are allocated in a sorted container in the slot of the event. This means all commands associated with the event will execute in the order they were declared.

This an example of how to create an event that triggers when a number changes:
```
§ my_number_variable>(20) #
§ my_event>Ev -my_number_variable -alter #
```

Commands could be linked with this event like this:
```
§ echo "hello" ## my_event
```

There are different available flags associated with each variable type and events could need one or more arguments depending on the focused property that triggers the event itself. Details about the flags and events can be found in [Events](Events.md).
