food = ["Apples", "Pears", "Oranges", "Peaches"]

print(food)

food.append(input("Give me another food: "))

print(food)

foodLength = len(food)

index_to_find = (int(input("Give me a number: ")))
#Check to make sure they give a valid input
while index_to_find > foodLength:
    index_to_find = (int(input("There are only {} items in the list, give me another number: ".format(foodLength))))

index_to_find -= 1

print(food[index_to_find])

food += ["Grapes"]

print(food)

food.insert(0, "Pizza")

print(food)

food.pop()

print(food)

doublefood = food * 2
removeFood = input("Give me a food to remove: ")

#Check to make sure they give a valid input
while removeFood not in doublefood:
    removeFood = input("That food isn't in the list, give me another food: ")
while removeFood in doublefood:
    doublefood.remove(removeFood)

print(doublefood)

print(food)

#Iterate through each food item
for item in food:
    foodOpinion = ""
    # Validate that they give us yes or no answer only
    while not (foodOpinion == "yes" or foodOpinion == "no"):
        foodOpinion = input("Do you like {}? Yes or No?".format(item))
        foodOpinion = foodOpinion.lower()

    if foodOpinion == "yes":
        continue
    elif foodOpinion == "no":
        food.remove(item)

print(food)

newFood = []

#Iterate though each food item, reverse the letters and put into a new list
for item in food:
    item = item[::-1]
    newFood.append((item))

print(newFood)
food.pop()
print(food)