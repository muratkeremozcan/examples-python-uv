# The Liskov Substitution Principle (LSP) states that objects of a superclass
# should be replaceable with objects of its subclasses without breaking the application.

# If class B is a subclass of class A, then we should be able to replace A with B
# without breaking the behavior of the program.

# In the below examples, Square inherits from Rectangle, but they violate LSP because:
# A Rectangle allows independent width/height changes
# But a Square must keep width = height, so changing one affects the other

# This means code expecting a Rectangle might break if given a Square
# violating the principle that subclasses should be substitutable for their base classes.


class Rectangle0:
    def __init__(self, h, w):
        self.h = h
        self.w = w


class Square0(Rectangle0):
    def __init__(self, w):
        self.h = w
        self.w = w


# The 4x4 Square object would no longer be a square if we assign 7 to h.
square = Square0(4)
square.h = 7
print("Square0:", square.h, square.w)


######################


class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h

    # Define set_h to set h
    def set_h(self, h):
        self.h = h

    # Define set_w to set w
    def set_w(self, w):
        self.w = w


class Square(Rectangle):
    def __init__(self, w):
        self.w, self.h = w, w

    # Define set_h to set w and h
    def set_h(self, h):
        self.h = h
        self.w = h

    # Define set_w to set w and h
    def set_w(self, w):
        self.w = w
        self.h = w


# Each of the setter methods of Square change both h and w attributes,
# while setter methods of Rectangle change only one attribute at a time,
# so the Square objects cannot be substituted for Rectangle into programs
# that rely on one attribute staying constant.

square = Square(4)
square.set_h(7)
print("Square:", square.h, square.w)

square.set_w(7)
print("Square:", square.h, square.w)


#############

# when we violate LSP what should we do instead?
# The key is that inheritance should model true "is-a" relationships
# where the child can fully substitute for the parent.
# If you're forcing the relationship, composition is usually the better choice.

# 1. use composition instead of inheritance


class SquareComposition:
    def __init__(self, size):
        self.rectangle = Rectangle(size, size)

    def set_h(self, h):
        self.rectangle.set_h(h)
        self.rectangle.set_w(h)

    def set_w(self, w):
        self.rectangle.set_h(w)
        self.rectangle.set_w(w)


# 2. Extract Common Base Class - Have both inherit from a shared parent:

# class Shape:
# 	def area(self):
# 	  pass

# class Rectangle(Shape): ...
# class Square(Shape): ...

# 3 make class immutable:  If you can't change width/height after creation, the LSP violation disappears:

# class Square:
#     def __init__(self, size):
#         self._size = size
#     @property
#     def size(self):
#         return self._size
#     def with_size(self, new_size):
#         return Square(new_size)


####### Inheritance vs Composition ########


class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


dog = Dog()
print(dog.speak())  # "Woof!"

###
# Problem: What if you need a RobotDog that doesn't eat or sleep like a real dog?
# Composition (Has-A Relationship)


class Speaker:
    def speak(self):
        return "Some sound"


class Dog:
    def __init__(self):
        self.speaker = Speaker()

    def speak(self):
        return "Woof!"


class RobotDog:
    def __init__(self):
        self.speaker = Speaker()

    def speak(self):
        return "Beep!"


## TS version
# class Animal {
#   speak(): string {
#     return "Some sound";
#   }
# }

# class Dog extends Animal {
#   speak(): string {
#     return "Woof!";
#   }
# }

# const dog = new Dog();
# console.log(dog.speak());  // "Woof!"

# composition:
# class Speaker {
#   speak(): string {
#     return "Some sound";
#   }
# }

# class Dog {
#   constructor(private speaker: Speaker) {
#     this.speaker = new Speaker();
#   }

#   speak(): string {
#     return "Woof!";
#   }
# }

# class RobotDog {
#   constructor(private speaker: Speaker) {
#     this.speaker = new Speaker();
#   }

#   speak(): string {
#     return "Beep boop";
#   }
# }

# const dog = new Dog();
# console.log(dog.speak());  // "Woof!"

# const robot = new RobotDog();
# console.log(robot.speak());  // "Beep boop"
