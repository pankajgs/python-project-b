def magic(word, s):
    # function that performs the checking operation
    lenght = len(s)
    i = 0
    count = 0
    success = 0
    while (i < lenght):
        if ((s[i].isalpha()) == True):
            # taking only alphabetical characters into consideration
            count = count + 1
            if (s[i] in word):
                success = success + 1
        i = i + 1

    if (success == count):
        print("true")
    else:
        print("false")


word = input("enter the word:")
s = input("enter the string :")
magic(word, s)  # calling function