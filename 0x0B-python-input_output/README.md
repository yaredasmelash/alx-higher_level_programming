# Python - Input/Output

In this project, I practiced file handling in Python. I used the builtin `with`,
`open`, and `read` functions with the `json` module to read and write files and
serialize and deserialize objects with JSON.

## Tests :heavy_check_mark:

* [tests](./tests): Folder of test files. Provided by Holberton School.

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File        | Prototype               |
| ----------- | ----------------------- |
| `0-read_file.py` | `def read_file(filename=""):` |
| `1-write_file.py` | `def write_file(filename="", text=""):` |
| `2-append_write.py` | `def append_write(filename="", text=""):` |
| `3-to_json_string.py` | `def to_json_string(my_obj):` |
| `4-from_json_string.py` | `def from_json_string(my_str):` |
| `5-save_to_json_file.py` | `def save_to_json_file(my_obj, filename):` |
| `6-load_from_json_file.py` | `def load_from_json_file(filename):` |
| `7-add_item.py` | `def load_from_json_file(filename):` |
| `8-class_to_json.py` | `def class_to_json(obj):` |
| `9-student.py` | `def __init__(self, first_name, last_name, age):` |
| `10-student.py` | `def __init__(self, first_name, last_name, age):` |
| `11-student.py` | `def __init__(self, first_name, last_name, age):` |
| `12-pascal_triangle.py` | `def pascal_triangle(n):`|
| `100-append_after.py` | `def append_after(filename="", search_string="", new_string=""):` |

## Tasks :page_with_curl:

* **0. Read file**
  * [0-read_file.py](./0-read_file.py): Python function that prints the contents of a UTF8 text
  file to standard output.

* **1. Write to a file**
  * [1-write_file.py](./1-write_file.py): Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

* **2. Append to a file**
  * [2-append_write.py](./2-append_write.py): Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
* **3 To JSON string**
  * [3-to_json_string.py](./3-to_json_string.py): Write a function that returns the JSON representation of an object (string):

* **4. From JSON string to Object**
  * [4-from_json_string.py](./4-from_json_string.py): Write a function that returns an object (Python data structure) represented by a JSON string:

* **5. Save Object to a file**
  * [5-save_to_json_file.py](./5-save_to_json_file.py): Write a function that writes an Object to a text file, using a JSON representation: