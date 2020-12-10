f = open("input.txt", "r")
input = []

for riga in f:
    input.append(riga.split(sep=" "))

for i in range(0, len(input)):
    input[i][2] = input[i][2].replace("\n", "")

# determino i valori X e Y

for i in range(0, len(input)):
    input[i][0] = input[i][0].split(sep="-")
    input[i][0][0] = int(input[i][0][0])
    input[i][0][1] = int(input[i][0][1])

# elimino i due punti
for i in range(0, len(input)):
    input[i][1] = input[i][1].replace(":", "")

# check per ogni riga che sia presente almeno x
# e al max y

def checkAlmenoXY (x, y, key, stringa):
    contatore = 0
    for c in stringa:
        if c == key:
            contatore += 1
    
    if contatore >= x and contatore <= y:
        return True
    else: 
        return False

howManyPWValid = 0
for riga in input:
    if checkAlmenoXY(riga[0][0], riga[0][1], riga[1], riga[2]):
        howManyPWValid += 1

print(howManyPWValid)

# parte due

def checkTruePassword(x,y,key, stringa):
    firstOccurence = stringa[x-1]==key
    secondOccurence = stringa[y-1]==key

    if firstOccurence != secondOccurence:
        return True
    else:
        return False

howManyPWValid = 0
for riga in input:
    if checkTruePassword(riga[0][0], riga[0][1], riga[1], riga[2]):
        howManyPWValid += 1

print(howManyPWValid)