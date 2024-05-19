import task_template as task

text_number = int(input("Enter a number btw. 1 and 3 to select: "))
print(text_number)

if text_number >= 1 and text_number <= 3:
    chosen_text = task.TEXTS[text_number - 1]
    split_of_words = chosen_text.split()
    number_of_words = len(split_of_words)
    print("There are", number_of_words, "words in the selected text")

    a = 0

    for i in split_of_words:
        words = str(i)
        print(words)

        if words[0].isupper():
            a=a+1 
            print("true\n")
        else:
            a=a+0 
            print("false\n")
    print(a)

else:
    print("Wrong selection of text, program will quit")
    quit()
