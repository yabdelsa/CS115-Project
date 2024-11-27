menuStr = """Enter a letter to choose an option:\n
            e - Enter preferences\n
            r - Get recommendations\n
            p - Show most popular artist\n
            h - How popular is the most likes\n
            m - Which user has the most likes\n
            q - Save and quit\n"""

database = []

def newUser(file):
    names=[]
    for line in file:
        names.append(line.split(":")[0])
    return newUser not in names

def menu():
    option = input(menuStr).lower()
    while option not in ["erphmq"]:
        option = input(menuStr).lower()

def enterPreferences(name):
    artist = input("Enter an artist that you like ( Enter to finish ): ")
    while artist:
        if newUser(name):
            
try:
    with open("musicrecplus.txt", "r") as file:
        if newUser(file):
            name = input("""Enter your name ( put a $ symbol
                            after your name if you wish your preferences 
                            to remain private ): """)
            private = (name[-1]=="$")
            enterPreferences(name)
        menu()
except:
    with open("musicrecplus.txt", "w") as file:
        menu()
