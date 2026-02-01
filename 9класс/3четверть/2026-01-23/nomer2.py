str = input("")
def longest(str):
    words = str.split()
    return max(words , key = len)
print(f"Cамое длинное слово: {longest(str)}")
