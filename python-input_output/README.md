# 0-read_file

## Description
This module defines a function `read_file` that reads a UTF-8 encoded text file and prints its content to stdout.  

It is a simple utility to display the contents of a text file in the console.

## Function

### read_file(filename="")

- **Arguments:**
  - `filename` (str): Name of the file to read. Defaults to an empty string.
- **Behavior:**
  - Opens the file in read mode using `with` statement.
  - Reads the entire content of the file.
  - Prints the content to stdout.
- **Notes:**
  - File permission or missing file exceptions are **not handled**.
  - The function assumes the file is UTF-8 encoded.

## Example

```python
read_file("my_file_0.txt")
