#MOST CURRENT VERSION

import tkinter as tk
import random
root = tk.Tk()

rules_x = 'Choose from letters a-j for the column(delete this text)'
rules_y = 'Choose a number from 1-10 for the row(delete this text)'
'''
def clear_entry1(entry1):
    
    if entry1.get() == rules_x:
        
        entry1.delete(0, END)

def clear_entry2(entry2):
    
    entry2.delete(0, END)
'''     
    
entry1 = tk.Entry(root,width=40)
entry1.insert(tk.END, rules_x)
entry1.focus_set()
entry1.pack()#(row=0,column=0)

entry2 = tk.Entry(root,width=40)
entry2.insert(tk.END, rules_y)
entry2.pack()#(row=100, column=0)


#entry1.bind("<Button-1>", clear_entry1)
#entry2.bind("<Button-1>", clear_entry2)

#==========================================

canvas = tk.Canvas(width = 1000,height=550)
canvas.pack(padx=50, pady=50)


shots = tk.Label(root, text = 'Shots taken')
shots.pack()
canvas.create_window(150,10, window=shots)

ships = tk.Label(root, text = 'Your Ships')
ships.pack()
canvas.create_window(800, 10, window=ships)


squares = 20
width_squares = 50

for row in range(squares):
    for column in range(squares):
        x = int(row * width_squares)
        y = int(column * width_squares)+50
        a = int(x + width_squares)
        b = int(y + width_squares)+50
        canvas.create_rectangle(x,y,a,b,fill='white', outline='black')

canvas.create_line(500,50,500,600, fill='red', width=3)

#========================================================
coordinates_col = {'a': 0,'b':50,'c':100, 'd':150, 'e':200, 'f':250, 'g':300, 'h':350, 'i':400,'j':450 }

coordinates_row = {'1': 100,'2':150,'3':200, '4':250, '5':300, '6':350, '7':400, '8':450, '9':500,'10':550 }

solv = {'a': 1,'b':2,'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9 , 'j':10}


coordinates_col2 = {'a': 500,'b':550,'c':600, 'd':650, 'e':700, 'f':750, 'g':800, 'h':850, 'i':900,'j':950 }

for value in coordinates_col:
    labels = tk.Label(root, text=value)
    canvas.create_window(int(coordinates_col[value]+25),50, window=labels)
 
for value in coordinates_row:
    labels_vert=tk.Label(root, text=value)
    canvas.create_window(0, int(coordinates_row[value])-25,window=labels_vert)

for value in coordinates_col2:
    labels_opp = tk.Label(root, text=value)
    canvas.create_window(int(coordinates_col2[value])+25,50, window=labels_opp)
       

def ur_turn():
    
    x = entry1.get()
    y = entry2.get()
    

    for value in coordinates_col.keys():

        if x == value:
        
            value = x    
    
    for value in coordinates_row.keys():
    
        if y == value:
        
            value = y
            
    for value in solv.keys():
        
        if x == value:
            v = solv[x]
            
    if x+y in coordList4:
        canvas.create_rectangle(coordinates_col[x], 50*(int(y)), int(v)*50, coordinates_row[y], fill='red')
    elif x+y in coordList31:
        canvas.create_rectangle(coordinates_col[x], 50*(int(y)), int(v)*50, coordinates_row[y], fill='red')
    elif x+y in coordList32:
        canvas.create_rectangle(coordinates_col[x], 50*(int(y)), int(v)*50, coordinates_row[y], fill='red')
    elif x+y in coordList2:
        canvas.create_rectangle(coordinates_col[x], 50*(int(y)), int(v)*50, coordinates_row[y], fill='red')
                    
    else:
        canvas.create_rectangle(coordinates_col[x], 50*(int(y)), int(v)*50, coordinates_row[y] , fill='blue')

#=================================================================



#======================================================

coordinates_ship_col = {'a': 500, 'b': 550, 'c': 600, 'd': 650, 'e':700, 'f':750, 'g':800, 'h':850, 'i':900, 'j':950 }
coordinates_ship_row = {'1': 50,'2':100,'3':150, '4':200, '5':250, '6':300, '7':350, '8':400, '9':450,'10':500 }
urshipcoords = []


clickcount = 17
shipcount = 5
f = 17
fs = 0
ss = 0

def click(event):
    x = event.x
    y = event.y
    z = 0
    global clickcount
    global shipcount
    global f
    global fs
    global ss
    
    
    if clickcount < f:
        a0,b0, a1,b1 = canvas.coords(fs)
    if clickcount < f-1:
        c0,d0, c1,d1 = canvas.coords(ss)
    if clickcount == 12:
        shipcount = 4
        f = clickcount
    elif clickcount == 8:
        shipcount = 3
        f = clickcount
    elif clickcount == 5:
        shipcount = 2
        f = clickcount
    elif clickcount == 2:
        shipcount = 1
        f = clickcount

    l=0
    o=0
  
    
    for n in coordinates_ship_col:
        l = coordinates_ship_col[n]
        if x in range(l, l+50):
            x = l
            break
    for m in coordinates_ship_row:
        o = coordinates_ship_row[m]
        if y in range(o, o+50):
            y = o
            break
    if clickcount > 0:       
        recentship = canvas.create_rectangle(l,o, l+50, o+50, fill='gray')
        x0,y0, x1,y1 = canvas.coords(recentship)
        
    if f == clickcount:
        fs = canvas.create_rectangle(x0,y0, x1,y1, fill='gray')
        urshipcoords.append(canvas.coords(recentship))
    elif clickcount == f - 1:
        if x0 == ((a0 + 50) or x0 == (a0-50)) and y0 == b0:
            ss = canvas.create_rectangle(x0,y0, x1,y1)
            urshipcoords.append(canvas.coords(recentship))
        elif y0 == ((b0 + 50) or y0 == (b0 - 50)) and x0 == a0:
            ss = canvas.create_rectangle(x0,y0, x1,y1)
            urshipcoords.append(canvas.coords(recentship))
        else:
            print("Please place a valid ship")
            canvas.create_rectangle(x0,y0, x1,y1, fill='white')
            clickcount +=1
                
    elif clickcount < f -1:
        if c0 >= (a0 + 50):
            if x0 >= (c0 + 50) and y0 == d0:
                urshipcoords.append(canvas.coords(recentship))
            else:
                print("Please place a valid ship")
                canvas.create_rectangle(x0,y0, x1,y1, fill='white')
                clickcount +=1
                    
        elif c0 <= (a0 - 50):
            if x0 <= (c0 - 50) and y0 == d0:
                urshipcoords.append(canvas.coords(recentship))
            else:
                print("Please place a valid ship")
                canvas.create_rectangle(x0,y0, x1,y1, fill='white')
                clickcount +=1
        elif d0 >= (b0 + 50):
            if y0 >= (d0 + 50) and x0 == a0:
                 urshipcoords.append(canvas.coords(recentship))
            else:
                print("Please place a valid ship")
                canvas.create_rectangle(x0,y0, x1,y1, fill='white')
                clickcount +=1
        elif d0 <= (b0 - 50):
            if y0 <= (d0 - 50) and x0 == a0:
                 urshipcoords.append(canvas.coords(recentship))
            else:
                print("Please place a valid ship")
                canvas.create_rectangle(x0,y0, x1,y1, fill='white')
                clickcount +=1        
               
    clickcount -= 1
    #print(clickcount)
canvas.bind('<Button-1>', click)

#=========================================================
coordinatesx = [500, 550, 600, 650, 700, 750, 800, 850, 900, 950]
coordinatesy = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]


coordinate1 = random.choice(coordinatesx)

coordinate2 = random.choice(coordinatesy)

shots_taken = []
            
def shoot_shot():
    
    global coordinate1
    global coordinate2
    
    global coordinatesx
    global coordinatesy
    

    coordinate1 = random.choice(coordinatesx)#choice(coordinatesx)
    #shots_taken.append(coordinate1)

    coordinate2 = random.choice(coordinatesy)#choice(coordinatesy)
    #shots_taken.append(coordinate2)
    
    shot = canvas.create_rectangle(int(coordinate1), int(coordinate2),int(coordinate1)+50,int(coordinate2)+50, fill = check_shot())
 
#def del_hit():
    
    
def check_shot():
    
    global coordinate1
    global coordinate2
    
    global urshipcoords
    
    for i in range(17):
       
        for j in range(4):
            
            if urshipcoords[i][0] == float(coordinate1) and urshipcoords[i][1] == float(coordinate2):
  
                return 'red'
                
            
    return 'blue'
        #print(j)
        
        #print(urshipcoords[i][j])
    
fire = tk.Button(root,text='FIRE',command= ur_turn )#.grid(row=500, column=0)
fire.pack()
cu = tk.Button(root,text='Next turn',command =shoot_shot)
cu.pack()    

#===========

col = ['a','b','c','d','e','f','g','h','i','j']
row = ['1','2','3','4','5','6','7','8','9','10']
both = ['col', 'row']
coordList4 = []
coordList31 = []
coordList32 = []
coordList2 = []

def enemyshipplace(s):
    randplacecol = random.choice(col)
    randplacerow = random.choice(row)
    x = random.choice(both)
    #print(x)
    if x == 'col':
        x = col
        if randplacecol == 'a':
            valueX = 0
        elif randplacecol == 'b':
            valueX = 1
        elif randplacecol == 'c':
            valueX = 2
        elif randplacecol == 'd':
            valueX = 3
        elif randplacecol == 'e':
            valueX = 4
        elif randplacecol == 'f':
            valueX = 5
        elif randplacecol == 'g':
            valueX = 6
        elif randplacecol == 'h':
            valueX = 7
        elif randplacecol == 'i':
            valueX = 8
        elif randplacecol == 'j':
            valueX = 9
        if s == 'ship4':
            if valueX >= 5:
                for i in range(4):
                    coordList4.append(col[valueX] + randplacerow)
                    valueX -= 1
            elif valueX <= 4:
                for i in range(4):
                    coordList4.append(col[valueX] + randplacerow)
                    valueX += 1
        elif s == 'ship31':
            if valueX >= 5:
                for i in range(3):
                    coordList31.append(col[valueX] + randplacerow)
                    valueX -= 1
            elif valueX <= 4:
                for i in range(3):
                    coordList31.append(col[valueX] + randplacerow)
                    valueX += 1
        elif s == 'ship32':
            if valueX >= 5:
                for i in range(3):
                    coordList32.append(col[valueX] + randplacerow)
                    valueX -= 1
            elif valueX <= 4:
                for i in range(3):
                    coordList32.append(col[valueX] + randplacerow)
                    valueX += 1
        elif s == 'ship2':
            if valueX >= 5:
                for i in range(2):
                    coordList2.append(col[valueX] + randplacerow)
                    valueX -= 1
            elif valueX <= 4:
                for i in range(2):
                    coordList2.append(col[valueX] + randplacerow)
                    valueX += 1
    
    
    elif x == 'row':
        x = row
        #for i in x:
        if s == 'ship4':
            valueY = int(randplacerow)
            if valueY >= 6:
                for i in range(4):
                    coordList4.append(randplacecol + str(valueY))
                    #print(coordList4)
                    valueY -= 1
            elif valueY <= 5:
                for i in range(4):
                    coordList4.append(randplacecol + str(valueY))
                    valueY += 1
        elif s == 'ship31':
            valueY = int(randplacerow)
            if valueY >= 6:
                for i in range(3):
                    coordList31.append(randplacecol + str(valueY))
                    #print(coordList4)
                    valueY -= 1
            elif valueY <= 5:
                for i in range(3):
                    coordList31.append(randplacecol + str(valueY))
                    valueY += 1
        elif s == 'ship32':
            valueY = int(randplacerow)
            if valueY >= 6:
                for i in range(3):
                    coordList32.append(randplacecol + str(valueY))
                    #print(coordList4)
                    valueY -= 1
            elif valueY <= 5:
                for i in range(3):
                    coordList32.append(randplacecol + str(valueY))
                    valueY += 1            
        elif s == 'ship2':
            valueY = int(randplacerow)
            if valueY >= 6:
                for i in range(2):
                    coordList2.append(randplacecol + str(valueY))
                    #print(coordList4)
                    valueY -= 1
            elif valueY <= 5:
                for i in range(2):
                    coordList2.append(randplacecol + str(valueY))
                    valueY += 1
                
    
            

enemyshipplace('ship4')
enemyshipplace('ship31')
enemyshipplace('ship32')
enemyshipplace('ship2')
while True:
    for i in coordList31:
        if i in coordList4:
            coordList31.clear()
            enemyshipplace('ship31')
            continue
    for i in coordList32:
        if i in coordList4 or i in coordList31:
            coordList32.clear()
            enemyshipplace('ship32')
            continue
    for i in coordList2:
        if i in coordList4 or i in coordList31 or i in coordList32:
            coordList2.clear()
            enemyshipplace('ship2')
            continue
    break

print(coordList4)
print(coordList31)
print(coordList32)
print(coordList2)

#===========================================================
root.mainloop()
            