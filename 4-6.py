#დავალება N4
# def clean_text(text):
#     new_text = ""
#
#     for i in text:
#         if i.isalnum():
#             new_text = new_text + i.lower()
#
#     return new_text
#
#
# def is_palindrome(text):
#     if text == text[::-1]:
#         return True
#     else:
#         return False
#
#
# text = input("შეიყვანე ტექსტი: ")
# text = clean_text(text)
#
# if is_palindrome(text):
#     print(f"თქვენი ტექსტი '{text}' პალინდრომია.")
# else:
#     not_palindrome = False
#
#     for i in range(len(text)):
#         temp = text[:i] + text[i + 1:]
#
#         if is_palindrome(temp):
#             print("არ არის პალინდრომი.")
#             print(f"ერთი სიმბოლოს წაშლით მივიღებთ: {temp}")
#             not_palindrome = True
#             break
#
#     if not_palindrome == False:
#         print("ერთი სიმბოლოს წაშლით პალინდრომის მიღება შეუძლებელია.")




#დავალება N5
# name = input("შეიყვანე თქვენი სახელი: ")
# if len(name.split()) != 1:
#     print("გთხოვთ სახელში დაწეროთ მხოლოდ ერთი სიტყვა. ")
# else:
#     print("შესაძლო ზედმესახელები: ")
#     print(name)
#     print(name + "slayer")
#     print("lord" + name)
#     print("pro" + name)
#     print("The" + name + "Fighter")




#დავალება N6
# import random
# numbers = input("შეიყვანე რიცხვები, (ერთმანეთის გამოტოვებით): ")
# numbers = numbers.split()
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#
# print("აირჩიე, როგორ გინდა დავალგო შენი რიცხვები: ")
# print("დაწერე 1, თუ გსრურს რიცხვების ზრდადობით დალაგება. ")
# print("დაწერე 2, თუ გსრურს რიცხვების კლებადობით დალაგება. ")
# print("დაწერე 3, თუ გსრურს რიცხვების შემთხვევითობის პრინციპით დალაგება. ")
# print("დაწერე 4, თუ გსრურს მხოლოდ უნიკალური რიცხვების გამოტანა. ")
#
# choice = input("შენი არჩევანია: ")
# if choice == "1":
#     numbers.sort()
#     print(numbers)
# elif choice == "2":
#     numbers.sort(reverse=True)
#     print(numbers)
# elif choice == "3":
#     random.shuffle(numbers)
#     print(numbers)
# elif choice == "4":
#     numbers = list(set(numbers))
#     print(numbers)
# else:
#     print("აირჩიეთ მხოლოდ ამ 4 ვარანტიდან, რომელიმე")
