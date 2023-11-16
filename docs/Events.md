# Events
    1. [Main page](README.md)
This is a full table of general event flags. Any of these flags must be provided as an argument to the `Ev` function.
 - `alter`: the most generic event recognizition, triggers whenever the variable changes its value, state, or any of its internal properties.
 - `increase`: applies to numbers and strings only. Triggered when number increases value or string increases length.
 - `decrease`: applies to numbers and strings only. Trrigers when number decreaes value or string decreases length.
 - `deletion`: Triggers when the variable is deleted and clear from memory.
 - `equals`: Triggers when argument 1 and argument 2 of `Ev` are equal in value. If the arguments are not the same type, the function will interpret a random comparable internal property. For instance, the length of a string would be compared to the value of an integer.
 - `dequals`: Triggers when argument 1 and argument 2 of `Ev` stop being equal in value. If the arguments are not the same type, the function will interpret a random comparable equal internal property. For instance, the length of a string would be compared to the value of an integer.

Other specific flags:
 - `syncrod`: Triggers when variable is applied to a syncro.
 - `dsyncrod`: Triggers when variable is deleted from a syncro.