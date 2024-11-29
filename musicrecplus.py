menuStr = """Enter a letter to choose an option:\n
e - Enter preferences\n
r - Get recommendations\n
p - Show most popular artist\n
h - How popular is the most popular\n
m - Which user has the most likes\n
q - Save and quit\n
"""

database = []

def newUser(name, file):
    """
    Returns True if user's name is not found in file
    Returns False if user's name is found in file
    """
    names=[]
    for line in file:
        names.append(line.split(":")[0])
    return name not in names

def menu():
    option = input(menuStr).lower()
    while option not in ["e", "r", "p", "h", "m", "q"]:
        option = input(menuStr).lower()
    return option

def enterPreferences(name, file):
    """
    Prompts the user to enter their favorite artists and updates the database. 
    """
    artists = ""
    artist = input("Enter an artist that you like ( Enter to finish ): ").title()
    while artist:
        artists += artist + ","
        artist = input("Enter an artist that you like ( Enter to finish ): ").title()
    artists = artists[:-1]
    artists = artists.rstrip(',')
    artists_list = artists.split(',')
    artists_list.sort()
    artists_s = ', '.join(artists_list)
    if newUser(name, open(file, "r")):
        open(file, "w").write(name+":"+artists_s)
        

def getRecommendations(name, file): 


def showMostPopularArtist(file):
    artist_counts = {} 
    lines = open(file, "r").readlines()
    for line in lines:
        user, artists = lines.split(":")
        
        if not user.endswith("$"):
            for artist in artists.strip().split(','):
                artist_counts[artist] = artst_counts.get(artist, 0) + 1
    if artist_counts:
        most_popular_count = max(artist_counts.values()) 
        most_popular_count = [artist for artist, count in artist_counts.items() if count == most_popular_count] 
        print("Most Popular Artist(s): " + ', '.join(most_popular_count))
    else: 
        print("Sorry. no artists found") 
        

def showUserWithMostLikes(file):
    """
    Shows how popular the most like artist is by counting the number of users who like it
    """
    artist_counts = {}
    lines = open(file, "r").readlines()
    for line in lines:
        user, artists = line.split(":")
        if not user.endwith("$"):
            for artist in artists.strip().split(','):
                artist_counts[artist] = artist_counts.get(artist, 0) + 1
    if artist_counts: 
        most_liked_count = max(artist_counts.values())
        print(most_liked_count) 
    else: 
        print("Sorry, no artists found")


def main(file):
    name = input("Enter your name ( put a $ symbol after your name if you wish your preferences to remain private ): ")
    private = (name[-1]=="$")
    txt = open("musicrecplus.txt", "w") # create file if doesn't exist
    if newUser(name, open(file, "r")):
        print("Welcome, new user!")
        enterPreferences(name, file)
        
    option = menu() 
    while option != 'q': 
        if option == 'e':
            enterPreferences(name, file)
        elif option == 'r':
            print("Get Recommendations") 
        elif option == 'p':
            print("Show Most Popular Artist")
        elif option == 'h':
            print("How Popular is the Most Popular")
        elif option == 'm':
            print("Which User Has the Most Likes")
        option = menu()
    print("Save and Quit")
            
main("musicrecplus.txt")
