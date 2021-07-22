import numpy as np

message = "Прооес!лась,. гроза: седа;яы"  # str(input()).lower
message = list(message.lower())
key = "компас"  # str(input())

key_arr = []
for i in key:
    if i not in key_arr:
        key_arr.append(i)
alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
alphabet = list(alphabet)
for el in alphabet:
    if el in key_arr:
        alphabet[alphabet.index(el)] = ""
alph_key = list("".join(key_arr) + "".join(alphabet))
# print(alph_key)
row1, row2, row3, row4 = np.array_split(alph_key, 4)
matrix = [row1, row2, row3, row4]
# for elem in matrix:
#     print(elem)

symbols = ["!", ",", ".", "?", ":", ";", " ", ' ']
for s in symbols:
    if s in message:
        message.remove(s)
# print(message)
if len(message) % 2 != 0:
    message.append('x')

bigramm = []
for i in range(0, len(message) - 1, 2):
    if message[i] != message[i + 1]:
        bigramm.append(message[i] + message[i + 1])
    else:
        bigramm.append(message[i] + 'x')
# print(*bigramm)

for i in range(len(matrix)):
    for j in bigramm:
        if (j[:1] or j[1:]) in matrix[i]:
            # j[:1] = i[i.find(j[:1])]
            print(1)
