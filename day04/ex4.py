import re

f = open("input.txt", "r")

each_new_line_in_file = []

passports = []
passport = []
for riga in f:
    if riga.find(" ")>=0:
        passport = passport + riga.split(sep=" ")
    elif riga != "\n":
        passport = passport + [riga]
    if riga == "\n":
        passports.append(passport)
        passport = []

for i in range(0, len(passports)):
    for j in range(0, len(passports[i])):
        passports[i][j] = passports[i][j].replace("\n", "")

for i in range(0, len(passports)):
    passports[i] = sorted(passports[i])

for i in range(0, len(passports)):
    if passports[i][1].find("cid") >= 0:
        passports[i].remove(passports[i][1])

print("meme")

def check_if_passport_is_valid(passport, fields):
    if len(passport) == len(fields):
        return True
    else:
        return False

def check_all_passports(passports, fields):
    count = 0
    for passport in passports:
        if check_if_passport_is_valid(passport, fields):
            count += 1
    return count


fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

fields = sorted(fields)


print(check_all_passports(passports, fields))

def check_stricter_passport (passport, fields):
    valid_semi_passports =[]
    for e in passport:
        if check_if_passport_is_valid(e, fields):
            valid_semi_passports.append(e)

    count = 0
    for e in valid_semi_passports:
        if check_byr(e[0]) and check_ecl(e[1]) and check_eyr(e[2]) and check_hcl(e[3]) and check_hgt(e[4]) and check_iyr(e[5]) and check_pid(e[6]):
            count += 1
    return count

def check_byr(byr):
    if int(byr[4:]) >= 1920 and int(byr[4:])<=2002:
        return True
    else:
        return False

def check_ecl(ecl):
    possible_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ecl[4:] in possible_ecl:
        return True
    else:
        return False

def check_eyr(eyr):
    if int(eyr[4:]) >= 2020 and int(eyr[4:])<=2030:
        return True
    else:
        return False

def check_hcl(hcl):
    if re.search('#([0-9]|[a-f]){6}', hcl[4:]) == None:
        return False
    else:
        return True

def check_hgt(hgt):
    if hgt.find('cm') >= 0:
        hgt = hgt[:-2]
        if int(hgt[4:])>=150 and int(hgt[4:])<=193:
            return True
        else:
            return False
    elif hgt.find('in') >= 0:
        hgt = hgt[:-2]
        if int(hgt[4:])>=59 and int(hgt[4:])<=76:
            return True
        else:
            return False
    else:
        return False

def check_iyr (iyr):
    if int(iyr[4:]) >= 2010 and int(iyr[4:])<=2020:
        return True
    else:
        return False

def check_pid (pid):
    if re.search('[0-9]{9}', pid[4:]) == None:
        return False
    else:
        return True

print(check_stricter_passport(passports, fields))
