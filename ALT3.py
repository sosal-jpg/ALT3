import tkinter as tk
from math import *
import time

def left(event):#creates a ball
    global x1,y1,circle
    x1=event.x
    y1=event.y
    canv.delete("all")#clears canvas
    circle = canv.create_oval(x1+5, y1+5, x1-5, y1-5,fill='#000000')

def move(event):#draws a line
    global line,length
    try :canv.delete(line)
    except: pass
    length=sqrt((x1-event.x)**2+(y1-event.y)**2)
    line=canv.create_line(x1,y1,event.x,event.y,width=3,arrow=tk.LAST,arrowshape=(length*10/250,length*13/250,length*7/250))

def left_up(event):#draws final line
    global x2, y2,line,length
    try:canv.delete(line)
    except:pass
    x2=event.x
    y2=event.y
    length=sqrt((x1-x2)**2+(y1-y2)**2)
    line=canv.create_line(x1,y1,x2,y2,width=3,arrow=tk.LAST,arrowshape=(length*10/250,length*13/250,length*7/250))

def stop():# reset function, doesn't fully work
    global stp,x1,x2,y1,y2,canvas,line,circle
    stp=True
    canv.delete('all')
    line=canv.create_line(x1,y1,event.x,event.y,width=3,arrow=tk.LAST,arrowshape=(length*10/250,length*13/250,length*7/250))
    circle = canv.create_oval(x1 + 5, y1 + 5, x1 - 5, y1 - 5, fill='#000000')
def start():
    global line,circle,x,y,x0,y0,f,t,vx,vy,vx0,vy0,m,windx,windy,y_count,x_count,k,fx,stp
    if x1 is not None:
        try :wind_magn=float(entr_wind.get())
        except:wind_magn=0
        try :wind_ang=float(entr_ang.get())
        except:wind_ang=0
        try:m=float(entr_mass.get())
        except:print('no mass')
        else:
            stp = False
            f=9.8*m#mg
            x=x0=x1
            y=y0=y1
            windx=cos(wind_ang)*wind_magn
            windy=sin(wind_ang)*wind_magn
            v=2*length/3
            try: vx=vx0=v*(x2-x1)/(length*2)-windx#calculates x and y velocity
            except: vx0=0
            try: vy=vy0=v*(y2-y1)/(length*2)-windy
            except: vy0=0

            t = tick / (1000)#tick in seconds

            vx=vx0/(e**(k*t/m))#calculates x and y velocity after tick
            vx0=vx

            if vy>=0: vy=(k*vy0-f)/(k*e**(k*t/m))+f/k
            else:vy=(((k*vy0+f)*(e**(k*t/m)))/k)-(f/k)
            vy0 = vy

            x+=vx*tick/1000#calculates coordinates of the ball
            y+=vy*tick/1000

            canv.delete('all')
            circle = canv.create_oval(x + 5, y + 5, x - 5, y - 5, fill='#000000')#draws new circle
            window.after(tick, my_mainloop)

def my_mainloop():
    global line,circle,x,y,x0,y0,f,t,vx,vy,vx0,vy0,m,windx,windy,y_count,x_count,tf,k,fx,stp
    if tf:#modulates wall touch
        if y<=5 or y>=875:
            if y<=5: y=5
            else: y=875
            vy0=-vy*(1-loss)
    if x <= 5 or x >= 1855:
        if x<=5 and (x_count==1 or x_count==2):
            x_count=0
            vx0=-vx*(1-loss)
        elif x>=1855 and (x_count==0 or x_count==2):
            x_count=1
            vx0=-vx*(1-loss)

    vx = vx0 / (e ** (k * t / m))#x and y velocity
    vx0 = vx

    if vy >= 0:vy = (k * vy0 - f) / (k * e ** (k * t / m)) + f / k
    else:vy = (((k * vy0 + f) * (e ** (k * t / m))) / k) - (f / k)
    vy0 = vy

    if y_count!= 4 :
        y +=vy*tick/(1000)#y
        if y<=5.1: y_count+=1
        else: y_count=0
    elif tf:#if the ball remains at the low height for 3 ticks, y coordinate stops changing
        tf=False
        y=5
        x0=x
        fx = f *0.2

    if not tf:#if y is constant
        if abs(vx)<4: vx=0#if x velocity<4 and the ball is on the ground, it stops moving
    x +=vx*tick/1000#x
    print(vx,vy)
    canv.delete('all')
    circle = canv.create_oval(x + 5, y+5, x - 5, y-5, fill='#000000')

    if not stp: window.after(tick, my_mainloop)#stops the program
    else:
        stop()
        stp = False

stp=False
x1=None
y1=None
x2=None
y2=None
k=0.01#air resistance coefficient
scale=1/20
loss=0.4#loss of speed when hitting a wall
e=exp(1)#exponenta
tick=30#update time
x_count=2
y_count=0
tf=True

window=tk.Tk() #Window creation
height=window.winfo_screenheight()#height and width of user's screen
width=window.winfo_screenwidth()
window.state('zoomed')#makes window zoomed

canv=tk.Canvas(window,height=height*13/16, width=width,background='#9ACEEB')#creates canvas
canv.bind('<Button-1>',left)
canv.bind('<ButtonRelease-1>',left_up)
canv.bind('<B1-Motion>',move)#on actions with the left mouse button, functions are executed
canv.place(x=0,y=0)

fr=tk.Frame(window,height=height*3/16,width=width)
fr.place(x=0,y=height*13/16+2)

label1=tk.Label(fr,text='Wind')
label1.grid(column=0,row=0)

label2=tk.Label(fr,text='Angle')
label2.grid(column=1,row=0)

label3=tk.Label(fr,text='Mass')
label3.grid(column=0,row=2)

entr_wind=tk.Entry(fr)
entr_wind.grid(column=0,row=1,padx=2,pady=2)

entr_ang=tk.Entry(fr)
entr_ang.grid(column=1,row=1,padx=2,pady=2)

entr_mass=tk.Entry(fr)
entr_mass.grid(column=0,row=3,padx=2,pady=2)

restart=tk.Button(fr,command=stop,text='Reset',height=2,width=8)
restart.grid(column=20,row=0,padx=2,pady=2)

start=tk.Button(fr,command=start,text='Start',height=2,width=8)
start.grid(column=20,row=1,padx=2,pady=2)

window.mainloop()
