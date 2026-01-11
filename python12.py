string = input("Enter a string: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

mid = len(string) // 2
if string[:mid] == string[mid:]:
    print("Symmetrical")
else:
    print("Not Symmetrical")
