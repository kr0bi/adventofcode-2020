f = open("input.txt", "r")
input = []

for riga in f:
    input.append(int(riga.replace("\n", "")))

def findSomma (input, numero):
    for i in range(0, len(input)):
        for j in range(0, len(input)):
            if input[i]+input[j]==numero:
                return (input[i], input[j])
    return (-1, -1)

result = (findSomma(input, 2020))
print(result)
print(result[0]*result[1])


def findSommaTripla (input, numero):
    for i in range(0, len(input)):
        for j in range(0, len(input)):
            for k in range(0, len(input)):
                if input[i]+input[j]+input[k]==numero:
                    return (input[i], input[j], input[k])
    return (-1, -1, -1)

result2 = findSommaTripla(input, 2020)
print(result2)
print(result2[0]*result2[1]*result2[2])


def findSommaHash(input, numero):
    hashmap = {}
    for i in range(0, len(input)):
        if input[i] in hashmap:
            return (input[hashmap[input[i]]], input[i])
            # index = hashmap[input[i]]
            # targetHolder.append(input[index])
            # targetHolder.append(input[i])
        else:
            hashmap[numero-input[i]] = i
    return (-1, -1)

print(findSommaHash(input, 2020))