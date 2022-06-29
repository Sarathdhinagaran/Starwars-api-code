import json
import requests
import json
url = "https://swapi.dev/api/films"
def getApi(url):
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


def problem1():
    url = "https://swapi.dev/api/films"
    json_data=getApi(url)
    films=json_data['results']
    print("\n Problem 1: The following ships appeared in Return of the Jedi - ")
    for film in films:
        if film['title']=="Return of the Jedi":
            for url in film['starships']:
                response=getApi(url)
                print(response['name'])

## problem 2 

ships=[]

def getShipData(url):
    json_data=getApi(url)
    global ships
    ships=json_data['results']
    while json_data['next'] is not None:
        json_data=getApi(json_data['next'])
        ships.extend(json_data['results'])
    return ships

def problem2():
    url = "https://swapi.dev/api/starships/"
    ships=getShipData(url)
    print("\n Problem 2: The following ships have hyperrating >= 1.0 ")
    for ship in ships:
        if ship['hyperdrive_rating'] != "unknown" and float(ship['hyperdrive_rating']) >= 1.0:
            print(ship['name'])

def problem3():
    url = "https://swapi.dev/api/starships/"
    global ships
    print("\n Problem 3: The following ships have crews between 3 and 100")
    for ship in ships:
        if (("-" not in str(ship['crew']) and ship['crew'] != "unknown" )) and (int(ship['crew'].replace(",", "")) > 3 and int(ship['crew'].replace(",", "")) < 100):
            print(ship['name'])

if __name__ == "__main__":
    problem1()
    problem2()
    problem3()
