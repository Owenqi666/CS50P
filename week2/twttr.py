def shorten(word):
    vowels = "aeiouAEIOU"
    result = ""
    for c in word:
        if c not in vowels:
            result += c
    return result

if __name__ == "__main__":
    x = input("Input: ")
    print(shorten(x))