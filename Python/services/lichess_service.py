import urllib.request, json
import pprint

def getPlayerFromLichess(userName):
    with urllib.request.urlopen(f"https://lichess.org/api/user/{userName}") as url:
        data = json.loads(url.read().decode())
        pprint.pprint(data)
        id = data["id"]
        lichessName = data["username"]
        rating = data["perfs"]["blitz"]["rating"]
        return (id, lichessName, rating)
