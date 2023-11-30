# Events
> [Main page](Documentation.md)
## What events are

They refer to the occurrence of an action, that can be initialized either by the user, the terminal, the environment, a function, another event, etc. Examples of events are the mouse movement, a key press, a change in the internal property of an object, etc. 

It is possible through HobL to recognize these events at different levels and in different environments (related to terminal). The main purpose of events is to use them as triggers and link the execution of different custom commands to its occurrence.

In HobL, events are a subset of generalized objects and as such they need to be declared through a method `Ev` available specifically at the terminal on which the event should occur. Note that events are linked to the terminal in which they are constructed, even if more than one terminal can have the same event or even if it occurs at more than one terminal, only the terminal in which the declaration of event recognition was done will trigger its linked commands.
## How to use events

As mentioned, events are a type of generalized object variable that needs to be initialized through the `Ev` method. The form and type of event is limited to the type of object to which it relates, for instance, a number variable may have an event related to the increment in its numerical value, but a string cannot have this property unless we specify some internal property of the string that has the property of not being a string but a number; for instance, its length.

Events act as containers for all the commands that you link to the event. These commands are stored inside the event object and will be executed in the same order in which they were created. Once the last command is executed the event is destroyed, this means the variable is no longer existent, no new commands can be associated to it, and if the event were to occur again, nothing will be executed.

This is an example of how to create an event related to the increase of the value of a number.
```
// First we create the number variable
§ my_number>(1714) #

// Then create the event
§ my_event>Ev -my_number -increase #
```
Note that we give arguments to the `Ev` method; the first one being the object we want to "observe", and the second argument corresponds to an event flag. 

## Events flags

Flags are the set of possible events related to the different type of objects available in HobL. Some object may share some flags but not all of them have the same properties. To create an event it is necessary to specify a flag, this will tell HobL what does it need to look out for in the object. Some flags relate one or more objects. The next is a full listing of all the event flags and its utilization.

| Flag | Applies to | Description |
|:-----:|:------------:|:-----------------------:|
|`alter`|any object|Triggers whenever some internal property of the object changes, it is the most general type of flag and can trigger very easily, be careful when to use.|
|`increase`|numbers|Triggers when the numerical value of a number increases.|
|`decrease`|numbers|Triggers when the numerical value of a number decreases.|
|`deletion`|any object|Triggers when the object is deleted and cleared from memory.|
|`equals`|numbers, strings|Triggers when one of two specified objects of the same type changes its value, making it equal to the other.|
|`dequals`|numbers, strings|Triggers when one of two specified objects that shared value changes.|
|`syncrod`|any object applicable to a syncro|Triggers when a syncro is applied over the object.|
|`dsyncrod`|any object that has a syncro|Triggers when the object is deleted from the syncro.|
|`connected`|terminal|Triggers when the current terminal is connected to a remote terminal.|
|`dconnected`|terminal|Triggers when the current terminal is disconnected from the remote terminal.|
|`verbose`|strings|Triggers when the variable increases its length.|
|`dverbose`|strings|Triggers when the variable decreases its lentgh.|
|`weighted`|strings|Triggers when the weight (the sum of the UNICODE index of each letter) of the string increases.|
|`dweighted`|strings|Triggers when the weight of the string decreases.|
