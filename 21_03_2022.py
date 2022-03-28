import requests

def show_characters():
    response = requests.get('http://hp-api.herokuapp.com/api/characters')
    characters = response.json()
    for character in characters:
        print(character.get('name'))

def show_actors():
    response = requests.get('http://hp-api.herokuapp.com/api/characters')
    characters = response.json()
    actors = {}
    for character in characters:
        actors[character.get('name')] = character.get('actor')
    for key, value in actors.items():
        print(key, ' : ', value)

def get_females():
    response = requests.get('http://hp-api.herokuapp.com/api/characters/staff')
    characters = response.json()
    for character in characters:
        if character.get('gender') == 'female':
            print(character.get('name'))

def find_character_by_eyes():
    response = requests.get('http://hp-api.herokuapp.com/api/characters')
    characters = response.json()
    eye_colors = []
    for character in characters:
        eye_colors.append(character.get('eyeColour'))
    print(set(eye_colors))
    color = input("Wybierz kolor z listy: ")
    for character in characters:
        while True:
            if color == character.get('eyeColour'):
                print(character.get('name'))
            break

while True:
    print('1. Pokaż wszystkie postaci')
    print('2. Pokaż kobiety wśród Hogwarts staff: ')
    print('3. Pokaż postaci i aktorów: ')
    print('4. Wybierz kolor oczu z listy aby znaleźć postaci z podaną cechą: ')
    print('0. Wyjdź z programu')
    option = input('Wybierz opcję: ')
    if option == "1":
        show_characters()
    elif option == "2":
        get_females()
    elif option == "3":
        show_actors()
    elif option == "4":
        find_character_by_eyes()
    elif option == "0":
        break