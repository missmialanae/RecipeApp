#import recipe class
from recipe import Recipe

#Things for tomorrow's A'Mia
#you already started working on the random recipe method
#look into how global variables in python works
#see if you would benefit from making the food list a global variable
#make a method that will keep adding the recipes to a list that will make it easier to pick at random
#finish random method
#see how to store longer and more information about objects

def randomRecipe():
    #this method will allow the user to generate a random recipe from the file of known recipe
    #we can probably do this by taking the file putting the file into a list
    food = []
    return 0

def saveFile(recipeName):
    #purpose: to save the new recipe to a file to keep track of known recipe that the user knows
    recipeList = open("recipes.txt", "a")
    recipeList.write(f"{recipeName.name} \n")
    recipeList.close()
    return 0

def keep():
    #what if we create a method that takes no parameters at all it just reads the file
    print("Now showing all recipes:") 
    opened = open("recipes.txt", "r")
    readFile(opened)
    return 0

def readFile(rlist):
    #to be able to read the file without having to call it all of the time which can be annoying
    #you would want to read the file when you call Random Recipe and be able to pick from those recipes
    #or when you want to view all of the recipes that you may know 
    with open("recipes.txt", "r") as rlist:
        lines = rlist.readlines()

        for line in lines:
            print(line.rstrip())

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


def main():
   #user gets to choose between add a new recipe or random recipe

   print("0. Show All Recipes")
   print("1. Add a new recipe")
   print("2. Randomized recipe")
   #print("3. Search Recipe")

   #get user input but it can only be one or two
   choice = int(input())

   #if the user is a good person
   if choice == 0:
       keep()
   if choice == 1:
       addRecipe()
       return 0
   if choice == 2:
       print("Random Reciped")
       return 0 
   #if the user hates me
   while choice < 0:
       print("This is not a valid option. Please select 1 or 2")
       choice = int(input())
       
   while choice >= 3:
        print("This is not a valid option. Please select 1 or 2")
        choice = int(input())
        if choice == 0:
            keep()
            break
        if choice == 1:
            addRecipe()
            break
        if choice == 2:
            print("Randomized Recipe")
            #go to method
            break

   #gotta be a way to fix these lines of code to make it shorter but for now this will do

#start the program
if __name__ == "__main__":
    main()