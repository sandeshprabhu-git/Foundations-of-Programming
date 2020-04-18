"""

Given a string, return the sum of the numbers appearing in the string, ignoring all other characters. A number is a series of 1 or more digit chars in a row. (Note: Character.isDigit(char) tests if a char is one of the chars '0', '1', .. '9'. Integer.parseInt(string) converts a string to an int.)


sumNumbers("abc123xyz") → 123
sumNumbers("aa11b33") → 44
sumNumbers("7 11") → 18

"""

def sumNumbers(S):
    if not S:
        return 0
    sum=0
    temp = ""
    for i in S:
        if i.isdigit():
            temp += i
        else:
            if temp:
                sum += int(temp)
                temp = ""
    if temp:
        sum += int(temp)
    return sum


print(sumNumbers("abc123xyz"))
print(sumNumbers("7 11"))
print(sumNumbers("aa11b33"))