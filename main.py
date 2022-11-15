# Kata 08 №1

"""
Find Mean
Find the mean (average) of a list of numbers in an array.

Information
To find the mean (average) of a set of numbers add
all the numbers together and divide by the number of values in the
list.

For an example list of 1, 3, 5, 7

1. Add all of the numbers

1+3+5+7 = 16
2. Divide by the number of values in the list. In this example there are 4 numbers in the list.

16/4 = 4
3. The mean (or average) of this list is 4
"""


def find_average(nums):  # по условию nums - список цифр
    if not nums:  # проверка на пустой список
        return 0
    else:
        summa = 0  # дополнительная переменная с суммой
        for number in nums:  # перебираем список nums на составляющие
            summa = summa + number  # прибавляем к сумме каждый элемент списка
        total = summa / len(nums)  # делим сумму на число элементов списка
        return total  # возвращаем результат


# Kata 08 02
"""
Your task is simply to count the total number of lowercase letters in a string.

Examples
lowercaseCount("abc"); ===> 3

lowercaseCount("abcABC123"); ===> 3

lowercaseCount("abcABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"); ===> 3

lowercaseCount(""); ===> 0;

lowercaseCount("ABC123!@€£#$%^&*()_-+=}{[]|\':;?/>.<,~"); ===> 0

lowercaseCount("abcdefghijklmnopqrstuvwxyz"); ===> 26
"""


def lowercase_count(strng):  # подается строка с данными
    summa = 0  # дополнительная переменная для счетчика
    for letter in strng:  # перебираем данные
        if letter.islower():  # islower() - возвращается истину, если символ в строке в нижнем регистре
            summa = summa + 1  # счетчик
    return summa


# Kata 08 #03

"""You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this 
is not clear enough, here are some examples:

As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

Example (Input --> Output)

"Hello World" --> "World Hello"
"Hi There." --> "There. Hi"
Happy coding!"""


def reverse(st):
    list_new = st.split()
    list_new.reverse()
    string = " ".join(list_new)
    return string


# Kata 08 #04

"""Overview
Hello, this is my first Kata so forgive me if it is of poor quality.

In this Kata you should fix/create a program that returns the following values:

false/False if either a or b (or both) are not numbers
a % b plus b % a if both arguments are numbers
You may assume the following:

If a and b are both numbers, neither of a or b will be 0.
Language-Specific Instructions
Javascript and PHP
In this Kata you should try to fix all the syntax errors found in the code.

Once you think all the bugs are fixed run the code to see if it works. A correct solution should return the values 
specified in the overview.

Extension: Once you have fixed all the syntax errors present in the code (basic requirement), you may attempt to 
optimise the code or try a different approach by coding it from scratch."""


def my_first_kata(a, b):
    a = str(a)  # Перегоняем в строку, иначе костыль снизу не работает
    b = str(b)  # Перегоняем в строку, иначе костыль снизу не работает
    if a.isdigit() and b.isdigit() or a == [] or b == []:  # isdigit() - проверяет строку на наличие цифр внутри
        a = int(a)  # перегоняем обратно в число
        b = int(b)  # перегоняем обратно в число
        return a % b + + b % a
    else:
        return False


# Unfinished Loop - Bug Fixing #1
"""
    Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished for loop!
"""


def create_array(n):
    res = []
    i = 1
    while i <= n:
        res += [i]
        i = i + 1
    return res


# Get the mean of an array

"""
It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students 
come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.

Return the average of the given array rounded down to its nearest integer.

The array will never be empty.
"""


def get_average(marks):
    summa = 0
    for i in marks:
        summa = i + summa
    return int(summa / len(marks))


# Grasshopper - Messi Goals

"""
Messi's Goal Total
Use variables to find the sum of the goals Messi scored in 3 competitions

Information
Messi goal scoring statistics:

Competition	Goals
La Liga	43
Champions League	10
Copa del Rey	5
Task
Create these three variables and store the appropriate values using the table above:
la_liga_goals
champions_league_goals
copa_del_rey_goals
Create a fourth variable named total_goals that stores the sum of all of Messi's goals for this year.
"""

la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals

# Opposites Attract

"""
Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. 
If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

Write a function that will take the number of petals of each flower and return true if they are in love and false 
if they aren't.
"""


def lovefunc(flower1, flower2):
    if flower1 % 2 == 0 and flower2 % 2 == 0:
        return False
    elif flower1 % 2 > 0 and flower2 % 2 > 0:
        return False
    else:
        return True


# Grader

"""
Create a function that takes a number as an argument and returns a grade based on that number.

Score	Grade
Anything greater than 1 or less than 0.6	"F"
0.9 or greater	"A"
0.8 or greater	"B"
0.7 or greater	"C"
0.6 or greater	"D"

"""


def grader(score):
    if score > 1 or score < 0.6:
        return "F"
    elif 0.6 <= score < 0.7:
        return "D"
    elif 0.7 <= score < 0.8:
        return "C"
    elif 0.8 <= score < 0.9:
        return "B"
    elif 0.9 <= score:
        return "A"
