from tkinter import *
import sys
import tkinter.messagebox
import time
from datetime import datetime

root = Tk()

root.title("VOTING SYSTEM")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d+0+0" %(width,height))
root.resizable(0,0)
root.wm_attributes("-topmost",1)


red = 0
blue = 0
none = 0
attempts = 3
time_vote = {}

frame = Frame(root)


def but1():
    global red
    red = red+1
    time.sleep(2)
    main_win()
    

def but2():
    global blue
    
    blue = blue+1

    time.sleep(2)
    main_win()

def but3():
    global none
    none = none+1

    time.sleep(2)
    main_win()


    


def buttons(frame):

    for obj in frame.winfo_children():
        obj.destroy()
        
    label_info = Label(frame,text = "Cast Your Vote: ", bg = "red", font = ("times",30,"bold"),fg = "white")
    label_info.pack(side = LEFT)


    b1 = Button(frame, text = "BJP",height = 15,width = 15, font = ("Courier", 30,'bold'),command = but1,bg = "ORANGE")
    b2= Button(frame, text = "CONGRESS",font = ("Courier", 30,'bold'),height = 15,width = 15, command = but2,bg = "GREEN")
    b3 = Button(frame, text = "NOTA",font = ("Courier", 30,'bold'),height = 15,width = 15, command = but3,bg = "BLACK",fg = "STEEL BLUE")
    

    b1.pack(side = LEFT)
    b2.pack(side = LEFT)
    b3.pack(side = LEFT)


def end(frame,root,attempts):

    #frame.pack_forget()

    for obj in frame.winfo_children():
        obj.destroy()
        
    root.title("ADMIN PANEL")
    #frame = Frame(root)
    label = Label(frame, text = "Enter ID and Password", bg = "red", font = ("times",30,"bold"),
              fg = "white")
    label.grid(row = 0, column = 0,pady = 20)

    userlabel = Label(frame, text = "USER ID: ", font = ("times",30,"bold"),
              fg = "black")
    pwdlabel = Label(frame, text = "PASSWORD: ", font = ("times",30,"bold"),
              fg = "black")

    user_id = Entry(frame, font = "Helvetica 20 bold", justify='center')
    pwd = Entry(frame, font = "Helvetica 20 bold", justify='center')

    userlabel.grid(row = 1, column = 0,pady = 30)
    pwdlabel.grid(row = 2, column = 0,pady = 30)
    #pwd.focus()

    user_id.grid(row = 1, column = 1)
    pwd.grid(row = 2, column = 1)

    goButton = Button(frame,
                   text="Go!", height = 3, width = 12, font = ("Courier", 20,'bold'),bg = "green",
                    command=lambda: result(user_id,pwd, frame,root, attempts))

    goButton.grid(row = 3, column = 0,pady = 50)
    #goButton.bind('<Return>',lambda: result(user_id,pwd, frame,root, attempts))

    
    
    
def result(user_id,pwd,frame,root,attempts):

    
    while attempts > 0:

        if len(user_id.get()) == 0:
            tkinter.messagebox.showinfo("ERROR","ID can't be empty.")
            end(frame,root,attempts)

        elif len(pwd.get()) == 0:
            tkinter.messagebox.showinfo("ERROR","Password can't be empty.")
            end(frame,root,attempts)
            

        elif user_id.get() == "Raunak" and pwd.get() == "HelloWorld":
            with open("election_data.txt",'a') as ed:

                for i,j in time_vote.items():
                    s = i+" voted at "+j+"\n"
                    ed.write(s)
            with open("election_data.txt",'r') as ed:
                data = ed.readline()
                for j in ed:
                    print(j)
            
                    
                
            tkinter.messagebox.showinfo("BJP!!","BJP GOT "+str(red) +" votes...")
            tkinter.messagebox.showinfo("CONGRESS!!!","CONGRESS GOT "+str(blue)+ " votes...")
            tkinter.messagebox.showinfo("NOTA!!!","NOTA WAS VOTED "+ str(none)+" times...")
                
            if(int(red) > int(blue)):
                tkinter.messagebox.showinfo("HURAY!!!","BJP WON BY " + str(red - blue) +" votes...")
                    
            if(int(blue) >  int(red)):
                tkinter.messagebox.showinfo("HURAY!!!","CONGRESS WON BY " +str(blue - red) +" votes...")

            elif(int(red) == int(blue)):
                    
                tkinter.messagebox.showinfo("DRAW!!!","NO TEAM WON...")
            break

        else:
            tkinter.messagebox.showinfo("ERROR","WRONG ID or PASSWORD!!")
            attempts = attempts-1
            tkinter.messagebox.showinfo("ATTEMPTS", "ATTEMPTS REMAINING: "+str(attempts))

            end(frame,root,attempts)
            

    tkinter.messagebox.showinfo("CREATED BY-: ", "Raunak Jalan")

    root.destroy()

    
def main_win():

    for obj in frame.winfo_children():
      obj.destroy()

    time_rem = '1'
    no_of_voters = 5
    
    if len(time_vote)<no_of_voters:

        label = Label(frame, bg = "red", font = ("times",50,"bold"),fg = "white")
        label.grid(row = 0, column = 0,pady = 20)

        tick(label)
        
        label_def = Label(frame, text = "Enter ID:", bg = "red", font = ("times",30,"bold"),
                      fg = "white")
        label_def.grid(row = 1, column = 0,pady = 20)

        user_label = Label(frame, text = "USER Name: ", font = ("times",30,"bold"),
                      fg = "black")

        user_name = Entry(frame, font = "Helvetica 20 bold", justify='center')


        user_label.grid(row = 2, column = 0,pady = 30)

        user_name.grid(row = 2, column = 1)

        go_Button = Button(frame,
                        text="Go!", height = 3, width = 12, font = ("Courier", 20,'bold'),bg = "green",
                        command=lambda: get_data(user_name, frame,root))

        go_Button.grid(row = 4, column = 0,pady = 50)

        end_Button = Button(frame, text = "END VOTING",font = ("Courier", 20,'bold'),height = 3,width = 12, command = lambda:end(frame,root,attempts),bg = "RED")
        end_Button.grid(row = 4, column = 1,pady = 50)

        label_time_rem = Label(frame, bg = "red", font = ("times",20,"bold"),fg = "white")
        label_time_rem.grid(row = 6, column = 0,pady = 20)
        time_remain(label_time_rem,frame,root,attempts)


        label_voters_rem = Label(frame, text = "Voters REMAINING: "+str(no_of_voters-len(time_vote)), bg = "red", font = ("times",20,"bold"),fg = "white")
        label_voters_rem.grid(row = 7, column = 0,pady = 20)

    else:
        tkinter.messagebox.showinfo("SORRY","Voting Closed...")
        end(frame,root,attempts)        


def get_data(user_name, frame,root):
    time_data = time.strftime('%H:%M:%S')
    if len(user_name.get())!=0:
        time_vote[user_name.get()] = time_data
        buttons(frame)
    else:
        tkinter.messagebox.showinfo("ERROR","ID FIELD CANNOT BE EMPTY.")
    
    
def tick(label_config):
    time_string = time.strftime('%H:%M:%S')
    label_config.config(text = time_string)
    label_config.after(200,lambda:tick(label_config))

def time_remain(label_config,frame,root,attempts):

    time_data = time.strftime('%H:%M:%S')
    time_end = "16:00:00"
    FMT = "%H:%M:%S"
    
    tdelta = datetime.strptime(time_end,FMT)-datetime.strptime(time_data,FMT)
    
    if int(tdelta.total_seconds())>=int('0'):
        time_remain_hrs = (tdelta.total_seconds())//3600
        time_remain_tot = (tdelta.total_seconds())//60
        label_config.config(text = "TIME REMAINING: {0} hrs \n\t{1} minutes and {2} seconds.".format(time_remain_hrs, time_remain_tot,tdelta.total_seconds()))
        label_config.after(200,lambda:time_remain(label_config,frame,root,attempts))
        
    else:
        tkinter.messagebox.showinfo("SORRY","Voting Closed...")
        end(frame,root,attempts)
    

def callback():
    return


frame.pack()
main_win()
root.protocol("WM_DELETE_WINDOW", callback)

root.mainloop()
