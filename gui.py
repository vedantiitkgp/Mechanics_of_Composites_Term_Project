import tkinter as tk
from tkinter.font import Font,NORMAL
from main import *
root = tk.Tk()

root.title("Term Project")
frame0 = tk.Frame(master =root)
frame0.pack()

frame1 = tk.Frame(master=frame0,width = 150,height = 300,relief=tk.RAISED,bd=3)
frame1.columnconfigure([0,1,2], weight=1, minsize=100)
frame1.rowconfigure([0,1,2,3,4,5,6,7,8,9], weight=1, minsize=50)

lbl_E1_fibre = tk.Label(master=frame1,text='E1-Fibre =',font="Helvetica 25 bold")
lbl_E1_fibre.grid(row=0,column=0,padx = 2,pady=2)
ent_E1_fibre = tk.Entry(master=frame1,width=10,font = "Helvetica 20 bold")
ent_E1_fibre.grid(row=0,column=1,pady=2,ipady=5)
lbl_E1_fibre_unit = tk.Label(master=frame1,text='GPa',font="Helvetica 20 bold")
lbl_E1_fibre_unit.grid(row=0,column=2)

lbl_E2_fibre = tk.Label(master=frame1,text='E2-Fibre =',font="Helvetica 25 bold")
lbl_E2_fibre.grid(row=1,column=0,padx = 2,pady=2)
ent_E2_fibre = tk.Entry(master=frame1,width=10,font = "Helvetica 20 bold")
ent_E2_fibre.grid(row=1,column=1,padx = 2,pady=2,ipady=5)
lbl_E2_fibre_unit = tk.Label(master=frame1,text='GPa',font="Helvetica 20 bold")
lbl_E2_fibre_unit.grid(row=1,column=2)

lbl_nu12_fibre = tk.Label(master=frame1,text='nu12-Fibre =',font="Helvetica 25 bold")
lbl_nu12_fibre.grid(row=2,column=0,padx = 2,pady=2)
ent_nu12_fibre = tk.Entry(master=frame1,width=10,font = "Helvetica 20 bold")
ent_nu12_fibre.grid(row=2,column=1,padx = 2,pady=2,ipady=5)

lbl_nu23_fibre = tk.Label(master=frame1,text='nu23-Fibre =',font="Helvetica 25 bold")
lbl_nu23_fibre.grid(row=3,column=0,padx = 2,pady=2)
ent_nu23_fibre = tk.Entry(master=frame1,width=10,font = "Helvetica 20 bold")
ent_nu23_fibre.grid(row=3,column=1,padx = 2,pady=2,ipady=5)

lbl_G12_fibre = tk.Label(master=frame1,text='G12-Fibre =',font="Helvetica 25 bold")
lbl_G12_fibre.grid(row=4,column=0,padx = 2,pady=2)
ent_G12_fibre = tk.Entry(master=frame1,width=10,font = "Helvetica 20 bold")
ent_G12_fibre.grid(row=4,column=1,padx = 2,pady=2,ipady=5)
lbl_G12_fibre_unit = tk.Label(master=frame1,text='GPa',font="Helvetica 20 bold")
lbl_G12_fibre_unit.grid(row=4,column=2)

lbl_G23_fibre = tk.Label(master=frame1,text='G23-Fibre =',font="Helvetica 25 bold")
lbl_G23_fibre.grid(row=5,column=0,padx = 2,pady=2)
ent_G23_fibre = tk.Entry(master=frame1,width=10,font = "Helvetica 20 bold")
ent_G23_fibre.grid(row=5,column=1,padx = 2,pady=2,ipady=5)
lbl_G23_fibre_unit = tk.Label(master=frame1,text='GPa',font="Helvetica 20 bold")
lbl_G23_fibre_unit.grid(row=5,column=2)

lbl_E_matrix = tk.Label(master=frame1,text='E-Matrix =',font="Helvetica 25 bold")
lbl_E_matrix.grid(row=6,column=0,padx = 2,pady=2)
ent_E_matrix = tk.Entry(master=frame1,width=10,font = "Helvetica 20 bold")
ent_E_matrix.grid(row=6,column=1,padx = 2,pady=2,ipady=5)
lbl_E_matrix_unit = tk.Label(master=frame1,text='GPa',font="Helvetica 20 bold")
lbl_E_matrix_unit.grid(row=6,column=2)

lbl_nu_matrix = tk.Label(master=frame1,text='nu-Matrix =',font="Helvetica 25 bold")
lbl_nu_matrix.grid(row=7,column=0,padx = 2,pady=2)
ent_nu_matrix = tk.Entry(master=frame1,width=10,font = "Helvetica 20 bold")
ent_nu_matrix.grid(row=7,column=1,padx = 2,pady=2,ipady=5)

lbl_G_matrix = tk.Label(master=frame1,text='G-Matrix =',font="Helvetica 25 bold")
lbl_G_matrix.grid(row=8,column=0,padx = 2,pady=2)
ent_G_matrix = tk.Entry(master=frame1,width=10,font = "Helvetica 20 bold")
ent_G_matrix.grid(row=8,column=1,padx = 2,pady=2,ipady=5)
lbl_G_matrix_unit = tk.Label(master=frame1,text='GPa',font="Helvetica 20 bold")
lbl_G_matrix_unit.grid(row=8,column=2)

lbl_Volume_fraction = tk.Label(master=frame1,text='Volume fraction =',font="Helvetica 25 bold")
lbl_Volume_fraction.grid(row=9,column=0,padx = 2,pady=5)
ent_Volume_fraction = tk.Entry(master=frame1,width=10,font = "Helvetica 20 bold")
ent_Volume_fraction.grid(row=9,column=1,padx = 2,pady=5,ipady=5)

frame1.pack(side=tk.LEFT,fill=tk.BOTH)

frame2 = tk.Frame(master=frame0,width = 150,height = 300,relief=tk.RIDGE,bd=5)
frame2.columnconfigure([0,1,2], weight=1, minsize=150)
frame2.rowconfigure([0,1,2,3,4,5,6,7,8], weight=1, minsize=50)

lbl_E1 = tk.Label(master=frame2,text='E1 =',font="Helvetica 25 bold")
lbl_E1.grid(row=0,column=0,padx = 2,pady=2)
lbl_E1_value= tk.Label(master=frame2,width=10,text=" ",bg="black",font = "Helvetica 20 bold")
lbl_E1_value.grid(row=0,column=1,pady=2,ipady=2)
lbl_E1_unit = tk.Label(master=frame2,text='GPa',font="Helvetica 20 bold")
lbl_E1_unit.grid(row=0,column=2)

lbl_E2 = tk.Label(master=frame2,text='E2 =',font="Helvetica 25 bold")
lbl_E2.grid(row=1,column=0,padx = 2,pady=2)
lbl_E2_value= tk.Label(master=frame2,width=10,text=" ",bg="black",font = "Helvetica 20 bold")
lbl_E2_value.grid(row=1,column=1,pady=2,ipady=2)
lbl_E2_unit = tk.Label(master=frame2,text='GPa',font="Helvetica 20 bold")
lbl_E2_unit.grid(row=1,column=2)

lbl_E3 = tk.Label(master=frame2,text='E3 =',font="Helvetica 25 bold")
lbl_E3.grid(row=2,column=0,padx = 2,pady=2)
lbl_E3_value= tk.Label(master=frame2,width=10,text=" ",bg="black",font = "Helvetica 20 bold")
lbl_E3_value.grid(row=2,column=1,pady=2,ipady=2)
lbl_E3_unit = tk.Label(master=frame2,text='GPa',font="Helvetica 20 bold")
lbl_E3_unit.grid(row=2,column=2)

lbl_nu12 = tk.Label(master=frame2,text='nu12 =',font="Helvetica 25 bold")
lbl_nu12.grid(row=3,column=0,padx = 2,pady=2)
lbl_nu12_value= tk.Label(master=frame2,width=10,text=" ",bg="black",font = "Helvetica 20 bold")
lbl_nu12_value.grid(row=3,column=1,pady=2,ipady=2)
lbl_nu12_unit = tk.Label(master=frame2,text='',font="Helvetica 20 bold")
lbl_nu12_unit.grid(row=3,column=2)

lbl_nu13 = tk.Label(master=frame2,text='nu13 =',font="Helvetica 25 bold")
lbl_nu13.grid(row=4,column=0,padx = 2,pady=2)
lbl_nu13_value= tk.Label(master=frame2,width=10,text=" ",bg="black",font = "Helvetica 20 bold")
lbl_nu13_value.grid(row=4,column=1,pady=2,ipady=2)
lbl_nu13_unit = tk.Label(master=frame2,text='',font="Helvetica 20 bold")
lbl_nu13_unit.grid(row=4,column=2)

lbl_nu23 = tk.Label(master=frame2,text='nu23 =',font="Helvetica 25 bold")
lbl_nu23.grid(row=5,column=0,padx = 2,pady=2)
lbl_nu23_value= tk.Label(master=frame2,width=10,text=" ",bg="black",font = "Helvetica 20 bold")
lbl_nu23_value.grid(row=5,column=1,pady=2,ipady=2)
lbl_nu23_unit = tk.Label(master=frame2,text='',font="Helvetica 20 bold")
lbl_nu23_unit.grid(row=5,column=2)

lbl_G12 = tk.Label(master=frame2,text='G12 =',font="Helvetica 25 bold")
lbl_G12.grid(row=6,column=0,padx = 2,pady=2)
lbl_G12_value= tk.Label(master=frame2,width=10,text=" ",bg="black",font = "Helvetica 20 bold")
lbl_G12_value.grid(row=6,column=1,pady=2,ipady=2)
lbl_G12_unit = tk.Label(master=frame2,text='GPa',font="Helvetica 20 bold")
lbl_G12_unit.grid(row=6,column=2)

lbl_G13 = tk.Label(master=frame2,text='G13 =',font="Helvetica 25 bold")
lbl_G13.grid(row=7,column=0,padx = 2,pady=2)
lbl_G13_value= tk.Label(master=frame2,width=10,text=" ",bg="black",font = "Helvetica 20 bold")
lbl_G13_value.grid(row=7,column=1,pady=2,ipady=2)
lbl_G13_unit = tk.Label(master=frame2,text='GPa',font="Helvetica 20 bold")
lbl_G13_unit.grid(row=7,column=2)

lbl_G23 = tk.Label(master=frame2,text='G23 =',font="Helvetica 25 bold")
lbl_G23.grid(row=8,column=0,padx = 2,pady=5)
lbl_G23_value= tk.Label(master=frame2,width=10,text=" ",bg="black",font = "Helvetica 20 bold")
lbl_G23_value.grid(row=8,column=1,pady=5,ipady=2)
lbl_G23_unit = tk.Label(master=frame2,text='GPa',font="Helvetica 20 bold")
lbl_G23_unit.grid(row=8,column=2)

frame2.pack(side=tk.LEFT,fill=tk.BOTH)

frame3 = tk.Frame(master=root,width = 150,height = 70,relief=tk.RAISED,bd=3)

def reset_properties():
    ent_E1_fibre.delete(0, tk.END)
    ent_E2_fibre.delete(0, tk.END)
    ent_nu12_fibre.delete(0, tk.END)
    ent_nu23_fibre.delete(0, tk.END)
    ent_G12_fibre.delete(0, tk.END)
    ent_G23_fibre.delete(0, tk.END)
    ent_E_matrix.delete(0, tk.END)
    ent_nu_matrix.delete(0, tk.END)
    ent_G_matrix.delete(0, tk.END)
    ent_Volume_fraction.delete(0, tk.END)
    lbl_E1_value['bg'] = "black"
    lbl_E2_value['bg'] = "black"
    lbl_E3_value['bg'] = "black"
    lbl_nu12_value['bg'] = "black"
    lbl_nu13_value['bg'] = "black"
    lbl_nu23_value['bg'] = "black"
    lbl_G12_value['bg'] = "black"
    lbl_G13_value['bg'] = "black"
    lbl_G23_value['bg'] = "black"

reset = tk.Button(frame3, text ="Reset",height=2,width=10,font="Times 18 bold",bg="black",fg="white",command=reset_properties)
reset.place(x=50,y=0)

def calculate_lamina():
    E1_fibre = float(ent_E1_fibre.get())
    E2_fibre = float(ent_E2_fibre.get())
    nu12_fibre = float(ent_nu12_fibre.get())
    nu23_fibre = float(ent_nu23_fibre.get())
    G12_fibre = float(ent_G12_fibre.get())
    G23_fibre = float(ent_G23_fibre.get())
    E_matrix = float(ent_E_matrix.get())
    nu_matrix = float(ent_nu_matrix.get())
    G_matrix = float(ent_G_matrix.get())
    Volume_fraction = float(ent_Volume_fraction.get())
    E1,E2,E3,nu12,nu13,nu23,G12,G13,G23 = effective_lamina_properties(E1_fibre,E2_fibre,nu12_fibre,nu23_fibre,G12_fibre,G23_fibre,E_matrix,nu_matrix,G_matrix,Volume_fraction)
    lbl_E1_value['text'] = f"{E1}"
    lbl_E1_value['bg'] = "white"
    lbl_E2_value['text'] = f"{E2}"
    lbl_E2_value['bg'] = "white"
    lbl_E3_value['text'] = f"{E3}"
    lbl_E3_value['bg'] = "white"
    lbl_nu12_value['text'] = f"{nu12}"
    lbl_nu12_value['bg'] = "white"
    lbl_nu13_value['text'] = f"{nu13}"
    lbl_nu13_value['bg'] = "white"
    lbl_nu23_value['text'] = f"{nu23}"
    lbl_nu23_value['bg'] = "white"
    lbl_G12_value['text'] = f"{G12}"
    lbl_G12_value['bg'] = "white"
    lbl_G13_value['text'] = f"{G13}"
    lbl_G13_value['bg'] = "white"
    lbl_G23_value['text'] = f"{G23}"
    lbl_G23_value['bg'] = "white"

calculate = tk.Button(frame3, text ="Calculate",height=2,width=10,font="Times 18 bold",bg="black",fg="white",command=calculate_lamina)
calculate.place(x=450,y=0)

next_ = tk.Button(frame3, text ="Next",height=2,width=10,font="Times 18 bold",bg="black",fg="white")
next_.place(x=800,y=0)

frame3.pack(fill=tk.BOTH)
root.mainloop()