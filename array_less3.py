def array_clean(s):
    """
    Function will clear array from long elements
    """

    for index in range(len(s)):
        if len(s[index]) > 3:
            print(s[index])
            #s[index].pop

    pass

print(array_clean (["hello", "2", "world", ":-)"]))

print(array_clean ([["1234", "1567", "-2", "computer science"]]))

print(array_clean (["Russia", "Denmark", "Kazan"]))