'''
Write a recursive function that checks whether string A is a palindrome or Not.
Return 1 if the string A is a palindrome, else return 0.

Input 1:
A = "naman"

Input 2:
A = "strings"

Output 1:
1

Output 2:
0
'''
def checkPalindrome(string, start, end):
    if (start > end):
        return 1
    elif (string[start]!=string[end]):
        return 0
    else:
        return(checkPalindrome(string, start+1, end -1))

string = input()
print(checkPalindrome(string, 0, len(string)-1))