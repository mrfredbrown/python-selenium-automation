
def is_string_unique(string):
    set_string = set(string)
    return len(set_string) == len(string)

test_string = 'aabcde'
a = is_string_unique(test_string)
print(a)
test_string2 = 'abcde'
b = is_string_unique(test_string2)
print(b)