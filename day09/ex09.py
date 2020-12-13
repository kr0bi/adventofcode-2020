# c'e' un preambolo di 25 numeri
# i numeri successivi sono tutti apparte uno la somma di una di queste due coppie

f = open("input.txt", "r")

number_to_keep = 25

i = 0
preamble = []
rest_of_numbers = []
all_numbers = []
for riga in f:
    all_numbers.append(int(riga.replace("\n", "")))
    if i < number_to_keep:
        preamble.append(int(riga.replace("\n", "")))
    else:
        rest_of_numbers.append(int(riga.replace("\n", "")))
    i += 1

def silver (preamble, rest_of_numbers):
    # l'input e' il preambolo e il numero e quello successivo in rest_of_numbers
    for number in rest_of_numbers:
        pair = findSommaHash(preamble, number)
        if pair == (-1, -1):
            return number
        else:
            preamble.pop(0)
            preamble.append(number)
    return -1

def findSommaHash(input, numero):
    hashmap = {}
    for i in range(0, len(input)):
        if input[i] in hashmap:
            return (input[hashmap[input[i]]], input[i])
        else:
            hashmap[numero-input[i]] = i
    return (-1, -1)

invalid_number = (silver(preamble, rest_of_numbers))

def find_contiguous_set (input, invalid_number):
    current_sum = 0
    start_index = 0
    current_index = 0
    while True:
        somma_parziale = current_sum + input[current_index]
        if somma_parziale <invalid_number:
            current_sum += input[current_index]
            current_index += 1
        elif somma_parziale == invalid_number:
            return [start_index, current_index]
        else:
            current_sum = 0
            start_index += 1
            current_index = start_index

print(find_contiguous_set(all_numbers, invalid_number))

def gold (input, invalid_number):
    temp = find_contiguous_set(input, invalid_number)
    start_index = temp[0]
    end_index = temp[1]
    return max(input[start_index:end_index+1]) + min(input[start_index:end_index+1])

print(gold(all_numbers, invalid_number))

