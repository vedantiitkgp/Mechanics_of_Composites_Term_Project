import tkinter as tk
from tkinter.font import Font,NORMAL
from main import *
import os
import numpy as np
from tkinter import messagebox as tkMessageBox
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

chamis_var = tk.StringVar(frame1,"False")
R = tk.Radiobutton(frame1, text="Chamis correction", variable=chamis_var, value="True",font="Helvetica 25 bold",indicator = 0,background = "light blue")
R.grid(row=10,column=0,padx = 2,pady=5,ipady=5,columnspan=3)

frame1.pack(side=tk.LEFT,fill=tk.BOTH)

frame2 = tk.Frame(master=frame0,width = 150,height = 300,relief=tk.RIDGE,bd=5)
frame2.columnconfigure([0,1,2], weight=1, minsize=150)
frame2.rowconfigure([0,1,2,3,4,5,6,7,8], weight=1, minsize=50)

lbl_E1 = tk.Label(master=frame2,text='E1 =',font="Helvetica 25 bold")
lbl_E1.grid(row=0,column=0,padx = 2,pady=2)
lbl_E1_value= tk.Label(master=frame2,width=20,text=" ",bg="black",font = "Helvetica 20 bold")
lbl_E1_value.grid(row=0,column=1,pady=2,ipady=2)
lbl_E1_unit = tk.Label(master=frame2,text='GPa',font="Helvetica 20 bold")
lbl_E1_unit.grid(row=0,column=2)

lbl_E2 = tk.Label(master=frame2,text='E2 =',font="Helvetica 25 bold")
lbl_E2.grid(row=1,column=0,padx = 2,pady=2)
lbl_E2_value= tk.Label(master=frame2,width=20,text=" ",bg="black",font = "Helvetica 20 bold")
lbl_E2_value.grid(row=1,column=1,pady=2,ipady=2)
lbl_E2_unit = tk.Label(master=frame2,text='GPa',font="Helvetica 20 bold")
lbl_E2_unit.grid(row=1,column=2)

lbl_E3 = tk.Label(master=frame2,text='E3 =',font="Helvetica 25 bold")
lbl_E3.grid(row=2,column=0,padx = 2,pady=2)
lbl_E3_value= tk.Label(master=frame2,width=20,text=" ",bg="black",font = "Helvetica 20 bold")
lbl_E3_value.grid(row=2,column=1,pady=2,ipady=2)
lbl_E3_unit = tk.Label(master=frame2,text='GPa',font="Helvetica 20 bold")
lbl_E3_unit.grid(row=2,column=2)

lbl_nu12 = tk.Label(master=frame2,text='nu12 =',font="Helvetica 25 bold")
lbl_nu12.grid(row=3,column=0,padx = 2,pady=2)
lbl_nu12_value= tk.Label(master=frame2,width=20,text=" ",bg="black",font = "Helvetica 20 bold")
lbl_nu12_value.grid(row=3,column=1,pady=2,ipady=2)
lbl_nu12_unit = tk.Label(master=frame2,text='',font="Helvetica 20 bold")
lbl_nu12_unit.grid(row=3,column=2)

lbl_nu13 = tk.Label(master=frame2,text='nu13 =',font="Helvetica 25 bold")
lbl_nu13.grid(row=4,column=0,padx = 2,pady=2)
lbl_nu13_value= tk.Label(master=frame2,width=20,text=" ",bg="black",font = "Helvetica 20 bold")
lbl_nu13_value.grid(row=4,column=1,pady=2,ipady=2)
lbl_nu13_unit = tk.Label(master=frame2,text='',font="Helvetica 20 bold")
lbl_nu13_unit.grid(row=4,column=2)

lbl_nu23 = tk.Label(master=frame2,text='nu23 =',font="Helvetica 25 bold")
lbl_nu23.grid(row=5,column=0,padx = 2,pady=2)
lbl_nu23_value= tk.Label(master=frame2,width=20,text=" ",bg="black",font = "Helvetica 20 bold")
lbl_nu23_value.grid(row=5,column=1,pady=2,ipady=2)
lbl_nu23_unit = tk.Label(master=frame2,text='',font="Helvetica 20 bold")
lbl_nu23_unit.grid(row=5,column=2)

lbl_G12 = tk.Label(master=frame2,text='G12 =',font="Helvetica 25 bold")
lbl_G12.grid(row=6,column=0,padx = 2,pady=2)
lbl_G12_value= tk.Label(master=frame2,width=20,text=" ",bg="black",font = "Helvetica 20 bold")
lbl_G12_value.grid(row=6,column=1,pady=2,ipady=2)
lbl_G12_unit = tk.Label(master=frame2,text='GPa',font="Helvetica 20 bold")
lbl_G12_unit.grid(row=6,column=2)

lbl_G13 = tk.Label(master=frame2,text='G13 =',font="Helvetica 25 bold")
lbl_G13.grid(row=7,column=0,padx = 2,pady=2)
lbl_G13_value= tk.Label(master=frame2,width=20,text=" ",bg="black",font = "Helvetica 20 bold")
lbl_G13_value.grid(row=7,column=1,pady=2,ipady=2)
lbl_G13_unit = tk.Label(master=frame2,text='GPa',font="Helvetica 20 bold")
lbl_G13_unit.grid(row=7,column=2)

lbl_G23 = tk.Label(master=frame2,text='G23 =',font="Helvetica 25 bold")
lbl_G23.grid(row=8,column=0,padx = 2,pady=5)
lbl_G23_value= tk.Label(master=frame2,width=20,text=" ",bg="black",font = "Helvetica 20 bold")
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
    R.deselect()
    if os.path.exists("lamina_properties.txt"):
        os.remove("lamina_properties.txt")
reset = tk.Button(frame3, text ="Reset",height=2,width=10,font="Times 18 bold",bg="black",fg="white",command=reset_properties)
reset.place(x=50,y=0)

def calculate_lamina():
    E1_fibre = float(ent_E1_fibre.get())
    E2_fibre = float(ent_E2_fibre.get())
    nu12_fibre = float(ent_nu12_fibre.get())
    nu23_fibre = float(ent_nu23_fibre.get())
    G12_fibre = float(ent_G12_fibre.get())
    print(G12_fibre)
    G23_fibre = float(ent_G23_fibre.get())
    E_matrix = float(ent_E_matrix.get())
    nu_matrix = float(ent_nu_matrix.get())
    G_matrix = float(ent_G_matrix.get())
    Volume_fraction = float(ent_Volume_fraction.get())
    chamis_bool = bool(chamis_var.get())
    chamis_bool= False
    global E1,E2,nu12,G12
    E1,E2,E3,nu12,nu13,nu23,G12,G13,G23 = effective_lamina_properties(E1_fibre,E2_fibre,nu12_fibre,nu23_fibre,G12_fibre,G23_fibre,E_matrix,nu_matrix,G_matrix,Volume_fraction,chamis_correction=chamis_bool)
    print(G12)
    file1 = open("lamina_properties.txt","w")
    L = [f"E1 : {E1}\n",f"E2 : {E2}\n",f"E3 : {E3}\n",f"nu12 : {nu12}\n",f"nu13 : {nu13}\n",f"nu23 : {nu23}\n",f"G12 : {G12}\n",f"G13 : {G13}\n",f"G23 : {G23}\n"]
    file1.write("Properties of Lamina\n")
    file1.writelines(L)
    file1.close()
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
calculate.place(x=480,y=0)

def run_continue_():
    top3 = tk.Toplevel(root)
    top2frame0 = tk.Frame(master =top3)
    top2frame0.pack()
    
    top2frame1 = tk.Frame(master=top2frame0,width = 150,height = 100,relief=tk.RAISED,bd=3)
    top2frame1.columnconfigure([0,1,2], weight=1, minsize=100)
    top2frame1.rowconfigure([0,1,2,3,4], weight=1, minsize=50)
    
    lbl_X = tk.Label(master=top2frame1,text='X =',font="Helvetica 25 bold")
    lbl_X.grid(row=0,column=0,padx = 2,pady=2)
    ent_X = tk.Entry(master=top2frame1,width=10,font = "Helvetica 20 bold")
    ent_X.grid(row=0,column=1,pady=2,padx=4,ipady=5)
    lbl_X_unit = tk.Label(master=top2frame1,text='GPa',font="Helvetica 25 bold")
    lbl_X_unit.grid(row=0,column=2,padx = 2,pady=2)

    lbl_X_ = tk.Label(master=top2frame1,text="X' =",font="Helvetica 25 bold")
    lbl_X_.grid(row=1,column=0,padx = 2,pady=2)
    ent_X_ = tk.Entry(master=top2frame1,width=10,font = "Helvetica 20 bold")
    ent_X_.grid(row=1,column=1,pady=2,padx=4,ipady=5)
    lbl_X__unit = tk.Label(master=top2frame1,text='GPa',font="Helvetica 25 bold")
    lbl_X__unit.grid(row=1,column=2,padx = 2,pady=2)

    lbl_Y = tk.Label(master=top2frame1,text='Y =',font="Helvetica 25 bold")
    lbl_Y.grid(row=2,column=0,padx = 2,pady=2)
    ent_Y = tk.Entry(master=top2frame1,width=10,font = "Helvetica 20 bold")
    ent_Y.grid(row=2,column=1,pady=2,padx=4,ipady=5)
    lbl_Y_unit = tk.Label(master=top2frame1,text='GPa',font="Helvetica 25 bold")
    lbl_Y_unit.grid(row=2,column=2,padx = 2,pady=2)

    lbl_Y_ = tk.Label(master=top2frame1,text="Y' =",font="Helvetica 25 bold")
    lbl_Y_.grid(row=3,column=0,padx = 2,pady=2)
    ent_Y_ = tk.Entry(master=top2frame1,width=10,font = "Helvetica 20 bold")
    ent_Y_.grid(row=3,column=1,pady=2,padx=4,ipady=5)
    lbl_Y__unit = tk.Label(master=top2frame1,text='GPa',font="Helvetica 25 bold")
    lbl_Y__unit.grid(row=3,column=2,padx = 2,pady=2)

    lbl_S = tk.Label(master=top2frame1,text='S =',font="Helvetica 25 bold")
    lbl_S.grid(row=4,column=0,padx = 2,pady=2)
    ent_S = tk.Entry(master=top2frame1,width=10,font = "Helvetica 20 bold")
    ent_S.grid(row=4,column=1,pady=2,padx=4,ipady=5)
    lbl_S_unit = tk.Label(master=top2frame1,text='GPa',font="Helvetica 25 bold")
    lbl_S_unit.grid(row=4,column=2,padx = 2,pady=2)

    top2frame1.pack(side=tk.LEFT)
    
    top2frame2 = tk.Frame(master=top2frame0,width = 220,height = 40,relief=tk.RIDGE,bd=5)

    lbl_failure = tk.Label(master=top2frame2,text='Hashin Failure Result',font="Helvetica 25 bold",bg="light blue",height=8,width=60)
    lbl_failure.pack()
    top2frame2.pack(side=tk.LEFT)
   
    top2frame3 = tk.Frame(master=top3,width = 150,height = 70,relief=tk.RAISED,bd=3)

    back = tk.Button(top2frame3, text ="Back",height=2,width=10,font="Times 18 bold",bg="black",fg="white",command=top3.destroy)
    back.place(x=20,y=0)

    def test_laminas():
        X = float(ent_X.get())
        X_ = float(ent_X_.get())
        Y = float(ent_Y.get())
        Y_ = float(ent_Y_.get())
        S = float(ent_S.get())
        safety_factor = 99999
        failed_laminas = []
        for i,value in enumerate(stress_laminas):
            res = hashin_failure(value,X,X_,Y,Y_,S)
            if res[0]==False:
                safety_factor=min(safety_factor,res[1])
            else:
                failed_laminas.append(i)
        if(len(failed_laminas)==0):
            lbl_failure['text'] = f'Safety_factor for Laminate is {round(safety_factor,3)}'
        elif(len(failed_laminas)==1):
            lbl_failure['text'] = f'{len(failed_laminas)} laminas failed which is {[i for i in failed_laminas]}'
        else:
            lbl_failure['text'] = f'{len(failed_laminas)} laminas failed which are {[i for i in failed_laminas]}'
        print('Done')


    test = tk.Button(top2frame3, text ="Test",height=2,width=10,font="Times 18 bold",bg="black",fg="white",command=test_laminas)
    test.place(x=590,y=0)

    def finish_task():
        root.destroy()

    finish = tk.Button(top2frame3, text ="Finish",height=2,width=10,font="Times 18 bold",bg="black",fg="white",command=finish_task)
    finish.place(x=1150,y=0)

    top2frame3.pack(fill=tk.BOTH)
    top3.mainloop()

def run_continue():
    top2 = tk.Toplevel(root)
    top1frame0 = tk.Frame(master =top2)
    top1frame0.pack()
    top1frame1 = tk.Frame(master=top1frame0,width = 150,height = 300,relief=tk.RAISED,bd=3)
    top1frame1.columnconfigure([0,1,2], weight=1, minsize=100)
    top1frame1.rowconfigure([0,1,2,3], weight=1, minsize=50)
    noframe = tk.Frame(master=top1frame1)
    lbl_lamina_no = tk.Label(master=noframe,text='No of Laminas =',font="Helvetica 25 bold")
    lbl_lamina_no.grid(row=0,column=0,padx = 2,pady=2)
    ent_lamina_no = tk.Entry(master=noframe,width=10,font = "Helvetica 20 bold")
    ent_lamina_no.grid(row=0,column=1,pady=2,padx=4,ipady=5)
    laminate_frame = tk.Frame(master=top1frame1)
    def lamina_form_generate():
        try:
            for widget in laminate_frame.winfo_children():
                widget.destroy()
        except:
            pass
        lamina_count = int(ent_lamina_no.get())
        laminate_frame.columnconfigure([0,1,2], weight=1, minsize=100)
        laminate_frame.rowconfigure([i for i in range(lamina_count)], weight=1, minsize=50)
        global Lamina_sequence
        Lamina_sequence = []
        for i in range(lamina_count):
            lbl_lamina = tk.Label(master=laminate_frame,text=f'Lamina {i} angle =',font="Helvetica 25 bold")
            lbl_lamina.grid(row=i,column=0,padx = 2,pady=2)
            ent_lamina = tk.Entry(master=laminate_frame,width=10,font = "Helvetica 20 bold")
            ent_lamina.grid(row=i,column=1,pady=2,ipady=5)
            lbl_lamina_unit = tk.Label(master=laminate_frame,text='Deg',font="Helvetica 25 bold")
            lbl_lamina_unit.grid(row=i,column=2,padx = 2,pady=2)
            Lamina_sequence.append(ent_lamina)
    
    btn_lamina_no = tk.Button(noframe,text="Fill",height=2,width=10,font="Times 18 bold",bg="black",fg="white",command=lamina_form_generate)
    btn_lamina_no.grid(row=0,column=2,padx=2,pady=2,ipady=2) 
    noframe.pack()
    laminate_frame.pack()
    top1frame1.pack(side=tk.LEFT,fill=tk.BOTH)

    top1frame2 = tk.Frame(master=top1frame0,width = 100,height = 300,relief=tk.RIDGE,bd=5)
    top1frame2.columnconfigure([0,1,2,3,4], weight=1, minsize=100)
    top1frame2.rowconfigure([0,1,2,3,4], weight=1, minsize=50)

    lbl_N = tk.Label(master=top1frame2,text='N =',font="Helvetica 25 bold")
    lbl_N.grid(row=0,column=0,padx = 2,pady=2)
    ent_Nx = tk.Entry(master=top1frame2,width=5,font = "Helvetica 20 bold")
    ent_Nx.grid(row=0,column=1,pady=2,ipady=5)
    ent_Ny = tk.Entry(master=top1frame2,width=5,font = "Helvetica 20 bold")
    ent_Ny.grid(row=0,column=2,pady=2,ipady=5)
    ent_Nxy = tk.Entry(master=top1frame2,width=5,font = "Helvetica 20 bold")
    ent_Nxy.grid(row=0,column=3,pady=2,ipady=5)
    lbl_N_unit = tk.Label(master=top1frame2,text='N',font="Helvetica 25 bold")
    lbl_N_unit.grid(row=0,column=4,padx = 2,pady=2)

    lbl_M = tk.Label(master=top1frame2,text='M =',font="Helvetica 25 bold")
    lbl_M.grid(row=1,column=0,padx = 2,pady=2)
    ent_Mx = tk.Entry(master=top1frame2,width=5,font = "Helvetica 20 bold")
    ent_Mx.grid(row=1,column=1,pady=2,ipady=5)
    ent_My = tk.Entry(master=top1frame2,width=5,font = "Helvetica 20 bold")
    ent_My.grid(row=1,column=2,pady=2,ipady=5)
    ent_Mxy = tk.Entry(master=top1frame2,width=5,font = "Helvetica 20 bold")
    ent_Mxy.grid(row=1,column=3,pady=2,ipady=5)
    lbl_M_unit = tk.Label(master=top1frame2,text='N-m',font="Helvetica 25 bold")
    lbl_M_unit.grid(row=1,column=4,padx = 2,pady=2)


    lbl_ABD = tk.Label(master=top1frame2,text='',font="Helvetica 25 bold",bg="light blue")
    lbl_ABD.grid(column = 0, row = 2,columnspan = 5,rowspan=2, sticky = tk.W+tk.E)

    lbl_stress = tk.Label(master=top1frame2,text='',font="Helvetica 25 bold",bg="light blue")
    lbl_stress.grid(column = 0, row = 3,columnspan = 5,rowspan=2, sticky = tk.W+tk.E)

    top1frame2.pack(side=tk.LEFT,fill=tk.BOTH)
    top1frame3 = tk.Frame(master=top2,width = 150,height = 70,relief=tk.RAISED,bd=3)

    def back_lamina():
        top2.destroy()
        if os.path.exists("A.npy"):
            os.remove("A.npy")
        if os.path.exists("B.npy"):
            os.remove("B.npy")
        if os.path.exists("D.npy"):
            os.remove("D.npy")
        if os.path.exists("Stress_Laminas.npy"):
            os.remove("Stress_Laminas.npy")

    
    back = tk.Button(top1frame3, text ="Back",height=2,width=10,font="Times 18 bold",bg="black",fg="white",command=back_lamina)
    back.place(x=20,y=0)

    def generate_ABD():
        global A,B,D,z_laminas,Q_matrices,lamina_angles
        lamina_angles= []
        for value in Lamina_sequence:
            lamina_angles.append(int(value.get()))
        res = Laminate_parameters([E1_final,nu12_final,E2_final,G12_final],lamina_angles,1000)
        A,B,D = res[0],res[1],res[2]
        np.save('A',A)
        np.save('B',B)
        np.save('D',D)
        z_laminas,Q_matrices= res[3],res[4]
        lbl_ABD['text'] = 'A,B,D Matrices generated'
        print('Done')


    generate = tk.Button(top1frame3, text ="Generate",height=2,width=10,font="Times 18 bold",bg="black",fg="white",command=generate_ABD)
    generate.place(x=300,y=0)

    def calculate_stress():
        Nx = float(ent_Nx.get())
        Ny = float(ent_Ny.get())
        Nxy = float(ent_Nxy.get())
        Mx = float(ent_Mx.get())
        My = float(ent_My.get())
        Mxy = float(ent_Mxy.get())
        global stress_laminas
        stress_laminas = stress_lamina(A,B,D,z_laminas,Q_matrices,lamina_angles,[Nx,Ny,Nxy],[Mx,My,Mxy])
        np.save('Stress_Laminas',stress_laminas)
        lbl_stress['text'] = 'Stress in each lamina calculated!'
        print('Done')
    
    evaluate = tk.Button(top1frame3, text ="Evaluate",height=2,width=10,font="Times 18 bold",bg="black",fg="white",command=calculate_stress)
    evaluate.place(x=600,y=0)

    continue__ = tk.Button(top1frame3, text ="Continue",height=2,width=10,font="Times 18 bold",bg="black",fg="white",command=run_continue_)
    continue__.place(x=850,y=0)

    top1frame3.pack(fill=tk.BOTH)
    top2.mainloop()

def run_next():
    top1 = tk.Toplevel(root)
    topframe0 = tk.Frame(master =top1)
    topframe0.pack()
    topframe1 = tk.Frame(master=topframe0,width = 150,height = 300,relief=tk.RAISED,bd=3)
    topframe1.columnconfigure([0,1,2], weight=1, minsize=100)
    topframe1.rowconfigure([0,1,2,3,4,5,6,7,8,9], weight=1, minsize=50)
    
    tempframe = tk.Frame(master=topframe1)
    lbl_angle = tk.Label(master=tempframe,text='Angle =',font="Helvetica 25 bold")
    lbl_angle.grid(row=0,column=0,padx = 2,pady=2)
    ent_angle = tk.Entry(master=tempframe,width=10,font = "Helvetica 20 bold")
    ent_angle.grid(row=0,column=1,pady=2,ipady=5)
    tempframe.pack()
    v = tk.StringVar()
    def run_effective_angle():
        for widget in dataframe.winfo_children():
            widget.destroy()
        if(v.get()=="2" or v.get()=="3"):
            dataframe.columnconfigure([0,1,2], weight=1, minsize=50)
            dataframe.rowconfigure([0,1,2], weight=1, minsize=50)
            global ent_00
            ent_00 = tk.Entry(master=dataframe,width=5,font = "Helvetica 20 bold")
            ent_00.grid(row=0,column=0,pady=2,ipady=5)
            global ent_01
            ent_01 = tk.Entry(master=dataframe,width=5,font = "Helvetica 20 bold")
            ent_01.grid(row=0,column=1,pady=2,ipady=5)
            global ent_02
            ent_02 = tk.Entry(master=dataframe,width=5,font = "Helvetica 20 bold")
            ent_02.grid(row=0,column=2,pady=2,ipady=5)
            global ent_10
            ent_10 = tk.Entry(master=dataframe,width=5,font = "Helvetica 20 bold")
            ent_10.grid(row=1,column=0,pady=2,ipady=5)
            global ent_11
            ent_11 = tk.Entry(master=dataframe,width=5,font = "Helvetica 20 bold")
            ent_11.grid(row=1,column=1,pady=2,ipady=5)
            global ent_12
            ent_12 = tk.Entry(master=dataframe,width=5,font = "Helvetica 20 bold")
            ent_12.grid(row=1,column=2,pady=2,ipady=5)
            global ent_20
            ent_20 = tk.Entry(master=dataframe,width=5,font = "Helvetica 20 bold")
            ent_20.grid(row=2,column=0,pady=2,ipady=5)
            global ent_21
            ent_21 = tk.Entry(master=dataframe,width=5,font = "Helvetica 20 bold")
            ent_21.grid(row=2,column=1,pady=2,ipady=5)
            global ent_22
            ent_22 = tk.Entry(master=dataframe,width=5,font = "Helvetica 20 bold")
            ent_22.grid(row=2,column=2,pady=2,ipady=5)
        elif(v.get()=="4"):
            dataframe.columnconfigure([0,1], weight=1, minsize=50)
            dataframe.rowconfigure([0,1,2,3], weight=1, minsize=50)
            
            global ent_E1_new
            lbl_E1_new = tk.Label(master=dataframe,text='E1 =',font="Helvetica 25 bold")
            lbl_E1_new.grid(row=0,column=0,padx = 2,pady=2)
            ent_E1_new = tk.Entry(master=dataframe,width=5,font = "Helvetica 20 bold")
            ent_E1_new.grid(row=0,column=1,pady=2,ipady=5)

            global ent_E2_new
            lbl_E2_new = tk.Label(master=dataframe,text='E2 =',font="Helvetica 25 bold")
            lbl_E2_new.grid(row=1,column=0,padx = 2,pady=2)
            ent_E2_new = tk.Entry(master=dataframe,width=5,font = "Helvetica 20 bold")
            ent_E2_new.grid(row=1,column=1,pady=2,ipady=5)

            global ent_nu12_new
            lbl_nu12_new = tk.Label(master=dataframe,text='nu12 =',font="Helvetica 25 bold")
            lbl_nu12_new.grid(row=2,column=0,padx = 2,pady=2)
            ent_nu12_new = tk.Entry(master=dataframe,width=5,font = "Helvetica 20 bold")
            ent_nu12_new.grid(row=2,column=1,pady=2,ipady=5)

            global ent_G12_new
            lbl_G12_new = tk.Label(master=dataframe,text='G12 =',font="Helvetica 25 bold")
            lbl_G12_new.grid(row=3,column=0,padx = 2,pady=2)
            ent_G12_new = tk.Entry(master=dataframe,width=5,font = "Helvetica 20 bold")
            ent_G12_new.grid(row=3,column=1,pady=2,ipady=5)


    R1 = tk.Radiobutton(topframe1, text="Use the Same", variable=v, value="1",font="Helvetica 25 bold",command=run_effective_angle)
    R2 = tk.Radiobutton(topframe1, text="Q-Matrix", variable=v, value="2",font="Helvetica 25 bold",command=run_effective_angle)
    R3 = tk.Radiobutton(topframe1, text="S-Matrix", variable=v, value="3",font="Helvetica 25 bold",command=run_effective_angle)
    R4 = tk.Radiobutton(topframe1, text="Material Properties", variable=v, value="4",font="Helvetica 25 bold",command=run_effective_angle)
    R1.pack( anchor = tk.W)
    R2.pack( anchor = tk.W)
    R3.pack( anchor = tk.W)
    R4.pack( anchor = tk.W)

    dataframe = tk.Frame(master=topframe1)
    dataframe.pack()

    topframe1.pack(side=tk.LEFT,fill=tk.BOTH)

    topframe2 = tk.Frame(master=topframe0,width = 150,height = 300,relief=tk.RIDGE,bd=5)
    topframe2.columnconfigure([0,1,2], weight=1, minsize=150)
    topframe2.rowconfigure([0,1,2,3,4,5], weight=1, minsize=50)

    lbl_Ex = tk.Label(master=topframe2,text='Ex =',font="Helvetica 25 bold")
    lbl_Ex.grid(row=0,column=0,padx = 2,pady=2)
    lbl_Ex_value= tk.Label(master=topframe2,width=20,text=" ",bg="black",font = "Helvetica 20 bold")
    lbl_Ex_value.grid(row=0,column=1,pady=2,ipady=2)
    lbl_Ex_unit = tk.Label(master=topframe2,text='GPa',font="Helvetica 20 bold")
    lbl_Ex_unit.grid(row=0,column=2)

    lbl_Ey = tk.Label(master=topframe2,text='Ey =',font="Helvetica 25 bold")
    lbl_Ey.grid(row=1,column=0,padx = 2,pady=2)
    lbl_Ey_value= tk.Label(master=topframe2,width=20,text=" ",bg="black",font = "Helvetica 20 bold")
    lbl_Ey_value.grid(row=1,column=1,pady=2,ipady=2)
    lbl_Ey_unit = tk.Label(master=topframe2,text='GPa',font="Helvetica 20 bold")
    lbl_Ey_unit.grid(row=1,column=2)

    lbl_nuxy = tk.Label(master=topframe2,text='nuxy =',font="Helvetica 25 bold")
    lbl_nuxy.grid(row=2,column=0,padx = 2,pady=2)
    lbl_nuxy_value= tk.Label(master=topframe2,width=20,text=" ",bg="black",font = "Helvetica 20 bold")
    lbl_nuxy_value.grid(row=2,column=1,pady=2,ipady=2)
    lbl_nuxy_unit = tk.Label(master=topframe2,text='',font="Helvetica 20 bold")
    lbl_nuxy_unit.grid(row=2,column=2)

    lbl_Gxy = tk.Label(master=topframe2,text='Gxy =',font="Helvetica 25 bold")
    lbl_Gxy.grid(row=3,column=0,padx = 2,pady=2)
    lbl_Gxy_value= tk.Label(master=topframe2,width=20,text=" ",bg="black",font = "Helvetica 20 bold")
    lbl_Gxy_value.grid(row=3,column=1,pady=2,ipady=2)
    lbl_Gxy_unit = tk.Label(master=topframe2,text='GPa',font="Helvetica 20 bold")
    lbl_Gxy_unit.grid(row=3,column=2)

    lbl_etaxy_x = tk.Label(master=topframe2,text='etaxy-x =',font="Helvetica 25 bold")
    lbl_etaxy_x.grid(row=4,column=0,padx = 2,pady=2)
    lbl_etaxy_x_value= tk.Label(master=topframe2,width=20,text=" ",bg="black",font = "Helvetica 20 bold")
    lbl_etaxy_x_value.grid(row=4,column=1,pady=2,ipady=2)

    lbl_etaxy_y = tk.Label(master=topframe2,text='etaxy-y =',font="Helvetica 25 bold")
    lbl_etaxy_y.grid(row=5,column=0,padx = 2,pady=2)
    lbl_etaxy_y_value= tk.Label(master=topframe2,width=20,text=" ",bg="black",font = "Helvetica 20 bold")
    lbl_etaxy_y_value.grid(row=5,column=1,pady=2,ipady=2)
    
    def plotting_graphs():
        plot_properties_angle([E1_final,nu12_final,E2_final,G12_final],float(ent_angle.get()))
    plot_graphs = tk.Button(topframe2, text ="Plot Graphs",height=2,width=10,font="Times 18 bold",command=plotting_graphs)
    plot_graphs.grid(column = 0, row = 6,columnspan = 3, sticky = tk.W+tk.E)

    topframe2.pack(side=tk.LEFT,fill=tk.BOTH)
    topframe3 = tk.Frame(master=top1,width = 150,height = 70,relief=tk.RAISED,bd=3)
    def back_func():
        top1.destroy()
        if os.path.exists("lamina_variation_angle.jpg"):
            os.remove("lamina_variation_angle.jpg")
        if os.path.exists("planar_lamina_properties.txt"):
            os.remove("planar_lamina_properties.txt")
        
    back = tk.Button(topframe3, text ="Back",height=2,width=10,font="Times 18 bold",bg="black",fg="white",command=back_func)
    back.place(x=20,y=0)

    def calculate_effective():
        global E1_final,nu12_final,E2_final,G12_final
        if(v.get()=="1"):
            E1_final = E1
            nu12_final = nu12
            E2_final = E2
            G12_final = G12
        elif(v.get()=="2" or v.get()=="3"):
            mat = np.zeros((3,3),dtype=float)
            mat[0][0] = float(ent_00.get())
            mat[0][1] = float(ent_01.get())
            mat[0][2] = float(ent_02.get())
            mat[1][0] = float(ent_10.get())
            mat[1][1] = float(ent_11.get())
            mat[1][2] = float(ent_12.get())
            mat[2][0] = float(ent_20.get())
            mat[2][1] = float(ent_21.get())
            mat[2][2] = float(ent_22.get())
            if(v.get()=='2'):
                prop_list = effective_lamina_properties_angle(Q_matrix=True,data=mat,angle=0)
                E1_final,nu12_final,E2_final,G12_final = prop_list[0],prop_list[1],prop_list[2],prop_list[3]
            else:
                prop_list = effective_lamina_properties_angle(S_matrix=True,data=mat,angle=0)
                E1_final,nu12_final,E2_final,G12_final = prop_list[0],prop_list[1],prop_list[2],prop_list[3]
        else:
            E1_final = float(ent_E1_new.get())
            nu12_final = float(ent_nu12_new.get())
            E2_final = float(ent_E2_new.get())
            G12_final = float(ent_G12_new.get())
        Ex,nuxy,Ey,Gxy,etaxy_x,etaxy_y = effective_lamina_properties_angle(Material_properties=True,data=[E1_final,nu12_final,E2_final,G12_final],angle=float(ent_angle.get()))
        file1 = open("planar_lamina_properties.txt","w")
        L1 = [f"E1 : {E1_final}\n",f"nu12 : {nu12_final}\n",f"E2 : {E2_final}\n",f"G12 : {G12_final}\n"]
        L2 = [f"Ex : {Ex}\n",f"nuxy : {nuxy}\n",f"Ey : {Ey}\n",f"Gxy : {Gxy}\n",f"etaxy-x : {etaxy_x}\n",f"etaxy-y : {etaxy_y}\n\n"]
        file1.write("Planar properties of Lamina at 0 degree \n")
        file1.writelines(L1)
        file1.write(f"Planar properties of Lamina at  {round(float(ent_angle.get()),3)} degree \n")
        file1.writelines(L2)
        file1.close()
        lbl_Ex_value['text'] = f"{Ex}"
        lbl_Ex_value['bg'] = "white"
        lbl_Ey_value['text'] = f"{Ey}"
        lbl_Ey_value['bg'] = "white"
        lbl_nuxy_value['text'] = f"{nuxy}"
        lbl_nuxy_value['bg'] = "white"
        lbl_Gxy_value['text'] = f"{Gxy}"
        lbl_Gxy_value['bg'] = "white"
        lbl_etaxy_x_value['text'] = f"{etaxy_x}"
        lbl_etaxy_x_value['bg'] = "white"
        lbl_etaxy_y_value['text'] = f"{etaxy_y}"
        lbl_etaxy_y_value['bg'] = "white"

    calculate_eff = tk.Button(topframe3, text ="Calculate",height=2,width=10,font="Times 18 bold",bg="black",fg="white",command=calculate_effective)
    calculate_eff.place(x=400,y=0)

    continue_ = tk.Button(topframe3, text ="Continue",height=2,width=10,font="Times 18 bold",bg="black",fg="white",command = run_continue)
    continue_.place(x=800,y=0)

    topframe3.pack(fill=tk.BOTH)
    top1.mainloop()

next_ = tk.Button(frame3, text ="Next",height=2,width=10,font="Times 18 bold",bg="black",fg="white",command=run_next)
next_.place(x=950,y=0)

frame3.pack(fill=tk.BOTH)
root.mainloop()

