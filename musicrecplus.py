menuStr = """Enter a letter to choose an option:
e - Enter preferences
r - Get recommendations
p - Show most popular artist
h - How popular is the most popular
m - Which user has the most likes
q - Save and quit
"""

database = []

def isNewUser(user, database):
    """
    Returns True if user's name is not found in file.
    Returns False if user's name is found in file.
    """
    users = []
    for line in database:
        users.append(line.split(":")[0])
    return user not in users

def isPrivate(user):
    return user.endswith("$")

def menu():
    option = input(menuStr).lower()
    while option not in ["e","r","p","h","m","q"]:
        option = input(menuStr).lower()
    return option

def enterPreferences(user, database):
    """
    Prompts the user to enter their favorite artists and
    updates the database. 
    """
    artists = []
    artist = input("Enter an artist that you like ( Enter to finish ): ").title().strip()
    while artist:
        artists.append(artist)
        artist = input("Enter an artist that you like ( Enter to finish ): ").title().strip()
    artists.sort()
    artistsStr = ",".join(artists)
    for i in range(len(database)):
        user2 = database[i].split(":")[0]
        if user == user2:
            database[i] = user + ":" + artistsStr
            return None
    database.append(user + ":" + artistsStr)

def getRecommendations(user, database): 
    pass

def showMostPopularArtist(database):
    """
    Finds top three artists who appear most in database
    and prints each of their names.
    """
    artistCounts = {}
    for line in database:
        user, artists = line.split(":")
        if not isPrivate(user):
            for artist in artists.split(","):
                artistCounts[artist] = artistCounts.get(artist, 0) + 1
    if artistCounts:
        mostPopularArtists = []
        for i in range(3):
            for artist in artistCounts:
                if artistCounts[artist] == max(artistCounts.values()):
                    mostPopularArtists.append(artist)
                    del artistCounts[artist]
                    break
        for artist in mostPopularArtists:
            print(artist)
    else: 
        print("Sorry, no artists found.")     

def mostPopularCount(database):
    """
    Finds the artist who appears most in database and
    prints number of times it is found.
    """
    artistCounts = {}
    for line in database:
        user, artists = line.split(":")
        if not isPrivate(user):
            for artist in artists.split(","):
                artistCounts[artist] = artistCounts.get(artist, 0) + 1
    if artistCounts:
        mostPopularCount = max(artistCounts.values())
        print(mostPopularCount)
    else: 
        print("Sorry, no artists found.")

def showUserWithMostArtists(database):
    """
    Prints the names of the user(s) who like(s) the
    most artists.
    """
    userCounts = {}
    for line in database:
        user, artists = line.split(":")
        if not isPrivate(user):
            userCounts[user] = len(artists.split(","))
    if userCounts:
        maxArtists = max(userCounts.values())
        users = [user for user, count in userCounts.items() if count == maxArtists]
        for user in users:
            print(user)
    else:
        print("Sorry, no user found.")

def main(fileName, database):
    user = input("Enter your name ( put a $ symbol after your name if you wish your preferences to remain private ): ")
    
    try:
        file = open(fileName, "r")
        database = open(fileName, "r").readlines()
    except:
        file = open(fileName, "w")
    
    if isNewUser(user, database):
        enterPreferences(user, database)
    
    option = menu() 
    while option != "q": 
        if option == "e":
            enterPreferences(user, database)
        elif option == "r":
            print("Get Recommendations") 
        elif option == "p":
            showMostPopularArtist(database)
        elif option == "h":
            mostPopularCount(database)
        elif option == "m":
            showUserWithMostArtists(database)
        option = menu()
    with open(fileName, "w") as file:
        for line in database:
            file.write(line)
            
main("musicrecplus.txt", database)
