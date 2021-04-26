import time


def count_substring(string, sub_string):
    """cnt = 0      # O(n*m)
    if len(sub_string) > len(string):
        return 0
    if sub_string == " ":
        return 0
    if not sub_string: return 0
    for i in range(len(string)- len(sub_string)+1):
        stri = i
        patterni = i
        while stri< len(string) and patterni < len(sub_string) and string[stri] == sub_string[patterni]:
            stri+=1
            patterni +=1
        if patterni == len(sub_string): cnt+=1

    return cnt"""
    # O() hashing, Robin Karp algorithm
    cnt = 0

    if string is None or sub_string is None:
        return 0
    if string == "" or sub_string == "":
        return 0
    if len(sub_string) > len(string):
        return 0

    hashtext = Hash(string, len(sub_string))
    hashPattern = Hash(sub_string, len(sub_string))
    hashPattern.update()

    for i in range(len(string) - len(sub_string)+1):
        if hashtext.hash_value() == hashPattern.hash_value():
            #print("Here")
            if hashtext.text() == sub_string:
                #print("Value Here")
                cnt +=1
        hashtext.update()

    return cnt


class Hash:
    def __init__(self,text,size):
        self.str = text
        self.hash = 0
        for i in range(size):
            self.hash += ord(self.str[i])
        self.init = 0
        self.end = size


    def update(self):
        if self.end <= len(self.str)-1:
            self.hash -= ord(self.str[self.init])
            self.hash += ord(self.str[self.end])
            self.init +=1
            self.end +=1


    def hash_value(self):
        return self.hash


    def text(self):
        #print(self.str[self.init: self.end])
        return self.str[self.init:self.end]


