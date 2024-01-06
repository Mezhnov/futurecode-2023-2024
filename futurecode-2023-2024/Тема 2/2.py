"""""Задание 2

Напишите программу на Python, которая проверяет, является ли введенная строка палиндромом.
Программа должна вывести "YES", если строка - палиндром, и "NO" в противном случае.

Введите строку: radar
Результат: YES

Введите строку: python
Результат: NO
"""""

def is_palindrome(string):
    string = string.replace(" ", "").lower()
    if string == string[::-1]:
        return True
    else:
        return False

input_string = input("Введите строку: ")

if is_palindrome(input_string):
    print("Результат: YES")
else:
    print("Результат: NO")