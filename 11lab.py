import math
# returning the log of 2,3
print ("The value of log 2 with base 3 is : ", end="")
print (math.log(2,3))
# returning the log2 of 16
print ("The value of log2 of 16 is : ", end="")
print (math.log2(16))  
# returning the log10 of 10000
print ("The value of log10 of 10000 is : ", end="")
print (math.log10(10000))



import math 
# print the square root of 0
print(math.sqrt(0))
# print the square root of 4
print(math.sqrt(4))
# print the square root of 3.5
print(math.sqrt(3.5))


import math
a = math.pi/6
# returning the value of sine of pi/6
print ("The value of sine of pi/6 is : ", end="")
print (math.sin(a))
# returning the value of cosine of pi/6
print ("The value of cosine of pi/6 is : ", end="")
print (math.cos(a))
# returning the value of tangent of pi/6
print ("The value of tangent of pi/6 is : ", end="")
print (math.tan(a))


import math
a = math.pi/6
b = 30
# returning the converted value from radians to degrees
print ("The converted value from radians to degrees is : ", end="")
print (math.degrees(a))
# returning the converted value from degrees to radians
print ("The converted value from degrees to radians is : ", end="")
print (math.radians(b))


import math
# initializing argument
gamma_var = 6
# Printing the gamma value.
print ("The gamma value of the given argument is : "
                    + str(math.gamma(gamma_var)))



import random
PlayerOne = "Анна"
PlayerTwo = "Алекс"
 
AnnaScore = 0
AlexScore = 0

# У каждого кубика шесть возможных значений
diceOne = [1, 2, 3, 4, 5, 6]
diceTwo = [1, 2, 3, 4, 5, 6]

def playDiceGame():
    """Оба участника, Анна и Алекс, бросают кубик, используя метод shuffle"""
 
    for i in range(5):
        #оба кубика встряхиваются 5 раз
        random.shuffle(diceOne)
        random.shuffle(diceTwo)
    firstNumber = random.choice(diceOne) # использование метода choice для выбора случайного значения
    SecondNumber = random.choice(diceTwo)
    return firstNumber + SecondNumber
 
print("Игра в кости использует модуль random\n")
 
#Давайте сыграем в кости три раза
for i in range(3):
    # определим, кто будет бросать кости первым
    AlexTossNumber = random.randint(1, 100) # генерация случайного числа от 1 до 100, включая 100
    AnnaTossNumber = random.randrange(1, 101, 1) # генерация случайного числа от 1 до 100, не включая 101
 
    if( AlexTossNumber > AnnaTossNumber):
        print("Алекс выиграл жеребьевку.")
        AlexScore = playDiceGame()
        AnnaScore = playDiceGame()
    else:
        print("Анна выиграла жеребьевку.")
        AnnaScore = playDiceGame()
        AlexScore = playDiceGame()
 
    if(AlexScore > AnnaScore):
        print ("Алекс выиграл игру в кости. Финальный счет Алекса:", AlexScore, "Финальный счет Анны:", AnnaScore, "\n")
    else:
        print("Анна выиграла игру в кости. Финальный счет Анны:", AnnaScore, "Финальный счет Алекса:", AlexScore, "\n")

'''Игра в кости использует модуль random
 
Анна выиграла жеребьевку.
Анна выиграла игру в кости. Финальный счет Анны: 5 Финальный счет Алекса: 2 
 
Анна выиграла жеребьевку.
Анна выиграла игру в кости. Финальный счет Анны: 10 Финальный счет Алекса: 2 
 
Алекс выиграл жеребьевку.
Анна выиграла игру в кости. Финальный счет Анны: 10 Финальный счет Алекса: 8
Вот и все. Оставить комментарии можете в секции ниже.'''


from datetime import date
f = date(2021,11,13)
s = date(2020,10,11)
delta = f - s
print(delta)


import datetime
now=datetime.datetime.now()
now 
datetime.datetime(2021, 9, 27, 13, 59, 22, 649538)
from datetime import timedelta
now+timedelta(minutes=3)
datetime.datetime(2021, 9, 27, 14, 2, 22, 649538)
now+timedelta(minutes=-3)
datetime.datetime(2021, 9, 27, 13, 56, 22, 649538)

import datetime
now = datetime.time(7, 30, 0)
next_hour = datetime.time(10, 30, 0)
print('now < next_hour:', now < next_hour)
today = datetime.date.today()
next_week = datetime.date.today() + datetime.timedelta(days=7)
print('today > next_week:', today > next_week)

#now < next_hour: True
#today > next_week: False

import pytz
import datetime
tz_praha = pytz.timezone("Europe/Prague")
dt_praha = datetime.datetime.now(tz_praha)
print(dt_praha)

from tkinter import *
root = Tk()
c = Canvas(root, width=450, height=400, bg='dim gray')
c.pack()
c.create_line(120, 60, 90, 210, width=2, fill='white')
c.create_line(120, 60, 150, 210, width=2, fill='white')
c.create_line(103, 145, 138, 145, width=2, fill='white')
c.create_line(200, 110, 225, 210, width=2, fill='white')
c.create_line(250, 110, 208, 280, width=2, fill='white')
c.create_oval(300, 110, 350, 210, width=2, outline='white')
c.create_line(350, 110, 350, 210, width=2, fill='white')
root.mainloop()