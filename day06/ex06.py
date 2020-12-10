f = open("/Users/daniele/Magistrale/adventofcode/day06/input.txt", "r")

forms = []
group = []
for riga in f:
    if riga == "\n":
        forms.append(group)
        group = []
    else:
        group.append(riga[:-1])
forms.append(group)

print("meme")

def count_unique_character (group):
    dictionary = {}
    for person in group:
        for question in person:
            if question not in dictionary:
                dictionary[question] = 1

    return len(dictionary)

def count_repeated_character (group):
    dictionary = {}
    for person in group:
        for question in person:
            if question in dictionary:
                dictionary[question] += 1
            else:
                dictionary[question] = 1
    number_of_person = len(group)
    count = 0
    for key in dictionary:
        if number_of_person == dictionary[key]:
            count += 1
    return count

def silver (forms):
    result = 0
    for form in forms:
        result = result + count_unique_character(form)
    return result

def gold (forms):
    result = 0
    for form in forms:
        result = result + count_repeated_character(form)
    return result

print(silver(forms))
print(gold(forms))