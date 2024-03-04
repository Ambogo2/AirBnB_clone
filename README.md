# AIRBNB CLONE

![Alt Text](logo.png)

## Project Overview

The Airbnb clone is the first full web application project by ALX. The goal of the project is to deploy on the server a simple copy of the [AirBnB website](https://www.airbnb.com/).

## The comand line interpreter

The command line interpreter is used to manage objects without a visual interface.
Some commands available include:

- Create - creates a new instance of `basemodel` saves it to a Json file and prints its `id`
- Show - shows an object
- Update - update an attribute of an object
- Destroy - Destroy an object

The console works both in interactive and non interactive mode

### Interactive mode

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

### Non-interactive mode

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

## Project Folders and File structure

- `models directory` contains all classes used for the entire project.
- `tests directory` contains all unit tests.
- `console.py file` is the entry point of our command interpreter.
- `models/base_model.py` file is the base class of all our models.
  It contains common elements:
  _ attributes: id, created_at and updated_at
  _ methods: save() and to_json()
- `models/engine directory`contains all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.

## Classes

Every model should inherit from the `BaseModel`

| Class Name | Attributes                                                                                                                                            |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| BaseModel  | `id`, `created_at`, `updated_at`                                                                                                                      |
| User       | `email`, `password`, `first_name`, `last_name`                                                                                                        |
| State      | `name`, `state_id`                                                                                                                                    |
| City       | `name`                                                                                                                                                |
| Amenity    | `name`                                                                                                                                                |
| Place      | `city_id`, `user_id`, `name`, `description`, `number_rooms`, `number_bathrooms`,`max_guest`, `price_by_night`, ` latitude ``longitude ` `amenity_ids` |
| Review     | `place_id`, `user_id`, `text`                                                                                                                         |
