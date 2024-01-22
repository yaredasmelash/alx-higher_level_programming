# Python - Almost a circle

In this project, I encapsulated skills in Python object-oriented programming
by coding three connected classes to represent rectangles and squares. I wrote my
own test suite using the `unittest` module to test all functionality for each
class.

## Learning Objectives
What you should learn from this project:

* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

The three classes involved utilizing the following Python tools:
* Import
* Exceptions
* Private attributes
* Getter/setter
* Class/static methods
* Inheritance
* File I/O
* `args`/`kwargs`
* JSON and CSV serialization/deserialization
* Unittesting

## Tests :heavy_check_mark:

* [tests/](./tests): Folder containing the following
independently-developed test files:
  * [test_base.py](./tests/test_base.py)
  * [test_rectangle.py](./tests/test_rectangle.py)
  * [test_square.py](./tests/test_square.py)

## Classes :cl:

### [0. If it's not tested it doesn't work](./tests/)
* All your files, classes and methods must be unit tested and be PEP 8 validated. 


### Base
Represents the "base" class for all other classes in the project. Includes:

### [1. Base class](./models/base.py)
* Write the first class Base:

* Private class attribute `__nb_objects = 0`.
* Public instance attribute `id`.
* Class constructor `def __init__(self, id=None):`
  * If `id` is `None`, increments `__nb_objects` and assigns its value to the
  public instance attribute `id`.
  * Otherwise, sets the public instance attribute `id` to the provided `id`.
* Static method `def to_json_string(list_dictionaries):` that returns the JSON
string serialization of a list of dictionaries.
  * If `list_dictionaries` is `None` or empty, returns the string `"[]"`.
* Class method `def save_to_file(cls, list_objs):` that writes the JSON
serialization of a list of objects to a file.
  * The parameter `list_objs` is expected to be a list of `Base`-inherited
  instances.
  * If `list_objs` is `None`, the function saves an empty list.
  * The file is saved with the name `<cls name>.json` (ie. `Rectangle.json`)
  * Overwrites the file if it already exists.
* Static method `def from_json_string(json_string):` that returns a list of
objects deserialized from a JSON string.
  * The parameter `json_string` is expected to be a string representing a
  list of dictionaries.
  * If `json_string` is `None` or empty, the function returns an empty list.
* Class method `def create(cls, **dictionary):` that instantiates an object with
provided attributes.
  * Instantiates an object with the attributes given in `**dictionary`.
* Class method `def load_from_file(cls):` that returns a list of objects
instantiated from a JSON file.
  * Reads from the JSON file `<cls name>.json` (ie. `Rectangle.json`)
  * If the file does not exist, the function returns an empty list.
* Class method `def save_to_file_csv(cls, list_objs):` that writes the CSV
serialization of a list of objects to a file.
  * The parameter `list_objs` is expected to be a list of `Base`-inherited
  instances.
  * If `list_objs` is `None`, the function saves an empty list.
  * The file is saved with the name `<cls name>.csv` (ie. `Rectangle.csv`)
  * Serializes objects in the format `<id>,<width>,<height>,<x>,<y>` for
  `Rectangle` objects and `<id>,<size>,<x>,<y>` for `Square` objects.
* Class method `def load_from_file_csv(cls):` that returns a list of objects
instantiated from a CSV file.
  * Reads from the CSV file `<cls name>.csv` (ie. `Rectangle.csv`)
  * If the file does not exist, the function returns an empty list.
* Static method `def draw(list_rectangles, list_squares):` that draws
`Rectangle` and `Square` instances in a GUI window using the `turtle` module.
  * The parameter `list_rectangles` is expected to be a list of `Rectangle`
  objects to print.
  * The parameter `list_squares` is expected to be a list of `Square` objects
  to print.

### Rectangle

### [2. First Rectangle](./models/rectangle.py)
* Write the class Rectangle that inherits from Base:

Represents a rectangle. Inherits from `Base` with:

* Private instance attributes `__width`, `__height`, `__x`, and `__y`.
  * Each private instance attribute features its own getter/setter.
* Class constructor `def __init__(self, width, height, x=0, y=0, id=None):`

### [3. Validate attributes](./models/rectangle.py)
* Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded):

  * If either of `width`, `height`, `x`, or `y` is not an integer, raises a
  `TypeError` exception with the message `<attribute> must be an integer`.
  * If either of `width` or `height` is >= 0, raises a `ValueError` exception
  with the message `<attribute> must be > 0`.
  * If either of `x` or `y` is less than 0, raises a `ValueError` exception
  with the message `<attribute> must be >= 0`.
  
  ### [4. Area first](./models/rectangle.py)
* Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.

* Public method `def area(self):` that returns the area of the `Rectangle`
instance.

### [5. Display #0](./models/rectangle.py)
* Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here.
* Public method `def display(self):` that prints the `Rectangle` instance to
`stdout` using the `#` character.
  * Prints new lines for the `y` coordinate and spaces for the `x` coordinate.
  
  ### [6. __str__](./models/rectangle.py)
* Update the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>

* Overwrite of `__str__` method to print a `Rectangle` instance in the format
`[Rectangle] (<id>) <x>/<y>`.
 
 ### [7. Display #1](./models/rectangle.py)
* Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y

 ### [8. Update #0](./models/rectangle.py)
* Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute:
 
 ### [9. Update #1](./models/rectangle.py)
* Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes:
 
* Public method `def update(self, *args, **kwargs):` that updates an instance
of a `Rectangle` with the given attributes.
  * `*args` must be supplied in the following order:
    * 1st: `id`
    * 2nd: `width`
    * 3rd: `height`
    * 4th: `x`
    * 5th: `y`
  * `**kwargs` is expected to be a double pointer to a dictionary of new
  key/value attributes to update the `Rectangle` with.
  * `**kwargs` is skipped if `*args` exists.
* Public method `def to_dictionary(self):` that returns the dictionary
representation of a `Rectangle` instance.

### Square
 
 ### [10. And now, the Square!](./models/square.py)
* Write the class Square that inherits from Rectangle:

Represents a square. Inherits from `Rectangle` with:

* Class constructor `def __init__(self, size, x=0, y=0, id=None):`
  * The `width` and `height` of the `Rectangle` superclass are assigned using
  the value of `size`.
* Overwrite of `__str__` method to print a `Square` instance in the format
`[Square] (<id>) <x>/<y>`.
 
 ### [11. Square size](./models/square.py)
* Update the class Square by adding the public getter and setter size
 
 ### [12. Square update](./models/square.py)
* Update the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes:

* Public method `def update(self, *args, **kwargs):` that updates an instance
of a `Square` with the given attributes.
  * `*args` must be supplied in the following order:
    * 1st: `id`
    * 2nd: `size`
    * 3rd: `x`
    * 4th: `y`
  * `**kwargs` is expected to be a double pointer to a dictoinary of new
  key/value attributes to update the `Square` with.
  * `**kwargs` is skipped if `*args` exists.
 
 ### [13. Rectangle instance to dictionary representation](./models/rectangle.py)
* Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle:
 
* Public method `def to_dictionary(self):` that returns the dictionary
representation of a `Square`.
 
 ### [14. Square instance to dictionary representation](./models/square.py)
* Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square:


### [15. Dictionary to JSON string](./models/base.py)
* JSON is one of the standard formats for sharing data representation.


### [16. JSON string to file](./models/base.py)
* Update the class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file:


### [17. JSON string to dictionary](./models/base.py)
* Update the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string:


### [18. Dictionary to Instance](./models/base.py)
* Update the class Base by adding the class method def create(cls, **dictionary): that returns an instance with all attributes already set:


### [19. File to instances](./models/base.py)
* Update the class Base by adding the class method def load_from_file(cls): that returns a list of instances:


### [20. JSON ok, but CSV?](./models/)
* Update the class Base by adding the class methods def save_to_file_csv(cls, list_objs): and def load_from_file_csv(cls): that serializes and deserializes in CSV:


### [21. Let's draw it](./models/base.py)
* Update the class Base by adding the static method def draw(list_rectangles, list_squares): that opens a window and draws all the Rectangles and Squares:

---

## Author
* **Yared Asmelash**
 