import pyautogui as pg
import webbrowser as wb
import time as t

points = 0

pg.alert("This is your Score: " + str(points) + " It is 0 now. Answer questions correct to earn points. Have Fun!")

t.sleep(1)

show = pg.prompt("What is your favorite show? ")

if show == "The Office":
    wb.open("https://youtu.be/mfokPqeSNcw")
    pg.alert("That is a really good show!")
    points += 1000
elif show == "Wicked Tuna":
    pg.alert("I love fishing! ...Videos")
    points += 250
elif show == "Parks and Rec":
    wb.open("https://youtu.be/Tch4v0L0GHA")
    pg.alert("You are a good person! ")
    points += 1000
elif show == "Friends":
    pg.alert("Ha you have none. ")
    points += 1
elif show == "Judge Judy":
    wb.open("https://youtu.be/ICZa2764LJI")
    pg.alert("You are a good person. ")
    points += 1000000
elif show == "Sunday Night Football":
    pg.alert("Better get enough sleep. ")
    points += 50

else:
    pg.alert("Your favorite show is " + show)

t.sleep(20)
    
Food = pg.prompt("What is your favorite food? ")

if Food == "Pizza":
    wb.open("https://youtu.be/MtN1YnoL46Q")
    pg.alert("What kind? ")
    t.sleep(2)
    pg.alert("I don't want to know! HaHaha! ")
    points += 100
elif Food == "Sushi":
    pg.alert("I know where you live!!! ")
    points += 110
elif Food == "Calzones":
    wb.open("https://youtu.be/JMG1Nl7uWko")
    pg.alert("No ... Just ... No ... ")
    points -= 500
elif Food == "Mac and Cheese":
    wb.open("https://youtu.be/B2COl0ui4Sc")
    pg.alert("Cheesy")
    points += 91
elif Food == "Sandwich":
    wb.open("https://youtu.be/wUDqQSwdBjM")
    pg.alert("Ok... ")
    points += 68
elif Food == "Icecream":
    pg.alert("Cool. ")
    points += 111
    
else:
    pg.alert("WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY WHY!!! " + Food)

t.sleep(20)
    
Game = pg.prompt("What is your favorite game? ")

if Game == "Fortnite":
    wb.open("https://youtu.be/lSv-JYzs36Q")
    pg.alert("Fortnite is dead idiot! ")
    points -= 1000
elif Game == "Minecraft":
    wb.open("https://youtu.be/dgha9S39Y6M")
    pg.alert("...")
elif Game == "Call of Duty Black Ops 4":
    pg.alert("Why Spencer, why... ")
    points += 1000
elif Game == "Mario":
    wb.open("https://youtu.be/SlKGvfHErFc")
    pg.alert("Power Mushroom! ")
    points +=10
elif Game == "Street Fighter":
    pg.alert("Throw those punches! ")
    points += 10
elif Game == "agar.io":
    wb.open("https://www.google.com/search?q=agario&rlz=1C1GCEA_enUS751US751&oq=ag&aqs=chrome.1.69i57j0l5.1780j0j7&sourceid=chrome&ie=UTF-8")
    points += 10001

else:
    pg.alert("Flappy bird is better than " + Game)
    
t.sleep(20)

Costume = pg.prompt("What were you for Halloween? ")

if Costume == "Dwight":
    wb.open("https://youtu.be/GU2W_nlijx0")
    pg.alert("You gotta be kidding me! ")
    points += 11
elif Costume == "Nothing":
    wb.open("https://youtu.be/KMihKmoYfe8")
    pg.alert("you are smart! ")
    points += 1000
elif Costume == "A TV show":
    pg.alert("Nice! ")
    points += 100
elif Costume == "Eeyore":
    wb.open("https://youtu.be/CQI0E1WCLMU")
    pg.alert("O...K... ")
    points += 100
    
elif Costume == "The Grim Reaper":
    pg.alert("... ")
    points += 1
elif Costume == "Michal Scott":
    pg.alert("Fire in the Office! ")
    points += 1000

else:
    pg.alert("You are being " + Costume + " wow! ")

t.sleep(20)

Star = pg.prompt("Who is your favorite Star Wars character? ")

if Star == "Yoda":
    wb.open("https://youtu.be/U9t-slLl30E")
    pg.alert("May the force be with you. ") 
    points += 10000000
elif Star == "Darth Vader":
    wb.open("https://youtu.be/wxL8bVJhXCM")
    pg.alert("You are strong on the dark side. ")
    points += 124
elif Star == "Luke Skywalker":
    wb.open("https://youtu.be/U1MnMA0TzGI")
    pg.alert("Do you know who your father is? ")
    points += 53
elif Star == "Princess Lea":
    pg.alert("Who is your brother??? ")
    points += 17
elif Star == "Han Solo":
    pg.alert("Are you Solo? ")
    points += 23
elif Star == "Chewbacca":
    wb.open("https://youtu.be/gGPi-JqG7-A")
    pg.alert("Argaaa!!! ")
    points += 91
else:
    pg.alert("Your favorite character is " + Star + ". ")

t.sleep(10)

pg.alert("Your Score: " + str(points))
