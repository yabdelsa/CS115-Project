"""
CS115 Group Project
Created by Zachary Wilkinson, Yahia Abdelsalam, Thomas Webster
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
^ Signed by Zachary Wilkinson, Yahia Abdelsalam, Thomas Webster
"""

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

    Created by Thomas Webster
    """
    return user not in database

def isPrivate(user):
    """
    Returns True if user chose to be private.
    Returns False otherwise.

    Created by Yahia Abdelsalam
    """
    return user.endswith("$")

def menu():
    """
    Displays menu options and prompts user to select
    one until they input valid choice and then returns
    selection.

    Created by Yahia Abdelsalam
    """
    option = input(menuStr).lower()
    while option not in ["e","r","p","h","m","q"]:
        option = input(menuStr).lower()
    return option

def enterPreferences(user, database):
    """
    Prompts the user to enter their favorite artists and
    updates the database.

    Created by Thomas Webster
    """
    artists = []
    artist = input("Enter an artist that you like (Enter to finish): \n").title().strip()
    while artist:
        artists.append(artist)
        artist = input("Enter an artist that you like (Enter to finish): \n").title().strip()
    artists.sort()
    database[user] = artists

def getRecommendations(user, database):
    """
    Finds other user with most similar preferences
    to user and prints artists in their preferences
    that user does not also have.

    Created by Zachary Wilkinson
    """
    sameCounts = {}
    artists = database[user]
    for user2 in database:
        if user2 != user and not isPrivate(user2):
            artists2 = database[user2]
            for artist in artists2:
                if artist in artists:
                    sameCounts[user2] = sameCounts.get(user2, 0) + 1
    sameCounts = {user2: count for user2, count in sameCounts.items() if len(database[user2]) != count}
    if sameCounts:
        for user2 in sameCounts:
            if sameCounts[user2] == max(sameCounts.values()):
                recs = [artist for artist in database[user2] if artist not in artists]
                recs.sort()
                for rec in recs:
                    print(rec)
    else:
        print("No recommendations available at this time.")

def showMostPopularArtists(database):
    """
    Finds top three artists who appear most in database
    and prints each of their names.

    Created by Zachary Wilkinson
    """
    artistCounts = {}
    for user in database:
        if not isPrivate(user):
            artists = database[user]
            for artist in artists:
                artistCounts[artist] = artistCounts.get(artist, 0) + 1
    if artistCounts:
        mostPopularArtists = []
        artistCounts2 = artistCounts.copy()
        for i in range(3):
            for artist in artistCounts2:
                if artistCounts2[artist] == max(artistCounts2.values()):
                    mostPopularArtists.append(artist)
                    del artistCounts2[artist]
                    break
        maxCount = max(artistCounts.values())
        tied = [artist for artist in mostPopularArtists if artistCounts[artist] == maxCount]
        if tied:
            for artist in tied:
                print(artist)
        else:
            for artist in mostPopularArtists:
                print(artist)
    else: 
        print("Sorry, no artists found.")     

def mostPopularCount(database):
    """
    Finds the artist who appears most in database and
    prints number of times it is found.

    Created by Yahia Abdelsalam
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

    Created by Zachary Wilkinson
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
            print(user)
    else:
        print("Sorry, no user found.")

def main(fileName, database):
    """
    Prompts user to input their name, creates file
    if it doesn't exist, opens menu and runs function
    according to user selection until they quit, and
    finally writes to file.

    Created by Zachary Wilkinson, Yahia Abdelsalam, Thomas Webster
    """
    user = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private): \n")
    
    try:
        file = open(fileName, "r")
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            user2, artists = line.split(":")
            database[user2] = artists.split(",")
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
        sortedDatabase = {user2: database[user2] for user2 in sorted(database)}
        for user in sortedDatabase:
            artistsStr = ",".join(database[user])
            string = user + ":" + artistsStr
            file.write(string+"\n")
            
main("musicrecplus.txt", database)
