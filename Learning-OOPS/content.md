# Object-Oriented Programming (OOP) – Python (Clean & Complete Notes)



---

## 1️⃣ Function vs Method

### Function

* A **function** is an independent block of code
* It is **not associated with any class**
* Used for general-purpose logic

```python
def add(a, b):
    return a + b
```

```python
add(2, 3)
```

---

### Method

* A **method** is a function defined **inside a class**
* It usually operates on **object data or class data**

```python
class Car:
    def fuel_type(self):
        return "Petrol or Diesel"
```

#### Key Differences

| Function             | Method                         |
| -------------------- | ------------------------------ |
| Exists independently | Belongs to a class             |
| No `self` parameter  | Uses `self` or `cls`           |
| General logic        | Object- or class-related logic |

---

## 2️⃣ Class and Object

### Class

* A **class** is a blueprint or template
* It defines:

  * Attributes (data)
  * Methods (behavior)

```python
class Car:
    pass
```

---

### Object

* An **object** is an instance of a class
* Objects represent real entities created from the blueprint

```python
my_car = Car("Tata", "Safari")
```

A single class can create **multiple independent objects**.

---

## 3️⃣ Constructor (`__init__`)

* `__init__` is a **special method**
* Automatically executed when an object is created
* Used to initialize instance variables

```python
class Car:
    def __init__(self, brand, name):
        self.__brand = brand
        self.__name = name
```

* `self` refers to the **current object**
* Each object gets its own copy of instance variables

---

## 4️⃣ Instance Variables vs Class Variables

### Instance Variables

* Belong to a **specific object**
* Defined using `self`
* Each object has its **own copy**

```python
self.__brand = brand
self.__name = name
```

---

### Class Variables

* Belong to the **class itself**
* Shared among **all objects** of the class
* Defined outside `__init__`

```python
class Car:
    total_car = 0
```

```python
Car.total_car += 1
```

**Use cases:**

* Counters
* Common configuration
* Shared constants

---

## 5️⃣ Encapsulation

### Definition

**Encapsulation** is the process of **binding data and methods together** and **restricting direct access to internal data**.

---

### Private Variables

* Created using double underscore `__variable`
* Python applies **name mangling** to restrict access

```python
self.__brand
self.__name
```

```python
# Direct access is not allowed
my_car.__brand  # AttributeError
```

---

### Getter Method

* Provides **controlled read access** to private data

```python
def get_brand(self):
    return self.__brand + "!!!"
```

---

### `@property` (Pythonic Encapsulation)

* Allows accessing a method like an attribute
* Preferred way to expose read-only data

```python
@property
def model(self):
    return self.__name
```

```python
my_car.model
```

---

## 6️⃣ Types of Methods in a Class

### 6.1 Instance Methods

* Operate on **object data**
* First parameter is `self`

```python
def full_name(self):
    return f"{self.__brand} {self.__name}"
```

---

### 6.2 Static Methods

* Do **not** depend on object or class state
* Defined using `@staticmethod`
* Used for utility logic related to the class

```python
@staticmethod
def general_description():
    return "Cars are means of Transportation"
```

```python
Car.general_description()
```

---

## 7️⃣ Inheritance

### Definition

**Inheritance** allows a child class to acquire properties and methods of a parent class.

---

### Single Inheritance Example

```python
class Electric_Car(Car):
    def fuel_type(self):
        return "Electric Charge"
```

* Reuses parent class logic
* Enables method overriding

---

## 8️⃣ Polymorphism

### Definition

**Polymorphism** allows the same method name to behave differently depending on the object.

```python
my_tesla.fuel_type()
# Electric Charge

my_car.fuel_type()
# Petrol or Diesel
```

This is achieved through **method overriding**.

---

## 9️⃣ `isinstance()`

* Used to check whether an object belongs to a class or its parent classes
* Supports inheritance-aware type checking

```python
isinstance(my_tesla, Car)
isinstance(my_tesla, Electric_Car)
```

---

## 🔟 Multiple Inheritance

### Definition

**Multiple inheritance** occurs when a class inherits from more than one parent class.

---

### Example

```python
class Battery:
    def battery_info(self):
        return "This battery contains 100kwh"

class Engine:
    def engine_info(self):
        return "This engine is 200CC"

class ElectricCartwo(Battery, Engine, Car):
    pass
```

```python
my_new_tesla = ElectricCartwo("Tesla", "Model S")
my_new_tesla.battery_info()
my_new_tesla.engine_info()
```

---

## 1️⃣1️⃣ Method Resolution Order (MRO)

* Defines the order in which Python searches for methods
* Python uses **C3 linearization**

```python
ElectricCartwo.mro()
```

The order ensures:

* No ambiguity
* No repeated method calls

---

## 1️⃣2️⃣ Core OOP Terminology (Quick Reference)

* **Class**: Blueprint for objects
* **Object**: Instance of a class
* **Encapsulation**: Data hiding with controlled access
* **Inheritance**: Code reuse from parent class
* **Polymorphism**: Same method, different behavior
* **Instance Variable**: Object-specific data
* **Class Variable**: Shared class-level data
* **Instance Method**: Works on object data
* **Static Method**: Utility method without state

---

## 1️⃣3️⃣ Concept Memory Map

```
Function  → Independent
Method    → Inside class

Class     → Blueprint
Object    → Instance

self      → Object context
cls       → Class context
static    → No context

Single parent   → Inheritance
Multiple parent → Multiple inheritance

Same method     → Polymorphism
Hidden data     → Encapsulation
```
