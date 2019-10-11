############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def __repr__(self):
        return f'<MelonType code={self.code}>'

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings += pairing
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk_melon = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk_melon.add_pairing(['mint'])
    all_melon_types.append(musk_melon)

    casaba = MelonType('cas', 2003, 'orange', False, None, 'Casaba')
    casaba.add_pairing(['strawberries', 'mint'])
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', False, None, 'Crenshaw')
    crenshaw.add_pairing(['proscuitto'])
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yellow_watermelon.add_pairing(['ice cream'])
    all_melon_types.append(yellow_watermelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types: 
        print(f'{melon.name} pairs with {melon.pairings}')  

melon_types_lst = make_melon_types()
# print_pairing_info(melon_types_lst)


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = melon_dict.get(melon.code, melon)

    return melon_dict

# print(make_melon_type_lookup(melon_types_lst))



############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, harvested_field, harvester):
        '''defining a melon'''
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_field = harvested_field
        self.harvester = harvester

    def is_sellable(self):
        '''Categorizing melons as sellable or not sellable'''

        if (self.shape_rating > 5) and (self.color_rating > 5) and (self.harvested_field != 3):
            return True
        else:
            return False


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_code = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_code['yw'], 8,7,2,'Sheila')
    melon_2 = Melon(melons_by_code['yw'], 3,4,2, 'Sheila')
    melon_3 = Melon(melons_by_code['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_code['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_code['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_code['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_code['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_code['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_code['yw'], 7, 10, 3, 'Sheila')
    
    list_of_melons = [melon_1, melon_2, melon_3, melon_4, melon_5, 
    melon_6, melon_7, melon_8, melon_9
    ] 

    return list_of_melons

melons = make_melons(melon_types_lst)

# print(melons[0].melon_type is melons[1].melon_type)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            print(f'Harvested by {melon.harvester} from Field {melon.harvested_field} (CAN BE SOLD)')
        else:
            print(f'Harvested by {melon.harvester} from Field {melon.harvested_field} (NOT SELLABLE)')

get_sellability_report(melons)






