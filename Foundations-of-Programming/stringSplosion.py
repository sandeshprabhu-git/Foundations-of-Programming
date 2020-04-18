"""
Given a non-empty string like "Code" return a string like "CCoCodCode".


stringSplosion("Code") → "CCoCodCode"
stringSplosion("abc") → "aababc"
stringSplosion("ab") → "aab"

"""

def stringSplosion(S):
    result = ""
    for i in range(len(S)):
        result = result + S[:i+1]
    return result


print(stringSplosion("Code"))
print(stringSplosion("abc"))
print(stringSplosion("ab"))
