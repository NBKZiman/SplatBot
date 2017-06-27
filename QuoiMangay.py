
LIEUX = [
    {
        'nom': 'KFC',
        'type': ['fastfood', ' ']
    },
    {
        'nom': 'Urban Burger',
        'type': ['fastfood', 'burger', 'commande', ' ']
    },
    {
        'nom': 'Mange chez toi',
        'type': ['fastfood', 'burger', 'commande', 'gluten-free', 'commande', 'cher', ' ']
    },
    {
        'nom': 'Café des délices',
        'type': ['fastfood', 'commande', 'burger',' ']
    },
    {
        'nom': 'Italia Pizza',
        'type': ['fastfood', 'pizza', 'commande', ' ']
    },
    {
        'nom': 'Mac Donalds',
        'type': ['fastfood', 'burger', 'cher', ' ']
    },
    {
        'nom': 'Salad & Co',
        'type': ['cher', ' ']
    },
    {
        'nom': 'Memphis',
        'type': ['fastfood', 'cher', 'burger', ' ']
    },
    {
        'nom': 'Asian',
        'type': ['cher', ' ']
    },
    {
        'nom': 'BK',
        'type': ['burger', 'fastfood', 'cher', '  ']
    },
]

def add_type(name: str):
    self.type.append(str)

def is_type(name: 'str',types: list) -> bool:
    for i in types:
        if i == name :
            return True

def choix_Mangay(type: str) -> list:
    list_choix = []
    for i in LIEUX:
        if is_type(type, i['type']):
            list_choix.append(i['nom'] + '\n')
    return list_choix
