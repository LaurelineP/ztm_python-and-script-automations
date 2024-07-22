# Python
## Resources ( zip )
https://cdn.fs.teachablecdn.com/cBpbX3XSyqrkGLkBD1q0

## 📌 Terminal / Shell / Python Shell
Terminal - Allows you to run commands and also your programs.
There are other ways to execute code such as program in files.
- from shell enabling a programming context
- from files: which executes some program

In shell
write the command `python` which will reveal a python context for you to write some python and we will explore there for now


## 📌 Values and Types
Types: classification of what a value represents
| Data Type | Python keyword | Examples      |
|-----------|----------------|---------------|
| Integer     | int          | 0, 4, -2, 87  |
| Floating Point Number | float | 1.2, -1.3, 11.0, 1.873 |
| Chain of characters / a string | str   | 'hello', 'yu', 'I am 9' |


- Numbers ( integers, float ): are written as it is - typing numbers
- Strings: need to be wrapped by quotes ( single, double )
`"This is a valid string in python"
- and more that will follow...


## 📌 Functions
Named chunk of code ( snippet ) encapsulated in order  
to be invoked on demand to perform a specific task   
( the code within that function )  
It can also return a result ( output )  
It can also accept arguments ( values between parentheses )   
which are used within the code in within the function  
Depending on how we define the function.  
- invoke / call: the function named followed by parentheses
```py
# Defining a function
def say_name( name ): return name

# Invoking the function
say_name( "Lowla" )

# Once executed, in the shell we have the following result
# 'Lowla'
```

### Built in function
Python has its own functions we can use

```py
# Using built in function "type"
type( "Lowla")

# Using built in function "int"
int(123.123)

# Using built in function "float"
float(123)

# Returning 
# <class 'str'>
# 123.123
# 123
```


## 📌 Expressions
An expression is a statement evaluated in the code such as conditions   
for instance, using built in keywords.
A combination of values and operators ( =, -, + , etc... )

### Special operators
`//` integer division operators --> will enforce to return an integer  
`%` modulo operator --> return the remainder of a division
`**` power operator --> return the power of the 2 numbers combined

`==` comparison operator --> check if equal
`!=` not equal


```py
# Expression
1 + 1
# Returns 2

3 / 2
# Returns 1.5

3 // 2
# Returns 1

5 % 1.5
# Returns 0.5

2 ** 3
# Returns 8
```

Note: those evaluations are also ruled by   
the mathematics parentheses priority principle.


### Expression mixing values string and operators +

#### Concatenation
Adding the same type to another element being the same type - agrementing it:
this is concatenation. Can apply to string, tuple and array
```py
"Hello " + "Lowla"
# Returns "Hello Lowla"
```

#### Text Multiplication
We can multiply a string value to repeat that one

```py
"Ha" * 3
# Returns "HaHaHa"
```


## 📌 Variables
Its a way to store a value to be re-used at different moment
and can be re-assigned by providing a different variable.
```py
# Pattern <name-variable> = <value>
my_name = "Lowla"

# Printing my_name
print(my_name)

# Returns the value
# "Lowla"

```


## 📌 Variables naming
Naming convention in python is mainly snake case
`snake_case_variable`

Variable naming:
- can contain letters, underscore, number
- can not start with number
- should be different than the existing one
- should not be the same name of Python keywords   
( for, while, in, if, else, print, type, etc...)
- should not be the same as another variable name - to avoid overriding

## 📌 Errors
Errors can happen while programming and should be anticipated in order to 
prevent our code / program to stop or crash.
Key to debug: read the error - which is insightful

### Different type of error in Python
- Syntax Error: a misspell / a non interpreted character  
- Name Error: referring to a keyword that is misspell  
- Semantic Error: wrong logic implemented even if the syntax is correct:  
  this could lead to an unexpected output. Ex: missing parentheses in an
  operation


## 📌 F Strings
Allows to easily include a or multiple values on a string dynamically  
Introduced in 3.7 Python  
Short for Formatted String  
Prepended by f followed by quotes  
In-between quotes it is your string and the  
dynamic value between curly braces  
Values can be variable, expression or functions returning a value.
```py
my_name = 'Lowla'
my_str = f'Name: {name}'
# Returns "Name: Lowla"
```

## 📌 Objects, Attributes and Methods
**Objects** are way to organize data and functionality in Python
_Python is considered as an object oriented language - considering   
everything is an object: numbers, variable, functions, etc..._

**Methods** are functions in a context - bound to an object

**Attributes**: are stored value within an objects

From an object, accessing its methods or attributes is by appending a  
dot after

```py
# Accessing a string method "upper"
print("Hello you, How are you?".upper())
# Returns "HELLO YOU, HOW ARE YOU?"

# Accessing a string method "lower"
print("Hello you, How are you?".lower())
# Returns 'hello you, how are you?'
```

## 📌 Scripts
Second way of writing python, not in the shell but in a file.
Using the shell - is useful when you want to check something  
but if you want to save and longer and maintain your code, it is  
best to move forwards a file that then you will execute with the shell
Within a script we can also comment bits of code for better maintainability
- the file must be <filename>.py
- executing the script / file : `python <filename>.py`
- example: `python main.py`

```py
# in main.py
# Demo coding in a file to execute it as a script

text = 'Please answer the following questions'
print(text)

upper_text = text.upper()
print(upper_text)

lower_text = text.lower()
print(lower_text)

# Feeding the script with the user interaction
user_name = input('What is your name ? ')
user_age = int(input('How old are you'))
print(f'Your name is {user_name} and you are {user_age}')

```

```py
# In terminal
# Executing the script
python main.py

# Returns 
# Please answer the following questions
# PLEASE ANSWER THE FOLLOWING QUESTIONS
# please answer the following questions
# What is your name ? Lowla
# How old are you ? 100
# Your name is Lowla and you are 100
```


## 📌 Comments
Explaining some codes - those text are ignored for the code
execution but is useful for anyone reading it.
- inline comments
To create a comment: we need to add "#" at the beginning of the line
```py
# This is a comment
```
- multi line comments
To create a comment: we need to add "```" at the beginning of the line
this is called doc string
```py
"""
Multi
Line
Comments
"""
```


## 📌 Data Structure
A data structure is a specific way to organize data,  
it is possible to have nested list, objects for instance
### Lists ( `[ <value>, <value> ]` )
- stores different types of values
- syntax: values should be within square brackets separated by comma
- accessible via indexes wrapped by square brackets too  
( indexes are the position number starting with 0 )
- is mutable == can change values within
```py
favorites = [ 'Hey', 0 ]
# Returns [ 'Hey', 0 ]

type( favorites )
# Returns <class 'list'>

print(favorites[1])
print([ 'Hey', 0 ][0])
# Returns 0

print(favorites[0] === [ 'Hey', 0 ][0])
# Returns True

print(len(favourites))
# Return 2

favorites[0] = 'Aloha'
print(favorites)
['Aloha', 4]
```

### Tuples ( `( <value>, <value> )` )
Tuples are list but non mutable
- stores data, any type of values
- syntax: values should be within parentheses separated by comma
- accessible via indexes wrapped by square brackets too  
( indexes are the position number starting with 0 )
- is non mutable

```py
my_tuple = (1,2,'hey')

# Will raise an error as tuple cannot be mutable
my_tuple[0] = 0
# Trace-back (most recent call last):
#  File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
```
Function or methods for list and/or tuples
| function or method | list | tuple | dictionary |
| ---- | ----- | ------ | ------ |
| len() | [x] | [x] | [x]
| .append() | [x] | [] | [] |


### Dictionaries ( `{ x: <value> }` )
Allows to organize the data structure by name instead of indexes.
Dictionaries as Word with its corresponding definition but here it is 
its value.

- stores data, any type of values in a key : value pair way
- syntax: key/value pair should be express within curly braces
- accessible using square notation with the key: <variable-name>['<key>']
- values are mutable

```py
# Defining a dictionary
my_dict = {
  'name': 'dictionary',
  'word_number': 1
}

# Accessing value with dot notation
print( my_dict['name'] )
# Returns 'dictionary'

my_dict['extra_key'] = 'something'

print( my_dict )
# Returns {'name': 'dictionary', 'word_number': 1, 'extra_key': 'something' }

```


## 📌 `If` Statements 
Enabling to check for a condition in order for the program   
to apply the logic associated to that statement.
Indentation creates block = in this example, the code block
is the logic to apply

```py

if 2 == 2:
  print( 'is two')
# Returns "is two"

# Checking it is different - using `is not`
if 2 is not 1:
  print('Indeed 2 is not 1')

# Checking it is different - using `!=` prepended
if 2 != 1:
  print('Indeed 2 is not 1')

```

### `Elif` statement and `else` statement
`elif` Addon to a previous condition and not a default/ignored condition
`else` allows to close the condition to a fallback exit

```py
value = 2
if str(type(value)) == "<class 'str'>":
  print("The value is a string")
elif str(type(value)) == "<class 'int'>":
  print("The value is an integer")
else:
  print("The value is neither an integer nor string")
# Returns "The value is an integer"
```


## 📌 Or and And operators
Used in conditions by either enable multiple condition (OR) or by combining  
statements to valid a condition


## 📌  Loops
#### While loop
Keep iterate until the condition is not longer true

```py
# control variable
number = 10
while number != 0:
  print(number)

  # Ensures to decrease in order to go out of the loop
  number -= 1
```

Sequences: [ range, list, tuple, dictionary ( keys are the iterables ) ]

#### for loop
Loops/Iterates over a fixed number of times
If a number of time is needed - `range()` can be handy to create 
a collection of iterables up to the number passed as parameter.
Handy to repeat a task x times.
##### loops & sequenced data structure
```py
number = 10
"""
for <variable-holder> in <sequence>
combined to range(10) --> creating a sequence of items
"""
for n in range(10):
  print( n )

"""
Returns
0
1
2
3
4
5
6
7
8
9
"""
```

#### loops & dictionary data structure
```py
person = { "name": "Smith", "age": 100 }


""""
When looping over dictionaries, passing 1 variable would represent the key
"""
for key in person:
  print(f"The key is: \"{key}\"")

"""
When looping over dictionaries, we can get value using square notation
"""
for key in person:
  value = person[key]
  print(f'The value for the key "{key}" is "{value}"')

"""
Returning:
The value for the key "name" is "Smith"
The value for the key "age" is "100"
"""


"""
Or we can get the iterables of values from the dictionary
using <dictionary>.values()
"""
for value in person.values():
  print(f'The value is "{value}"')
  
"""
Returning:
The value is "Smith"
The value is "100"
"""



"""
Or we can get the collection of tuples ( keys, values ) iterables from the dictionary using <dictionary>.items()
We must provide 2 variables in order to get the item of each .items() tuples
"""
for key, value in person.items():
  print(f'The key is "{key}" and its value is "{value}"')

"""
Returning:
The key is "name" and its value is "Smith"
The key is "age" and its value is "100"
"""
```

## 📌  Modules, Libraries and Classes
Modules is like a toolbox - providing some functions / classes to use within the course
Libraries can contain multiple toolboxes ( modules )
Classes are the tiny toolbox for a specific moment


### 🔹 Class
- template creating object ( blueprint - skeleton of an
object that could be used to shape multiple objects )
- initializers ( functions ) are provided to create instances  
( instance: an object created from the blueprint )
- class often have built-in methods to do tasks attached to the
  concern of this class


### 🔹 Modules
A file or a folder containing file to import ans reuse as needed.
Note: while importing - we must keep in mind that Python is OOP, and so
is oriented the imports.

Folder modules, may need to add the `__init__.py` file to let the interpreter know
the file within can be imported - without it you might go crazy while trying to import.  

- **Folder and its nested file are accessible using dot notation**
  - "regular path": `<my-folder>.<my-file-name>` ( no need to specify   
  the file extension) as plain objects ( not string )
  - "relative path": `.<my-file-name>`

- **From same folder, import sibling file**
  - without that `__init__.py` your IDE might not be happy and not letting you  
  to import it.



### Useful modules 
| Module | Description |
| ------ | ----------- |
| datetime | anything related to dates |


```py
# Importing modules
import datetime

# Accessing class / functions from modules
# <variable> = datetime.datetime.now
now = datetime.datetime.now()

# Initializing a class and passing arguments to build the object
# with name arguments based 
new_years_day = datetime.datetime(year=now.year + 1, month=1, day=1)

```


## 📌 Installing Python & PyCharm
### 🔹 Installing Python ( mac )

Step 1: Check for Existing Python Installation
Before installing a new version of Python, it's a good idea to check if you already have Python installed on your Mac, which can sometimes be the case.

1. Open Terminal: You can find Terminal in the Applications folder under Utilities, or simply search for it using Spotlight (Cmd + Space).

2. Check Python Version: Type python --version or python3 --version and press Enter. If Python is installed, this will display the version number.



Step 2: Download Python
To download the latest version of Python:

1. Visit the Python Website: Open your web browser and go to the official Python website](https://www.python.org/).

2. Download Python: Click on "Downloads" and select the latest version for macOS. The website typically detects your OS and suggests the appropriate version.



Step 3: Install Python 
Once the download is complete:

1. Open the Installer: Locate the downloaded file (typically in the Downloads folder) and double-click on it.

2. Follow Installation Steps: The installer will guide you through the process. Make sure to select the option "Install launcher for all users" and "Add Python to PATH" if available.

3. Complete Installation: Click “Install” and enter your admin password if prompted.



Step 4: Verify Installation
After installation: 

1. Open Terminal Again: As in Step 1.

2. Check the Version: Type python3 --version and press Enter. This should display the newly installed Python version.



Step 5: Install pip (If Not Included)
pip is Python's package manager and is used to install Python packages. It usually comes with Python, but if not:

1. Download get-pip.py: Visit https://bootstrap.pypa.io/get-pip.py, and download the get-pip.py script.

2. Run the Script: In Terminal, navigate to the download location and run python3 get-pip.py.



### 🔹 Install Pycharm ( mac )
Prerequisites
- macOS: Ensure your Mac is running on macOS 10.13 (High Sierra) or later.

- Internet Connection: You'll need a stable internet connection to download PyCharm.

- Admin Rights: Be sure you have administrative privileges on your Mac to install new software.



Step 1: Downloading PyCharm
1. Open your Web Browser: Launch Safari, Chrome, or any other browser.

2. Visit the JetBrains Website: Go to the JetBrains official website.

3. Select the Edition: Choose between the Community Edition (free) and the Professional Edition (paid). Click on the “Download” button for the Community Edition.

4. Start the Download: The download should start automatically. If it doesn’t, click on the direct link provided on the webpage.



Step 2: Installing PyCharm
1. Open the Downloaded File: Locate the downloaded .dmg file in your “Downloads” folder and double-click to open it.

2. Install PyCharm: A new window will appear with the PyCharm icon and the “Applications” folder. Drag the PyCharm icon to the “Applications” folder. This will copy PyCharm into your Applications.

3. Wait for the Copy to Finish: This might take a few minutes depending on your Mac's performance.



Step 3: Running PyCharm
1. Open PyCharm: Go to your “Applications” folder and find PyCharm. Double-click to open it.

2. Initial Setup: The first time you open PyCharm, you’ll go through an initial setup process. This includes accepting the license agreement and configuring the IDE according to your preferences (like choosing a theme).

### 🔹 Installing Python ( windows )
Step 1: Download Python
1. Visit the Official Python Website: Open your web browser and go to the official Python website.

2. Select the Version: Click on the 'Downloads' tab. The website typically suggests the latest version for Windows.

3. Download the Installer: Click on the link to download the Python installer for Windows.



Step 2: Run the Installer
1. Locate the Installer: After the download is complete, locate the installer file, usually in your 'Downloads' folder.

2. Start Installation: Double-click the installer file to begin the installation process.

3. Select Installation Options:

  - Check 'Add Python to PATH': Before proceeding, make sure to tick the checkbox that says “Add Python to PATH”. This step is crucial as it allows you to run Python from the Command Prompt.

  - Choose Install Location: You can select the default location (recommended) or choose a specific location for Python installation.

4. Begin Installation: Click on “Install Now” (recommended) or “Customize Installation” if you need to change any settings.



Step 3: Verify the Installation 
1. Open Command Prompt: After the installation is complete, open the Command Prompt.

2. Check Python Version: Type python --version and press Enter. This command should return the version of Python you installed.

3. Verify Pip Installation: Type pip --version to ensure that pip (Python's package installer) is also installed.

### 🔹 Installing Pycharm ( windows )
Prerequisites
- macOS: Ensure your Mac is running on macOS 10.13 (High Sierra) or later.

- Internet Connection: You'll need a stable internet connection to download PyCharm.

- Admin Rights: Be sure you have administrative privileges on your Mac to install new software.



Step 1: Downloading PyCharm
1. Open your Web Browser: Launch Safari, Chrome, or any other browser.

2. Visit the JetBrains Website: Go to the JetBrains official website.

3. Select the Edition: Choose between the Community Edition (free) and the Professional Edition (paid). Click on the “Download” button for the Community Edition.

4. Start the Download: The download should start automatically. If it doesn’t, click on the direct link provided on the webpage.



Step 2: Installing PyCharm
1. Open the Downloaded File: Locate the downloaded .dmg file in your “Downloads” folder and double-click to open it.

2. Install PyCharm: A new window will appear with the PyCharm icon and the “Applications” folder. Drag the PyCharm icon to the “Applications” folder. This will copy PyCharm into your Applications.

3. Wait for the Copy to Finish: This might take a few minutes depending on your Mac's performance.

Step 3: Running PyCharm
1. Open PyCharm: Go to your “Applications” folder and find PyCharm. Double-click to open it.

2. Initial Setup: The first time you open PyCharm, you’ll go through an initial setup process. This includes accepting the license agreement and configuring the IDE according to your preferences (like choosing a theme).


## 🔹 Venv / Virtual Environment
Virtual Environment enables to install the required environment to run a project.
This allows to install contain the installed external packages for the project use
and to use the right version of python.
Note: `venv` is commonly used as the name of the virtual environment but could  
be different


### 1. Creating a virtual environment (CLI)
Will create a new folder that will contain an "image" of the python version your  
machine is referring to. This will be in this folder that all the package will be
installed once the environment enabled
`python -m venv` : create a virtual environment - by default this would be called `venv`
`python -m venv _venv_`: this example would create a virtual environment called `_venv_`

### 2. Activating the virtual environment (CLI)
Allows to request the context of the project folder virtual environment.
*"Use this python version and context*
- typing `activate` in the virtual environment parent folder
- other way: in the folder containing the virtual environment folder,  
  - mac:`source <venv>/bin/activate`
  - windows: `<venv>\Scripts\activate.bat`


  #### Linux ( POSIX )
  - with `bash/zsh`.      : `source <venv>/bin/activate`
  - with  `fish`          : `source <venv>/bin/activate.fish`
  - with `csh/tcsh`       : `source <venv>/bin/activate.csh`
  - with `powershell`     : `<venv>/bin/Activate.ps1`

  #### Windows
  - with `cmd.exe`       : `C:\> <venv>\Scripts\activate.bat`
  - with `powershell`    : `C:\> <venv>\Scripts\Activate.ps1`

### 3. Install packages
The Package Manager to install external packages: `pip` or `pip3`  
which is was installed along Python
`pip install <package-name>`

### 4. Use the installed package 
Now that your venv is contextualize and you've installed a package,  
you can import it in a file under the project

```sh
Project/
|
|____ venv/
    |___ bin/
        |___ <activate files>
        |___ <pip files>
        |___ <python files>
    |___ include/python/
    |___ lib/
        |___<packages and dependence packages>/
        |___ pip
        |___ pyvenv.cfg ( config for this project - auto generated on venv creation )

```

## 📌 Working With Files
### 🔹 Plaintext files:
The most basic files - computer files containing un-formatting text
  - For configurations files
  - For source code
  - For Notes and reminders
  - For data exchange

#### Reading and writing a text file
Using "open" built-in function 
1. open the file ( result as probably some binary content )
3. specify the mode: describe what action will be
2. apply the action you want to do
3. close : close the file reading - emptying the memory busyness

- POSSIBLE ACTIONS
  - 'r' to read
  - 'w' to write / override a whole file content
  - 'a' appends to the file content ( does not override )


| methods on files | description |
| ---------------- | ----------- |
| `.read()` | read a file |
| `.readline()` | read a file line |
| `.write(<string-content>)` | write into a file a new line |
| `.writelines(<string-list>)` | write into a file a new line, automatically goes at a new line |


##### FIRST WAY - OPEN AND CLOSE
```py
open(<file>, <mode>) as file:
  # ....
  file.close() # must be closed
  # file: filename with extension
  # mode: mode rights over the file
  #   - 'r': to read a file
```

##### SECOND WAY - OPEN AND AUTOMATICALLY CLOSE USING WITH
```py
with open(<file>, <mode>) as file:
  # ....
  # No need to close - the context will be close thanks to "with" keyword

```

### 🔹 CSV files
Comma Separated Values file is a file where we values are organized in 
columns and rowsquit
This module takes a file binary as first argument, and returns a reader `csv.reader`

There is a built-in module called `csv` that is available from python.

#### Reading CSV
Note - reading and 
1. open the file as we previously did: with `with open(<filepath>, 'r')`
2. read the csv `csv_reader = csv.reader(file)`: gives a file content iterable
3. iterate to read the values
4. note that the headers are printed - trick use `next(csv_reader)` so it
starts at the first row of values instead of the headers.
5. read a line: `.readline()`
6. read lines: `.readlines()`
6. read the whole content: `.read()`


#### Writing CSV
2 possibilities
1. open the file as we previously did: with `with open(<filepath>, 'w') as csv_file:`
2. using the `csv` built-in module:
```py
with open(<filepath>, 'w') as csv_file:
  csv_writer = csv.writer( csv_file )
  # write line
  csv_writer.writeline([ 'name', 'age' ])
  csv_writer.writeline([ 'Lowla', 100 ])

  # write multiple lines at once
  csv_writer.writelines([[ 'name', 'age' ], [ 'Lowla', 100 ]])
```
### Manipulating CSV Data - Example
### Process:
- should read file and get its content
- transform these into string in order to manipulate them
- do not forget to keep the headers in order to reuse them in 
following file generation
- generate the CSV file 


## 🗂️ Project: Input - Output
### Original instructions
- create a csv file with dad jokes or refers to original course content, to get the file
- from this file, generate another CSV file with an extra column
- this column will have values representing, in a human friendly way, an interpretation   
the vote value 2


## 🔹 PATHS AND FOLDERS
Using Python built-in module `pathlib`
```py
Path(<path-string>)
  # check if exist
  .exists()

  # check if directory
  .is_dir()

  # check if is file
  .is_file()

  # get name ( folder or file with extension )
  .name

  # get name without extension
  .stem

  # get info 
  .stat()

  # create iterator for a path to reach nested folder or file
  .iterdir();
```

### Create folders
```py
Path(<path-string>)
 # create a directory
  .mkdir() # can raise error
    # prevents from raising an error if not exitst
    .mkdir(exist_ok = True)

    # if path does not exist - error is not raised but will recursively create path missing folders
    .mkdir(exist_ok = True, parents: True)
```

### Copy / renaming and removing files & folders
Using Python built-in module `shutil` ( shell utils ? )
```py
import shutil
path = Path(<path-string>)

 # copy file
  shutil.copy(<src-path>, <target-path>)

# copy folder - path target must include the name folder 
  shutil.copytree(<src-path>, <target-path>, [dirs_exist_ok=True])
  #[dirs_exist_ok=True] optional: to copy recursively

# renaming is moving a file to another location 
  shutil.move(<src-path>, <target-path>)

# deleting for folder
<path>.rmdir()

# deleting a file
<path>.unlink(missing_ok = True)

# deleting a folder and its content
<path>.rmtree()
```

### Project 
[Project -  files and folder cleaner](./_02_path_and_folders/project__files_and_folder_cleaner/)
Guideline
- The folder that will be created "organized" which will contain the folders
  - "csv_files",
  - "text_files",
  - "folders"
- Run the command at the root level
- `/to_clean__original/` folder - is a work directory containing a study case of a folder  
disorganized
- duplicate `/to_clean__original/` in order to work on that duplicated folder instead of the original one
- In the terminal ( at the root level of the whole github repository ):
  - `python main.py project paths`: launches the program and you'll be prompted   
  to specify a path ( relative to the repository root level or absolute )
  - provide the path of a folder you want to clean: copy the relative or absolute path
  of the folder and paste it in the terminal where it has been asked
- observe the folder and its content changed


## 🔹 REGULAR EXPRESSIONS
Regular expression is a standardized tools that all programming languages
used - once learnt, the knowledge on this is reusable
It is a syntax describing patterns in a text

Website where we could try / test these pattern/

[pythex](https://pythex.org/)

## Basics

- `\` this allows to escapes key characters / or key syntax
- `.` this represents any kind of alphabetical character
- plain text


### Special Characters in Regexp
`\d` this represents any digits (0-9)
`\D` this represents any non digit character
`\w` this represents any alpha numeric characters
`\W` this represents any non alpha numeric characters
`\s` this represents white space
`\S` this represents non white space


### Matching Multiple Characters
Brackets allows to match groups of following characters

- `[]` used to match any characters specified in-between matching character
  - [a-z] used to match any lowercased letters / characters
  - [A-Z] used to match any uppercased letters / characters
  - [a-zA-Z] used to match any lowercased and uppercased letters / characters
  - [^<ANY-CHARACTERS-OR-PATTERN]>: used to match all **except** the characters in-between the brackets
- `()` used to match exact following characters and create a group


### Quantifiers
Represents the number of instances the pattern should match 
`?` matches **zero** or **one** instance of the previous character
`+` matches **one or more** instances of the previous character
`*` matches **zero** or more instances of the previous character

### Custom Quantifiers
- `{<n>[, <n>]}` used as a quantifier - applied to the prepended pattern *n being a number*
  - `a{2}`: examples matching a sequence of 2 following `a`
  - `a{3,5}`: examples matching a sequence of 3 or 5 following `a` 
  - a{2,}: examples matching a sequence of 2 and mor following `a` 

### Anchors
- `^` denotes the start of a string
- `$` denotes the end of a string


### Regular Expression in Python
The built-in module `re` provides us with some interesting 
tool to check a given string.

`import re`

Raw string to express the regexp 
`r''` - raw string - write regexp pattern in a string

### Library Methods
- `.search( <REG>, <TEXT> )` >returns  None | Matched value - returning the first matched result
- `.findall( <REG>, <TEXT> )` > returns a multiple values as a list of strings
- `.sub(<REG>, <TEXT>, <REPLACEMENT-TXT>)` substitute found text with the string we pass


#### Returned regexp methods
- `.group()`: value found in the match return object
- `.group(<n>)`: value of the regexp group defined value

### Alternation or OR
- Or operator with a pipe within a group
`(cat|dog)` - regexp to say to match either "cat" or "dog"

### Compilation flags
- `IGNORECASE` flag: makes the matching case insensitive
- `MULTILINE` flag: makes `^` and `$`  matching the entire lines rather than the entire string
- `DOTALL`: makes the dot character match all character including new lines

### Compile method ( from module re )
This method enhance the performance, especially if a same regular expression
is used several times ( in a loop for instance ) - but not all the time neither

```.compile(<regexp-string>, [ <flag> ])```






## Spreadsheets
### Openpyxl package
Python Package allowing to use python to create spreadsheets
new excel sheet, open existing sheet, read and write on a sheet
through the google services
- vocabulary
  - workbook  = represents the excel file in openpyxl, a collection of worksheet
  - worksheet = represents the sheet within the excel file in openpyxl
  Access visualization: workbook > worksheet > cell
- Manipulating a file: opening it and modifying does not need manual
file closing as it is automatic

#### Installation in project
- create and/or activate a virtual environment
- add the package "openpyxl" `pip install openpyxl`



#### OpenPyXl manipulations
- create a file (xlsx): 
```py
new_workbook = openpyxl.Workbook()
new_workbook.save(<filename>)
```
- get file content (xlsx): 
```py
new_workbook = openpyxl.load_workbook(<filename>)
```
- get access to worksheet ( current sheet )
```py
# selects the current work sheet
worksheet = new_workbook.active
```

- get access to a specific worksheet
```py
# access by brackets
# worksheet = new_workbook[<STR-WORKSHEET-NAME>]
worksheet = new_workbook['Sheet3'] # access sheet 3
```

- get worksheet name
```py
worksheet_title = worksheet.title

# modify sheet title
worksheet.title = <NEW-TITLE>
worksheet.save()
```

- get file content cell 
```py
# selects the current work sheet cell A1
worksheet['A1']
```

- get file content cell 
```py
# assign a new value to cell A1
worksheet['A1'] = 'Hello'
```

- delete a 
```py
# workbook - being a dictionary collection of worksheet
# worksheet [ also spreadsheet ] - being a the container of sheets
# sheets - being an excel content ( tab ) that has cells

# deleting the first worksheet
del workbook[0]
```

### GSpread: Google Spread Sheet
Package Automating all kind of google sheets operations from Python
- create and/or activate a virtual environment
- add the package "openpyxl" `pip install GSpread`

#### Google Spread Sheet x account x connection
A cloud system providing excel like sheets
- sign-in to google account in google cloud console  
 to get an api key to use google spreadsheet ( or create an account )
 Try not to do the following without acting upon "try for free"
- create a project > then select it
- scrolling down > check were "API and services" is > select it  
  - if you don't find it: find the search bar and look for   
  "API and services" and select
- Click on "enable API and Services" to select the services we want
- In API and Services page, search for
  - google drive API ( select the first one )  
  - then click the button "enable"
  - navigate to credentials - to create one
    - make sure google drive API is selected
    - make sure to select the access on "Application data"
    - finally, scroll down and select the fact we will not use the   
    Compute Engine, Kubernetes Engine, APP Engine or Cloud functions.
  - Click on "next" > leading to a Service account details  
  A service account is a special google account to represent a non human user needing to authenticate to the service to access the files
  --> here this would be used by the python code
  - Filling the information for a service account
    - Service account name: type a name
    - Service account id: automatically generated
    - Hit "create and continue" button to set the role for the account.
    - Select on the dropdown the category Project > Roles "Editor"
    - Hit continue > then "done"
    --> this will redirect to the home dashboard of enabled API and services  
  - Select the new service created "credentials" tab
  - Then, scrolling down, we could find the link of our service account created > click on it to access to the key
  - Select the "keys" tab > add a key > create new key
  - select the json format which will generate a JSON file containing your credentials.
  - download the file ( rename it if you want ) and make sure to not
  share the file

  Now we need to enable the google sheet api ( this was for the google drive )
  - go to "API and Services"
  - click on enable API
  - search for "google sheets" service to select
  - click enabled and that's done

  Now back to the project, we need to copy the keys
  - open the downloaded json > copy the value of "client_email"
  - create a spread sheet
  - the goal is to share the spread sheet with the copied "client_email"
  - share the spreadsheet > paste it the "client_email"  
  and ensure the role "Editor" is selected
  - uncheck the "notify" checkbox
  - confirm the share action


[!INFO]
> - we created an account, enabling the API keys to use for the services
> - we created an excel sheet that we shared to the email account created
> - we need to use the share link w/ the service account email ( hence the service account creation ) to connect to the cloud service serving this excel sheet

[!INFO]
> - Google Console created > to access Google Cloud Platform > to enable
> services [ google drive, google spreadsheet ]
> - created a spreadsheet > copy the google account email > 
   click on share and provide (paste) the email ( which enables the access through the credentials ( json file downloaded ))
> - run your script that connects to the google client > then open the
  existing spreadsheet
    - running the script before the sharing action, returned an error file not found from google
    - running the script after the sharing action, returned a successful 
    spreadsheet result


#### GSpread: instantiating the google account
  Now we can go back to code
  - import the `gspread` package
  - establish the connection using   
  `google_client = gspread.service_account(<json-file-path>)`
  - worksheet obtained by opening the file with `google_client.open(<name-of-spreadsheet-created>)`
  - accessing the worksheet > sheet: `worksheet.sheet1`
  - editing / adding content to one cell: `sheet.update_acell(<CELL>, <CONTENT>)`
  - editing / adding content to multiple cell: `sheet.update()`

