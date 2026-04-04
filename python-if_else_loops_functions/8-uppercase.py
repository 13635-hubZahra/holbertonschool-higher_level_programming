def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            char = chr(ord(c) - 32)
        else:
            char = c
        print("{:s}".format(char), end="")
    print("")
