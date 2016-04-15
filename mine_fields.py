#!/usr/bin/env python3

def is_mine(field):
    if field == '*':
        return True
    return False

def is_field_validate(field):
    if field == '*' or field == '.':
        return True
    return False

def replace_char_in_string(string, char, position):
   return string[:position] + char + string[position+1:]

def count_mine_in_table(tabs):
    count = 0
    for i in range(len(tabs)):
        for j in range(len(tabs[i])):
            if is_mine(tabs[i][j]):
                count += 1
    return count

def convert_dot_to_zero(tabs):
    for i in range(len(tabs)):
        for j in range(len(tabs[i])):
            if not is_mine(tabs[i][j]):
                tabs[i] = replace_char_in_string(tabs[i],'0',j)
    return tabs

def mine_fields(tabs):
    pass
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
