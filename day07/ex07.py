class Bag:
    def __init__(self, color, bags_contained):
        self.color = color
        self.bags_contained = bags_contained
    def contains_directly_shiny_gold(self):  
        if 'shiny gold' in self.bags_contained:
            return True
        else:
            return False

f = open("/Users/daniele/Magistrale/adventofcode-2020/day07/input.txt", "r")

bags = []
for riga in f:
    current_color = riga[:(riga.find("bags")-1)]
    what_contains = riga[(riga.find("contain")+len("contain")+1):]
    list_pair_quantity_bag = what_contains.split(sep=", ")
    bags_contained = {}
    for element in list_pair_quantity_bag:
        quantity = element[0]
        bag_color = element[2:(element.find("bag")-1)]
        bags_contained[bag_color] = quantity
    bags.append(Bag(current_color, bags_contained))

print(bags)

list_bags_gold_directly = []
for bag in bags:
    if bag.contains_directly_shiny_gold():
        list_bags_gold_directly.append(bag)

print(list_bags_gold_directly)