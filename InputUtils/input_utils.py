def main():
    
    # Test Cases

    name = get_input("Enter your name: ", str)
    print("Hello,", name)

    choice = get_choice_input("Choose: ", ["a", "b", "c"])
    print("You chose:", choice)

    file_path = get_file_path("Enter file path: ")
    print("File path:", file_path)

    dir_path = get_directory_path("Enter directory path: ")
    print("Directory path:", dir_path)

    date_input = get_date_input("Enter a date (YYYY-MM-DD): ")
    print("Date:", date_input)

    time_input = get_time_input("Enter a time (HH:MM): ")
    print("Time:", time_input)

    option = get_choice_from_list("Choose an option: ", ["Option 1", "Option 2", "Option 3"])
    print("Selected option:", option)

    multiline_input = get_multiline_input("Enter multiple lines of text: ")
    print("You entered:")
    print(multiline_input)

    yes_or_no = get_yes_or_no_input("Yes or no? ")
    print("Your choice:", yes_or_no)


def get_input(prompt, input_type):
    while True:
        try:
            user_input = input_type(input(prompt))
            if not user_input:
                raise ValueError("Input cannot be blank.")
            else:
                return user_input
        except ValueError as e:
            print("Invalid input. Please enter a valid value of type {}.".format(input_type.__name__))
        except EOFError:
            print("End of input. Exiting.")
            exit(1)


def get_choice_input(prompt, choices):
    while True:
        try:
            user_input = input(prompt)
            if user_input.lower() in choices:
                return user_input
            else:
                print("Invalid input. Please choose from the provided options.")
        except EOFError:
            print("End of input. Exiting.")
            exit(1)


def get_file_path(prompt):
    import os
    while True:
        try:
            file_path = input(prompt)
            if os.path.isfile(file_path):
                return file_path
            else:
                print("Invalid file path. Please enter a valid file path.")
        except EOFError:
            print("End of input. Exiting.")
            exit(1)


def get_directory_path(prompt):
    import os
    while True:
        try:
            dir_path = input(prompt)
            if os.path.isdir(dir_path):
                return dir_path
            else:
                print("Invalid directory path. Please enter a valid directory path.")
        except EOFError:
            print("End of input. Exiting.")
            exit(1)


def get_date_input(prompt):
    from datetime import datetime
    while True:
        try:
            date_str = input(prompt)
            return datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format. Please enter a date in the format 'YYYY-MM-DD'.")
        except EOFError:
            print("End of input. Exiting.")
            exit(1)


def get_time_input(prompt):
    from datetime import datetime
    while True:
        try:
            time_str = input(prompt)
            return datetime.strptime(time_str, '%H:%M').time()
        except ValueError:
            print("Invalid time format. Please enter a time in the format 'HH:MM'.")
        except EOFError:
            print("End of input. Exiting.")
            exit(1)


def get_choice_from_list(prompt, options_list):
    print("Options:")
    for index, option in enumerate(options_list):
        print(f"{index + 1}. {option}")

    while True:
        try:
            choice_index = int(input(prompt)) - 1
            if 0 <= choice_index < len(options_list):
                return options_list[choice_index]
            else:
                print("Invalid choice. Please enter a valid option number.")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the desired option.")
        except EOFError:
            print("End of input. Exiting.")
            exit(1)


def get_multiline_input(prompt):
    print(prompt)
    print("Enter your input below. Press Enter on an empty line to finish.")
    lines = []
    while True:
        try:
            line = input()
            if line:
                lines.append(line)
            else:
                return '\n'.join(lines)
        except EOFError:
            print("End of input. Exiting.")
            exit(1)


def get_yes_or_no_input(prompt):
    return get_choice_input(prompt, ["yes", "no"])


if __name__ == "__main__":
    main()