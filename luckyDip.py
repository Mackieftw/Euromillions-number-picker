import random #imports random library

lottoPick = random.sample(range(1,60), 6) #generates six random numbers between 1-59 for lotto

lottoPick.sort() #puts the generated numbers in order

print( "Lotto Lucky Dip is - ", lottoPick) # prints the numbers to the console

euroMain = random.sample(range(1,51), 5) #generates 5 main numbers

euroLuckyStar = random.sample(range(1,13), 2) # generates two lucky star numbers

euroLuckyStar.sort()
euroMain.sort()

print( "Euromillions lucky Dip is - ", euroMain, "Stars - ", euroLuckyStar)  #prints both main numbers and lucky stars 
