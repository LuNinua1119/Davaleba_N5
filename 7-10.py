#დავალება N7
# text = input("დაწერე ტექსტი: ")
# words = text.split()
# result = ""
# for word in words:
#     new_word = ""
#
#     for i in word:
#         if i.isalpha():
#             new_word += i
#
#     result = result + new_word
#
# print(f"გაფილტრული ტექსტი: {result}")




#დავალება N8
# numbers = input("შეიყვანე რიცხვები: (ციფრები უნდა იყოს ერთმანეთისგან განცალკევებული. ")
#
# numbers = numbers.split()
#
# for i in range(len(numbers)):
#     numbers[i] = int(numbers[i])
#
# while len(numbers) > 1:
#     new_row = []
#
#     for i in range(len(numbers) - 1):
#         new_row.append(numbers[i] + numbers[i + 1])
#
#     print(new_row)
#
#     numbers = new_row
#
# print(numbers)





#დავალება N9
# text = input("შეიყვანე ტექსტი: ")
# words = text.lower().split()
#
# count = {}
# for word in words:
#     if word in count:
#         count[word] += 1
#     else:
#         count[word] = 1
#
# max_count = 0
#
# for word in count:
#     if count[word] > max_count:
#         max_count = count[word]
#
# result = []
#
# for word in words:
#     if count[word] == max_count:
#         result.append(word)
#
# print(f'ყველაზე ხშირად დაწერილი სიტყვებია {result}')
# print(f'სულ განმეორდა, {max_count} -ჯერ' )





#დავალება N10
# text = input("შეიყვანე წინადადება: ")
#
# words = text.split()
#
# word_length = {}
#
# for word in words:
#     word_length[word] = len(word)
#
# print(word_length)
