0x00. AirBnB clone - The console
================================

-   By Guillaume
-   Weight: 5
-   Project to be done in teams of 2 people (My team: Arsene Awounou, Pericles Adjovi)

Concepts
--------

*For this project, students are expected to look at these concepts:*

-   [Python packages](https://alx-intranet.hbtn.io/concepts/66)
-   [AirBnB clone](https://alx-intranet.hbtn.io/concepts/74)

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png)

Background Context
------------------

### Welcome to the AirBnB clone project!

Before starting, please read the **AirBnB** concept page.

#### First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the **AirBnB clone**. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration...

Each task is linked and will help you to:

-   put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
-   create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
-   create all classes used for AirBnB (`User`, `State`, `City`, `Place`...) that inherit from `BaseModel`
-   create the first abstracted storage engine of the project: File storage.
-   create all unittests to validate all our classes and storage engine

### What's a command interpreter?

Do you remember the Shell? It's exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc...
-   Do operations on objects (count, compute stats, etc...)
-   Update attributes of an object
-   Destroy an object

Resources
---------

**Read or watch**:

-   [cmd module](https://alx-intranet.hbtn.io/rltoken/MwtmYsEqfmskPrrNiHL0Og "cmd module")
-   **packages** concept page
-   [uuid module](https://alx-intranet.hbtn.io/rltoken/ELAIbw03WT2ItzQOyrd2Pw "uuid module")
-   [datetime](https://alx-intranet.hbtn.io/rltoken/E6QCDx3_woD6929Q0zPPzQ "datetime")
-   [unittest module](https://alx-intranet.hbtn.io/rltoken/op1-rQGlw0wwwqNBsn1yaw "unittest module")
-   [args/kwargs](https://alx-intranet.hbtn.io/rltoken/C_a0EKbtvKdMcwIAuSIZng "args/kwargs")
-   [Python test cheatsheet](https://alx-intranet.hbtn.io/rltoken/tgNVrKKzlWgS4dfl3mQklw "Python test cheatsheet")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/uV5eZkRZ_XEqYbgPd-0CWw "explain to anyone"), **without the help of Google**:

### General

-   How to create a Python package
-   How to create a command interpreter in Python using the `cmd` module
-   What is Unit testing and how to implement it in a large project
-   How to serialize and deserialize a Class
-   How to write and read a JSON file
-   How to manage `datetime`
-   What is an `UUID`
-   What is `*args` and how to use it
-   What is `**kwargs` and how to use it
-   How to handle named arguments in a function

Requirements
------------

### Python Scripts

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/python3`
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should use the pycodestyle (version 2.7.*)
-   All your files must be executable
-   The length of your files will be tested using `wc`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files should end with a new line
-   All your test files should be inside a folder `tests`
-   You have to use the [unittest module](https://alx-intranet.hbtn.io/rltoken/op1-rQGlw0wwwqNBsn1yaw "unittest module")
-   All your test files should be python files (extension: `.py`)
-   All your test files and folders should start by `test_`
-   Your file organization in the tests folder should be the same as your project
-   e.g., For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
-   e.g., For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`
-   All your tests should be executed by using this command: `python3 -m unittest discover tests`
-   You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   We strongly encourage you to work together on test cases, so that you don't miss any edge case

### GitHub

**There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.**

More Info
---------

### Execution

Your shell should work like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

```

But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$

```

All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220126%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220126T142403Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=db13f7de2403e20e8f99f5bc5deb7e4ef086e7cfea3e5d69a31d238e47a378f8)

Tasks
-----

### 0\. README, AUTHORS

mandatory

-   Write a `README.md`:
    -   description of the project
    -   description of the command interpreter:
        -   how to start it
        -   how to use it
        -   examples
-   You should have an `AUTHORS` file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference [Docker's AUTHORS page](https://alx-intranet.hbtn.io/rltoken/_8n_z3pf5HWi1l7uv1E9iA "Docker's AUTHORS page")
-   You should use branches and pull requests on GitHub - it will help you as team to organize your work

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   File: `README.md, AUTHORS`

### 1\. Be pycodestyle compliant!

mandatory

Write beautiful code that passes the pycodestyle checks.

**Repo:**

-   GitHub repository: `AirBnB_clone`

### 2\. Unittests

mandatory

All your files, classes, functions must be tested with unit tests

```
guillaume@ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$

```

*Note that this is just an example, the number of tests you create can be different from the above example*.

**Warning:**

Unit tests must also pass in non-interactive mode:

```
guillaume@ubuntu:~/AirBnB$ echo "python3 -m unittest discover tests" | bash
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/AirBnB$

```

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   File: `tests/`

### 3\. BaseModel

mandatory

Write a class `BaseModel` that defines all common attributes/methods for other classes:

-   `models/base_model.py`
-   Public instance attributes:
    -   `id`: string - assign with an `uuid` when an instance is created:
        -   you can use `uuid.uuid4()` to generate unique `id` but don't forget to convert to a string
        -   the goal is to have unique `id` for each `BaseModel`
    -   `created_at`: datetime - assign with the current datetime when an instance is created
    -   `updated_at`: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
-   `__str__`: should print: `[<class name>] (<self.id>) <self.__dict__>`
-   Public instance methods:
    -   `save(self)`: updates the public instance attribute `updated_at` with the current datetime
    -   `to_dict(self)`: returns a dictionary containing all keys/values of `__dict__` of the instance:
        -   by using `self.__dict__`, only instance attributes set will be returned
        -   a key `__class__` must be added to this dictionary with the class name of the object
        -   `created_at` and `updated_at` must be converted to string object in ISO format:
            -   format: `%Y-%m-%dT%H:%M:%S.%f` (ex: `2017-06-14T22:31:03.285259`)
            -   you can use `isoformat()` of `datetime` object
        -   This method will be the first piece of the serialization/deserialization process: create a dictionary representation with "simple object type" of our `BaseModel`

```
guillaume@ubuntu:~/AirBnB$ cat test_base_model.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

guillaume@ubuntu:~/AirBnB$ ./test_base_model.py
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
{'my_number': 89, 'name': 'My First Model', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
JSON of my_model:
    my_number: (<class 'int'>) - 89
    name: (<class 'str'>) - My First Model
    __class__: (<class 'str'>) - BaseModel
    updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
    id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
    created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427

guillaume@ubuntu:~/AirBnB$

```

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   File: `models/base_model.py, models/__init__.py, tests/`

### 4\. Create BaseModel from dictionary

mandatory

Previously we created a method to generate a dictionary representation of an instance (method `to_dict()`).

Now it's time to re-create an instance with this dictionary representation.

```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>

```

Update `models/base_model.py`:

-   `__init__(self, *args, **kwargs)`:
    -   you will use `*args, **kwargs` arguments for the constructor of a `BaseModel`. (more information inside the **AirBnB clone** concept page)
    -   `*args` won't be used
    -   if `kwargs` is not empty:
        -   each key of this dictionary is an attribute name (**Note** `__class__` from `kwargs` is the only one that should not be added as an attribute. See the example output, below)
        -   each value of this dictionary is the value of this attribute name
        -   **Warning**: `created_at` and `updated_at` are strings in this dictionary, but inside your `BaseModel` instance is working with `datetime` object. You have to convert these strings into `datetime` object. Tip: you know the string format of these datetime
    -   otherwise:
        -   create `id` and `created_at` as you did previously (new instance)

```
guillaume@ubuntu:~/AirBnB$ cat test_base_model_dict.py
#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)

guillaume@ubuntu:~/AirBnB$ ./test_base_model_dict.py
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
<class 'datetime.datetime'>
--
{'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': '2017-09-28T21:03:54.052298', '__class__': 'BaseModel', 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302', 'name': 'My_First_Model'}
JSON of my_model:
    id: (<class 'str'>) - 56d43177-cc5f-4d6c-a0c1-e167f8c27337
    created_at: (<class 'str'>) - 2017-09-28T21:03:54.052298
    __class__: (<class 'str'>) - BaseModel
    my_number: (<class 'int'>) - 89
    updated_at: (<class 'str'>) - 2017-09-28T21:03:54.052302
    name: (<class 'str'>) - My_First_Model
--
56d43177-cc5f-4d6c-a0c1-e167f8c27337
[BaseModel] (56d43177-cc5f-4d6c-a0c1-e167f8c27337) {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337', 'created_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52298), 'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 3, 54, 52302), 'name': 'My_First_Model'}
<class 'datetime.datetime'>
--
False
guillaume@ubuntu:~/AirBnB$

```

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   File: `models/base_model.py, tests/`

### 5\. Store first object

mandatory

Now we can recreate a `BaseModel` from another one by using a dictionary representation:

```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>

```

It's great but it's still not persistent: every time you launch the program, you don't restore all objects created before... The first way you will see here is to save these objects to a file.

Writing the dictionary representation to a file won't be relevant:

-   Python doesn't know how to convert a string to a dictionary (easily)
-   It's not human readable
-   Using this file with another program in Python or other language will be hard.

So, you will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.

Now the flow of serialization-deserialization will be:

```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>

```

Magic right?

Terms:

-   **simple Python data structure**: Dictionaries, arrays, number and string. ex: `{ '12': { 'numbers': [1, 2, 3], 'name': "John" } }`
-   **JSON string representation**: String representing a simple data structure in JSON format. ex: `'{ "12": { "numbers": [1, 2, 3], "name": "John" } }'`

Write a class `FileStorage` that serializes instances to a JSON file and deserializes JSON file to instances:

-   `models/engine/file_storage.py`
-   Private class attributes:
    -   `__file_path`: string - path to the JSON file (ex: `file.json`)
    -   `__objects`: dictionary - empty but will store all objects by `<class name>.id` (ex: to store a `BaseModel` object with `id=12121212`, the key will be `BaseModel.12121212`)
-   Public instance methods:
    -   `all(self)`: returns the dictionary `__objects`
    -   `new(self, obj)`: sets in `__objects` the `obj` with key `<obj class name>.id`
    -   `save(self)`: serializes `__objects` to the JSON file (path: `__file_path`)
    -   `reload(self)`: deserializes the JSON file to `__objects` (only if the JSON file (`__file_path`) exists ; otherwise, do nothing. If the file doesn't exist, no exception should be raised)

Update `models/__init__.py`: to create a unique `FileStorage` instance for your application

-   import `file_storage.py`
-   create the variable `storage`, an instance of `FileStorage`
-   call `reload()` method on this variable

Update `models/base_model.py`: to link your `BaseModel` to `FileStorage` by using the variable `storage`

-   import the variable `storage`
-   in the method `save(self)`:
    -   call `save(self)` method of `storage`
-   `__init__(self, *args, **kwargs)`:
    -   if it's a new instance (not from a dictionary representation), add a call to the method `new(self)` on `storage`

```
guillaume@ubuntu:~/AirBnB$ cat test_save_reload_base_model.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)

guillaume@ubuntu:~/AirBnB$ cat file.json
cat: file.json: No such file or directory
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
-- Create a new object --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'my_number': 89, 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d'}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'name': 'My_First_Model', 'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372)}
-- Create a new object --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'name': 'My_First_Model', 'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'my_number': 89, 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301)}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py
-- Reloaded objects --
[BaseModel] (080cce84-c574-4230-b82a-9acb74ad5e8c) {'id': '080cce84-c574-4230-b82a-9acb74ad5e8c', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973308), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 51, 973301), 'name': 'My_First_Model', 'my_number': 89}
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'updated_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47381), 'created_at': datetime.datetime(2017, 9, 28, 21, 7, 25, 47372), 'name': 'My_First_Model', 'my_number': 89}
-- Create a new object --
[BaseModel] (e79e744a-55d4-45a3-b74a-ca5fae74e0e2) {'id': 'e79e744a-55d4-45a3-b74a-ca5fae74e0e2', 'updated_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151750), 'created_at': datetime.datetime(2017, 9, 28, 21, 8, 6, 151711), 'name': 'My_First_Model', 'my_number': 89}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.e79e744a-55d4-45a3-b74a-ca5fae74e0e2": {"__class__": "BaseModel", "id": "e79e744a-55d4-45a3-b74a-ca5fae74e0e2", "updated_at": "2017-09-28T21:08:06.151750", "created_at": "2017-09-28T21:08:06.151711", "name": "My_First_Model", "my_number": 89}, "BaseModel.080cce84-c574-4230-b82a-9acb74ad5e8c": {"__class__": "BaseModel", "id": "080cce84-c574-4230-b82a-9acb74ad5e8c", "updated_at": "2017-09-28T21:07:51.973308", "created_at": "2017-09-28T21:07:51.973301", "name": "My_First_Model", "my_number": 89}, "BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"__class__": "BaseModel", "id": "ee49c413-023a-4b49-bd28-f2936c95460d", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "my_number": 89}}
guillaume@ubuntu:~/AirBnB$

```

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   File: `models/engine/file_storage.py, models/engine/__init__.py, models/__init__.py, models/base_model.py, tests/`

### 6\. Console 0.0.1

mandatory

Write a program called `console.py` that contains the entry point of the command interpreter:

-   You must use the module `cmd`
-   Your class definition must be: `class HBNBCommand(cmd.Cmd):`
-   Your command interpreter should implement:
    -   `quit` and `EOF` to exit the program
    -   `help` (this action is provided by default by `cmd` but you should keep it updated and documented as you work through tasks)
    -   a custom prompt: `(hbnb)`
    -   an empty line + `ENTER` shouldn't execute anything
-   Your code should not be executed when imported

**Warning:**

You should end your file with:

```
if __name__ == '__main__':
    HBNBCommand().cmdloop()

```

to make your program executable except when imported. Please don't add anything around - the Checker won't like it otherwise

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) help quit
Quit command to exit the program

(hbnb)
(hbnb)
(hbnb) quit
guillaume@ubuntu:~/AirBnB$

```

**No unittests needed**

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   File: `console.py`

### 7\. Console 0.1

mandatory

Update your command interpreter (`console.py`) to have these commands:

-   `create`: Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`. Ex: `$ create BaseModel`
    -   If the class name is missing, print `** class name missing **` (ex: `$ create`)
    -   If the class name doesn't exist, print `** class doesn't exist **` (ex: `$ create MyModel`)
-   `show`: Prints the string representation of an instance based on the class name and `id`. Ex: `$ show BaseModel 1234-1234-1234`.
    -   If the class name is missing, print `** class name missing **` (ex: `$ show`)
    -   If the class name doesn't exist, print `** class doesn't exist **` (ex: `$ show MyModel`)
    -   If the `id` is missing, print `** instance id missing **` (ex: `$ show BaseModel`)
    -   If the instance of the class name doesn't exist for the `id`, print `** no instance found **` (ex: `$ show BaseModel 121212`)
-   `destroy`: Deletes an instance based on the class name and `id` (save the change into the JSON file). Ex: `$ destroy BaseModel 1234-1234-1234`.
    -   If the class name is missing, print `** class name missing **` (ex: `$ destroy`)
    -   If the class name doesn't exist, print `** class doesn't exist ** (ex:`$ destroy MyModel`)`
    -   If the `id` is missing, print `** instance id missing **` (ex: `$ destroy BaseModel`)
    -   If the instance of the class name doesn't exist for the `id`, print `** no instance found **` (ex: `$ destroy BaseModel 121212`)
-   `all`: Prints all string representation of all instances based or not on the class name. Ex: `$ all BaseModel` or `$ all`.
    -   The printed result must be a list of strings (like the example below)
    -   If the class name doesn't exist, print `** class doesn't exist **` (ex: `$ all MyModel`)
-   `update`: Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`.
    -   Usage: `update <class name> <id> <attribute name> "<attribute value>"`
    -   Only one attribute can be updated at the time
    -   You can assume the attribute name is valid (exists for this model)
    -   The attribute value must be casted to the attribute type
    -   If the class name is missing, print `** class name missing **` (ex: `$ update`)
    -   If the class name doesn't exist, print `** class doesn't exist **` (ex: `$ update MyModel`)
    -   If the `id` is missing, print `** instance id missing **` (ex: `$ update BaseModel`)
    -   If the instance of the class name doesn't exist for the `id`, print `** no instance found **` (ex: `$ update BaseModel 121212`)
    -   If the attribute name is missing, print `** attribute name missing **` (ex: `$ update BaseModel existing-id`)
    -   If the value for the attribute name doesn't exist, print `** value missing **` (ex: `$ update BaseModel existing-id first_name`)
    -   All other arguments should not be used (Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty"` = `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`)
    -   `id`, `created_at` and `updated_at` cant' be updated. You can assume they won't be passed in the `update` command
    -   Only "simple" arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime

Let's add some rules:

-   You can assume arguments are always in the right order
-   Each arguments are separated by a space
-   A string argument with a space must be between double quote
-   The error management starts from the first argument to the last one

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
(hbnb) create BaseModel
2dd6ef5c-467c-4f82-9521-a772ea7d84e9
(hbnb) all BaseModel
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)

```

**No unittests needed**

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   File: `console.py`

### 8\. First User

mandatory

Write a class `User` that inherits from `BaseModel`:

-   `models/user.py`
-   Public class attributes:
    -   `email`: string - empty string
    -   `password`: string - empty string
    -   `first_name`: string - empty string
    -   `last_name`: string - empty string

Update `FileStorage` to manage correctly serialization and deserialization of `User`.

Update your command interpreter (`console.py`) to allow `show`, `create`, `destroy`, `update` and `all` used with `User`.

```
guillaume@ubuntu:~/AirBnB$ cat test_save_reload_user.py
#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)

guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"__class__": "BaseModel", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"__class__": "BaseModel", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287"}, "BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"__class__": "BaseModel", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"__class__": "BaseModel", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at": "2017-09-28T21:11:13.753337"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"__class__": "BaseModel", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {'id': '38a22b25-ae9c-4fa9-9f94-59b3eb51bfba', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347)}
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {'id': '9bf17966-b092-4996-bd33-26a5353cccb4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963049), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963058)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333852), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333862)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {'id': 'a42ee380-c959-450e-ad29-c840a898cfce', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504287), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504296)}
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544)}
-- Create a new User --
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'email': 'airbnb@mail.com', 'first_name': 'Betty', 'last_name': 'Bar', 'password': 'root'}
-- Create a new User 2 --
[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {'id': 'd0ef8146-4664-4de5-8e89-096d667b728e', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), 'email': 'airbnb2@mail.com', 'first_name': 'John', 'password': 'root'}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "updated_at": "2017-09-28T21:11:12.971544", "created_at": "2017-09-28T21:11:12.971521", "__class__": "BaseModel"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "updated_at": "2017-09-28T21:11:13.753347", "created_at": "2017-09-28T21:11:13.753337", "__class__": "BaseModel"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"id": "9bf17966-b092-4996-bd33-26a5353cccb4", "updated_at": "2017-09-28T21:11:14.963058", "created_at": "2017-09-28T21:11:14.963049", "__class__": "BaseModel"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "updated_at": "2017-09-28T21:11:14.333862", "created_at": "2017-09-28T21:11:14.333852", "__class__": "BaseModel"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"id": "a42ee380-c959-450e-ad29-c840a898cfce", "updated_at": "2017-09-28T21:11:15.504296", "created_at": "2017-09-28T21:11:15.504287", "__class__": "BaseModel"}, "User.38f22813-2753-4d42-b37c-57a17f1e4f88": {"id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "created_at": "2017-09-28T21:11:42.848279", "updated_at": "2017-09-28T21:11:42.848291", "email": "airbnb@mail.com", "first_name": "Betty", "__class__": "User", "last_name": "Bar", "password": "root"}, "User.d0ef8146-4664-4de5-8e89-096d667b728e": {"id": "d0ef8146-4664-4de5-8e89-096d667b728e", "created_at": "2017-09-28T21:11:42.848280", "updated_at": "2017-09-28T21:11:42.848294", "email": "airbnb_2@mail.com", "first_name": "John", "__class__": "User", "password": "root"}}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ ./test_save_reload_user.py
-- Reloaded objects --
[BaseModel] (af9b4cbd-2ce1-4e6e-8259-f578097dd15f) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971544), 'id': 'af9b4cbd-2ce1-4e6e-8259-f578097dd15f', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 12, 971521)}
[BaseModel] (2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333862), 'id': '2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 333852)}
[BaseModel] (9bf17966-b092-4996-bd33-26a5353cccb4) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963058), 'id': '9bf17966-b092-4996-bd33-26a5353cccb4', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 14, 963049)}
[BaseModel] (a42ee380-c959-450e-ad29-c840a898cfce) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504296), 'id': 'a42ee380-c959-450e-ad29-c840a898cfce', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 15, 504287)}
[BaseModel] (38a22b25-ae9c-4fa9-9f94-59b3eb51bfba) {'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753347), 'id': '38a22b25-ae9c-4fa9-9f94-59b3eb51bfba', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 13, 753337)}
[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'email': 'airbnb@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'last_name': 'Bar', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88', 'first_name': 'Betty'}
[User] (d0ef8146-4664-4de5-8e89-096d667b728e) {'password': '63a9f0ea7bb98050796b649e85481845', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848280), 'email': 'airbnb_2@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848294), 'id': 'd0ef8146-4664-4de5-8e89-096d667b728e', 'first_name': 'John'}
-- Create a new User --
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'password': 'root', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'email': 'airbnb@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'last_name': 'Bar', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68', 'first_name': 'Betty'}
-- Create a new User 2 --
[User] (fce12f8a-fdb6-439a-afe8-2881754de71c) {'password': 'root', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611354), 'email': 'airbnb_2@mail.com', 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611368), 'id': 'fce12f8a-fdb6-439a-afe8-2881754de71c', 'first_name': 'John'}
guillaume@ubuntu:~/AirBnB$
guillaume@ubuntu:~/AirBnB$ cat file.json ; echo ""
{"BaseModel.af9b4cbd-2ce1-4e6e-8259-f578097dd15f": {"updated_at": "2017-09-28T21:11:12.971544", "__class__": "BaseModel", "id": "af9b4cbd-2ce1-4e6e-8259-f578097dd15f", "created_at": "2017-09-28T21:11:12.971521"}, "User.38f22813-2753-4d42-b37c-57a17f1e4f88": {"password": "63a9f0ea7bb98050796b649e85481845", "created_at": "2017-09-28T21:11:42.848279", "email": "airbnb@mail.com", "id": "38f22813-2753-4d42-b37c-57a17f1e4f88", "last_name": "Bar", "updated_at": "2017-09-28T21:11:42.848291", "first_name": "Betty", "__class__": "User"}, "User.d0ef8146-4664-4de5-8e89-096d667b728e": {"password": "63a9f0ea7bb98050796b649e85481845", "created_at": "2017-09-28T21:11:42.848280", "email": "airbnb_2@mail.com", "id": "d0ef8146-4664-4de5-8e89-096d667b728e", "updated_at": "2017-09-28T21:11:42.848294", "first_name": "John", "__class__": "User"}, "BaseModel.9bf17966-b092-4996-bd33-26a5353cccb4": {"updated_at": "2017-09-28T21:11:14.963058", "__class__": "BaseModel", "id": "9bf17966-b092-4996-bd33-26a5353cccb4", "created_at": "2017-09-28T21:11:14.963049"}, "BaseModel.a42ee380-c959-450e-ad29-c840a898cfce": {"updated_at": "2017-09-28T21:11:15.504296", "__class__": "BaseModel", "id": "a42ee380-c959-450e-ad29-c840a898cfce", "created_at": "2017-09-28T21:11:15.504287"}, "BaseModel.38a22b25-ae9c-4fa9-9f94-59b3eb51bfba": {"updated_at": "2017-09-28T21:11:13.753347", "__class__": "BaseModel", "id": "38a22b25-ae9c-4fa9-9f94-59b3eb51bfba", "created_at": "2017-09-28T21:11:13.753337"}, "BaseModel.2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4": {"updated_at": "2017-09-28T21:11:14.333862", "__class__": "BaseModel", "id": "2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4", "created_at": "2017-09-28T21:11:14.333852"}, "User.246c227a-d5c1-403d-9bc7-6a47bb9f0f68": {"password": "root", "created_at": "2017-09-28T21:12:19.611352", "email": "airbnb@mail.com", "id": "246c227a-d5c1-403d-9bc7-6a47bb9f0f68", "last_name": "Bar", "updated_at": "2017-09-28T21:12:19.611363", "first_name": "Betty", "__class__": "User"}, "User.fce12f8a-fdb6-439a-afe8-2881754de71c": {"password": "root", "created_at": "2017-09-28T21:12:19.611354", "email": "airbnb_2@mail.com", "id": "fce12f8a-fdb6-439a-afe8-2881754de71c", "updated_at": "2017-09-28T21:12:19.611368", "first_name": "John", "__class__": "User"}}
guillaume@ubuntu:~/AirBnB$

```

**No unittests needed for the console**

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   File: `models/user.py, models/engine/file_storage.py, console.py, tests/`

### 9\. More classes!

mandatory

Write all those classes that inherit from `BaseModel`:

-   `State` (`models/state.py`):
    -   Public class attributes:
        -   `name`: string - empty string
-   `City` (`models/city.py`):
    -   Public class attributes:
        -   `state_id`: string - empty string: it will be the `State.id`
        -   `name`: string - empty string
-   `Amenity` (`models/amenity.py`):
    -   Public class attributes:
        -   `name`: string - empty string
-   `Place` (`models/place.py`):
    -   Public class attributes:
        -   `city_id`: string - empty string: it will be the `City.id`
        -   `user_id`: string - empty string: it will be the `User.id`
        -   `name`: string - empty string
        -   `description`: string - empty string
        -   `number_rooms`: integer - 0
        -   `number_bathrooms`: integer - 0
        -   `max_guest`: integer - 0
        -   `price_by_night`: integer - 0
        -   `latitude`: float - 0.0
        -   `longitude`: float - 0.0
        -   `amenity_ids`: list of string - empty list: it will be the list of `Amenity.id` later
-   `Review` (`models/review.py`):
    -   Public class attributes:
        -   `place_id`: string - empty string: it will be the `Place.id`
        -   `user_id`: string - empty string: it will be the `User.id`
        -   `text`: string - empty string

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   File: `models/state.py, models/city.py, models/amenity.py, models/place.py, models/review.py, tests/`

### 10\. Console 1.0

mandatory

Update `FileStorage` to manage correctly serialization and deserialization of all our new classes: `Place`, `State`, `City`, `Amenity` and `Review`

Update your command interpreter (`console.py`) to allow those actions: `show`, `create`, `destroy`, `update` and `all` with all classes created previously.

Enjoy your first console!

**No unittests needed for the console**

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   File: `console.py, models/engine/file_storage.py, tests/`


0x01. AirBnB clone - Web static
===============================

-   By Guillaume
-   Weight: 1
-   Ongoing project - started 02-03-2022, must end by 02-08-2022 (in 3 days) - you're done with 0% of tasks.
-   **Manual QA review must be done** (request it when you are done with the project)

Concepts
--------

*For this project, students are expected to look at these concepts:*

-   [HTML/CSS](https://alx-intranet.hbtn.io/concepts/2)
-   [The trinity of front-end quality](https://alx-intranet.hbtn.io/concepts/4)

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/9/135ef103cf7ed150c9760aadc66844113dfc3d35.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220205%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220205T115822Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=93a4c1e4b457b12b3a454f4de88a5c07126ea7dc39ef0cc84403609152e2676a)

Background Context
------------------

### Web static, what?

Now that you have a command interpreter for managing your AirBnB objects, it's time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to "design" / "sketch" / "prototype" each element:

-   Create simple HTML static pages
-   Style guide
-   Fake contents
-   No Javascript
-   No data loaded from anything

During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can't apply any design.

Before starting, please fork or clone the repository `AirBnB_clone` from your partner if you were not the owner of the previous project.

Resources
---------

**Read or watch**:

-   [Learn to Code HTML & CSS](https://alx-intranet.hbtn.io/rltoken/T9KyiA6_Tm3Ny6oTn08S-A "Learn to Code HTML & CSS") (*until "Creating Lists" included*)
-   [Inline Styles in HTML](https://alx-intranet.hbtn.io/rltoken/7NdYbImFNofpB_FXXn3otg "Inline Styles in HTML")
-   [Specifics on CSS Specificity](https://alx-intranet.hbtn.io/rltoken/z_OTPFCjmhXJJi7KJqBCbQ "Specifics on CSS Specificity")
-   [CSS SpeciFishity](https://alx-intranet.hbtn.io/rltoken/7iqk-el4ZVnKeyLoON8Rqg "CSS SpeciFishity")
-   [Introduction to HTML](https://alx-intranet.hbtn.io/rltoken/okP4V3RxFXHkEcQo19AnuQ "Introduction to HTML")
-   [CSS](https://alx-intranet.hbtn.io/rltoken/Ir8Ka59FO6Z_vJQ-gkSG_w "CSS")
-   [MDN](https://alx-intranet.hbtn.io/rltoken/BpSXtcWOGH0UT4XLCoQyJg "MDN")
-   [center boxes](https://alx-intranet.hbtn.io/rltoken/Tlje4XYwyZbUfHkQWGi1WQ "center boxes")

Learning Objectives
-------------------

At the end of this project, you are expected to be able to [explain to anyone](https://alx-intranet.hbtn.io/rltoken/Zb9sTIct2xdhDCDLGF-RyQ "explain to anyone"), **without the help of Google**:

### General

-   What is HTML
-   How to create an HTML page
-   What is a markup language
-   What is the DOM
-   What is an element / tag
-   What is an attribute
-   How does the browser load a webpage
-   What is CSS
-   How to add style to an element
-   What is a class
-   What is a selector
-   How to compute CSS Specificity Value
-   What are Box properties in CSS

Requirements
------------

### General

-   Allowed editors: `vi`, `vim`, `emacs`
-   All your files should end with a new line
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should be W3C compliant and validate with [W3C-Validator](https://alx-intranet.hbtn.io/rltoken/NzQ96QXtBTCMRDicPORzbA "W3C-Validator")
-   All your CSS files should be in `styles` folder
-   All your images should be in `images` folder
-   You are not allowed to use `!important` and `id` (`#...` in the CSS file)
-   You are not allowed to use tags `img`, `embed` and `iframe`
-   You are not allowed to use Javascript
-   Current screenshots have been done on `Chrome 56` or more.
-   No cross browsers
-   You have to follow all requirements but some `margin`/`padding` are missing - you should try to fit as much as you can to screenshots

More Info
---------

![](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step1.png)

Quiz questions
--------------

Show

Tasks
-----

### 0\. Inline styling

mandatory

Write an HTML page that displays a header and a footer.

Layout:

-   Body:
    -   no margin
    -   no padding
-   Header:
    -   color #FF0000 (red)
    -   height: 70px
    -   width: 100%
-   Footer:
    -   color #00FF00 (green)
    -   height: 60px
    -   width: 100%
    -   text `Best School` center vertically and horizontally
    -   always at the bottom at the page

Requirements:

-   You must use the `header` and `footer` tags
-   You are not allowed to import any files
-   You are not allowed to use the `style` tag in the `head` tag
-   Use inline styling for all your tags

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/98f4ac1b0644512ce7ae91a9e8e61e8fe174911d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220205%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220205T115822Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=acb06d3d160ea5189ff145c8bc77a2545d68caf692c3fd9665bec675736f3b32)

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   Directory: `web_static`
-   File: `0-index.html`

### 1\. Head styling

mandatory

Write an HTML page that displays a header and a footer by using the `style` tag in the `head` tag (same as `0-index.html`)

Requirements:

-   You must use the `header` and `footer` tags
-   You are not allowed to import any files
-   No inline styling
-   You must use the `style` tag in the `head` tag

The layout must be exactly the same as `0-index.html`

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   Directory: `web_static`
-   File: `1-index.html`

### 2\. CSS files

mandatory

Write an HTML page that displays a header and a footer by using CSS files (same as `1-index.html`)

Requirements:

-   You must use the `header` and `footer` tags
-   No inline styling
-   You must have 3 CSS files:
    -   `styles/2-common.css`: for global style (i.e. the `body` style)
    -   `styles/2-header.css`: for header style
    -   `styles/2-footer.css`: for footer style

The layout must be exactly the same as `1-index.html`

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   Directory: `web_static`
-   File: `2-index.html, styles/2-common.css, styles/2-header.css, styles/2-footer.css`

### 3\. Zoning done!

mandatory

Write an HTML page that displays a header and footer by using CSS files (same as `2-index.html`)

Layout:

-   Common:
    -   no margin
    -   no padding
    -   font color: #484848
    -   font size: 14px
    -   font family: `Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;`
    -   [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon.png "icon") in the browser tab
-   Header:
    -   color: white
    -   height: 70px
    -   width: 100%
    -   border bottom 1px #CCCCCC
    -   [logo](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/logo.png "logo") align on left and center vertically (20px space at the left)
-   Footer:
    -   color white
    -   height: 60px
    -   width: 100%
    -   border top 1px #CCCCCC
    -   text `Best School` center vertically and horizontally
    -   always at the bottom at the page

Requirements:

-   No inline style
-   You are not allowed to use the `img` tag
-   You are not allowed to use the `style` tag in the `head` tag
-   All images must be stored in the `images` folder
-   You must have 3 CSS files:
    -   `styles/3-common.css`: for the global style (i.e `body` style)
    -   `styles/3-header.css`: for the header style
    -   `styles/3-footer.css`: for the footer style

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/2be1eda05a0d9097c210f2d3482a59aa858c5711.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220205%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220205T115822Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=881f4243ba88f8001e714799e668c22912542cac65c03a6e0258b956fa194531)

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   Directory: `web_static`
-   File: `3-index.html, styles/3-common.css, styles/3-header.css, styles/3-footer.css, images/`

### 4\. Search!

mandatory

Write an HTML page that displays a header, footer and a filters box with a search button.

Layout: (based on `3-index.html`)

-   Container:
    -   between `header` and `footer` tags, add a `div`:
        -   classname: `container`
        -   max width 1000px
        -   margin top and bottom 30px - it should be 30px under the bottom of the `header` (screenshot)
        -   center horizontally
-   Filter section:
    -   tag `section`
    -   classname `filters`
    -   inside the `.container`
    -   color white
    -   height: 70px
    -   width: 100% of the container
    -   border 1px #DDDDDD with radius 4px
-   Button search:
    -   tag `button`
    -   text `Search`
    -   font size: 18px
    -   inside the section filters
    -   background color #FF5A5F
    -   text color #FFFFFF
    -   height: 48px
    -   width: 20% of the section filters
    -   no borders
    -   border radius: 4px
    -   center vertically and at 30px of the right border
    -   change opacity to 90% when the mouse is on the button

Requirements:

-   You must use: `header`, `footer`, `section`, `button` tags
-   No inline style
-   You are not allowed to use the `img` tag
-   You are not allowed to use the `style` tag in the `head` tag
-   All images must be stored in the `images` folder
-   You must have 4 CSS files:
    -   `styles/4-common.css`: for the global style (`body` and `.container` styles)
    -   `styles/3-header.css`: for the header style
    -   `styles/3-footer.css`: for the footer style
    -   `styles/4-filters.css`: for the filters style
-   `4-index.html` **won't be W3C valid**, don't worry, it's temporary

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/f959154b0cdf1cdf71ddef04e3787ef28462793e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220205%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220205T115822Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0c020c3761ddc0cb287bc457fad9b8187b12625fb57b4846a660d1cf6087dc4e)

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   Directory: `web_static`
-   File: `4-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/4-filters.css, images/`

### 5\. More filters

mandatory

Write an HTML page that displays a header, footer and a filters box.

Layout: (based on `4-index.html`)

-   Locations and Amenities filters:
    -   tag: `div`
    -   classname: `locations` for location tag and `amenities` for the other
    -   inside the section filters (same level as the `button` Search)
    -   height: 100% of the section filters
    -   width: 25% of the section filters
    -   border right #DDDDDD 1px only for the first left filter
    -   contains a title:
        -   tag: `h3`
        -   font weight: 600

        -   text `States` or `Amenities`
    -   contains a subtitle:
        -   tag: `h4`
        -   font weight: 400

        -   font size: 14px
        -   text with fake contents

Requirements:

-   You must use: `header`, `footer`, `section`, `button`, `h3`, `h4` tags
-   No inline style
-   You are not allowed to use the `img` tag
-   You are not allowed to use the `style` tag in the `head` tag
-   All images must be stored in the `images` folder
-   You must have 4 CSS files:
    -   `styles/4-common.css`: for the global style (`body` and `.container` styles)
    -   `styles/3-header.css`: for the header style
    -   `styles/3-footer.css`: for the footer style
    -   `styles/5-filters.css`: for the filters style

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/85bfa50b96c2985723daa75b5e22f75ef16e2b2e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220205%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220205T115822Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=27ac77e98cc50ae5867251edaa1c786f5725dd59a925bc266a93739cb77d96ed)

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   Directory: `web_static`
-   File: `5-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/5-filters.css, images/`

### 6\. It's (h)over

mandatory

Write an HTML page that displays a header, footer and a filters box with dropdown.

Layout: (based on `5-index.html`)

-   Update Locations and Amenities filters to display a contextual dropdown when the mouse is on the filter `div`:
    -   tag `ul`
    -   classname `popover`
    -   text should be fake now
    -   inside each `div`
    -   not displayed by default
    -   color #FAFAFA
    -   width same as the `div` filter
    -   border #DDDDDD 1px with border radius 4px
    -   no list display
    -   Location filter has 2 levels of `ul`/`li`:
        -   state -> cities
        -   state name must be display in a `h2` tag (font size 16px)

Requirements:

-   You must use: `header`, `footer`, `section`, `button`, `h3`, `h4`, `ul`, `li` tags
-   No inline style
-   You are not allowed to use the `img` tag
-   You are not allowed to use the `style` tag in the `head` tag
-   All images must be stored in the `images` folder
-   You must have 4 CSS files:
    -   `styles/4-common.css`: for the global style (`body` and `.container` styles)
    -   `styles/3-header.css`: for the header style
    -   `styles/3-footer.css`: for the footer style
    -   `styles/6-filters.css`: for the filters style

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/6262f13624dca23ca19db505c44f88faddb82ebb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220205%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220205T115822Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0341b5a9417325d2b2adcab7d8daf63e0d8e221e840c33794743c1a377596ea3) ![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/6e6bdfa13fa88a5f439d9e2b1dade826dd95529b.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220205%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220205T115822Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6cba3c4987767187194297cc92f0a211c17b46a5e1d930ed84a2c93a351021d1)

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   Directory: `web_static`
-   File: `6-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, images/`

### 7\. Display results

mandatory

Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on `6-index.html`)

-   Add Places section:
    -   tag: `section`
    -   classname: `places`
    -   same level as the filters section, inside `.container`
    -   contains a title:
        -   tag: `h1`
        -   text: `Places`
        -   align in the top left
        -   font size: 30px
    -   contains multiple "Places" as listing (horizontal or vertical) describe by:
        -   tag: `article`
        -   width: 390px
        -   padding and margin 20px
        -   border #FF5A5F 1px with radius 4px
        -   contains the place name:
            -   tag: `h2`
            -   font size: 30px
            -   center horizontally

Requirements:

-   You must use: `header`, `footer`, `section`, `article`, `button`, `h1`, `h2`, `h3`, `h4`, `ul`, `li` tags
-   No inline style
-   You are not allowed to use the `img` tag
-   You are not allowed to use the `style` tag in the `head` tag
-   All images must be stored in the `images` folder
-   You must have 5 CSS files:
    -   `styles/4-common.css`: for the global style (i.e. `body` and `.container` styles)
    -   `styles/3-header.css`: for the header style
    -   `styles/3-footer.css`: for footer style
    -   `styles/6-filters.css`: for the filters style
    -   `styles/7-places.css`: for the places style

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/bca4d17fbe21a58b66a9d5d6b85df4801d147dd0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220205%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220205T115822Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7280e4d4705454fc0b12e03f3eb4c670685877b376c9971e78d6ca842f728974)

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   Directory: `web_static`
-   File: `7-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/7-places.css, images/`

### 8\. More details

mandatory

Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.

Layout: (based on `7-index.html`)

Add more information to a Place `article`:

-   Price by night:
    -   tag: `div`
    -   classname: `price_by_night`
    -   same level as the place name
    -   font color: #FF5A5F
    -   border: #FF5A5F 4px rounded
    -   min width: 60px
    -   height: 60px
    -   font size: 30px
    -   align: the top right (with space)
-   Information section:
    -   tag: `div`
    -   classname: `information`
    -   height: 80px
    -   border: top and bottom #DDDDDD 1px
    -   contains (align vertically):
        -   Number of guests:
            -   tag: `div`
            -   classname: `max_guest`
            -   width: 100px
            -   fake text
            -   [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_group.png "icon")
        -   Number of bedrooms:
            -   tag: `div`
            -   classname: `number_rooms`
            -   width: 100px
            -   fake text
            -   [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_bed.png "icon")
        -   Number of bathrooms:
            -   tag: `div`
            -   classname: `number_bathrooms`
            -   width: 100px
            -   fake text
            -   [icon](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_bath.png "icon")
-   User section:
    -   tag: `div`
    -   classname: `user`
    -   text `Owner: <fake text>`
    -   `Owner` text should be in bold
-   Description section:
    -   tag: `div`
    -   classname: `description`

Requirements:

-   You must use: `header`, `footer`, `section`, `article`, `button`, `h1`, `h2`, `h3`, `h4`, `ul`, `li` tags
-   No inline style
-   You are not allowed to use the `img` tag
-   You are not allowed to use the `style` tag in the `head` tag
-   All images must be stored in the `images` folder
-   You must have 5 CSS files:
    -   `styles/4-common.css`: for the global style (i.e. `body` and `.container` styles)
    -   `styles/3-header.css`: for the header style
    -   `styles/3-footer.css`: for the footer style
    -   `styles/6-filters.css`: for the filters style
    -   `styles/8-places.css`: for the places style

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/f4b2d4ef94bd3a2e7e1ddefa81236595686d270e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220205%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220205T115822Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=657b880a7df03232509073d025b8c403c85542435b35f6f41bb595c9518d18a6)

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   Directory: `web_static`
-   File: `8-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/8-places.css, images/`

### 9\. Full details

#advanced

Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on `8-index.html`)

Add more information to a Place `article`:

-   List of Amenities:
    -   tag `div`
    -   classname `amenities`
    -   margin top 40px
    -   contains:
        -   title:
            -   tag `h2`
            -   text `Amenities`
            -   font size 16px
            -   border bottom #DDDDDD 1px
        -   list of amenities:
            -   tag `ul` / `li`
            -   no list style
            -   icons on the left: [Pet friendly](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_pets.png "Pet friendly"), [TV](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_tv.png "TV"), [Wifi](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/icon_wifi.png "Wifi"), etc... feel free to add more
-   List of Reviews:
    -   tag `div`
    -   classname `reviews`
    -   margin top 40px
    -   contains:
        -   title:
            -   tag `h2`
            -   text `Reviews`
            -   font size 16px
            -   border bottom #DDDDDD 1px
        -   list of review:
            -   tag `ul` / `li`
            -   no list style
            -   a review is described by:
                -   `h3` tag for the user/date description (font size 14px). Ex: "From Bob Dylan the 27th January 2017"
                -   `p` tag for the text (font size 12px)

Requirements:

-   You must use: `header`, `footer`, `section`, `article`, `button`, `h1`, `h2`, `h3`, `h4`, `ul`, `li` tags
-   No inline style
-   You are not allowed to use the `img` tag
-   You are not allowed to use the `style` tag in the `head` tag
-   All images must be stored in the `images` folder
-   You must have 5 CSS files:
    -   `styles/4-common.css`: for the global style (`body` and `.container` styles)
    -   `styles/3-header.css`: for the header style
    -   `styles/3-footer.css`: for the footer style
    -   `styles/6-filters.css`: for the filters style
    -   `styles/100-places.css`: for the places style

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2021/12/f54486a431a05ea3477e337e0e953686d3c6ffd0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220205%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220205T115823Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=0b74770866647846870b69ec31e665455829ac9c624ba0ecf0bfa0848c2268b8)

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   Directory: `web_static`
-   File: `100-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/100-places.css, images/`

### 10\. Flex

#advanced

Improve the Places section by using [Flexible boxes](https://alx-intranet.hbtn.io/rltoken/Xc-nBlQHexwNaCuKYpZ2-A "Flexible boxes") for all Place articles

[Flexbox Froggy](https://alx-intranet.hbtn.io/rltoken/PZz46Gkdj5Mo9-AWERPhQA "Flexbox Froggy")

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   Directory: `web_static`
-   File: `101-index.html, styles/4-common.css, styles/3-header.css, styles/3-footer.css, styles/6-filters.css, styles/101-places.css, images/`

### 11\. Responsive design

#advanced

Improve the page by adding [responsive design](https://alx-intranet.hbtn.io/rltoken/9mRhZcLRxmsuCyF8q7S8Ww "responsive design") to display correctly in mobile or small screens.

Examples:

-   no horizontal scrolling
-   redesign search bar depending of the width
-   etc.

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   Directory: `web_static`
-   File: `102-index.html, styles/102-common.css, styles/102-header.css, styles/102-footer.css, styles/102-filters.css, styles/102-places.css, images/`

### 12\. Accessibility

#advanced

Improve the page by adding [Accessibility support](https://alx-intranet.hbtn.io/rltoken/JO-zonPvzBUfqpYRZDAtug "Accessibility support")

Examples:

-   Colors contrast
-   Header tags
-   etc.

**Repo:**

-   GitHub repository: `AirBnB_clone`
-   Directory: `web_static`
-   File: `103-index.html, styles/103-common.css, styles/103-header.css, styles/103-footer.css, styles/103-filters.css, styles/103-places.css, images/`