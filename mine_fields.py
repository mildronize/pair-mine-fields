#!/usr/bin/env python3

def is_mine(field):
    if field == '*':
        return True
    return False

def is_field_validate(field):
    if field == '*' or field == '.':
        return True
    return False

if __name__ == '__main__':

    # I/O
    m = int(input())
    n = int(input())
    print("m = "+ str(m) + " n = " + str(n))
    tabs = []
    for i in range(m):
        tabs.append(str(input()))

    for tab in tabs:
        print(tab)
