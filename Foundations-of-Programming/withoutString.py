"""
Given two strings, base and remove, return a version of the base string where all instances of the remove string have been removed (not case sensitive). 
You may assume that the remove string is length 1 or more. Remove only non-overlapping instances, so with "xxx" removing "xx" leaves "x".


withoutString("Hello there", "llo") → "He there"
withoutString("Hello there", "e") → "Hllo thr"
withoutString("Hello there", "x") → "Hello there"

"""


def withoutString(main, substring):
    if not main:
        return
    if not substring:
        return main
    return main.replace(substring, "")

def withoutString2(main, substring):
    if not main:
        return
    if not substring:
        return main
    resultString = ""
    i=0
    while i<len(main):
        if main[i:i+len(substring)] == substring:
            i += len(substring)
        else:
            resultString += main[i]
            i += 1
    return resultString


print(withoutString("Hello there", "llo"))
print(withoutString2("Hello there", "llo"))