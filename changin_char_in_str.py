"""str = "sahil"
# print(str[1])
# str[2] = "g" , 'str' object does not support item assignment
new_str = list(str)

new_str.insert(2,"g")

print (new_str)

str2 = "".join(new_str)

print (str2)
"""

def mutate_string(string, position, character):
    str1 = list(string)
    str1[position] = character
    str2 = "".join(str1)
    
    return str2

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)