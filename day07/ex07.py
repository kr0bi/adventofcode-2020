class Bag:
    def __init__(self, color, bags_contained):
        self.color = color
        self.bags_contained = bags_contained

    def contains_directly_shiny_gold(self):
        if 'shiny gold' in self.bags_contained:
            return True
        else:
            return False

    def contains_this_bag(self, color_bag):
        if color_bag in self.bags_contained:
            return True
        else:
            return False


f = open("/Users/daniele/Magistrale/adventofcode-2020/day07/input.txt", "r")

bags = []
for riga in f:
    current_color = riga[:(riga.find("bags") - 1)]
    what_contains = riga[(riga.find("contain") + len("contain") + 1):]
    list_pair_quantity_bag = what_contains.split(sep=", ")
    bags_contained = {}
    for element in list_pair_quantity_bag:
        quantity = element[0]
        bag_color = element[2:(element.find("bag") - 1)]
        bags_contained[bag_color] = quantity
    bags.append(Bag(current_color, bags_contained))

set_bags_gold = set()
for bag in bags:
    if bag.contains_directly_shiny_gold():
        set_bags_gold.add(bag)

for i in range(0, len(bags)):
    for bag in bags:
        for bags_with_gold in set_bags_gold:
            if bag.contains_this_bag(bags_with_gold.color):
                if bag not in set_bags_gold:
                    set_bags_gold.add(bag)
                    break
                else:
                    break
# silver
print(len(set_bags_gold))

# prendo una lista di bags che contengono direttamente il gold
# cerco un'altra bag che contiene una della lista precedente 
# se la contiene la aggiungo alla lista
# ripeto per bags volte

def find_gold_bag(bags):
    for bag in bags:
        if bag.color == "shiny gold":
            return bag
    return None

gold_bag = find_gold_bag(bags)

# current bag
# contenuti
# richiama per ogni figlio

def calculate_how_many_bags_in_gold(current_bag, bags):
    if "other" in current_bag.bags_contained:
        return 0
    else:
        list_bags = []
        for bag in bags:
            for color_bag_contained in current_bag.bags_contained:
                if color_bag_contained == bag.color:
                    list_bags.append(bag)
        sum = 0
        for bag in list_bags:
            quantita = int(current_bag.bags_contained[bag.color])
            sum = sum + quantita * (1 + calculate_how_many_bags_in_gold(bag, bags))
        return sum

# gold
print(calculate_how_many_bags_in_gold(gold_bag, bags))
