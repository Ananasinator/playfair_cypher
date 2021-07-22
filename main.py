alphabet = list(map(str, str(input())))
# put input()

key = str(input())
message = str(input())
# put input()

# NOTE: creating an array of alphabets using the given alphabet
alphabets_arr = [alphabet]
for i in range(len(alphabet)):
    alphabet.append(alphabet[0])
    alphabet.pop(0)
    str_al = ' '.join(alphabet)
    if str_al.split(" ")[0] == 'а':
        break
    alphabets_arr.append(str_al.split(" "))

for els in alphabets_arr:
    print(str(els) + "\n")

# NOTE: creating a string of continued key at the length of message needed to encrypt
code_str = ""
counter = 0
for i in range(len(message)):
    if counter == len(key):
        counter = 0
    code_str += key[counter]
    counter += 1

print(code_str)
# list(code_str)
h_ind, v_ind = 0, 0
answer = ""
for i in range(len(code_str)):
    h_ind = alphabets_arr[0].index(code_str[i])
    for j in range(len(alphabet)+1):
        if alphabets_arr[j][0] == message[i]:
            v_ind = j
            break
    # print(h_ind, alphabets_arr[0][h_ind], v_ind, alphabets_arr[v_ind][0])
    # print(alphabets_arr[v_ind][h_ind])
    answer += alphabets_arr[v_ind][h_ind]
print(answer)
