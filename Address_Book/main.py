# Address Book (version 0.01)
from tkinter import *
from tkinter import messagebox
from DB.db_conn import Database

DB = Database('DB/contacts_data.db')


def populate_list():

    contacts_list.delete(0, END)
    
    for row in DB.fetch():
        contacts_list.insert(END, row)

def add_data():

    if f_name.get() == '' or l_name.get() == '' or email_addr.get() == '':
        messagebox.showerror('Requirements Error', 'Please fill in all the fields')
        return
    
    DB.insert(f_name.get(), l_name.get(), email_addr.get())
    contacts_list.delete(0, END)
    contacts_list.insert(END, (f_name.get(), l_name.get(), email_addr.get()))
    
    clear_data()
    populate_list()
    entry_first.focus()

def select_item(event):

    try:
        global selected_item
        
        index = contacts_list.curselection()[0]
        selected_item = contacts_list.get(index)

        entry_first.delete(0, END)
        entry_first.insert(END, selected_item[1])

        entry_last.delete(0, END)
        entry_last.insert(END, selected_item[2])

        entry_email.delete(0, END)
        entry_email.insert(END, selected_item[3])
    
    except IndexError:
        pass
    

def remove_data():

    DB.remove(selected_item[0])

    clear_data()
    populate_list()

def update_data():

    DB.update(selected_item[0], f_name.get(), l_name.get(), email_addr.get())

    populate_list()

def clear_data():

    entry_first.delete(0, END)
    entry_last.delete(0, END)
    entry_email.delete(0, END)


# Create Window
app = Tk()

# Page Defaults
default_font = 'Arial, 12'
bg_color = '#fff'
fg_color = '#262626'
light_gray = '#ddd'
add_color = '#269269'
remove_color = '#e23e23'
update_color = '#296296'
clear_color = '#777'

# Person Data
# First NameFrame
f_name_frame = Frame(app, bg=bg_color)
f_name_frame.pack(fill='both')

# First Name Label
label_first = Label(f_name_frame, text='First Name:', bg=bg_color, fg=fg_color)
label_first.pack(side='left', padx=(20, 6), pady=(20, 10))

# Getter
f_name = StringVar()
# Entry Fields (first name)
entry_first = Entry(f_name_frame, width=37, bg=light_gray, fg=fg_color, \
                   font=default_font, border=0, textvariable=f_name)
entry_first.focus()
entry_first.pack(side='left', pady=(20, 10))

# ______________________________________________

# Last Name Frame
l_name_frame = Frame(app, bg=bg_color)
l_name_frame.pack(fill='both')

# Last Name Label
label_last = Label(l_name_frame, text='Last Name:', bg=bg_color, fg=fg_color)
label_last.pack(side='left', padx=(20, 7), pady=(0, 10))

# Getter
l_name = StringVar()
# Entry Fields (last name)
entry_last = Entry(l_name_frame, width=37, bg=light_gray, fg=fg_color, \
                   font=default_font, border=0, textvariable=l_name)
entry_last.pack(side='left', pady=(0, 10))

# ______________________________________________

# Email Address Frame
email_frame = Frame(app, bg=bg_color)
email_frame.pack(fill='both')

# Last Name Label
label_email = Label(email_frame, text='Email Addr:', bg=bg_color, fg=fg_color)
label_email.pack(side='left', padx=(20, 5), pady=(0, 10))

# Getter
email_addr = StringVar()
# Entry Fields (last name)
entry_email = Entry(email_frame, width=37, bg=light_gray, fg=fg_color, \
                   font=default_font, border=0, textvariable=email_addr)
entry_email.pack(side='left', pady=(0, 20))

# ______________________________________________

# Listbox Frame
listbox_frame = Frame(app, bg=bg_color)
listbox_frame.pack(fill='both', expand=True)

# Contacts List
contacts_list = Listbox(listbox_frame, bg=bg_color, fg=fg_color, \
                    font=default_font, highlightthickness=0, border=0)
contacts_list.pack(side='left', fill='both', padx=(24, 0), pady=(20, 0), expand=True)

# Scrollbar
y_scroll = Scrollbar(listbox_frame)
y_scroll.pack(side='left', fill='y')

# Set Listbox to Scrollbar
contacts_list.configure(yscrollcommand=y_scroll.set)
y_scroll.configure(command=contacts_list.yview)

# Bind Selected
contacts_list.bind('<<ListboxSelect>>', select_item)


# ______________________________________________

# Buttons Frame
btns_frame = Frame(app, bg=bg_color, height=40)
btns_frame.pack(fill='both')

# Add Entry Button
add_btn = Button(btns_frame, text='Add', bg=add_color, fg=bg_color, \
                 relief='flat', command=add_data)
add_btn.pack(side='left', fill='both', expand=True)

# Remove Entry Button
remove_btn = Button(btns_frame, text='Remove', bg=remove_color, fg=bg_color, \
                    relief='flat', command=remove_data)
remove_btn.pack(side='left', fill='both', expand=True)

# Update Fields Button
update_btn = Button(btns_frame, text='Update', bg=update_color, fg=bg_color, \
                    relief='flat', command=update_data)
update_btn.pack(side='left', fill='both', expand=True)

# Clear Fields Button
clear_btn = Button(btns_frame, text='Clear', bg=clear_color, fg=bg_color, \
                   relief='flat', command=clear_data)
clear_btn.pack(side='left', fill='both', expand=True)


if __name__ == '__main__':

    populate_list()
    
    app.title('Contacts')
    app.geometry('450x600+0-33')
    app.resizable(False, False)
    app.configure(bg=bg_color)
    app.mainloop()
