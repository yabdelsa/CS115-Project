menuStr = "Enter a letter to choose an option:\ne - Enter preferences\nr - Get recommendations\np - Show most popular artist\nh - How popular is the most likes\nm - Which user has the most likes\nq - Save and quit\n"

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
    while option not in ["erphmq"]:
        option = input(menuStr).lower()

def enterPreferences(name, file):
    artists = ""
    artist = input("Enter an artist that you like ( Enter to finish ): ")
    while artist:
        artists += artist + ","
        artist = input("Enter an artist that you like ( Enter to finish ): ")
    artists = artists[:-1]
    if newUser(name, open(file, "r")):
        open(file, "w").write(name+":"+artists)

def main(file):
    name = input("Enter your name ( put a $ symbol after your name if you wish your preferences to remain private ): ")
    private = (name[-1]=="$")
    txt = open("musicrecplus.txt", "w") # create file if doesn't exist
    if newUser(name, open(file, "r")):
        enterPreferences(name, file)
    menu() 

main("musicrecplus.txt")
