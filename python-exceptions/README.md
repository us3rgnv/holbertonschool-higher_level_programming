# Holberton School - Higher Level Programming: Python Tasks

This repository contains solutions for various Python tasks covering data structures, exceptions, and more. Each task is implemented according to Holberton School specifications.

## Directory Structure

- `python-data_structures/` - Tasks related to lists, tuples, and basic data structures.
- `python-more_data_structures/` - Advanced data structures tasks (sets, dictionaries, maps).
- `python-exceptions/` - Tasks involving exception handling.

---

## Task List

### Python Data Structures

1. **0-print_list_integer.py**  
   Function: `print_list_integer(my_list=[])`  
   Prints all integers in a list, one per line.

2. **1-element_at.py**  
   Function: `element_at(my_list, idx)`  
   Returns the element at a given index or `None` if index is invalid.

3. **2-replace_in_list.py**  
   Function: `replace_in_list(my_list, idx, element)`  
   Replaces an element in a list at a specific index.

4. **3-print_reversed_list_integer.py**  
   Function: `print_reversed_list_integer(my_list=[])`  
   Prints all integers of a list in reverse order.

5. **4-new_in_list.py**  
   Function: `new_in_list(my_list, idx, element)`  
   Replaces an element in a list without modifying the original list.

6. **5-no_c.py**  
   Function: `no_c(my_string)`  
   Removes all occurrences of 'c' and 'C' from a string.

7. **6-print_matrix_integer.py**  
   Function: `print_matrix_integer(matrix=[[]])`  
   Prints a matrix of integers.

8. **7-add_tuple.py**  
   Function: `add_tuple(tuple_a=(), tuple_b=())`  
   Adds two tuples element-wise.

9. **8-multiple_returns.py**  
   Function: `multiple_returns(sentence)`  
   Returns a tuple with the length of the string and its first character.

10. **9-max_integer.py**  
    Function: `max_integer(my_list=[])`  
    Returns the largest integer in a list.

11. **10-divisible_by_2.py**  
    Function: `divisible_by_2(my_list=[])`  
    Returns a list of booleans indicating if elements are divisible by 2.

12. **11-delete_at.py**  
    Function: `delete_at(my_list=[], idx=0)`  
    Deletes an element at a specific position in a list.

13. **12-switch.py**  
    Simple program that switches values of two variables.

---

### Python More Data Structures

0. **0-square_matrix_simple.py**  
   Function: `square_matrix_simple(matrix=[])`  
   Returns a new matrix with all elements squared.

1. **1-search_replace.py**  
   Function: `search_replace(my_list, search, replace)`  
   Replaces all occurrences of a value in a list with another.

2. **2-uniq_add.py**  
   Function: `uniq_add(my_list=[])`  
   Adds all unique integers in a list.

3. **3-common_elements.py**  
   Function: `common_elements(set_1, set_2)`  
   Returns a set of common elements in two sets.

4. **4-only_diff_elements.py**  
   Function: `only_diff_elements(set_1, set_2)`  
   Returns elements that are in only one of the sets.

5. **5-number_keys.py**  
   Function: `number_keys(a_dictionary)`  
   Returns the number of keys in a dictionary.

6. **6-print_sorted_dictionary.py**  
   Function: `print_sorted_dictionary(a_dictionary)`  
   Prints dictionary keys in sorted order.

7. **7-update_dictionary.py**  
   Function: `update_dictionary(a_dictionary, key, value)`  
   Updates or adds a key/value pair in a dictionary.

8. **8-simple_delete.py**  
   Function: `simple_delete(a_dictionary, key="")`  
   Deletes a key from a dictionary if it exists.

9. **9-multiply_by_2.py**  
   Function: `multiply_by_2(a_dictionary)`  
   Returns a new dictionary with all values multiplied by 2.

10. **10-best_score.py**  
    Function: `best_score(a_dictionary)`  
    Returns the key with the highest integer value.

11. **11-multiply_list_map.py**  
    Function: `multiply_list_map(my_list=[], number=0)`  
    Returns a new list with all elements multiplied by a number using `map`.

12. **12-roman_to_int.py**  
    Function: `roman_to_int(roman_string)`  
    Converts a Roman numeral string to an integer.

---

### Python Exceptions

0. **0-safe_print_list.py**  
   Function: `safe_print_list(my_list=[], x=0)`  
   Safely prints `x` elements of a list, returns number of elements printed.

---

### Git Workflow Example

```bash
# Add all changes
git add .

# Commit changes
git commit -m "Add task_name.py solution"

# Push to remote
git push origin main

# If remote has new changes
git pull --rebase origin main
git push origin main
