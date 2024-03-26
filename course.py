from tkinter import*
from tkinter import font
from tkinter import messagebox
from tkinter.messagebox import askyesno
from PIL import  ImageTk,Image
import sys
root = Tk()
root.geometry("500x500")
root.resizable(width=False, height=False)
root.title("Международные поддавки")
canvas = Canvas(root, width=900, height=900, bg='#fff')
canvas.pack()
im_bl,im_red,im_bl_d,im_red_d  = ImageTk.PhotoImage(file="IMG/Blue.png"), ImageTk.PhotoImage(file="IMG/RED.png"),ImageTk.PhotoImage(file="IMG/Blue_d.png"),ImageTk.PhotoImage(file="IMG/RED_d.png")
shahiki = [0,im_bl,im_red,im_bl_d,im_red_d]
hod_bl = True 
hod_red = False
vozm_hod_bl,vozm_hod_red = False,False
vzatie_bl ,vz_d,vzatie_red = False,False,False
hod_dm_bl,hod_dm_red = False,False
c_bl,c_red = 20,20
lst3 = []
pole = [[0,2,0,2,0,2,0,2,0,2],
        [2,0,2,0,2,0,2,0,2,0],
        [0,2,0,2,0,2,0,2,0,2],
        [2,0,2,0,2,0,2,0,2,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0]] 
def new_game():
    global board
    global c_red,c_bl,pole,hod_bl,hod_red,vozm_hod_bl,vozm_hod_red,vzatie_bl ,vzatie_red, hod_dm_bl,hod_dm_red,vzatie_bl_d
    hod_bl = True 
    hod_red = False
    vozm_hod_bl,vozm_hod_red = False,False
    vzatie_bl ,vzatie_bl_d,vzatie_red = False,False,False
    hod_dm_bl,hod_dm_red = False,False
    pole = [[0,2,0,2,0,2,0,2,0,2],
        [2,0,2,0,2,0,2,0,2,0],
        [0,2,0,2,0,2,0,2,0,2],
        [2,0,2,0,2,0,2,0,2,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0],
        [0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0]]
    c_bl,c_red = 20,20
    board()
      

def register(): #Регистрация пользователя
    global logg ,passs , txt,label
    lg = logg.get()
    ps = passs.get()
    if len(lg) == 0 or len(ps) == 0:
        return messagebox.showinfo(message="Вы не ввели логин/пароль!")
    else:
        file = open("lp.txt","r+")        
        a = file.read().split()
        if len(a) > 0:
            for i in range(len(a)):
                if a[i] == lg and a[i+1] == ps:
                    break
                else:
                    file.write(lg+' '+ps+' ')
        else:
            file.write(lg+' '+ps+' ')
        file.close()
        messagebox.showinfo('www',message="Регистрация/авторизация прошла успешно!")
        txt.place_forget()
        txt0.place_forget()
        txt1.place_forget()
        bt.place_forget()
        logg.place_forget()
        passs.place_forget()
        root.geometry("900x1000")
        root.geometry(f"+{(root.winfo_screenwidth() - 700) // 2}+{(root.winfo_screenheight() - 1050) // 2}")
        root.resizable(width=False, height=False)
        label = Label(root,text='Ход синих',width=900,height=100,font=("Arial", 20))
        label.pack()
        canvas.bind("<Button-1>",click)
        board()

def win():
    global c_bl,c_red
    global new_game
    if c_red == 0:
        if askyesno(message='Красные победили начать новую игру?'):
            new_game()
        else:
            sys.exit()
    if c_bl == 0:
        if askyesno(message='Синие победили начать новую игру?'):
            new_game()
        else:
            sys.exit()

def board(): #Отрисовка доски
    global pole ,canvas   
    fill = '#fff'
    outline = '#000'
    k = 90
    canvas.delete('all')
    for i in range(10):
        for j in range(10):
            x1, y1, x2, y2 = i * k, j * k, i * k + k, j * k + k
            canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline)
            fill, outline = outline, fill
        fill, outline = outline, fill
    for i in range(10):
        for j in range(10):
            q = pole[j][i]
            if q:
                canvas.create_image(i * k, j * k, anchor=NW, image=shahiki[q])

dm,dm1  = [],[]
def vozm_hod_damka(x,y):
    global dm, hod_dm_bl,hod_dm_red,dm1
    if pole[y][x] == 3:
        dm = []
        z = []
        z.append(y)
        z.append(x)
        dm.append(z)
        z = []
        for i in range(1,11):
                if y-i == -1 or x+i == 10:
                    break
                if pole[y-i][x+i] == 0:
                    z.append(y-i)
                    z.append(x+i)
                    dm.append(z)
                    z = []
                    
                else:
                    break
        for i in range(1,11):
                if y-i == -1 or x-i == -1:
                    break
                if pole[y-i][x-i] == 0:
                    z.append(y-i)
                    z.append(x-i)
                    dm.append(z)
                    z = []
                    
                else:
                    break
        for i in range(1,11):
                if y+i == 10 or x+i == 10:
                    break
                if pole[y+i][x+i] == 0:
                    z.append(y+i)
                    z.append(x+i)
                    dm.append(z)
                    z = []
                    
                else:
                    break
        for i in range(1,11):
                if y+i == 10 or x-i == -1:
                    break
                if pole[y+i][x-i] == 0:
                    z.append(y+i)
                    z.append(x-i)
                    dm.append(z)
                    z = []
                    
                else:
                    break
                
        if len(dm) != 0:
            hod_dm_bl = True
        else:
            hod_dm_bl = False
    elif pole[y][x] == 4:
        dm1 = []
        z = []
        z.append(y)
        z.append(x)
        dm1.append(z)
        z = []
        for i in range(1,11):
                if y-i == -1 or x+i == 10:
                    break
                if pole[y-i][x+i] == 0:
                    z.append(y-i)
                    z.append(x+i)
                    dm1.append(z)
                    z = []
                    
                else:
                    break
        for i in range(1,11):
                if y-i == -1 or x-i == -1:
                    break
                if pole[y-i][x-i] == 0:
                    z.append(y-i)
                    z.append(x-i)
                    dm1.append(z)
                    z = []
                    
                else:
                    break
        for i in range(1,11):
                if y+i == 10 or x+i == 10:
                    break
                if pole[y+i][x+i] == 0:
                    z.append(y+i)
                    z.append(x+i)
                    dm1.append(z)
                    z = []
                    
                else:
                    break
        for i in range(1,11):
                if y+i == 10 or x-i == -1:
                    break
                if pole[y+i][x-i] == 0:
                    z.append(y+i)
                    z.append(x-i)
                    dm1.append(z)
                    z = []
                    
                else:
                    break
                
        if len(dm1) != 0:
            hod_dm_red = True
        else:
            hod_dm_red = False
    else:
        hod_dm_red = False
        hod_dm_bl = False

def vozm_hoda_bl(x,y):
    global vozm_hod_damka
    global prev_y_bl,prev_x_bl,dm
    global vozm_hod_bl
    if pole[y][x] == 1: 
        dm = []
        if 0 <= x <= 8:
            if (pole[y-1][x+1] == 0 ) or (pole[y-1][x-1] == 0):
                vozm_hod_bl = True
                prev_y_bl = y 
                prev_x_bl = x
            else:
                vozm_hod_bl = False
        if x == 9:
            if pole[y-1][x-1] == 0:
                vozm_hod_bl = True
                prev_y_bl = y 
                prev_x_bl = x
            else:
                vozm_hod_bl = False
        if x == 0:
            if pole[y-1][x+1] == 0:
                vozm_hod_bl = True
                prev_y_bl = y 
                prev_x_bl = x
            else:
                vozm_hod_bl = False
   
def vozm_hoda_red(x,y):
    global vozm_hod_red
    global prev_y_red,prev_x_red
    global vozm_hod_bl
    if pole[y][x] == 2:
        if 0 <= x <= 8:
            if (pole[y+1][x+1] == 0) or (pole[y+1][x-1] == 0):
                vozm_hod_red = True
                prev_y_red = y 
                prev_x_red = x
            else:
                vozm_hod_red = False
        if x == 0:
            if pole[y+1][x+1] == 0:
                vozm_hod_red = True
                prev_y_red = y 
                prev_x_red = x
            else:
                vozm_hod_red = False
        if x == 9:
            if pole[y+1][x-1] == 0:
                vozm_hod_red = True
                prev_y_red = y 
                prev_x_red = x
            else:
                vozm_hod_red = False
l2 = []
f1 ,f2,f3,f4= False,False,False,False
def dam_bl():
    global vzatie_bl_d,vzatie_bl,x_p,y_p,f1,l2,l3,f2
    f1 ,f2,f3,f4= False,False,False,False
    for i in range(10):
        for j in range(10):
            
            if pole[i][j] == 3:
                for ii in range(1,11):
                    if i-ii == 0 or j+ii == 9 or i == 0 or j == 9:
                        break 
                    if pole[i-ii][j+ii] == 0:
                        continue
                    if (pole[i-ii][j+ii] == 2 or pole[i-ii][j+ii] == 4) and pole[i-ii-1][j+ii+1] == 0:
                        l2.append([i,j])
                        l2.append([i-ii,j+ii])
                        l2.append([i-ii-1,j+ii+1])
                        vzatie_bl = True
                        x_p = i-ii-1
                        y_p = j+ii+1
                    else:
                        break
    l3 = l2.copy()

    if len(l2) != 0:                    
        for k in range(12):
            x = x_p -k
            y = y_p + k
            if x == -1 or y == 10:
                break
            if pole[x][y] == 0:
                l2.append([x,y])
                for l in range(1,11):
                    if x-l == 0 or y-l == 0 or x == 0 or y == 0:
                        break 
                    if pole[x-l][y-l] == 0:
                        continue
                    if (pole[x-l][y-l] == 2 or pole[x-l][y-l] == 4) and pole[x-l-1][y-l-1] == 0 and pole[x-l+1][y-l+1] == 0:
                        l3.append([x,y])
                        f1 = True
                        break

                for l in range(1,11):
                    if x+l == 9 or y+l == 9 or x == 9 or y == 9:
                        break 
                    if pole[x+l][y+l] == 0:
                        continue
                    if (pole[x+l][y+l] == 2 or pole[x+l][y+l] == 4) and pole[x+l+1][y+l+1] == 0 and pole[x+l-1][x+l-1] == 0:
                        l3.append([x,y])
                        f1 = True
                        break
    if f1:
        if len(l3) != 0:
            lst3.append(l3)
            
            
    else:
        if len(l2) != 0:
            lst3.append(l2)
    l2,l3 = [],[]        
#----------------------------------------------------------------------------------------------------------    
    for i in range(10):
        for j in range(10):
            if pole[i][j] == 3:
                for ii in range(1,11):
                    if i-ii == 0 or j-ii == 0 or i == 0 or j == 0:
                        break 
                    if pole[i-ii][j-ii] == 0:
                        continue
                    if (pole[i-ii][j-ii] == 2 or pole[i-ii][j-ii] == 4) and pole[i-ii-1][j-ii-1] == 0:
                        l2.append([i,j])
                        l2.append([i-ii,j-ii])
                        l2.append([i-ii-1,j-ii-1])
                        vzatie_bl = True
                        x_p = i-ii-1
                        y_p = j-ii-1
                    else:
                        break
    l3 = l2.copy()

    if len(l2) != 0:                    
        for k in range(12):
            x = x_p -k
            y = y_p - k
            if x == -1 or y == -1:
                break
            if pole[x][y] == 0:
                l2.append([x,y])
                for l in range(1,11):
                    if x-l == 0 or y+l == 9 or x == 0 or y == 9:
                        break 
                    if pole[x-l][y+l] == 0:
                        continue
                    if (pole[x-l][y+l] == 2 or pole[x-l][y+l] == 4) and pole[x-l-1][y+l+1] == 0 and pole[x-l+1][y+l-1] == 0:
                        l3.append([x,y])
                        f2 = True
                        break


                for l in range(1,11):
                    if x+l == 9 or y-l == 0 or x == 9 or y == 0:
                        break 
                    if pole[x+l][y-l] == 0:
                        continue
                    if (pole[x+l][y-l] == 2 or pole[x+l][y-l] == 4) and pole[x+l+1][y-l-1] == 0 and pole[x+l-1][y-l+1] == 0:
                        l3.append([x,y])
                        f2 = True
                        break
    if f2:
        if len(l3) != 0:
            lst3.append(l3)           
    else:
        if len(l2) != 0:
            lst3.append(l2)
    l2,l3 = [],[]
#---------------------------------------------------------------------------------------------------!-------  
    for i in range(10):
        for j in range(10):
            
            if pole[i][j] == 3:
                for ii in range(1,11):
                    if i+ii == 9 or j-ii == 0 or i == 9 or j == 0:
                        break 
                    if pole[i+ii][j-ii] == 0:
                        continue
                    if (pole[i+ii][j-ii] == 2 or pole[i+ii][j-ii] == 4) and pole[i+ii+1][j-ii-1] == 0:
                        l2.append([i,j])
                        l2.append([i+ii,j-ii])
                        l2.append([i+ii+1,j-ii-1])
                        vzatie_bl = True
                        x_p = i+ii+1
                        y_p = j-ii-1
                    else:
                        break
    l3 = l2.copy()

    if len(l2) != 0:                    
        for k in range(12):
            x = x_p +k
            y = y_p - k
            if x == 10 or y == -1:
                break
            if pole[x][y] == 0:
                l2.append([x,y])
                for l in range(1,11):
                    if x-l == 0 or y-l == 0 or x == 0 or y == 0:
                        break 
                    if pole[x-l][y-l] == 0:
                        continue
                    if (pole[x-l][y-l] == 2 or pole[x-l][y-l] == 4) and pole[x-l-1][y-l-1] == 0 and pole[x-l+1][y-l+1] == 0:
                        l3.append([x,y])
                        f3 = True
                        break

                for l in range(1,11):
                    if x+l == 9 or y+l == 9 or x == 9 or y == 9:
                        break 
                    if pole[x+l][y+l] == 0:
                        continue
                    if (pole[x+l][y+l] == 2 or pole[x+l][y+l] == 4) and pole[x+l+1][y+l+1] == 0 and pole[x+l-1][x+l-1] == 0:
                        l3.append([x,y])
                        f3 = True
                        break
    if f3:
        if len(l3) != 0:
            lst3.append(l3)           
    else:
        if len(l2) != 0:
            lst3.append(l2)
    l2,l3 = [],[]        
#----------------------------------------------------------------------------------------------------------    
    for i in range(10):
        for j in range(10):
            if pole[i][j] == 3:
                for ii in range(1,11):
                    if i+ii == 9 or j+ii == 9 or i == 9 or j == 9:
                        break 
                    if pole[i+ii][j+ii] == 0:
                        continue
                    if (pole[i+ii][j+ii] == 2 or pole[i+ii][j+ii] == 4) and pole[i+ii+1][j+ii+1] == 0:
                        l2.append([i,j])
                        l2.append([i+ii,j+ii])
                        l2.append([i+ii+1,j+ii+1])
                        vzatie_bl = True
                        x_p = i+ii+1
                        y_p = j+ii+1
                    else:
                        break
    l3 = l2.copy()

    if len(l2) != 0:                    
        for k in range(12):
            x = x_p + k
            y = y_p + k
            if x == 10 or y == 10:
                break
            if pole[x][y] == 0:
                l2.append([x,y])
                for l in range(1,11):
                    if x-l == 0 or y+l == 9 or x == 0 or y == 9:
                        break 
                    if pole[x-l][y+l] == 0:
                        continue
                    if (pole[x-l][y+l] == 2 or pole[x-l][y+l] == 4) and pole[x-l-1][y+l+1] == 0 and pole[x-l+1][y+l-1] == 0:
                        l3.append([x,y])
                        f4 = True
                        break


                for l in range(1,11):
                    if x+l == 9 or y-l == 0 or x == 9 or y == 0:
                        break 
                    if pole[x+l][y-l] == 0:
                        continue
                    if (pole[x+l][y-l] == 2 or pole[x+l][y-l] == 4) and pole[x+l+1][y-l-1] == 0 and pole[x+l-1][y-l+1] == 0:
                        l3.append([x,y])
                        f4 = True
                        break
    if f4:
        if len(l3) != 0:
            lst3.append(l3)           
    else:
        if len(l2) != 0:
            lst3.append(l2)
    l2,l3 = [],[]
    print(f1)
def proverka_bl():
    global dam_bl
    global vzatie_bl ,lst3,vzatie_bl_d
    global pole
    lst2,lst1 = [],[]   
    for i in range(10):
        for j in range(10):
            if pole[i][j] == 1 and (i >= 2 and j <= 7):
                if  (pole[i-1][j+1] == 2 or pole[i-1][j+1] == 4) and pole[i-2][j+2] == 0:
                    lst2.append(i)
                    lst2.append(j)
                    lst1.append(lst2)
                    lst2 = []

                    lst2.append(i-1)
                    lst2.append(j+1)
                    lst1.append(lst2)
                    lst2 = []

                    lst2.append(i-2)
                    lst2.append(j+2)
                    lst1.append(lst2)
                    lst2 = []
                    lst3.append(lst1)
                    lst1 = []
                    vzatie_bl = True
            if  pole[i][j] == 1 and (j <= 7 and i <= 7):
                if (pole[i+1][j+1] == 2 or pole[i+1][j+1] == 4)  and pole[i+2][j+2] == 0:
                    lst2.append(i)
                    lst2.append(j)
                    lst1.append(lst2)
                    lst2 = []

                    lst2.append(i+1)
                    lst2.append(j+1)
                    lst1.append(lst2)
                    lst2 = []

                    lst2.append(i+2)
                    lst2.append(j+2)
                    lst1.append(lst2)
                    lst2 = []
                    lst3.append(lst1)
                    lst1 = []
                    vzatie_bl = True
                    
            if pole[i][j] == 1 and (j >= 2 and i >= 2):
                if (pole[i-1][j-1] == 2 or pole[i-1][j-1] == 4)  and pole[i-2][j-2] == 0:
                    lst2.append(i)
                    lst2.append(j)
                    lst1.append(lst2)
                    lst2 = []

                    lst2.append(i-1)
                    lst2.append(j-1)
                    lst1.append(lst2)
                    lst2 = []

                    lst2.append(i-2)
                    lst2.append(j-2)
                    lst1.append(lst2)
                    lst2 = []
                    lst3.append(lst1)
                    lst1 = []
                    vzatie_bl = True
            if pole[i][j] == 1 and (j >= 2 and i <= 7):
                if (pole[i+1][j-1] == 2 or pole[i+1][j-1] == 4)  and pole[i+2][j-2] == 0:
                    lst2.append(i)
                    lst2.append(j)
                    lst1.append(lst2)
                    lst2 = []

                    lst2.append(i+1)
                    lst2.append(j-1)
                    lst1.append(lst2)
                    lst2 = []

                    lst2.append(i+2)
                    lst2.append(j-2)
                    lst1.append(lst2)
                    lst2 = []
                    lst3.append(lst1)
                    lst1 = []
                    vzatie_bl = True
            
            if pole[i][j] == 3:
                dam_bl()    
    if len(lst3) == 0:
        vzatie_bl = False      
def dam_red():
    global vzatie_red,x_p,y_p,f1,l2,l3,f2
    f1 ,f2,f3,f4= False,False,False,False
    for i in range(10):
        for j in range(10):
            
            if pole[i][j] == 4:
                for ii in range(1,11):
                    if i-ii == 0 or j+ii == 9 or i == 0 or j == 9:
                        break 
                    if pole[i-ii][j+ii] == 0:
                        continue
                    if (pole[i-ii][j+ii] == 1 or pole[i-ii][j+ii] == 3) and pole[i-ii-1][j+ii+1] == 0:
                        l2.append([i,j])
                        l2.append([i-ii,j+ii])
                        l2.append([i-ii-1,j+ii+1])
                        vzatie_red = True
                        x_p = i-ii-1
                        y_p = j+ii+1
                    else:
                        break
    l3 = l2.copy()

    if len(l2) != 0:                    
        for k in range(12):
            x = x_p -k
            y = y_p + k
            if x == -1 or y == 10:
                break
            if pole[x][y] == 0:
                l2.append([x,y])
                for l in range(1,11):
                    if x-l == 0 or y-l == 0 or x == 0 or y == 0 :
                        break 
                    if pole[x-l][y-l] == 0:
                        continue
                    if (pole[x-l][y-l] == 1 or pole[x-l][y-l] == 3) and pole[x-l-1][y-l-1] == 0 and pole[x-l+1][y-l+1] == 0:
                        l3.append([x,y])
                        f1 = True
                        break

                for l in range(1,11):
                    if x+l == 9 or y+l == 9 or x == 9 or y == 9:
                        break 
                    if pole[x+l][y+l] == 0:
                        continue
                    if (pole[x+l][y+l] == 1 or pole[x+l][y+l] == 3) and pole[x+l+1][y+l+1] == 0 and pole[x+l-1][x+l-1] == 0:
                        l3.append([x,y])
                        f1 = True
                        break
    if f1:
        if len(l3) != 0:
            lst3.append(l3)
            
            
    else:
        if len(l2) != 0:
            lst3.append(l2)
    l2,l3 = [],[]        
#----------------------------------------------------------------------------------------------------!!!!------    
    for i in range(10):
        for j in range(10):
            if pole[i][j] == 4:
                for ii in range(1,11):
                    if i-ii == 0 or j-ii == 0 or i == 0 or j == 0:
                        break 
                    if pole[i-ii][j-ii] == 0:
                        continue
                    if (pole[i-ii][j-ii] == 1 or pole[i-ii][j-ii] == 3) and pole[i-ii-1][j-ii-1] == 0:
                        l2.append([i,j])
                        l2.append([i-ii,j-ii])
                        l2.append([i-ii-1,j-ii-1])
                        vzatie_red = True
                        x_p = i-ii-1
                        y_p = j-ii-1
                    else:
                        break
    l3 = l2.copy()

    if len(l2) != 0:                    
        for k in range(12):
            x = x_p -k
            y = y_p - k
            if x == -1 or y == -1:
                break
            if pole[x][y] == 0:
                l2.append([x,y])
                for l in range(1,11):
                    if x-l == 0 or y+l == 9 or x == 0 or y == 9:
                        break 
                    if pole[x-l][y+l] == 0:
                        continue
                    if (pole[x-l][y+l] == 1 or pole[x-l][y+l] == 3) and pole[x-l-1][y+l+1] == 0 and pole[x-l+1][y+l-1] == 0:
                        l3.append([x,y])
                        f2 = True
                        break


                for l in range(1,11):
                    if x+l == 9 or y-l == 0 or x == 9 or y == 0:
                        break 
                    if pole[x+l][y-l] == 0:
                        continue
                    if (pole[x+l][y-l] == 1 or pole[x+l][y-l] == 3) and pole[x+l+1][y-l-1] == 0 and pole[x+l-1][y-l+1] == 0:
                        l3.append([x,y])
                        f2 = True
                        break
    if f2:
        if len(l3) != 0:
            lst3.append(l3)           
    else:
        if len(l2) != 0:
            lst3.append(l2)
    l2,l3 = [],[]
#---------------------------------------------------------------------------------------------------!-------  
    for i in range(10):
        for j in range(10):
            
            if pole[i][j] == 4:
                for ii in range(1,11):
                    if i+ii == 9 or j-ii == 0 or i == 9 or j == 0:
                        break 
                    if pole[i+ii][j-ii] == 0:
                        continue
                    if (pole[i+ii][j-ii] == 1 or pole[i+ii][j-ii] == 3) and pole[i+ii+1][j-ii-1] == 0:
                        l2.append([i,j])
                        l2.append([i+ii,j-ii])
                        l2.append([i+ii+1,j-ii-1])
                        vzatie_red = True
                        x_p = i+ii+1
                        y_p = j-ii-1
                    else:
                        break
    l3 = l2.copy()

    if len(l2) != 0:                    
        for k in range(12):
            x = x_p +k
            y = y_p - k
            if x == 10 or y == -1:
                break
            if pole[x][y] == 0:
                l2.append([x,y])
                for l in range(1,11):
                    if x-l == 0 or y-l == 0 or y == 0 or  x == 0:
                        break 
                    if pole[x-l][y-l] == 0:
                        continue
                    if (pole[x-l][y-l] == 1 or pole[x-l][y-l] == 3) and pole[x-l-1][y-l-1] == 0 and pole[x-l+1][y-l+1] == 0:
                        l3.append([x,y])
                        f3 = True
                        break

                for l in range(1,11):
                    if x+l == 9 or y+l == 9 or x == 9 or y == 9:
                        break 
                    if pole[x+l][y+l] == 0:
                        continue
                    if (pole[x+l][y+l] == 1 or pole[x+l][y+l] == 3) and pole[x+l+1][y+l+1] == 0 and pole[x+l-1][x+l-1] == 0:
                        l3.append([x,y])
                        f3 = True
                        break
    if f3:
        if len(l3) != 0:
            lst3.append(l3)
            
            
    else:
        if len(l2) != 0:
            lst3.append(l2)
    l2,l3 = [],[]        
#----------------------------------------------------------------------------------------------------------    
    for i in range(10):
        for j in range(10):
            if pole[i][j] == 4:
                for ii in range(1,11):
                    if i+ii == 9 or j+ii == 9 or i == 9 or j == 9:
                        break 
                    if pole[i+ii][j+ii] == 0:
                        continue
                    if (pole[i+ii][j+ii] == 1 or pole[i+ii][j+ii] == 3)  and pole[i+ii+1][j+ii+1] == 0:
                        l2.append([i,j])
                        l2.append([i+ii,j+ii])
                        l2.append([i+ii+1,j+ii+1])
                        vzatie_red = True
                        x_p = i+ii+1
                        y_p = j+ii+1
                    else:
                        break
    l3 = l2.copy()

    if len(l2) != 0:                    
        for k in range(12):
            x = x_p + k
            y = y_p + k
            if x == 10 or y == 10:
                break
            if pole[x][y] == 0:
                l2.append([x,y])
                for l in range(1,11):
                    if x-l == 0 or y+l == 9 or x == 0 or y == 9:
                        break 
                    if pole[x-l][y+l] == 0:
                        continue
                    if (pole[x-l][y+l] == 1 or pole[x-l][y+l] == 3) and pole[x-l-1][y+l+1] == 0 and pole[x-l+1][y+l-1] == 0:
                        l3.append([x,y])
                        f4 = True
                        break


                for l in range(1,11):
                    if x+l == 9 or y-l == 0 or y == 0 or x == 9:
                        break 
                    if pole[x+l][y-l] == 0:
                        continue
                    if (pole[x+l][y-l] == 1 or pole[x+l][y-l] == 3) and pole[x+l+1][y-l-1] == 0 and pole[x+l-1][y-l+1] == 0:
                        l3.append([x,y])
                        f4 = True
                        break
    if f4:
        if len(l3) != 0:
            lst3.append(l3)           
    else:
        if len(l2) != 0:
            lst3.append(l2)
    l2,l3 = [],[]
def proverka_red():
    global dam_red
    global vzatie_red ,lst3
    global pole
    lst2,lst1 = [],[]
    for i in range(10):
        for j in range(10):
            if pole[i][j] == 2 and (i <= 7 and j >= 2):
                if  (pole[i+1][j-1] == 1 or pole[i+1][j-1] == 3 ) and pole[i+2][j-2] == 0:
                    lst2.append(i)
                    lst2.append(j)
                    lst1.append(lst2)
                    lst2 = []

                    lst2.append(i+1)
                    lst2.append(j-1)
                    lst1.append(lst2)
                    lst2 = []

                    lst2.append(i+2)
                    lst2.append(j-2)
                    lst1.append(lst2)
                    lst2 = []
                    lst3.append(lst1)
                    lst1 = []
                    vzatie_red = True
            if  pole[i][j] == 2 and (j >= 2 and i >= 2):
                if (pole[i-1][j-1] == 1 or pole[i-1][j-1] == 3)  and pole[i-2][j-2] == 0:
                    lst2.append(i)
                    lst2.append(j)
                    lst1.append(lst2)
                    lst2 = []

                    lst2.append(i-1)
                    lst2.append(j-1)
                    lst1.append(lst2)
                    lst2 = []

                    lst2.append(i-2)
                    lst2.append(j-2)
                    lst1.append(lst2)
                    lst2 = []
                    lst3.append(lst1)
                    lst1 = []
                    vzatie_red = True
                    
            if pole[i][j] == 2 and (j <= 7 and i >= 2):
                if (pole[i-1][j+1] == 1 or pole[i-1][j+1] == 3) and pole[i-2][j+2] == 0:
                    lst2.append(i)
                    lst2.append(j)
                    lst1.append(lst2)
                    lst2 = []

                    lst2.append(i-1)
                    lst2.append(j+1)
                    lst1.append(lst2)
                    lst2 = []

                    lst2.append(i-2)
                    lst2.append(j+2)
                    lst1.append(lst2)
                    lst2 = []
                    lst3.append(lst1)
                    lst1 = []
                    vzatie_red = True
            if pole[i][j] == 2 and (j <= 7 and i <= 7):
                if (pole[i+1][j+1] == 1 or pole[i+1][j+1] == 3) and pole[i+2][j+2] == 0:
                    lst2.append(i)
                    lst2.append(j)
                    lst1.append(lst2)
                    lst2 = []

                    lst2.append(i+1)
                    lst2.append(j+1)
                    lst1.append(lst2)
                    lst2 = []

                    lst2.append(i+2)
                    lst2.append(j+2)
                    lst1.append(lst2)
                    lst2 = []
                    lst3.append(lst1)
                    lst1 = []
                    vzatie_red = True
            if pole[i][j] == 4:
                dam_red()
    if len(lst3) == 0:
        vzatie_red = False            
#----------------------------------------------------------------------------------------------------------------------------------
def click(event):
    global hod_bl,hod_red,lst3,c_bl,c_red,dm,hod_dm_bl,dm1,l2,l3
    global win, vozm_hod_damka
    x,y = event.x//90 ,event.y//90    

    if hod_bl:
        if not vzatie_bl:
            label.config(text = 'Ход синих')
            if pole[y][x] != 0:
                vozm_hoda_bl(x,y)
                vozm_hod_damka(x,y)
            else:
                if vozm_hod_bl and not hod_dm_bl :
                    if y != 0:
                        if (pole[y][x] == 0 and y +1 == prev_y_bl and x-1 == prev_x_bl) or  (pole[y][x] == 0 and y +1 == prev_y_bl and x+1 == prev_x_bl):
                            pole[y][x] = 1
                            pole[prev_y_bl][prev_x_bl] = 0
                            proverka_red()
                            hod_bl = False
                            hod_red = True
                    if y == 0:
                        if (pole[y][x] == 0 and y +1 == prev_y_bl and x-1 == prev_x_bl) or  (pole[y][x] == 0 and y +1 == prev_y_bl and x+1 == prev_x_bl):
                            pole[y][x] = 3
                            pole[prev_y_bl][prev_x_bl] = 0
                            proverka_red()
                            hod_bl = False
                            hod_red = True  
                if hod_dm_bl:
                    if pole[y][x] == 0 and ([y,x] in dm):
                        pole[y][x] , pole[dm[0][0]][dm[0][1]] = 3,0
                        dm = []
                        proverka_red()
                        hod_red = True
                        hod_bl = False
        if vzatie_bl:
            label.config(text='Обязательное взятие синих')
            if pole[y][x] == 0:
                for i in lst3:
                    if [y,x] in i:
                        if pole[i[0][0]][i[0][1]] == 1:
                            pole[i[0][0]][i[0][1]],pole[i[1][0]][i[1][1]],pole[y][x] = 0,0,1
                        if pole[i[0][0]][i[0][1]] == 3:
                            pole[i[0][0]][i[0][1]],pole[i[1][0]][i[1][1]],pole[y][x] = 0,0,3
                        c_red -= 1
                        win()
                        lst3 = []
                        l3 ,l2 = [],[]
                        proverka_bl()
                        if not vzatie_bl:
                            if y == 0:
                                pole[y][x] = 3
                            hod_bl = False
                            hod_red = True
                            proverka_red()
                            
    if hod_red:
        if not vzatie_red:
            label.config(text = 'Ход красных')
            if pole[y][x] != 0:
                vozm_hoda_red(x,y)
                vozm_hod_damka(x,y)
            else:
                if vozm_hod_red and not hod_dm_red:
                    if y != 9:
                        if (pole[y][x] == 0 and y - 1 == prev_y_red and x-1 == prev_x_red) or  (pole[y][x] == 0 and y - 1 == prev_y_red and x+1 == prev_x_red):
                            pole[y][x] = 2
                            pole[prev_y_red][prev_x_red] = 0
                            proverka_bl()
                            hod_red = False
                            hod_bl = True 
                            if vzatie_bl:
                                label.config(text = 'Обязательное взятие синих')
                            if not vzatie_bl:
                                label.config(text = 'Ход синих')
                    else:
                        if (pole[y][x] == 0 and y - 1 == prev_y_red and x-1 == prev_x_red) or  (pole[y][x] == 0 and y - 1 == prev_y_red and x+1 == prev_x_red):
                            pole[y][x] = 4
                            pole[prev_y_red][prev_x_red] = 0
                            proverka_bl()
                            hod_red = False
                            hod_bl = True 
                            if vzatie_bl:
                                label.config(text = 'Обязательное взятие синих')
                            if not vzatie_bl:
                                label.config(text = 'Ход синих')
                if hod_dm_red:
                    if pole[y][x] == 0 and ([y,x] in dm1):
                        pole[y][x] , pole[dm1[0][0]][dm1[0][1]] = 4,0
                        dm1 = []
                        proverka_bl()                        
                        hod_red = False
                        hod_bl = True
                        if vzatie_bl:
                            label.config(text='Обязательное взятие синих')
                        else:
                            label.config(text = 'Ход синих')
        if vzatie_red:
            label.config(text='Обязательное взятие красных')
            if pole[y][x] == 0:
                for i in lst3:
                    if [y,x] in i:
                        if pole[i[0][0]][i[0][1]] == 2:
                            pole[i[0][0]][i[0][1]],pole[i[1][0]][i[1][1]],pole[i[2][0]][i[2][1]] = 0,0,2
                        if pole[i[0][0]][i[0][1]] == 4:
                            pole[i[0][0]][i[0][1]],pole[i[1][0]][i[1][1]],pole[y][x] = 0,0,4
                        c_bl -= 1
                        win()
                        lst3 = []
                        proverka_red()
                        if not vzatie_red:
                            if y == 9:
                                pole[y][x] = 4
                            hod_bl = True
                            hod_red = False
                            proverka_bl()
                            
                            if not vzatie_bl:
                                label.config(text = 'Ход синих')
                            else:
                                label.config(text = 'Обязательное взятие синих')
    board()

txt0 = Label(root,text="Зарегестрируйтесь/авторизиуйтесь для игры",font=("Arial",15))   
txt0.place(x=50,y=50) 
txt = Label(root,text="Введите логин",font=("Arial",16))
txt.place(x=170 ,y=100)
logg = Entry(root,width=30,bd=2)
logg.place(x=150 ,y=150)
txt1= Label(root,text="Введите пароль",font=("Arial",16))
txt1.place(x=160 ,y=220)
passs = Entry(root,width=30,bd=2)
passs.place(x=150 ,y=270)
fnt=font.Font(size=12)
bt = Button(root,text="Зарегестрироваться/начать игру",width=45,height=3,font=fnt,command=register)
bt.place(x=40 ,y=320)
mainloop()