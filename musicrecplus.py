menuStr = """Enter a letter to choose an option:
e - Enter preferences
r - Get recommendations
p - Show most popular artists
h - How popular is the most popular
m - Which user has the most likes
q - Save and quit
"""

database = {}

def isNewUser(user, database):
    """
    Returns True if user's name is not found in file.
    Returns False if user's name is found in file.
    """
    return user not in database

def isPrivate(user):
    """
    Returns True if user chose to be private.
    Returns False otherwise.
    """
    return user.endswith("$")

def menu():
    """
    Displays menu options and prompts user to select
    one until they input valid choice and then returns
    selection.
    """
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
    database[user] = artists

def getRecommendations(user, database): 
    sameCounts = {}
    artists = database[user]
    for user2 in database:
        if user2 != user and not isPrivate(user2)
            artists2 = database[user2]
            for artist in artists2:
                if artist in artists:
                    sameCounts[user2] = sameCounts.get(user2, 0) + 1
    for user2 in sameCounts:
        artists2 = database[user2]
        
    if sameCounts:
        
    else:
        print("No recommendations available at this time.")

def showMostPopularArtists(database):
    """
    Finds top three artists who appear most in database
    and prints each of their names.
    """
    artistCounts = {}
    for user in database:
        if not isPrivate(user):
            artists = database[user]
            for artist in artists:
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
            print(artist.strip())
    else: 
        print("Sorry, no artists found.")     

def mostPopularCount(database):
    """
    Finds the artist who appears most in database and
    prints number of times it is found.
    """
    artistCounts = {}
    for user in database:
        if not isPrivate(user):
            artists = database[user]
            for artist in artists:
                artistCounts[artist] = artistCounts.get(artist, 0) + 1
    if artistCounts:
        mostPopularCount = max(artistCounts.values())
        print(mostPopularCount)
    else: 
        print("Sorry, no artists found.")

def showUsersWithMostArtists(database):
    """
    Prints the names of the user(s) who like(s) the
    most artists.
    """
    userCounts = {}
    for user in database:
        if not isPrivate(user):
            artists = database[user]
            userCounts[user] = len(artists)
    if userCounts:
        maxArtists = max(userCounts.values())
        users = [user for user, count in userCounts.items() if count == maxArtists]
        users.sort()
        for user in users:
            print(user.strip())
    else:
        print("Sorry, no user found.")

def main(fileName, database):
    """
    Prompts user to input their name, creates file
    if it doesn't exist, opens menu and runs function
    according to user selection until they quit, and
    finally writes to file.
    """
    user = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): ")
    
    try:
        file = open(fileName, "r")
        lines = file.readlines()
        for line in lines:
            user2, artists = line.split(":")
            database[user2] = artists
    except FileNotFoundError:
        file = open(fileName, "w")
    
    if isNewUser(user, database):
        enterPreferences(user, database)
    
    option = menu() 
    while option != "q": 
        if option == "e":
            enterPreferences(user, database)
        elif option == "r":
            getRecommendations(user, database)
        elif option == "p":
            showMostPopularArtists(database)
        elif option == "h":
            mostPopularCount(database)
        elif option == "m":
            showUsersWithMostArtists(database)
        option = menu()
    with open(fileName, "w") as file:
        for user in database:
            artistsStr = ",".join(database[user])
            string = user + ":" + artistsStr
            file.write(string)
            
main("musicrecplus.txt", database)
