# Modules 
Modules refer to something you can import and export in order to consume
existing and defined functions.

## Folder module
When the module is a folder, it needs an __init__.py file
- In this file add the variable `__all__` and assign a List of 
  the filename it has 

This will enable you to import the content from that folder name module
`from <MODULE> import <MODULE_FUNCTION>`

```py
from _01_working_with_file import plain_text