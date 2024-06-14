# Recommendation Program
# Joshua Younger


# game object**********************************************************


class Game:
    def __init__(self, name, platform, genre, company, rating):
        self.name = name 
        self.platform = platform
        self.genre = genre
        self.company = company
        self.rating = rating

# Variables************************************************************
game_1 = Game("Sly Cooper", "Playstation", "Platformer", "Sucker Punch", "8")
game_2 = Game("Final Fantasy 7", "Playstation", "JRPG", "Square Enix", "9")
game_3 = Game("Nier Automata", "Playstation", "Action RPG", "Square Enix", "10")
game_4 = Game("Halo", "Xbox", "Shooter", "Microsoft", "9")
game_5 = Game("Mario Kart 8 Deluxe", "Nintendo", "Racing", "Nintendo", "9")
game_6 = Game("Forza 5", "Xbox", "Racing", "Microsoft", "7")
game_7 = Game("The Legend of Zelda: Breath of the Wild", "Nintendo", "Adventure", "Nintendo", "10")
game_8 = Game("Star Fox: Assault", "Nintendo", "Shooter", "Nintendo", "7")
game_9 = Game("Star Wars: Rouge Squadron 2", "Nintendo", "Shooter", "Lucas Arts", "9")
game_10 = Game("Mobile Suit Gundam: Gundam vs Zeta Gundam", "Playstation", "Action", "Bandai", "10")

game_list = []
game_list.append(game_1)
game_list.append(game_2)
game_list.append(game_3)
game_list.append(game_4)
game_list.append(game_5)
game_list.append(game_6)
game_list.append(game_7)
game_list.append(game_8)
game_list.append(game_9)
game_list.append(game_10)

# greet****************************************************************
def greet():
    return "Welcome to the video game library."
# recommend based on variables*****************************************
def search():
    return(input("How would you like to search: Type 'K' for Keyword, Type 'P' for Platform, 'G' for Genre, 'C' for Company, 'R' for Rating"))

def show_library():
    titles = []
    for i in game_list:
        titles.append(i.name)
    print(titles)
    
def recommend():
    recommend_list = []
    question = search()
    if question == "P":
        platform = input("Which platform would you like to search by?")
        for i in game_list:
            if i.platform == platform:
                recommend_list.append(i.name)
        if len(recommend_list) == 0:
            print("I am sorry, we do not have this platform.")
        else:
            print("Results: " + str(recommend_list))
    elif question == "G":
        genre = input("What genre are you looking for?")
        for i in game_list:
            if i.genre == genre:
                recommend_list.append(i.name)
        if len(recommend_list) == 0:
            print("Sorry, we can not find that genre.")
        else:
            print("Results: " + str(recommend_list))
    elif question == "C":
        company = input("Which developer are you looking for?")
        for i in game_list:
            if i.company == company:
                recommend_list.append(i.name)
        if len(recommend_list) == 0:
            print("Sorry, we have no titles from this developer")
        else:
            print("Results: " + str(recommend_list))
    elif question == "K":
        name = input("Type in your keyword.")
        for i in game_list:
            if i.name[:4] == name[:4]:
                recommend_list.append(i.name)
        if len(recommend_list) == 0:
            print("Sorry, we have no matches. make sure the spelling is right")
        else:
            print("Results: " + str(recommend_list))
    elif question == "R":
        rating_counter = 10
        while rating_counter != 0:
            for i in game_list:
                if i.rating == str(rating_counter):
                    recommend_list.append(i.name)
            rating_counter -= 1
        print("Games at the front are the highest rated: " + str(recommend_list))
    else:
        print("Sorry, that is not an option.")
    end = input("Would you like to search again?")
    if end == "Yes":
        recommend_list.clear
        recommend()
    elif end == "No":
        print("Thank you for using my program.")
# call functions*******************************************************
greet()
show_library()
#search()
recommend()