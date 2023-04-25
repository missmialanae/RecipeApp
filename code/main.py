#import recipe class
from recipe import Recipe
import random

#Things for tomorrow's A'Mia
#issue: need to work on random recipe function
#issue:sometimes when running random recipe to many times you get a blank answer
#need to make a replay kind of button so the user can add more recipes if they need to, or pick a new random recipe
#creat random list prints really ugly
#need to simplify the code in some places
#issue: need to work on main menu code so badly its is ass
#see how to store longer and more information about objects

def secondChoice():
    #let the user be able to choose between one random recipe or print out a weekly list 
    print("Do you want a meal plan or a random meal?")
    print("1. Meal Prep")
    print("2. Random Meal")
    choice2 = int(input())

    #good person
    if choice2 == 1:
        print("Meal Prepping now...")
        createRandomList()
        return 0
    if choice2 == 2:
        print("Random Meal")
        randomRecipe()
        return 0
    
    #if user is bad
    while choice2 == 0:
        print("Not Valid. Please Try Again")
        choice2 = int(input())
    while choice2 >= 3:
        print("Not Valid. Please Try Again")
        choice2 = int(input())
        if choice2 == 1:
            print("Meal Prepping now...")
            createRandomList()
            break
        if choice2 == 2:
            print("Random Meal")
            randomRecipe()
            break
    #gotta be a better wayt to write this code but loops don't like me for some reason :(
    return 0

    return 0
def createRandomList():
    #create a random list of meals from the list of recipes that we know
    #ask the user how many days they want a meal for
    print("How many days would you like to prep for?")
    days = int(input())
    #use those days to populate the number of items in that list 
    #create an empty list to store those but that can only fit 7 days (for now, hehehe)
    mealprep = []
    #call convertList to convert the file into a list and bring it into the method
    currentList = convertList()
    #shuffle the list 
    random.shuffle(currentList)
    #this is list comprehension i need to learn more about this 
    currentList= [x for x in currentList if x != " "]
    mealprep = currentList
    counter = 0
    #i suck at coding btw
    while counter < days:
        print(mealprep[counter])
        counter +=1
        #it prints kind of ugly but its okay we will try to fix that later
    quitGame()
    return 0
def isItAList(listy):
    #just checking to make sure that the list is actually a list and i am not stupid
    currentList = listy
    if isinstance(currentList, list):
        print("this is a list")
    else:
        print("no dumbass")
def convertList():
    filez = open("recipes.txt", "r")
    randomList= filez.readlines()
    
    for line in randomList:
        newList = line.split(";")
    return newList
def randomRecipe():
    newList = convertList()
    #isItAList(newList)
    #the list is now here but we need to remove the random empty set that may appear
    #random.shuffle will shuffle the  entirelist
    random.shuffle(newList)
    newList = [x for x in newList if x != " "]
    #now instead of the entire list we need to bring the first item back
    print(newList[0])
    #this works fine might want to rewrite it with a loop instead
    print("Do you want to select a new recipe? 1 for Yes, 2 for No")
    chose = int(input())
    if chose == 2:
        quitGame()
    #is it better to reshuffle the list or go tot he next one?
    while chose == 1:
        random.shuffle(newList)
        newList = [x for x in newList if x != " "]
        print(newList[0])
        print("Do you want to select a new recipe? 1 for Yes, 2 for No")
        chose = int(input())
        if chose == 2:
            quitGame()
    return 0
def saveFile(recipeName):
    #purpose: to save the new recipe to a file to keep track of known recipe that the user knows
    recipeList = open("recipes.txt", "a")
    #DO NOT FUCKING CHANGE THIS LINE IT PRINTS HOW YOU LIKE IT
    recipeList.write(f"{recipeName.name}; ")
    recipeList.close()
    #this should be the end of adding a recipe therefore i should be able to run quitGame
    quitGame()
    return 0
def showAll():
    #what if we create a method that takes no parameters at all it just reads the file
    str = ""
    opened = open("recipes.txt", "r")
    with open("recipes.txt", "r") as rlist:
        #read should keep the file as an file
        lines = rlist.read().split(";")
        #isItAList(rlist) this is not a list
        #isItAList(lines) #this is a list because of readlines
        for line in lines:
            words = line.split(";")
            print(words)
    #gonna leave it like this for now. it may help with the building of the recipe functions later
    #gonna run quitGame method so the user can decide if they want to do something else or quit
    quitGame()
    return 0
def readFile():
    #to be able to read the file without having to call it all of the time which can be annoying
    #you would want to read the file when you call Random Recipe and be able to pick from those recipes
    #or when you want to view all of the recipes that you may know 

    with open("recipes.txt", "r") as rlist:
        lines = rlist.readlines()
    
    #note right here it is not a list
    #isItAList(rlist)
    return 0
def saveRecipe(recipe):
    #purpose: this currently saves the recipe to a list that sends it

    #store the recipe in a list or dictionary
    foods = [] #does this need to be a global variable?
    foods.append(recipe)

    print("Going to add to File")
    saveFile(recipe)

    return 0
def addRecipe():
    #purpose:when the user selects add a recipe this allows them to add a recipe to the list of recipes that the user knows. 
    #Once the user gives us a recipe we want to be able to store it in a file to keep all of the other recipes that we know.

    #user gives a new recipe that they know
    #note: this should allow numbers and special characters and such just in case 
    print("What is the name of the recipe that you want to add?")
    recipe1 = Recipe(input())

    #later we will give it more function like adding the ingredients and adding the instructions
    #making sure to pass it to the next method which will be save recipe

    saveRecipe(recipe1)
    return 0
def quitGame():
    print("press any key to go back to menu or q to quit")
    menuinput = input()
    #need to make a list of valid characters that will cause the program to quit
    quitChars = ('q', 'Q')
    if menuinput not in quitChars:
        main()
    else:
        quit()
    return 0
def main():
   #user gets to choose between add a new recipe or random recipe

   print("0. Show All Recipes")
   print("1. Add a new recipe")
   print("2. Randomized recipe")
   #print("3. Search Recipe")
   print("4.Quit")

   #get user input but it can only be one or two
   choice = int(input())

   #if the user is a good person
   if choice == 0:
       showAll()
   if choice == 1:
       addRecipe()
       return 0
   if choice == 2:
       print("Random Reciped")
       secondChoice()
       return 0 
   if choice == 4:
       quit()

   #if the user hates me
   while choice < 0:
       print("This is not a valid option. Please select 1 or 2")
       choice = int(input())
       
   while choice >= 3:
        print("This is not a valid option. Please select 1 or 2")
        choice = int(input())
        if choice == 0:
            showAll()
            break
        if choice == 1:
            addRecipe()
            break
        if choice == 2:
            print("Randomized Recipe")
            secondChoice()
            break
       
   #gotta be a way to fix these lines of code to make it shorter but for now this will do
#start the program
if __name__ == "__main__":
    main()