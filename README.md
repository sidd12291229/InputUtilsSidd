## InputUtilsSidd - Utility Functions for User Inputs

[![PyPI Version](https://img.shields.io/pypi/v/InputUtilsSidd)](https://pypi.org/project/InputUtilsSidd/)

[PyPI Link for this project](https://pypi.org/project/InputUtilsSidd/)

### Installation

You can easily install InputUtilsSidd using pip:

```bash
pip install InputUtilsSidd
```

### Provided Functions

1. `get_input(prompt, input_type)`

   This function prompts the user with the given `prompt` message and expects input of the specified `input_type`. It keeps prompting until valid input of the specified type is provided. If the input is blank, it raises a `ValueError`.

   - `prompt`: The message to display to the user as the input prompt.
   - `input_type`: The type of input expected (e.g., `int`, `float`, `str`, etc.).

2. `get_choice_input(prompt, choices)`

   This function prompts the user with the given `prompt` message and expects the user to choose from a list of `choices`. It keeps prompting until a valid choice is made and returns the chosen option.

   - `prompt`: The message to display to the user as the input prompt.
   - `choices`: A list of options from which the user can choose.

3. `get_file_path(prompt)`

   This function prompts the user with the given `prompt` message and expects a file path input. It checks if the provided path corresponds to an existing file and returns the valid file path.

   - `prompt`: The message to display to the user as the input prompt.

4. `get_directory_path(prompt)`

   This function prompts the user with the given `prompt` message and expects a directory path input. It checks if the provided path corresponds to an existing directory and returns the valid directory path.

   - `prompt`: The message to display to the user as the input prompt.

5. `get_date_input(prompt)`

   This function prompts the user with the given `prompt` message and expects a date input in the format `YYYY-MM-DD`. It converts the input into a Python `date` object and returns it.

   - `prompt`: The message to display to the user as the input prompt.

6. `get_time_input(prompt)`

   This function prompts the user with the given `prompt` message and expects a time input in the format `HH:MM`. It converts the input into a Python `time` object and returns it.

   - `prompt`: The message to display to the user as the input prompt.

7. `get_choice_from_list(prompt, options_list)`

   This function prompts the user with the given `prompt` message and displays a list of options. The user is expected to choose an option by providing the corresponding number. It returns the selected option from the list.

   - `prompt`: The message to display to the user as the input prompt.
   - `options_list`: A list of options from which the user can choose.

8. `get_multiline_input(prompt)`

   This function prompts the user with the given `prompt` message and expects multiple lines of text as input. The user can input multiple lines, and pressing Enter on an empty line will indicate the end of input. It returns the entered lines as a single string.

   - `prompt`: The message to display to the user as the input prompt.

9. `get_yes_or_no_input(prompt)`

   This function is a specialized version of `get_choice_input`, where the user is prompted with the given `prompt` message and expects either "yes" or "no" as input. It returns the chosen option ("yes" or "no").

   - `prompt`: The message to display to the user as the input prompt.

With these utility functions, you can simplify user interactions and ensure smoother user experiences in your Python programs. Enjoy using `InputUtilsSidd` for interactive user inputs!
### Example Usage
```python
import InputUtilsSidd as utils

# Example usage of the utility functions:

# Get a simple input from the user
name = utils.get_input("Enter your name: ", input_type=str)
print(f"Hello, {name}!")

# Get a choice input from the user
options = ["apple", "banana", "orange"]
chosen_option = utils.get_choice_input("Choose a fruit: ", options)
print(f"You chose: {chosen_option}")

# Get a valid file path from the user
file_path = utils.get_file_path("Enter the file path: ")
print(f"File path: {file_path}")

# Get a valid directory path from the user
dir_path = utils.get_directory_path("Enter the directory path: ")
print(f"Directory path: {dir_path}")

# Get a date input from the user
selected_date = utils.get_date_input("Enter a date (YYYY-MM-DD): ")
print(f"Selected date: {selected_date}")

# Get a time input from the user
selected_time = utils.get_time_input("Enter a time (HH:MM): ")
print(f"Selected time: {selected_time}")

# Get a choice from a list
options_list = ["Option A", "Option B", "Option C"]
selected_option = utils.get_choice_from_list("Select an option: ", options_list)
print(f"Selected option: {selected_option}")

# Get multiline input from the user
description = utils.get_multiline_input("Enter a description (press Enter on a new line to end):\n")
print(f"Description:\n{description}")

# Get yes or no input from the user
response = utils.get_yes_or_no_input("Do you want to continue? (yes/no): ")
if response == "yes":
    print("You chose to continue.")
else:
    print("You chose to stop.")
```
