import tkinter as tk
from math import *
import time


def refr_coor(x,y):
    global scale
    entr_y.configure(state='normal')
    entr_x.configure(state='normal')
    entr_y.delete(0, 'end')
    entr_x.delete(0, 'end')
    entr_y.insert(0, round(y / scale, 2))
    entr_x.insert(0, round(x / scale, 2))
    entr_y.configure(state='disabled')
    entr_x.configure(state='disabled')

def refr_vel(vx,vy):
    global scale
    entr_vy.configure(state='normal')
    entr_vx.configure(state='normal')
    entr_vy.delete(0, 'end')
    entr_vx.delete(0, 'end')
    entr_vy.insert(0, round(vy / scale, 2))
    entr_vx.insert(0, round(vx / scale, 2))
    entr_vy.configure(state='disabled')
    entr_vx.configure(state='disabled')
def button_click(event):
    if event.keysym == 'Return':
        b_start.invoke()
    elif event.keysym == 'Escape':
        restart.invoke()
    print(window.focus_get())


def temp_text(event):
    global prev_text
    prev_text = event.widget.get()
    event.widget.delete(0, "end")


def is_text(event):
    global circle,x1,y1,r,canv,circle,x2,y2,scale
    if event.widget.get() == '':
        event.widget.delete(0, "end")
        event.widget.insert(0, prev_text)
    else:
        try:
            artf = float(event.widget.get())
        except:
            event.widget.delete(0, "end")
            event.widget.insert(0, prev_text)
        else:
            if event.widget == entr_height: circl()
    x1n=x1
    y1n=y1
    if x1+r>width:
        x1n=width-r-1
    if x1-r<0:
        x1n=r+1
    if y1+r>height:
        y1n=height-r-1
    if y1-r<0:
        y1n=r+1
    x2+=x1n-x1
    y2 += y1n - y1
    x1=x1n
    y1=y1n
    canv.delete("all")  # clears canvas
    circle = canv.create_oval(x1 + r, y1 + r, x1 - r, y1 - r, fill='#000000')
    if length != 0: line = canv.create_line(x1, y1, x2, y2, width=3, arrow=tk.LAST, arrowshape=(sqrt(10 + 10 / 25), sqrt(10 + length * 20 / 25), sqrt(10 + length * 7 / 25)), fill='#e31212')
    try:
        l = float(entr_height.get())
    except:
        l = 100
    scale = height / l
    refr_coor(x1,y1)
    time.sleep(0.1)

def creation():
    global line, circle, x, y, x0, y0, f, t, vx, vy, vx0, vy0, m, windx, windy, y_count, label7, label_adt, r_art, h_art, entr_radius, r_real,entr_vx,entr_vy, r, x_count, k, fx, stp, height, entr_y, entr_x, width, canv, fr, label1, label2, label3, label5, entr_wind, entr_ang, entr_mass, restart, b_start, l, scale, entr_height, label4

    r_art = tk.StringVar(value='0.5')
    r_art.trace('w', circl)

    h_art = tk.StringVar(value='10')
    h_art.trace('w', circl)

    height = window.winfo_height()
    width = window.winfo_width()
    canv = tk.Canvas(window, height=height * 13 / 16, width=width, background='#9ACEEB')  # creates canvas
    canv.bind('<Button-1>', left)
    canv.bind('<ButtonRelease-1>', left_up)
    canv.bind('<B1-Motion>', move)  # on actions with the left mouse button, functions are executed
    canv.place(x=0, y=0)

    fr = tk.Frame(window, height=height * 3 / 16, width=width)
    fr.place(x=0, y=height * 13 / 16 + 2)

    label_adt = tk.Label(fr, text='4567')
    label_adt.place(x=-1000, y=-1000)

    label1 = tk.Label(fr, text='Wind')
    label1.grid(column=0, row=0)

    label2 = tk.Label(fr, text='Angle')
    label2.grid(column=1, row=0)

    label3 = tk.Label(fr, text='Mass')
    label3.grid(column=0, row=2)

    label4 = tk.Label(fr, text='Height')
    label4.grid(column=1, row=2)

    label5 = tk.Label(fr, text='y')
    label5.grid(column=4, row=0)

    label6 = tk.Label(fr, text='x')
    label6.grid(column=5, row=0)

    label7 = tk.Label(fr, text='radius')
    label7.grid(column=2, row=2)

    label8 = tk.Label(fr, text='vy')
    label8.grid(column=4, row=2)

    label8 = tk.Label(fr, text='vx')
    label8.grid(column=5, row=2)

    entr_wind = tk.Entry(fr)
    entr_wind.insert(0, '0')
    entr_wind.grid(column=0, row=1, padx=2, pady=2)

    entr_ang = tk.Entry(fr)
    entr_ang.insert(0, '0')
    entr_ang.grid(column=1, row=1, padx=2, pady=2)

    entr_mass = tk.Entry(fr)
    entr_mass.insert(0, '1')
    entr_mass.grid(column=0, row=3, padx=2, pady=2)

    entr_height = tk.Entry(fr, textvariable=h_art)
    entr_height.grid(column=1, row=3, padx=2, pady=2)

    entr_y = tk.Entry(fr,state='disabled')
    entr_y.insert(0, '0')
    entr_y.grid(column=4, row=1, padx=2, pady=2)

    entr_x = tk.Entry(fr,state='disabled')
    entr_x.insert(0, '0')
    entr_x.grid(column=5, row=1, padx=2, pady=2)

    entr_vy = tk.Entry(fr,state='disabled')
    entr_vy.insert(0, '0')
    entr_vy.grid(column=4, row=3, padx=2, pady=2)

    entr_vx = tk.Entry(fr,state='disabled')
    entr_vx.insert(0, '0')
    entr_vx.grid(column=5, row=3, padx=2, pady=2)

    entr_radius = tk.Entry(fr, textvariable=r_art)
    entr_radius.grid(column=2, row=3, padx=2, pady=2)

    entr_ang.bind("<FocusIn>", temp_text)
    entr_mass.bind("<FocusIn>", temp_text)
    entr_wind.bind("<FocusIn>", temp_text)
    entr_height.bind("<FocusIn>", temp_text)
    entr_y.bind("<FocusIn>", temp_text)
    entr_x.bind("<FocusIn>", temp_text)
    entr_radius.bind("<FocusIn>", temp_text)

    entr_ang.bind("<FocusOut>", is_text)
    entr_mass.bind("<FocusOut>", is_text)
    entr_wind.bind("<FocusOut>", is_text)
    entr_height.bind("<FocusOut>", is_text)
    entr_y.bind("<FocusOut>", is_text)
    entr_x.bind("<FocusOut>", is_text)
    entr_radius.bind("<FocusOut>", is_text)

    window.bind('<Return>', is_focused)
    window.bind('<Escape>', is_focused)

    restart = tk.Button(fr, command=stop, text='Reset', height=2, width=8)
    restart.grid(column=3, row=1, padx=2, pady=2)

    b_start = tk.Button(fr, command=start, text='Start', height=2, width=8)
    b_start.grid(column=3, row=3, padx=2, pady=2)

    height = round(height * 13 / 16)

    # print(width,height)


def left(event):  # creates a ball
    global x1, y1, circle, r, r_real,entr_x,entr_y,scale
    if stp:
        try:
            r_real = float(entr_radius.get())
        except:
            r_real = 0.5
        try:
            l = float(entr_height.get())
        except:
            l = 100
        scale = height / l
        r = ceil(r_real * scale)
        if r < 2: r = 4
        x1 = event.x
        y1 = event.y
        canv.delete("all")  # clears canvas
        circle = canv.create_oval(x1 + r, y1 + r, x1 - r, y1 - r, fill='#000000')
        try:
            l = float(entr_height.get())
        except:
            l = 100
        scale = height / l
        refr_coor(x1, y1)
    # print(event.x,event.y)


def move(event):  # draws a line
    global line, length,x2,y2,x1,y1
    if stp:
        try:
            canv.delete(line)
        except:
            x2 = x1
            y2 = x2
        length = sqrt((x1 - event.x) ** 2 + (y1 - event.y) ** 2)
        line = canv.create_line(x1, y1, event.x, event.y, width=3, arrow=tk.LAST, arrowshape=(sqrt(10 + length * 10 / 25), sqrt(10 + length * 20 / 25), sqrt(10 + length * 7 / 25)),fill='#e31212')


def left_up(event):  # draws final line
    global x2, y2, line, length,x1,y1
    if stp:
        try:
            canv.delete(line)
        except:
            pass
        x2 = event.x
        y2 = event.y
        try:
            length = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        except:
            x2=x1
            y2=x2
        line = canv.create_line(x1, y1, x2, y2, width=3, arrow=tk.LAST, arrowshape=(sqrt(10 + length * 10 / 25), sqrt(10 + length * 20 / 25), sqrt(10 + length * 7 / 25)),fill='#e31212')


def stop():  # reset function
    global stp, x1, x2, y1, y2, canvas, line, circle,scale
    stp = True
    canv.delete('all')
    circle = canv.create_oval(x1 + r, y1 + r, x1 - r, y1 - r, fill='#000000')
    if length != 0: line = canv.create_line(x1, y1, x2, y2, width=3, arrow=tk.LAST, arrowshape=(sqrt(10 + 10 / 25), sqrt(10 + length * 20 / 25), sqrt(10 + length * 7 / 25)),fill='#e31212')
    refr_coor(x1, y1)
    v = 2 * length / (0.1 * scale)
    try:
        vx = vx0 = v * (x2 - x1) / (length * 2)  # calculates x and y velocity
    except:
        vx0 = 0
    try:
        vy = vy0 = v * (y2 - y1) / (length * 2)
    except:
        vy0 = 0
    refr_vel(abs(vx), vy)

def start():
    global line, circle, x, y, x0, y0, f, t, vx, vy, vx0, vy0, m, windx, windy, y_count, y_count1, x_count, k, fx, stp, height, width, scale, entr_height, tf, l,x1,y1,x2,y2
    if x1 is not None and stp:
        x1n = x1
        y1n = y1
        if x1 + r > width:
            x1n = width - r - 1
        if x1 - r < 0:
            x1n = r + 1
        if y1 + r > height:
            y1n = height - r - 1
        if y1 - r < 0:
            y1n = r + 1
        x2 += x1n - x1
        y2 += y1n - y1
        x1 = x1n
        y1 = y1n
        canv.delete("all")  # clears canvas
        circle = canv.create_oval(x1 + r, y1 + r, x1 - r, y1 - r, fill='#000000')

        try:
            l = float(entr_height.get())
        except:
            l = 100
        refr_coor(x1, y1)
        time.sleep(0.1)
        try:
            wind_magn = float(entr_wind.get())
        except:
            wind_magn = 0
        try:
            wind_ang = float(entr_ang.get())
        except:
            wind_ang = 0
        try:
            m = float(entr_mass.get())
        except:
            m = 1
        try:
            l = float(entr_height.get())
        except:
            l = 100
        scale = height / l
        stp = False
        tf = True
        y_count = 0
        y_count1 = 0
        k = 0.47 * 1.275 * 3.14 * (r_real ** 2)  # air resistance coefficient
        f = 9.8 * m  # mg
        x = x0 = x1
        y = y0 = y1
        windx = cos(radians(-wind_ang)) * wind_magn
        windy = sin(radians(wind_ang + 180)) * wind_magn
        if abs(windx) < 0.01: windx = 0
        if abs(windy) < 0.01: windy = 0
        v = 2 * length / (0.1 * scale)
        try:
            vx = vx0 = v * (x2 - x1) / (length * 2)  # calculates x and y velocity
        except:
            vx0 = 0
        try:
            vy = vy0 = v * (y2 - y1) / (length * 2)
        except:
            vy0 = 0
        if length <= 3: vx = vy = vx0 = vy0 = 0
        t = tick / (1000)  # tick in seconds

        vx = (vx0 - windx) / (e ** (k * t / m)) + windx  # calculates x and y velocity after tick
        vx0 = vx

        vy = (k * vy0 - k * windy - f) / (k * e ** (k * t / m)) + f / k + windy
        vy0 = vy

        x += vx * scale * tick / 1000  # calculates coordinates of the ball
        y += vy * scale * tick / 1000

        refr_vel(abs(vx), vy)

        refr_coor(x, y)

        canv.delete('all')
        circle = canv.create_oval(x + r, y + r, x - r, y - r, fill='#000000')  # draws new circle
        window.after(tick, my_mainloop)


def my_mainloop():
    global line, circle, x, y, x0, y0, f, t, vx, vy, vx0, vy0, m, windx, windy, y_count, x_count, tf, k, fx, stp, height, width, y_count1, tf
    if tf:  # modulates wall touch
        if y <= r or y >= height - r:
            if y <= r:
                y = r
            else:
                y = height - r
            vy0 = -vy * (1 - loss)
    if x <= r or x >= width - r:
        if x <= r:
            x = r
        else:
            x = width - r
        vx0 = -vx * (1 - loss)

    vx = (vx0 - windx) / (e ** (k * t / m)) + windx  # calculates x and y velocity after tick
    vx0 = vx

    if y_count != 4 and y_count1 != 4:
        vy = (k * vy0 - k * windy - f) / (k * e ** (k * t / m)) + f / k + windy
        vy0 = vy
        y += vy * scale * tick / (1000)  # y
        if y <= r + 0.1:
            y_count += 1
        elif y >= height - r - 0.1:
            y_count1 += 1
            y_count = 0
        else:
            y_count1 = 0
            y_count = 0
    elif tf:  # if the ball remains near the wall for 4 ticks, y coordinate stops changing
        tf = False
        vy=0
        if y_count == 4:
            y = r
        else:
            y = height - r
    x += vx * scale * tick / 1000  # x
    canv.delete('all')
    circle = canv.create_oval(x + r, y + r, x - r, y - r, fill='#000000')

    refr_vel(abs(vx), vy)

    refr_coor(x, y)

    if not stp:
        window.after(tick, my_mainloop)  # stops the program
    else:
        stop()


def circl(*args):
    global circle, r, r_real, l,line
    try:
        try:
            r_real = float(entr_radius.get())
        except:
            r_real = 0.5
        try:
            l = float(entr_height.get())
        except:
            l = 100
        scale = height / l
        r = ceil(r_real * scale)
        if r < 2: r = 4
        if stp: circle = canv.create_oval(x1 + r, y1 + r, x1 - r, y1 - r, fill='#000000')
    except:
        pass
    else:
        if stp:
            canv.delete('all')
            circle = canv.create_oval(x1 + r, y1 + r, x1 - r, y1 - r, fill='#000000')
    if length != 0: line = canv.create_line(x1, y1, x2, y2, width=3, arrow=tk.LAST, arrowshape=(sqrt(10 + 10 / 25), sqrt(10 + length * 20 / 25), sqrt(10 + length * 7 / 25)),fill='#e31212')
    refr_coor(x1, y1)
    v = 2 * length / (0.1 * scale)
    try:
        vx = vx0 = v * (x2 - x1) / (length * 2)  # calculates x and y velocity
    except:
        vx0 = 0
    try:
        vy = vy0 = v * (y2 - y1) / (length * 2)
    except:
        vy0 = 0
    refr_vel(abs(vx), vy)


def is_focused(event):
    if window.focus_get()._w == '.':
        button_click(event)
    else:
        window.focus_set()


stp = True
x1 = None
y1 = None
x2 = None
y2 = None

l = 10
loss = 0.3  # loss of speed when hitting a wall
e = exp(1)  # exponenta
tick = 30  # update time
x_count = 2
y_count = 0
y_count1 = 0
tf = True

window = tk.Tk()  # Window creation
height = window.winfo_screenheight()  # height and width of user's screen
width = window.winfo_screenwidth()
window.state('zoomed')  # makes window zoomed

window.after(30, creation)
window.mainloop()

