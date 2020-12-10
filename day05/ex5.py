f = open("input.txt", "r")
tickets = []
for riga in f:
    tickets.append(riga.replace("\n", ""))

def convert_column_to_number (column):
    if len(column) > 0:
        return convert_f(column[:1], len(column)-1) + convert_column_to_number(column[1:])
    else:
        return 0

def convert_f(val, exp):
    if (val=='B' or val=='R'):
        return pow(2, exp)
    else:
        return 0


def find_seat (ticket):
    # first part
    row = ticket[:7]
    column = ticket[7:]

    n1 = convert_column_to_number(row)
    n2 = convert_column_to_number(column)

    return [n1, n2]

seat_id = []
for ticket in tickets:
    seat_id.append(find_seat(ticket))


def search_max_id(seat_id):
    max = 0
    for seat in seat_id:
        current = seat[0] * 8 + seat[1]
        if max < current:
            max = current
    return max

def search_list_id(seat_id):
    list_id = []
    for seat in seat_id:
        list_id.append(seat[0] * 8 + seat[1])
    return list_id



print(search_max_id(seat_id))
list_id = sorted(search_list_id(seat_id))

def search_my_seat (list_id):
    prec = list_id[0]
    succ = list_id[2]
    for i in range (1, len(list_id) - 1):
        current = list_id[i]
        if prec + 1 == current and succ - 1 == current:
            prec = list_id[i]
            succ = list_id[i+2]
        else:
            if prec + 1 != current:
                return list_id[i]-1
            elif succ -1 != current:
                return list_id[i]+1
    return -1

print(search_my_seat(list_id))