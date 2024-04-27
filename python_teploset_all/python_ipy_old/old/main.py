import tkinter.ttk
from tkinter import *
from PIL import ImageTk, Image
import datetime, threading
from time import sleep


def main_page():
    q = Tk()
    q.resizable(width=False, height=False)
    q.overrideredirect(1)
    width_of_window = 1000
    height_of_window = 600
    screen_width = q.winfo_screenwidth()
    screen_height = q.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width_of_window / 2)
    y_coordinate = (screen_height / 2) - (height_of_window / 2)
    q.geometry('%dx%d+%d+%d' % (width_of_window, height_of_window, x_coordinate, y_coordinate))
    time = datetime.datetime.now().strftime("%d.%m.%Y  %H:%M:%S")
    Frame(q, width=1000, height=600, bg='#343434').place(x=0, y=0)

    label_1 = Label(width=20, height=20, text=time, fg='white', bg='#343434')
    label_1.configure(font=('Calibri', 12))
    label_1.place(x=840, y=390)

    def time_update():
        while True:
            label_1['text'] = datetime.datetime.now().strftime("%d.%m.%Y  %H:%M:%S")
            sleep(0.5)

    # Абоненты
    def a_button(x, y, img1, img2, command_shell):
        image_1 = ImageTk.PhotoImage(Image.open(img1))
        image_2 = ImageTk.PhotoImage(Image.open(img2))

        def enter(e):
            myButton1['image'] = image_1

        def leave(e):
            myButton1['image'] = image_2

        myButton1 = Button(q, image=image_2, command=command_shell, bg='#343434', relief='sunken',
                           activebackground='#343434', bd=0)
        myButton1.bind('<Enter>', enter)
        myButton1.bind('<Leave>', leave)
        myButton1.place(x=x, y=y)

    def a_shell():
        print('Клик абоненты')
        a = Tk()
        a.title('Абоненты')
        a.resizable(width=False, height=False)
        width_of_window = 1000
        height_of_window = 500
        screen_width = a.winfo_screenwidth()
        screen_height = a.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (width_of_window / 2)
        y_coordinate = (screen_height / 2) - (height_of_window / 2)
        a.geometry('%dx%d+%d+%d' % (width_of_window, height_of_window, x_coordinate, y_coordinate))
        Frame(a, width=1000, height=500, bg='#343434').place(x=0, y=0)

        my_tree = tkinter.ttk.Treeview(a)
        my_tree.place(relx=0.01, rely=0.228, x=00, y=0)
        my_tree.configure(
            columns=(
                'ФИО',
                'Улица',
                'Дом',
                'Помещение',
                'Номер договора',
                'Дата заключения',
                'Дата расторжения',
                'Телефон',
                'E-mail',
            )
        )

        my_tree.heading('#0', text='ID', anchor=W)
        my_tree.heading('ФИО', text='ФИО', anchor=W)
        my_tree.heading('Улица', text='Улица', anchor=W)
        my_tree.heading('Дом', text='Дом', anchor=W)
        my_tree.heading('Помещение', text='Помещение', anchor=W)
        my_tree.heading('Номер договора', text='Номер договора', anchor=W)
        my_tree.heading('Дата заключения', text='Дата заключения', anchor=W)
        my_tree.heading('Дата расторжения', text='Дата расторжения', anchor=W)
        my_tree.heading('Телефон', text='Телефон', anchor=W)
        my_tree.heading('E-mail', text='E-mail', anchor=W)

        my_tree.column('#0', stretch=NO,minwidth=25, width=50)
        my_tree.column('#1', stretch=NO,minwidth=25, width=100)
        my_tree.column('#2', stretch=NO,minwidth=25, width=120)
        my_tree.column('#3', stretch=NO,minwidth=25, width=55)
        my_tree.column('#4', stretch=NO,minwidth=25, width=100)
        my_tree.column('#5', stretch=NO,minwidth=25, width=125)
        my_tree.column('#6', stretch=NO,minwidth=25, width=125)
        my_tree.column('#7', stretch=NO,minwidth=25, width=125)
        my_tree.column('#8', stretch=NO,minwidth=25, width=100)
        my_tree.column('#9', stretch=NO,minwidth=25, width=80)

        my_tree.insert(parent='', index='end', text=1, iid=0, values=('Иванов Иван Иванович',
                                                                      'Комсомольская',
                                                                      '30',
                                                                      '-',
                                                                      '204/2022',
                                                                      '05.04.2022',
                                                                      '-',
                                                                      '-',
                                                                      '-',
                                                                      ))

    # Импорт в таблицу
    def i_button(x, y, img1, img2, command_shell):
        image_1 = ImageTk.PhotoImage(Image.open(img1))
        image_2 = ImageTk.PhotoImage(Image.open(img2))

        def enter(e):
            myButton1['image'] = image_1

        def leave(e):
            myButton1['image'] = image_2

        myButton1 = Button(q, image=image_2, command=command_shell, bg='#343434', relief='sunken',
                           activebackground='#343434', bd=0)
        myButton1.bind('<Enter>', enter)
        myButton1.bind('<Leave>', leave)
        myButton1.place(x=x, y=y)

    def i_shell():
        print('Клик импорт таблицы')

    # Реестр
    def r_button(x, y, img1, img2, r_shell):
        image_1 = ImageTk.PhotoImage(Image.open(img1))
        image_2 = ImageTk.PhotoImage(Image.open(img2))

        def enter(e):
            myButton1['image'] = image_1

        def leave(e):
            myButton1['image'] = image_2

        myButton1 = Button(q, image=image_2, command=r_shell, bg='#343434', relief='sunken', activebackground='#343434',
                           bd=0)
        myButton1.bind('<Enter>', enter)
        myButton1.bind('<Leave>', leave)
        myButton1.place(x=x, y=y)

    def r_shell():
        print('Клик реестр')

    # Выход
    def e_button(x, y, img1, img2, e_shell):
        image_1 = ImageTk.PhotoImage(Image.open(img1))
        image_2 = ImageTk.PhotoImage(Image.open(img2))

        def enter(e):
            myButton1['image'] = image_1

        def leave(e):
            myButton1['image'] = image_2

        myButton1 = Button(q, image=image_2, command=e_shell, bg='#343434', relief='sunken', activebackground='#343434',
                           bd=0)
        myButton1.bind('<Enter>', enter)
        myButton1.bind('<Leave>', leave)
        myButton1.place(x=x, y=y)

    def e_shell():
        q.destroy()

    a_button(5, 10, 'layers/buttons/a2.png', 'layers/buttons/a1.png', a_shell)
    i_button(5, 545, 'layers/buttons/i2.png', 'layers/buttons/i1.png', i_shell)
    r_button(5, 70, 'layers/buttons/r2.png', 'layers/buttons/r1.png', r_shell)
    e_button(950, 10, 'layers/buttons/e2.png', 'layers/buttons/e1.png', e_shell)

    thr_timer = threading.Thread(target=time_update)
    thr_timer.start()
    q.mainloop()

main_page()
