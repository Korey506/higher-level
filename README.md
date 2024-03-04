# AirBnB - The Console

## Description

The repository includes the early phase of a student project aimed at developing a replica of the AirBnB platform. This phase introduces a backend interface, referred to as a console, designed to handle program data. Through console commands, users can create, modify, and delete objects, along with managing file storage. Persistence across sessions is achieved through JSON serialization/deserialization.

## The Command Interpreter: 				`console.py`

The command interpreter is used to interact with the program making it possible for the user to create, destroy, show and update stored data

### How to Start it:

1. Clone this repository to your local machine.  	`git clone https://github.com/Korede456/AirBnB_clone.git`
2. Navigate to the project directory.			`cd AirBnB_clone`
3. Run the command interpreter script.			`./console.py`

### How to use it:

### Once the interpreter is running, you will see the   `(hbnb)` prompt

## commands

* create - Creates an instance based on given class
* destroy - Destroys an object based on class UUID
* show - Shows an object based on class and UUID
* all - Shows all objects the program has access to, or all objects of a given class
* update - Updates existing attributes an object basws on class name and UUID
* quit - Exits the program (EOF will as will)
