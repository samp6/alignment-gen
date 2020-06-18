the_file = open("opposites.txt", "r")

text = str(the_file.read())

new_text = text.replace("\n", "\",\"")
print(str(new_text))

new_file = open("opposites.py", "w")

new_file.write(new_text)

the_file.close()
new_file.close()