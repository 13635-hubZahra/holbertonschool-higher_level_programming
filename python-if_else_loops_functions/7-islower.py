#!/usr/bin/python3
def islower(c):
        if ord(c) > 96 and ord(c) < 123:
            return True
        else :
            return False
c = input("")
for i in range (len(c)):
    if islower(cumle[i]):
        print(f"'{cumle[i]}' balacadi")
    else:
        print(f"'{cumle[i]} boyukdu")
