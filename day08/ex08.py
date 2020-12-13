import copy

f = open("input.txt", "r")

input = []
for riga in f:
    a = riga.replace("\n", "").split(sep=" ")
    a[1] = int(a[1])
    input.append(a)

instruction_count = []
for instruction in input:
    instruction_count.append(instruction + [0])

assert len(input) == len(instruction_count)

def silver (istru_count):
    istruction_count = copy.deepcopy(istru_count)
    acc = 0
    i = 0
    is_looping = True
    while is_looping:
        if i == len(istruction_count):
            is_looping = False
            break
        elif istruction_count[i][2] == 1:
            break
        elif istruction_count[i][0] == 'acc':
            acc += istruction_count[i][1]
            istruction_count[i][2] += 1
            i += 1
        elif istruction_count[i][0] == 'nop':
            istruction_count[i][2] += 1
            i += 1
        elif istruction_count[i][0] == 'jmp':
            istruction_count[i][2] += 1
            i += istruction_count[i][1]
    return acc, is_looping

def count_jmp_nop (instruction_count):
    count = 0
    for instruction in instruction_count:
        if instruction[0] == 'jmp' or instruction[0] == 'nop':
            count += 1
    return count

def gold(instruction_count):
    numbers_of_copy = count_jmp_nop(instruction_count)
    instruction_count_copy = []
    for i in range(0, numbers_of_copy):
        instruction_count_copy.append(copy.deepcopy(instruction_count))
    j = 0
    for i in range(0, len(instruction_count)):
        if instruction_count_copy[j][i][0] == 'jmp':
            instruction_count_copy[j][i][0] = 'nop'
            acc, is_looping = silver(instruction_count_copy[j])
            j += 1
        elif instruction_count_copy[j][i][0] == 'nop':
            instruction_count_copy[j][i][0] = 'jmp'
            acc, is_looping = silver(instruction_count_copy[j])
            j += 1
        if is_looping == False:
            return acc


print(silver(instruction_count))
print(gold(instruction_count))

