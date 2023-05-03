# import this


def pigs():
    bricks = int(input("Enter three digits (each digit for one pig): "))
    total = bricks % 10 + bricks // 100 + bricks // 10 % 10
    print(total)
    print(total // 3)
    print(total % 3)
    print(total % 3 == 0)

def taki():
    print('"Shuffle, Shuffle, Shuffle", say it together!\nChange colors and directions,\nDon\'t back down and stop the player!\n\tDo you want to play Taki?\n\tPress y\\n')

def code():
    encrypted_message = "!XgXnXiXcXiXlXsX XnXoXhXtXyXpX XgXnXiXnXrXaXeXlX XmXaX XI"
    print(encrypted_message[::-2])

def replace():
    input_str = input("Please enter a string: ")

    if len(input_str) > 0:
        first_char = input_str[0]
        input_str = first_char + input_str[1:].replace(first_char, 'e')
        print(input_str)
    else:
        print("Error: input string is empty")

def half_upper():
    input_str = input("Please enter a string: ")
    midpoint = len(input_str) // 2
    if len(input_str) % 2 == 0:
        modified_str = input_str[:midpoint].lower() + input_str[midpoint:].upper()
    else:
        modified_str = input_str[:midpoint + 1].lower() + input_str[midpoint:].upper()
    print(modified_str)


def palindrom():
    input_str = input("Please enter a string: ")
    input_str = input_str.lower().replace(" ", "")

    if input_str == input_str[::-1]:
        print("OK")
    else:
        print("NOT")

def degrees():
    temp_str = input("Enter temperature with suffix: ")
    temp_suffix = temp_str[-1].upper()
    temp = float(temp_str[:-1])

    if temp_suffix == "C":
        temp_f = (9 * temp + (32 * 5)) / 5
        print(f"{temp_f:.2f}F")
    elif temp_suffix == "F":
        temp_c = (5 * temp - 160) / 9
        print(f"{temp_c:.2f}C")
    else:
        print("Invalid input")

import calendar
def date():
    date_str = input("Enter a date: ")
    day, month, year = map(int, date_str.split('/'))
    day_of_week = calendar.weekday(year, month, day)

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(days[day_of_week])


def last_early(my_str):
    my_str = my_str.lower()
    last_char = my_str[-1]
    return last_char in my_str[:-1]


def distance(num1, num2, num3):
    dist_2 = abs(num1 - num2)
    dist_3 = abs(num1 - num3)
    if (dist_2 <= 1 and dist_3 >= 2) or (dist_3 <= 1 and dist_2 >= 2):
        return True
    return False


def filter_teens(a = 13, b = 13, c = 13):
    return fix_age(a) + fix_age(b) + fix_age(c)

def fix_age(age):
    if age in [13, 14, 17, 18, 19]:
        return 0
    else:
        return age

def chocolate_maker(small, big, x):
    if small + big * 5 >= x:
        return True
    else:
        return False


def func(num1, num2):
    """Calculates the sum of num1 and num2.
       :param num1: num1 value
       :param num2: num2 value
       :type num1: int
       :type num2: int
       :return: The sum of num1 and num2
       :rtype: int
       """
    return num1 + num2


def shift_left(my_list):
    """Shifts a list of length 3 one step to the left.
       :param my_list: my_list value
       :type my_list: list
       :return: The new list.
       :rtype: list
       """
    return [my_list[1], my_list[2], my_list[0]]


def format_list(my_list):
    """
       :param my_list: my_list value
       :type my_list: list
       :return: the words in the even indexes and the word in the last index.
       :rtype: str
       """
    return "{}, and {}".format(", ".join(my_list[::2]), my_list[-1])


def extend_list_x(list_x, list_y):
    """extent list_x.
       :param list_x: list_x value
       :param list_y: list_y value
       :type list_x: list
       :type list_y: list
       :return: The new list.
       :rtype: list
       """
    list_x.reverse()
    while list_y:
        list_x.append(list_y.pop())
    list_x.reverse()
    return list_x


def are_lists_equal(list1, list2):
    """Check if the lists are equal.
       :param list1: list1 value
       :param list2: list2 value
       :type list1: list
       :type list2: list
       :return: True if yes False if no.
       :rtype: bool
       """
    return sorted(list1) == sorted(list2)


def longest(my_list):
    """Find the longest str.
       :param my_list: my_list value
       :type my_list: list
       :return: The longest str.
       :rtype: str
       """
    return max(my_list, key=len)


def squared_numbers(start, stop):
    """Create a list that contains all the squares of the numbers between start and stop (inclusive).
        :param start: start value
        :param stop: stop value
        :type start: int
        :type stop: int
        :return: The list.
        :rtype: list
        """
    lst = []
    while start <= stop:
        lst.append(pow(start, 2))
        start += 1
    return lst


def is_greater (my_list, n):
    """Create a list that contains all numbers in my_list that is bigger than n
        :param my_list: my_list value
        :param n: n value
        :type my_list: list
        :type n: int
        :return: The list.
        :rtype: list
        """
    lst = []
    for num in my_list:
        if num > n:
            lst.append(num)
    return lst

def numbers_letters_count(my_str):
    """Create a list in which the first element represents the number of digits in the string,
        and the second element represents everything that is not a digit.
        :param my_str: my_str value
        :type my_str: str
        :return: The list.
        :rtype: list
        """
    lst = [0, 0]
    for tav in my_str:
        if tav.isdigit():
            lst[0] += 1
        else:
            lst[1] += 1
    return lst


def seven_boom(end_number):
    """Create a list in the range of numbers 0 to end_number inclusive, with certain numbers replaced
        by the string 'BOOM', if The number is a multiple of the number 7 or contains the digit 7.
        :param end_number: end_number value
        :type end_number: int
        :return: The list.
        :rtype: list
        """
    lst = []
    for i in range(end_number + 1):
        if i % 7 == 0 or str(i).__contains__("7"):
            lst.append("BOOM")
        else:
            lst.append(i)
    return lst


def sequence_del(my_str):
    """Deletes the letters appearing in a sequence.
       :param my_str: my_str value
       :type my_str: list
       :return: The new str.
       :rtype: str
       """
    result = ''
    for i in range(len(my_str)):
        if i == 0 or my_str[i] != my_str[i-1]:
            result += my_str[i]
    return result

def groceries():
    """The program asks the user to enter a number (digit) in the range one to nine.
        Depending on the number received, an action is performed.
       """
    product_list = input("Enter a list of products separated by commas: ").split(',')

    while True:
        choice = int(input("Enter a number: "))
        if choice == 1:
            print("Product list: ", product_list)
        elif choice == 2:
            print("Number of products: ", len(product_list))
        elif choice == 3:
            product = input("Enter a product name: ")
            if product in product_list:
                print(product, "is on the list")
            else:
                print(product, "is not on the list")
        elif choice == 4:
            product = input("Enter a product name: ")
            print(product, "appears", product_list.count(product), "times on the list")
        elif choice == 5:
            product = input("Enter a product name: ")
            if product in product_list:
                product_list.remove(product)
                print(product, "has been removed from the list")
            else:
                print(product, "is not on the list")
        elif choice == 6:
            product = input("Enter a product name: ")
            product_list.append(product)
            print(product, "has been added to the list")
        elif choice == 7:
            invalid_products = [product for product in product_list if len(product) < 3 or not product.isalpha()]
            if invalid_products:
                print("Invalid products: ", invalid_products)
            else:
                print("There are no invalid products in the list")
        elif choice == 8:
            product_list = list(set(product_list))
            print("All duplicates have been removed from the list")
        else:
            break


def arrow(my_char, max_length):
    """Creates a str representing an arrow structure, built from the input, where the center of
        the arrow (the longest line) is the length of the size passed as a parameter.
       :param my_char: my_char value
       :param max_length: max_length value
       :type my_char: str
       :type max_length: int
       :return: The arrow str.
       :rtype: str
       """
    arrow_parts = []
    for i in range(1, max_length + 1):
        arrow_parts.append((my_char + " ") * i)
    for i in range(max_length - 1, 0, -1):
        arrow_parts.append((my_char + " ") * i)
    return "\n".join(arrow_parts)


def format_string():
    """Updates the format_string variable.
       """
    data = ("self", "py", 1.543)
    format_string = "Hello %s.%s learner, you have only %.1f units left before you master the course!"

    print(format_string % data)

def sort_prices(list_of_tuples):
    """Sortes the list by prices from the bigest to the smallest
       :param list_of_tuples: list_of_tumples value
       :type list_of_tuples: list
       :return: The sorted list.
       :rtype: list
       """
    print(type(list_of_tuples))
    return sorted(list_of_tuples, key=lambda x: float(x[1]), reverse=True)


def mult_tuple(tuple1, tuple2):
    """Creates a tuple containing all the pairs that can be created from the members of the tuples passed as arguments.
       :param tuple1: tuple1 value
       :param tuple2: tuple2 value
       :type tuple1: tuple
       :type tuple2: tuple
       :return: The new tuple.
       :rtype: tuple
       """
    lst = []
    for a in tuple1:
        for b in tuple2:
            lst.append((a, b))
            lst.append((b, a))
    return tuple(lst)


def sort_anagrams(list_of_strings):
    """Creates a list of the same strings transferred, but in the following way: the list is divided into lists
        so that each "internal" list consists of words that are anagrams of each other.
       :param list_of_strings: list_of_strings value
       :type list_of_strings: list
       :return: The new list.
       :rtype: list
       """
    anagram_lists = {}
    for word in list_of_strings:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagram_lists:
            anagram_lists[sorted_word] = [word]
        else:
            anagram_lists[sorted_word].append(word)

    sorted_anagrams = []
    for word in list_of_strings:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_lists and sorted_word not in sorted_anagrams:
            sorted_anagrams.append(sorted_word)

    lst = []
    for anagram in sorted_anagrams:
        lst.append(anagram_lists[anagram])

    return lst


def dict():
    """Creates a dict and performs action on it, depending on the digit that the user keyed:
       """
    dict = {"first_name" : "Mariah",
            "last_name": "Carey",
            "birth_date" : "27.03.1970",
            "hobbies" : ["Sing", "Compose", "Act"]}
    num = int(input("Enter a number: "))
    if num == 1:
        print(dict.get("last_name"))
    elif num == 2:
        print(dict.get("birth_date").split('.')[1])
    elif num == 3:
        print(len(dict.get("hobbies")))
    elif num == 4:
        print(dict.get("hobbies")[-1])
    elif num == 5:
        dict.get("hobbies").append("Cooking")
        print(dict.get("hobbies"))
    elif num == 6:
        print(tuple(dict.get("birth_date").split('.')))
    else:
        dict["age"] = 2023 - int(dict.get("birth_date").split('.')[2])
        print(dict.get("age"))


def count_chars(my_str):
    """Creates a dict, so that each element in it is a pair consisting of a key: a character from the passed string,
        and a value: the number of times the character appears in the string.
       :param my_str: my_str value
       :type my_str: str
       :return: The dict.
       :rtype: dict
       """
    char_count = {}
    for char in my_str.replace(" ", ""):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def inverse_dict(my_dict):
    """Inverses the dict so that the values are the keys and the keys are the values
       :param my_dict: my_dict value
       :type my_dict: dict
       :return: The inversed dict.
       :rtype: dict
       """
    inverted = {}
    for key, value in my_dict.items():
        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value].append(key)
    for key in inverted:
        inverted[key].sort()
    return inverted


def are_files_equal(file1, file2):
    """Checks if the contexts of the files is equal
       :param file1: file1 value
       :param file2: file2 value
       :type file1: str
       :type file2: str
       :return: True if equal False if not.
       :rtype: bool
       """
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        return f1.read() == f2.read()


def task_on_file():
    """Gets a path and a task and do the task on the file in the path
       """
    file_path = input("Enter a file path: ")
    task = input("Enter a task (sort, rev, or last): ")

    with open(file_path, "r") as file:
        lines = file.readlines()

    if task == "sort":
        words = []
        for line in lines:
            words.extend(line.strip().split())
        sorted_words = sorted(list(set(words)))
        print(sorted_words)
    elif task == "rev":
        for line in lines:
            reversed_line = line.strip()[::-1]
            print(reversed_line)
    elif task == "last":
        n = int(input("Enter a number: "))
        for line in lines[-n:]:
            print(line.strip())
    else:
        print("Invalid task")


def copy_file_content(source, destination):
    """Copy the content in source to destination
       :param source: source value
       :param destination: destination value
       :type source: str
       :type destination: str
       """
    with open(source, 'r') as f_source, open(destination, 'w') as f_destination:
        content = f_source.read()
        f_destination.write(content)


def who_is_missing(file_name):
    """Finds the missing number in file_name and write it in found.txt
       :param file_name: file_name value
       :type file_name: str
       :return: The missing number.
       :rtype: int
       """
    with open(file_name, 'r') as f:
        numbers = f.read().strip().split(',')
        numbers = [int(num) for num in numbers]
        n = len(numbers) + 1
        sorted_numbers = sorted(numbers)
        for i in range(1, n):
            if i not in sorted_numbers:
                with open(r'C:\found.txt', 'w') as f2:
                    f2.write(str(i))
                return i


def my_mp3_playlist(file_path):
    """Creates a tuple in which the first member is a string representing the name of the longest song in the file,
        The second member is a number representing the number of songs the file contains,
        The third member is a string representing the name of the operation that appears in the file the largest number of times
       :param file_path: file_path value
       :type file_path: str
       :return: The tuple.
       :rtype: tuple
       """
    
    with open(file_path, 'r') as f:
        lines = f.readlines()
        longest_song_length = 0
        longest_song_name = ''
        operation_count = {}
        song_count = len(lines)

        for line in lines:
            parts = line.strip().split(';')
            song_name = parts[0]
            performer_name = parts[1]
            song_length = parts[2]
            minutes, seconds = map(int, song_length.split(':'))
            total_seconds = minutes * 60 + seconds
            if total_seconds > longest_song_length:
                longest_song_length = total_seconds
                longest_song_name = song_name
            operation_name = performer_name
            if operation_name in operation_count:
                operation_count[operation_name] += 1
            else:
                operation_count[operation_name] = 1

        max_count = 0
        max_operation_name = ''
        for operation_name, count in operation_count.items():
            if count > max_count:
                max_count = count
                max_operation_name = operation_name
        return (longest_song_name, song_count, max_operation_name)


def my_mp4_playlist(file_path, new_song):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    if len(lines) < 3:
        lines += ['\n'] * (3 - len(lines))
    lines[2] = new_song + ';' + lines[2].split(';')[1] + ';' + lines[2].split(';')[2] + "\n"
    with open(file_path, 'w') as f:
        f.writelines(lines)
    with open(file_path, 'r') as f:
        print(f.read())



if __name__ == '__main__':
      # pigs()
      # taki()
      # code()
      # replace()
      # half_upper()
      # palindrom()
      # degrees()
      # date()
      # print(last_early("X"))
      # print(distance(4, 5, 3))
      # print(filter_teens(2, 1, 15))
      # print(chocolate_maker(3, 2, 10))
      # help(func)
      # print(shift_left(['monkey', 2.0, 1]))
      # print(format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]))
      # print(extend_list_x([4,5,6], [1,2,3]))
      # print(are_lists_equal([0.6, 1, 2, 3], [9, 0, 5, 10.5]))
      # print(longest(["111", "234", "2000", "goru", "birthday", "09"]))
      # print(squared_numbers(-3, 3))
      # print(is_greater([1, 30, 25, 60, 27, 28], 28))
      # print(numbers_letters_count("Python 3.6.3"))
      # print(seven_boom(17))
      # print(sequence_del("Heeyyy   yyouuuu!!!"))
      # groceries()
      # print(arrow('*', 5))
      # format_string()
      # print(sort_prices([('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]))
      # print(mult_tuple((1, 2, 3), (4, 5, 6)))
      # print(sort_anagrams(['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']))
      # dict()
      # print(count_chars("abra cadabra"))
      # print(inverse_dict({'I': 3, 'love': 3, 'self.py!': 2}))
      # print(are_files_equal("c:\vacation.txt", "c:\work.txt"))
      # task_on_file()
      # source = input("source: ")
      # destination = input("destination: ")
      # copy_file_content(source, destination)
      # name_file = input("name file: ")
      # print(who_is_missing(name_file))
      # songs = input("Enter path: ")
      # print(my_mp3_playlist(songs))
      songs = input("Enter path: ")
      print(my_mp4_playlist(songs, "Python Love Story"))

