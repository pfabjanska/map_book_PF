

users:list=[
    {'name': 'Patrycja','location':'Kutno','posts':100},
    {'name': 'Dobrawa','location':'Warszawa','posts':200},
    {'name': 'Maja','location':'Inowrocław','posts':300},
    {'name': 'Mateusz','location':'Żeronice','posts':400},
]


def get_user_info(users_data:list)->None:
    for user in users_data:
        print(f'Twoj znajomy {user["name"]} z miejscowosci {user["location"]} opublikowal {user["posts"]} postow.')

get_user_info(users)


