def is_palindrone(s):
    s = s.replace(" ","").lower()
    return s == s[::-1]

my_input = input("enter the string: ")
if is_palindrone(my_input):
    print("the string is palindrone")
else:
    print("not a palindrone")

