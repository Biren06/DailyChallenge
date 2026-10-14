x = input("enter palindrome string:")
print(x[::-1])
if x == x[::-1]:
    print("the string is palindrome.")
else:
    print("the string is not palindrome.")
