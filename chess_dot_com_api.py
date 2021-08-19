from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives
import pprint
import requests

pretty = pprint.PrettyPrinter()

def printing_leaderboards():
    data = get_leaderboards().json
    print(data)        #prints data in original format
    print(data.json)   #prints data in json format
    print(data.json['daily'])   #parsesdate for daily
    pretty.pprint(data)        #pprint with json looks pretty asf

    categories = data.keys()


    for category in categories:
        print("Category :", category)
        for idx, entry in enumerate(data[category]):
            #print(f'Rank : {idx + 1} | Username : {entry["username"]} | Rating : {entry["score"]}')
            print(entry)

def player_rating(username):
    pata = get_player_stats(username).json
    pretty.pprint(pata)

    categories = ['chess_blitz', 'chess_rapid', 'tactics']
    for category in categories:
        print("Category :", category)
        print(f' Current : {pata[category]["last"]["rating"]}')
        print(f' Best : {pata[category]["best"]["rating"]}')


player_rating('DolanDark69')

def recent_game(username):
    data = get_player_game_archives(username).json
    url = data["archives"][-1]
    games = requests.get(url).json()
    print(games)
    game = games["games"][-1]
    pretty.pprint(game)

recent_game('DolanDark69')
