# Head First Design Patterns

In this repo I'll be going through Head First Design Principles and programming examples in python.

## Chapters
1. **Strategy Pattern** [Simuduck]
> Strategy pattern lets the algorithm vary independently from the clients that use it.

2. **Observer Pattern** [WeatherData]
> Defines a one-to-many dependency between objects so that when on object changes state, all of its dependenents are notified and updated.

## Design Principles:
1. **Page 9**: Identify aspects of your application that vary and separate them from what stays the same

   
   > Take the parts that vary and encapsulate them, so that later you can alter or extend the parts that vary without affecting those that do not.
   
2. **Page 11**: Program to an interface, not an implementation


3. **Page 23**: Favor composition over inheritence
   
    > Prefer HAS_A to IS_A relationships. It lets you change your behavior at runtime. Composition is used in many design patterns.

4. **Page 54**: Strive for loosely couples designs between objects that interact

   > Flexible designs allow us to build flexible systems that can handle changed, because they minimize interdependency between objects.
