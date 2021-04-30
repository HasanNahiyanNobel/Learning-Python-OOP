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
1. To create a class method we need the `@classmethod` *decorator* just before the method. This method will take the class as its first argument. However, convention to write this is `cls`, not `class`—as the second one is already a keyword in python.
1. Used class method as a setter.
1. Used class method as alternative constructor.
1. Schafer clears the mist:
	- If a method uses `self` somewhere inside—it should be **regular method**.
	- If it uses `cls` inside—should be a **class method**.
	- If it uses neither of them—should be a **static method**.
	


## 4. Inheritance
1. Created an inherited class using `pass`.
1. Used `help` method to have a good overview of the inherited class. This method looks *really* helpful. :3
