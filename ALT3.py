import tkinter as tk
from math import *

def button_click(event):
    if event.keysym=='Return': b_start.invoke()
    elif event.keysym=='Escape':restart.invoke()
def temp_text(event):
    global prev_text
    prev_text=event.widget.get()
    event.widget.delete(0,"end")

def is_text(event):
    if event.widget.get()=='':
        event.widget.delete(0, "end")
        event.widget.insert(0,prev_text)
    else:
        try: artf=float(event.widget.get())
        except:
            event.widget.delete(0, "end")
            event.widget.insert(0, prev_text)

def creation():
    global line, circle, x, y, x0, y0, f, t, vx, vy, vx0, vy0, m, windx, windy, y_count, label7, x_count, k, fx, stp, height,entr_y,entr_x, width,canv,fr,label1,label2,label3,label5,entr_wind,entr_ang,entr_mass,restart,b_start,l,scale,entr_height,label4
    height = window.winfo_height()
    width = window.winfo_width()
    canv = tk.Canvas(window, height=height * 13 / 16, width=width, background='#9ACEEB')  # creates canvas
    canv.bind('<Button-1>', left)
    canv.bind('<ButtonRelease-1>', left_up)
    canv.bind('<B1-Motion>', move)  # on actions with the left mouse button, functions are executed
    canv.place(x=0, y=0)

    fr = tk.Frame(window, height=height * 3 / 16, width=width)
    fr.place(x=0, y=height * 13 / 16 + 2)

    label1 = tk.Label(fr, text='Wind')
    label1.grid(column=0, row=0)

    label2 = tk.Label(fr, text='Angle')
    label2.grid(column=1, row=0)

    label3 = tk.Label(fr, text='Mass')
    label3.grid(column=0, row=2)

    label4 = tk.Label(fr, text='Height')
    label4.grid(column=1, row=2)
    
    label5 = tk.Label(fr, text='y')
    label5.grid(column=3, row=0,sticky='N')

    label6 = tk.Label(fr, text='x')
    label6.grid(column=4, row=0,sticky='N')

    label7 = tk.Label(fr)
    label7.grid(column=0, row=4)

    entr_wind = tk.Entry(fr)
    entr_wind.insert(0,'0')
    entr_wind.grid(column=0, row=1, padx=2, pady=2)

    entr_ang = tk.Entry(fr)
    entr_ang.insert(0, '0')
    entr_ang.grid(column=1, row=1, padx=2, pady=2)

    entr_mass = tk.Entry(fr)
    entr_mass.insert(0, '1')
    entr_mass.grid(column=0, row=3, padx=2, pady=2)

    entr_height = tk.Entry(fr)
    entr_height.insert(0, '100')
    entr_height.grid(column=1, row=3, padx=2, pady=2)

    entr_y = tk.Entry(fr)
    entr_y.insert(0, '0')
    entr_y.grid(column=3, row=1, padx=2, pady=2)

    entr_x = tk.Entry(fr)
    entr_x.insert(0, '0')
    entr_x.grid(column=4, row=1, padx=2, pady=2)

    entr_ang.bind("<FocusIn>",temp_text)
    entr_mass.bind("<FocusIn>", temp_text)
    entr_wind.bind("<FocusIn>", temp_text)
    entr_height.bind("<FocusIn>", temp_text)

    entr_ang.bind("<FocusOut>",is_text)
    entr_mass.bind("<FocusOut>", is_text)
    entr_wind.bind("<FocusOut>", is_text)
    entr_height.bind("<FocusOut>", is_text)

    restart = tk.Button(fr, command=stop, text='Reset', height=2, width=8)
    restart.grid(column=2, row=1, padx=2, pady=2)

    b_start = tk.Button(fr, command=start, text='Start', height=2, width=8)
    b_start.grid(column=2, row=3, padx=2, pady=2)

    window.bind('<Return>',button_click)
    window.bind('<Escape>',button_click)

    height = round(height*13/16)
    #print(width,height)
def left(event):#creates a ball
    global x1,y1,circle
    if stp:
        x1=event.x
        y1=event.y
        canv.delete("all")#clears canvas
        circle = canv.create_oval(x1+5, y1+5, x1-5, y1-5,fill='#000000')
        try:l=float(entr_height.get())
        except:l=100
        scale = height / l
        entr_y.delete(0,'end')
        entr_x.delete(0, 'end')
        entr_y.insert(0,round(y1/scale,2))
        entr_x.insert(0,round(x1/scale,2))
        label7.configure(text=f'{round(5/scale,3)}')
    #print(event.x,event.y)

def move(event):#draws a line
    global line,length
    if stp:
        try :canv.delete(line)
        except: pass
        length=sqrt((x1-event.x)**2+(y1-event.y)**2)
        line=canv.create_line(x1,y1,event.x,event.y,width=3,arrow=tk.LAST,arrowshape=(sqrt(10+length*10/25),sqrt(10+length*20/25),sqrt(10+length*7/25)))

def left_up(event):#draws final line
    global x2, y2,line,length
    if stp:
        try:canv.delete(line)
        except:pass
        x2=event.x
        y2=event.y
        length=sqrt((x1-x2)**2+(y1-y2)**2)
        line=canv.create_line(x1,y1,x2,y2,width=3,arrow=tk.LAST,arrowshape=(sqrt(10+length*10/25),sqrt(10+length*20/25),sqrt(10+length*7/25)))

def stop():# reset function
    global stp,x1,x2,y1,y2,canvas,line,circle
    stp=True
    canv.delete('all')
    line=canv.create_line(x1,y1,x2,y2,width=3,arrow=tk.LAST,arrowshape=(sqrt(10+length*10/25),sqrt(10+length*20/25),sqrt(10+length*7/25)))
    circle = canv.create_oval(x1 + 5, y1 + 5, x1 - 5, y1 - 5, fill='#000000')
def start():
    global line,circle,x,y,x0,y0,f,t,vx,vy,vx0,vy0,m,windx,windy,y_count,y_count1,x_count,k,fx,stp,height,width,scale,entr_height,tf
    if x1 is not None and stp:
        try :wind_magn=float(entr_wind.get())
        except:wind_magn=0
        try :wind_ang=float(entr_ang.get())
        except:wind_ang=0
        try:m=float(entr_mass.get())
        except:m=1
        try:l=float(entr_height.get())
        except:l=100
        scale = height / l
        stp = False
        tf=True
        y_count=0
        y_count1=0
        k = 0.47 * 1.275 * 3.14 * (0.5 ** 2)  # air resistance coefficient
        f=9.8*m#mg
        x=x0=x1
        y=y0=y1
        windx=cos(radians(-wind_ang))*wind_magn
        windy=sin(radians(wind_ang+180))*wind_magn
        if abs(windx)<0.01:windx=0
        if abs(windy)<0.01:windy=0
        v=2*length/(0.1*scale)
        try: vx=vx0=v*(x2-x1)/(length*2)#calculates x and y velocity
        except: vx0=0
        try: vy=vy0=v*(y2-y1)/(length*2)
        except: vy0=0
        if length<=5: vx=vy=vx0=vy0=0
        t = tick / (1000)#tick in seconds

        vx=(vx0-windx)/(e**(k*t/m))+windx#calculates x and y velocity after tick
        vx0=vx

        vy = (k * vy0-k*windy - f) / (k * e ** (k * t / m)) + f / k + windy
        vy0 = vy

        x+=vx*scale*tick/1000#calculates coordinates of the ball
        y+=vy*scale*tick/1000

        entr_y.delete(0,'end')
        entr_x.delete(0, 'end')
        entr_y.insert(0,round(y/scale,2))
        entr_x.insert(0,round(x/scale,2))

        canv.delete('all')
        circle = canv.create_oval(x + 5, y + 5, x - 5, y - 5, fill='#000000')#draws new circle
        window.after(tick, my_mainloop)

def my_mainloop():
    global line,circle,x,y,x0,y0,f,t,vx,vy,vx0,vy0,m,windx,windy,y_count,x_count,tf,k,fx,stp,height,width,y_count1,tf
    if tf:#modulates wall touch
        if y<=5 or y>=height-5:
            if y<=5:y=5
            else:y=height-5
            vy0=-vy*(1-loss)
    if x <= 5 or x >= width-5:
        if x<=5: x=5
        else: x=width-5
        vx0=-vx*(1-loss)

    vx=(vx0-windx)/(e**(k*t/m))+windx # calculates x and y velocity after tick
    vx0 = vx

    vy = (k * vy0-k*windy - f) / (k * e ** (k * t / m)) + f / k + windy
    vy0 = vy

    if y_count!= 4 and y_count1!= 4 :
        y +=vy*scale*tick/(1000)#y
        if y<=5.1: y_count+=1
        elif y >= height-5.1:
            y_count1 += 1
            y_count=0
        else:
            y_count1=0
            y_count = 0
    elif tf:#if the ball remains near the wall for 4 ticks, y coordinate stops changing
        tf=False
        if y_count==4: y=5
        else:y=height-5
    #y += vy * scale * tick / (1000)  # y
    x +=vx*scale*tick/1000#x
    #print(vx,vy)
    canv.delete('all')
    circle = canv.create_oval(x + 5, y+5, x - 5, y-5, fill='#000000')

    entr_y.delete(0, 'end')
    entr_x.delete(0, 'end')
    entr_y.insert(0, round(y / scale, 2))
    entr_x.insert(0, round(x / scale, 2))

    if not stp: window.after(tick, my_mainloop)#stops the program
    else:
        stop()

stp=True
x1=None
y1=None
x2=None
y2=None

l=10
loss=0.4#loss of speed when hitting a wall
e=exp(1)#exponenta
tick=30#update time
x_count=2
y_count=0
y_count1=0
tf=True

window=tk.Tk() #Window creation
height=window.winfo_screenheight()#height and width of user's screen
width=window.winfo_screenwidth()
window.state('zoomed')#makes window zoomed

window.after(30, creation)
window.mainloop()
