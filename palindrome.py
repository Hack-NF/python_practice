# for reversing string
def reverse_str(s):
    if len(s) == 0:
        return s
    return reverse_str(s[1:]) + s[0] 
                                                         # stri = s[::-1]
# for checking palindrome
def check_palindrom(st, re_st):
    if st == re_st:
        print("It is a palindrome")
    else:
        print("Not a palindrome")

st = input("Enter a string: ")
re_st = reverse_str(st)
print("reversed: ", re_st)
check_palindrom(st, re_st )

    