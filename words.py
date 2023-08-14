print("Hello! give me a sentence and I will tell you how many words have been used in it.")

user_sentence = input("your sentence: ")
list = user_sentence.split(" ")

print(list)
print(len(list))