from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#quit subroutine
def quit():
    main_window.destroy()

#print details of all the camps
def print_camp_details ():
    global j_names, total_entries, name_count, frame
    name_count = 0
    Label(frame, font='bold',text="Row").grid(column=0,row=7)
    Label(frame, font='bold',text="Leader").grid(column=1,row=7)
    Label(frame, font='bold',text="Location").grid(column=2,row=7)
    Label(frame, font='bold',text="Number of Campers").grid(column=3,row=7)
    Label(frame, font='bold',text="Weather").grid(column=4,row=7)
    frame.grid(column =0, row = 7)

    while name_count < total_entries :
        Label(frame, text=name_count).grid(column=0,row=name_count+8) 
        Label(frame, text=(camp_details[name_count][0])).grid(column=1,row=name_count+8)
        Label(frame, text=(camp_details[name_count][1])).grid(column=2,row=name_count+8)
        Label(frame, text=(camp_details[name_count][2])).grid(column=3,row=name_count+8)
        Label(frame, text=(camp_details[name_count][3])).grid(column=4,row=name_count+8)
        name_count += 1

#add the next camper to the list
def append_name ():
    global camp_details, entry_leader,entry_location,entry_campers,entry_weather, total_entries
    if len(entry_leader.get()) != 0 :
        # Check if it's a number
        if int(entry_campers.get()) != ValueError:
            try: 
                int(entry_leader.get())
                messagebox.showerror('error', "Leader's name aint a number")
            except ValueError:
                try:
                    int(entry_location.get())
                    messagebox.showerror('error', 'location is not a number')
                except ValueError:
                    # Check if the number is between 10 to 15
                    if int(entry_campers.get()) >= 10 and int(entry_campers.get()) <= 15:
                        # Check if a weather option has been selected 
                        if len(entry_weather.get()) != 0:
                            camp_details.append([entry_leader.get(),entry_location.get(),entry_campers.get(),entry_weather.get()])
                            entry_leader.delete(0,'end')
                            entry_location.delete(0,'end')
                            entry_campers.delete(0,'end')
                            entry_weather.delete(0,'end')
                            total_entries +=  1
                            print_camp_details()
                            
                        else:
                            messagebox.showerror('error', 'What is your weather?')
                    else:
                        messagebox.showerror('error', 'Number of campers must be between 10 to 15')
        else:
            messagebox.showerror('error', 'Needs to be a whole number')
    else:
        messagebox.showerror('error', 'What is your leader name?')
#delete a row from the list
def delete_row ():
    global camp_details, delete_item, total_entries, name_count
    try:
        del camp_details[int(delete_item.get())]
        total_entries -= 1
        delete_item.delete(0,'end')
        for widget in frame.winfo_children():
            widget.destroy()
        frame.pack_forget()
        print_camp_details()
    except IndexError:
        messagebox.showerror('error', 'That row does not exist')
    except ValueError:
        messagebox.showerror('error', 'Is that even a number?')

#create the buttons and labels along with image
def setup_buttons():
    global camp_details, entry_leader,entry_location,entry_campers,entry_weather, total_entries, delete_item
    Button(main_window, text="Quit",command=quit) .grid(column=0, row=1)
    Button(main_window, text="Update",command=append_name) .grid(column=1,row=1)
    Label(main_window, text="Leader").grid(column=0,row=2)
    entry_leader = Entry(main_window)
    entry_leader.grid(column=1,row=2)
    Label(main_window, text="Location") .grid(column=0,row=3)
    entry_location = Entry(main_window)
    entry_location.grid(column=1,row=3)
    Label(main_window, text="Number of Campers") .grid(column=0,row=4)
    entry_campers = Entry(main_window)
    entry_campers.grid(column=1,row=4)
    Label(main_window, text="Weather").grid(column=0,row=5)
    weather = StringVar()
    entry_weather = ttk.Combobox(main_window, textvariable=weather, values=('Sunny', 'Cloudy', 'Rain', 'Snow'), state='readonly')
    entry_weather.grid(column=1,row=5)
    Label(main_window, text="Row #") .grid(column=0,row=6)
    delete_item = Entry(main_window)
    delete_item.grid(column=1,row=6)
    Button(main_window, text="Delete",command=delete_row) .grid(column=2,row=6)
#start the program running
def main():
    global main_window
    global camp_details, entry_name,entry_age,entry_gender, total_entries, frame
    camp_details = []
    total_entries = 0
    main_window = Tk()
    setup_buttons()
    frame = Frame(main_window)
    main_window.mainloop()
    
main()