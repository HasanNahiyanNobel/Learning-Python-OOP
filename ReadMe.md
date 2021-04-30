# Learning Log

Learning from [this](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) tutorial of Corey Schafer.



## 1. Classes and Instances
1. Created a class with `pass`.
1. Created instances of that class and manually added something which I believe should be called class variables.
1. Added `__init__` method to class.
1. Added a method to class. Got a basic understanding of how `self` works.
1. Had a *gooder* understanding of how `self` is actually passed.



## 2. Class Variables
1. Added a class variable and used it in a function of class, only to know that things *doesn't* work like this.
1. Used `self` to access a ~~class~~ instance variable.
1. Used class name instead of `self` to use a variable like static, as per my understanding.



## 3. Class Methods and Static Methods
1. Regular methods of a class automatically takes the instance as the first argument (which we conventionally call `self`).
1. To create a class method we need the `@classmethod` *decorator* just before the method. This method will take the class as its first argument. However, convention to write this is `cls`, not `class`—as the second one is already a keyword in Python.
1. Used class method as a setter.
1. Used class method as alternative constructor.
1. Schafer clears the mist:
	- If a method uses `self` somewhere inside—it should be **regular method**.
	- If it uses `cls` inside—should be a **class method**.
	- If it uses neither of them—should be a **static method**.
	


## 4. Inheritance
1. Created an inherited class using `pass`.
1. Used `help` method to have a good overview of the inherited class. This method looks *really* helpful. :3
1. Learnt how class variable having same name is looked up from the inherited class.
1. Created a new subclass `Manager`.
1. Learnt the use of `isinstance` and `issubclass`.



## 5. Special (Magic/Dunder) Methods
1. `__repr__` is used for logging and debugging stuffs. `__str__` is sort of self-descriptive—like `toString()` method in Java.
1. Learnt a use-case for `__repr__`, but still couldn't quite understand the difference from `__str__`.
1. Used `__str__`. Learnt that in the context of `print()` function, `__str__` is given preference over `__repr__`, and still both can be access but calling them explicitly.
1. Used `__add__` method.
1. Used `__len__` method.



## 6. Property Decorators: Getters, Setters and Deleters
1. Learnt the use of `@property` decorator.
