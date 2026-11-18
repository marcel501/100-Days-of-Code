Python object oriented programming learning pathway
===================================================

# Introduction

Object oriented programming (OOP) is one of the main features of the python language. It allows for more intuitive programming methodology which offers vastly different capabilities to procedural programming.




## Background


As a Imperative based paradigm OOP focuses on the object in mind. That object can be anything concrete such as a specific button, person, house, road, planet, etc. Such objects are generally grouped under what is called a class, which is a generic specification of that object and defines what qualities it may have. A planet for example may have a radius while a house may have an area or height.

Objects are defined utilising the class specification. A specific name and height for a person; radius and name for the planet, and other specific objects may be defined based on initial specifications. In the context of computers, buttons or toggles may be modeled such that it has a name, possible states and the function of those states. Such definitions are called attributes, and they describe the object.

Methods are another element of OOP. These are essentially functions which exist within the object. Since it is specified by a class, each instance will have the same functions; however, the execution is scoped to that particular instance. The example of toggling a toggle will mean a method will be called in a specific toggle object (dark mode toggle for example).





___

# Python OOP

Like described in the background, Python OOP is composed of classes, objects, attributes and methods.

The relation between these elements can be visualised in a hierarchical format.

```
                    ---------
                    | Class |
                    ---------
                        |
                        |
                       \|/
                    ----------
                    | Object |
                    ----------
                        |
                -----------------
               \|/             \|/
            ----------    -------------
            | Method |    | Attribute |
            ----------    -------------
```




## Class

A class is a top level element of OOP which defines a generic specification (template) for which object instances can be created.

Class creation is the first step into the OOP workflow. The simplest format of a class is:
```
class <name_of_class>:
    
    # Attribute specifications
    <attribute1> = <value>
    <attribute2> = <value>
    <attribute3> = <value>
    
    # Method specifications
    def <method1>():
        <statement>

    def <method2>():
        <statement>
```

Two main points must be known to construct a class: Its attributes and methods.

While the simple format of the class may be sufficient, it may present problems later down the line. The issue is presented due to shared mutability, which is a state where the class attributes are both shared and mutable to all its instances. This allows all objects to change the class attributes if the object itself is not selected. The solution to shared mutability is to eliminate the possibility of sharing, mutability or both.

This is what the "__init__" method proves to solve, it essentially is a method which wraps the attributes such that all instances are contained under their own object initialisation (no access to the class).

The contained format of a class therefore becomes:
```
class <name_of_class>:
  
    # First method: initialisation of scoped attributes
    def __init__(self, <attribute1>, <attribute2>, <attribute3>):
        <attribute1> = self
        <attribute2> = self
        <attribute3> = self
    
    def <method2>():
        <statement>

    def <method3>():
        <statement>
```

The most powerful keywords in the concept of a contained class is the "self" keyword. This allows the class to function as a dynamic template, allowing objects to have their own environment and customised behaviour under the specifications of the class itself.




## Object

An object is a discrete 'thing' which an instance of a class, which in turn is a specification of a generic object.

Objects are first created. This is done by calling the class to create an instance (a virtual copy of the class) which then can be manipulated. The first step within objects, is to define attributes (what it has); then define its methods (what it does).

An object can be initiated with a contained example class "people" using:
```
Amy = people("Amy", 'F')
```




## Principles

Along with the basic definitions of OOP elements, OOP features several distinctive principles which guide developers on how such elements should be optimally used.



### Encapsulation

Encapsulation is one of the principles of OOP which describes how an object controls its own data. In respect to this, state is the current set value for a particular attribute for an object.



### Inheritance

Principle of OOP which describes how classes can inherit methods and attributes from other classes:
```
                        -----------
                        | Class 1 |
                        -----------
                             |
                     -----------------
                    \|/             \|/
                -----------     -----------
                | Class 2 |     | Class 4 |
                -----------     -----------
                     |        
                     |       
                    \|/     
                -----------
                | Class 3 |
                -----------
```

This is a powerful structure which enables higher order grouping capabilities - objects may have data related to many things. The last class (instance declaration class) offers the most specific specification towards the object, such class shall only include specifications which are necessary - more generic specifications can be provided in the parent class (the class before it).

Such a structure produces a tree like structure which functions on parent classes and children classes - this is the indication of traversal within such structure.

In terms of an object, the structure is irrelevant. All specifications (inherited or not) are treated as if they where within the same template class - everything stays relatively the same, its only the class based perspective that changes.



### Polymorphism

A principle of OOP describing the capability of a single method to have a different function for different objects.



### Abstraction

Another principle of OOP allowing the inclusion of logic to object creation. It is effectively a rule within OOP which allows a complete definition of objects utilising abstract methods to check the objects data against a particular rule.



### Composition

Powerful principle of OOP which combines the focused capabilities of objects to perform a complex task.

An object can influence other objects, such as calling a method or creating a new object.



