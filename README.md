PYPI LINK: https://pypi.org/project/InputUtilsSidd/
INSTALL IN PYTHON: pip install InputUtilsSidd

In this script, we define a set of utility functions to interactively get various types of user inputs.

- get_input(prompt, input_type):
  This function prompts the user with the given 'prompt' message and expects input of the specified 'input_type'.
  It keeps prompting until valid input of the specified type is provided. If the input is blank, it raises a ValueError.

- get_choice_input(prompt, choices):
  This function prompts the user with the given 'prompt' message and expects the user to choose from a list of 'choices'.
  It keeps prompting until a valid choice is made and returns the chosen option.

- get_file_path(prompt):
  This function prompts the user with the given 'prompt' message and expects a file path input.
  It checks if the provided path corresponds to an existing file and returns the valid file path.

- get_directory_path(prompt):
  This function prompts the user with the given 'prompt' message and expects a directory path input.
  It checks if the provided path corresponds to an existing directory and returns the valid directory path.

- get_date_input(prompt):
  This function prompts the user with the given 'prompt' message and expects a date input in the format 'YYYY-MM-DD'.
  It converts the input into a Python date object and returns it.

- get_time_input(prompt):
  This function prompts the user with the given 'prompt' message and expects a time input in the format 'HH:MM'.
  It converts the input into a Python time object and returns it.

- get_choice_from_list(prompt, options_list):
  This function prompts the user with the given 'prompt' message and displays a list of options.
  The user is expected to choose an option by providing the corresponding number.
  It returns the selected option from the list.

- get_multiline_input(prompt):
  This function prompts the user with the given 'prompt' message and expects multiple lines of text as input.
  The user can input multiple lines, and pressing Enter on an empty line will indicate the end of input.
  It returns the entered lines as a single string.

- get_yes_or_no_input(prompt):
  This function is a specialized version of 'get_choice_input', where the user is prompted with the given 'prompt' message
  and expects either "yes" or "no" as input. It returns the chosen option ("yes" or "no").

Each function is designed to handle user inputs gracefully, providing helpful error messages for incorrect input.
Use these utility functions to simplify user interactions and enhance the overall user experience in your Python programs.