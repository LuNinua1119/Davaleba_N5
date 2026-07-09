# #დავალება N1
# import random
# import string
#
#
# while True:
#     password_lenght = input("რა სიგრძის პაროლი გსურს?  ")
#
#     if not password_lenght.isdigit():
#         print("ჩაწერეთ მხოლოდ ციფრი")
#         continue
#
#     password_lenght = int(password_lenght)
#     if password_lenght == 0:
#         print("პაროლი ვერ იქნება 0 ინდექსიანია შეიყვანეთ 0 ზე დიდი ციფრი. ")
#         continue
#     break
#
#
# upper = input("გსურთ, რომ გამოვიყენო დიდი ასოები? y/n ")
# lower = input("გსურს, რომ გამოვიყენო პატარა ასოები? y/n ")
# number = input("გსურს, რომ გამოვიყენო ციფრები? y/n ")
# symbols = input("გსურს, რომ გამოვიყენო სინმბოლოები? y/n ")
#
# password = ""
#
# if upper == "y":
#     password += string.ascii_uppercase
#
# if lower == "y":
#     password += string.ascii_lowercase
#
# if number == "y":
#     password += string.digits
#
# if symbols == "y":
#     password += string.punctuation
#
# if password == "":
#     print("უნდა გამოიყენო მინიმუმ ერთი სტილი, რათა შედგეს პაროლი.  ")
#     exit()
# #
# # final_password = ""
# # for i in range(password_lenght):
# #     final_password += random.choice(password)
# #
# # print(f'შენი პაროლია {final_password}' )





# #დავალება N2
# password = input("შეიყვანე პაროლი: ")
# password_strenght = 0
#
# if len(password) >= 12:
#     password_strenght += 3
# elif len(password) >= 8:
#     password_strenght += 2
# elif len(password) >= 6:
#     password_strenght += 1
# else:
#     print("შეყვანილი პაროლი არის ძალიან პატარა. გთხოვ გაართულოთ პაროლი.")
#
#
# if any(c.isdigit() for c in password):
#     password_strenght += 2
#
# if any(not c.isalnum() for c in password):
#     password_strenght += 2
#
# if any(c.isupper() for c in password) and any(c.islower() for c in password):
#     password_strenght += 2
#
# if len(set(password)) == len(password):
#     password_strenght += 1
#
# if password_strenght <= 3:
#     print(f'თქვენ მიერ ჩაწერილი პაროლი სუსტია. {password_strenght} ქულა. ')
# if password_strenght <= 7:
#     print(f'თქვენ მიერ ჩაწერილი პაროლი საშუალო სიძლიერისაა. {password_strenght} ქულა. ')
# if password_strenght >= 8:
#     print(f'თქვენ მიერ ჩაწერილი პაროლი ძლიერია. {password_strenght} ქულა. ')




#დავალება N3
# def fibonacci(c):
#     fib = [0, 1]
#
#     while len(fib) < c:
#         fib.append(fib[-1] + fib[-2])
#
#     return fib[:c]
#
# while True:
#     text = input('შეიყვანე ციფრი: ')
#
#     if text.isdigit():
#         c = int(text)
#         break
#     else:
#         print(f'თქვენი შემოყვანილი სიმბოლო {text} არასწორია. გთხოვოთ დაწეროთ მხოლოდ რიცხვი')
#
# print(fibonacci(c)