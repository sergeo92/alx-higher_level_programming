#!/usr/bin/python3

def uppercase(str):
    new_txt = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            new_txt += chr(ord(c)-32)
        else:
            new_txt += c
    print('{}'.format(new_txt))


def main():
    pass


if __name__ == "__main__":
    main()
