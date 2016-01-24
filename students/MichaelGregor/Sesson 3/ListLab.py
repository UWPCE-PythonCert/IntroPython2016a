food = ["Apples", "Pears", "Oranges", "Peaches"]

print(food)

food.append(input("Give me another food: "))

print(food)

foodLength = len(food)

index_to_find = (int(input("Give me a number: ")))
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
while removeFood not in doublefood:
    removeFood = input("That food isn't in the list, give me another food: ")
while removeFood in doublefood:
    doublefood.remove(removeFood)

print(doublefood)

print(food)

for item in food:
    foodOpinion = input("Do you like {}? ".format(item))
    foodOpinion = foodOpinion.lower()
    if foodOpinion == "yes":
        continue
    elif foodOpinion == "no":
        food.remove(item)
    else

print(food)

