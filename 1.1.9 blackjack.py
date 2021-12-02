#blackjack
#this will be the death of me

#sorry if it's messy, it's tech week for the musical and if 
#this is anything like real blackjack, the messiness may be more realistic

#some of the code works on the screen, some works in the terminal, so keep an eye on both if possible

#importing turtles (turtle and random)
import turtle as trtl
import random as rand

#game configuration
#where variables will be created and stored
scorePlayer = 0
cardNumPlayer = 0
cardOutline = "black" #color of the outline
cardOpen = "white" #color of the open card face
cardBack = "firebrick" #color of the back card face
tableColor = "dark green" #color of the background, supposed to be the table
buttonColor = "yellow" #color of the stand button
fontSetup = ("Arial", 30, "normal") #font for labels of buttons
fontSetupCard = ("Arial", 50, "normal") #font for letters on cards
deckX = 100 
deckY = -200 #for school
deckY2 = -100 #for home
deckI = 0 #calculates amount of cards
deckII = 0 #calculates amount of sides
playerCardI = 0 #the amount of repetitions for making the sides of the card
playerCardX = -300 #the first location for the cards to spawn at
playerCardY = 200
playerValueX = -253 #x coord for the number/letter on the card
playerValueY = 85 #y coord for the number/letter on the card
currentValue = 0 #current value for each new card
currentCharacter = 0 #current character for each new card
totalValue = 0 #sum of all values added up
gameEnded = False
endStatement = ""
values = [2,3,4,5,6,7,8,9,10,11,12,13,14] #11 turns into ace, 12 turns into jack, 13 turns into queen, 14 turns into king

#initialize turtles
#where turtles will be made
player = trtl.Turtle() #creates player cards
player.pu()
player.hideturtle()
player.speed(0)
player.pensize(3)
player.color(cardOutline)
player.fillcolor(cardOpen)

deck = trtl.Turtle() #creates pile of cards for the deck
deck.pu()
deck.speed(0)
deck.pensize(3)
deck.color(cardOutline)
deck.fillcolor(cardBack)

stand = trtl.Turtle() #creates stand button
stand.pu()
stand.speed(0)
stand.pensize(5)
stand.color(cardOutline)
stand.fillcolor(buttonColor)
stand.shape("circle")
stand.shapesize(10) #makes the button graphic
#stand.goto(-350,-285) #for school
stand.goto(-150,-185) #for home
stand.stamp() #makes a slightly smaller button base
stand.shapesize(10.1)
#stand.goto(-350,-275) #for school
stand.goto(-150,-175) #for home

writer = trtl.Turtle() #creates stand phrase on buttton
writer.pu()
writer.hideturtle()
writer.speed(0)

character = trtl.Turtle() #creates letters on cards
character.pu()
character.hideturtle()
character.speed(0)

#game functions
#where functions will be defined to be used in events
def create_deck():
    global deckI, deckII, deckX, deckY2 #sets variables from earlier
    while (deckI < 5): #creates deck of cards
        deck.pu()
        deck.goto(deckX,deckY2)
        deck.pd()
        deck.begin_fill()
        while(deckII < 2):
            deck.forward(120)
            deck.right(90)
            deck.forward(180)
            deck.right(90)
            deckII += 1
        deck.end_fill()
        deckII = 0
        deckY2 += 5
        deckI += 1
    deck.pu()
    #deck.goto(360,-280) #for school
    deck.goto(160, -180) #for home
    deck.shape("square")
    deck.color("firebrick")
    deck.shapesize(5.8)

def create_labels():
    #writer.goto(-413,-180) #for school
    writer.goto(-213, -80) #for home
    writer.pd()
    print(writer.write("STAND",font=fontSetup))
    writer.pu()
    #writer.goto(330,-230) #for school
    writer.goto(130,-80) #for home
    writer.pd()
    print(writer.write("HIT",font=fontSetup))

def set_value():
    global values, playerCardX, playerCardY, currentValue, currentCharacter, totalValue
    currentValue = rand.randint(2,14)
    if (currentValue > 10):
        if (currentValue == 11): #turns into an ace
            currentValue = 11
            currentCharacter = "a"
        if (currentValue == 12): #turns into an ace
            currentValue = 10
            currentCharacter = "j"
        if (currentValue == 13): #turns into an ace
            currentValue = 10
            currentCharacter = "q"                    
        if (currentValue == 14): #turns into an ace
            currentValue = 10
            currentCharacter = "k"
    else:
        currentCharacter = currentValue
    totalValue += currentValue

def player_hit(x,y): #calls two other functions to make a new card
    player_card()
    player_number()

def player_stand(x,y):
    global gameEnded, totalValue, endStatement
    gameEnded = True
    if (totalValue == 21):
        endStatement = "Congratulations, you got blackjack!"
    elif (totalValue < 21):
        endStatement = "You stood with {}!".format(totalValue)
    else:
        endStatement = "You went bust with {}!".format(totalValue)

def player_card(): #makes a card on the player side
    global playerCardX, playerCardY, playerCardI
    player.pu()
    player.goto(playerCardX, playerCardY)
    player.pd()
    player.begin_fill()
    while (playerCardI != 2):
        player.forward(120)
        player.right(90)
        player.forward(180)
        player.right(90)
        playerCardI += 1
    player.end_fill()
    playerCardX += 150
    playerCardI = 0

def player_number(): #makes a number on a card on the player side
    global playerValueX, playerValueY, currentCharacter, fontSetupCard
    set_value() #runs the function that creates the number value
    character.goto(playerValueX,playerValueY)
    if (currentCharacter == 10):
        character.goto(playerValueX - 20,playerValueY)
        character.pd()
        print(character.write(currentCharacter,font=fontSetupCard))
    else:
        character.pd()
        print(character.write(currentCharacter,font=fontSetupCard))
    playerValueX += 150 #sets up x value for next card
    character.pu()

#events
wn = trtl.Screen() #continues showing screen
wn.bgcolor(tableColor)

create_deck()
create_labels()
player_card()
player_number()
trtl.update()

while (gameEnded != True):
    if (scorePlayer < 21 or cardNumPlayer <= 4):
        deck.onclick(player_hit)

    if (scorePlayer < 21 or cardNumPlayer <= 4):
        stand.onclick(player_stand)

deck.reset()
character.reset()
stand.reset()
writer.reset()
player.reset()
character.hideturtle()
character.pu()
character.goto(-200,50)
print(character.write(endStatement,font=fontSetupCard))

totalValue = 0
gameEnded = False

wn.mainloop()