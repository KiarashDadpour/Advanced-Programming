# This Python code encrypts a message using the Caesar Cipher technique.

main_text = input("enter your text for encryption : ").split()
step = int(input("enter the step : "))
reference_str = "abcdefghijklmnopqrstuvwxyz"
list_text = list(main_text)
for i in range(len(main_text)):
    if list_text[i] == " ":
        continue
    position = reference_str.find(list_text)
    list_text = reference_str[(position+step)%26]
Ciphertext = "".join(list_text)
print(list_text)
