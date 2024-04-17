from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title("CONTACT LIST")
width = 850
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry('850x600')
root.resizable(True, True)
root.config(bg="white")

# ============================VARIABLES===================================
FIRSTNAME = StringVar()
LASTNAME = StringVar()
GENDER = StringVar()
AGE = StringVar()
ADDRESS_UNIT = StringVar()
ADDRESS_CIVIC = StringVar()
ADDRESS_STREET = StringVar()
ADDRESS_CITY = StringVar()
ADDRESS_PROVINCE = StringVar()
ADDRESS_POSTAL_CODE = StringVar()
PHONE = StringVar()
EMAIL = StringVar()
WEBSITE = StringVar()
mem_id = None  # Variable to store selected member ID for update

# Entry fields for update window
entry_firstname = None
entry_lastname = None
entry_gender = None
entry_age = None
entry_address_unit = None
entry_address_civic = None
entry_address_street = None
entry_address_city = None
entry_address_province = None
entry_address_postal_code = None
entry_phone = None
entry_email = None
entry_website = None

# ============================METHODS=====================================
def Database():
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, gender TEXT, age TEXT, address_unit TEXT, address_civic TEXT, address_street TEXT, address_city TEXT, address_province TEXT, address_postal_code TEXT, phone TEXT, email TEXT, website TEXT)"
    )
    cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def SubmitData():
    if FIRSTNAME.get() == "" or LASTNAME.get() == "" or GENDER.get() == "" or AGE.get() == "" or ADDRESS_UNIT.get() == "" or ADDRESS_CIVIC.get() == "" or ADDRESS_STREET.get() == "" or ADDRESS_CITY.get() == "" or ADDRESS_PROVINCE.get() == "" or ADDRESS_POSTAL_CODE.get() == "" or PHONE.get() == "" or EMAIL.get() == "" or WEBSITE.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO `member` (firstname, lastname, gender, age, address_unit, address_civic, address_street, address_city, address_province, address_postal_code, phone, email, website) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), int(AGE.get()), str(ADDRESS_UNIT.get()),
             str(ADDRESS_CIVIC.get()), str(ADDRESS_STREET.get()), str(ADDRESS_CITY.get()),
             str(ADDRESS_PROVINCE.get()), str(ADDRESS_POSTAL_CODE.get()), str(PHONE.get()), str(EMAIL.get()),
             str(WEBSITE.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        FIRSTNAME.set("")
        LASTNAME.set("")
        GENDER.set("")
        AGE.set("")
        ADDRESS_UNIT.set("")
        ADDRESS_CIVIC.set("")
        ADDRESS_STREET.set("")
        ADDRESS_CITY.set("")
        ADDRESS_PROVINCE.set("")
        ADDRESS_POSTAL_CODE.set("")
        PHONE.set("")
        EMAIL.set("")
        WEBSITE.set("")


def UpdateContact():
    print("printing your data!")
    selectedRecord = getData()
    member_id = selectedRecord[0]
    # Check if UpdateWindow exists and destroy it before creating a new one
    
    global UpdateWindow
    if 'UpdateWindow' in globals() and UpdateWindow:
        UpdateWindow.destroy()

    FIRSTNAME.set(selectedRecord[1])
    LASTNAME.set(selectedRecord[2])
    GENDER.set(selectedRecord[3])
    AGE.set(selectedRecord[4])
    ADDRESS_UNIT.set(selectedRecord[5])
    ADDRESS_CIVIC.set(selectedRecord[6])
    ADDRESS_STREET.set(selectedRecord[7])
    ADDRESS_CITY.set(selectedRecord[8])
    ADDRESS_PROVINCE.set(selectedRecord[9])
    ADDRESS_POSTAL_CODE.set(selectedRecord[10])
    PHONE.set(selectedRecord[11])
    EMAIL.set(selectedRecord[12])
    WEBSITE.set(selectedRecord[13])

    # Create the UpdateWindow and populate it with entry fields and labels
    UpdateWindow = Toplevel()
    UpdateWindow.title("Update Contact")
    width = 850
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    UpdateWindow.resizable(True, True)
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))

    


# ===================FRAMES==============================
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactUpdateForm = Frame(UpdateWindow)
    ContactUpdateForm.pack(side=TOP, pady=10)

    # ===================LABELS===============================

    lbl_title = Label(FormTitle, text="Update Existing Record", font=('arial bold italic', 25), bg="Sky blue", width=400)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactUpdateForm, text="First Name", font=('times', 20), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(ContactUpdateForm, text="Last Name", font=('times', 20), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactUpdateForm, text="Gender", font=('times', 20), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(ContactUpdateForm, text="Age", font=('times', 20), bd=5)
    lbl_age.grid(row=3, sticky=W)
    lbl_address_unit = Label(ContactUpdateForm, text="Unit Number", font=('times', 20), bd=5)
    lbl_address_unit.grid(row=4, sticky=W)
    lbl_address_civic = Label(ContactUpdateForm, text="Civic Number", font=('times', 20), bd=5)
    lbl_address_civic.grid(row=5, sticky=W)
    lbl_address_street = Label(ContactUpdateForm, text="Street", font=('times', 20), bd=5)
    lbl_address_street.grid(row=6, sticky=W)
    lbl_address_city = Label(ContactUpdateForm, text="City", font=('times', 20), bd=5)
    lbl_address_city.grid(row=7, sticky=W)
    lbl_address_province = Label(ContactUpdateForm, text="Province", font=('times', 20), bd=5)
    lbl_address_province.grid(row=8, sticky=W)
    lbl_address_postal_code = Label(ContactUpdateForm, text="Postal Code", font=('times', 20), bd=5)
    lbl_address_postal_code.grid(row=9, sticky=W)
    lbl_phone = Label(ContactUpdateForm, text="Phone", font=('times', 20), bd=5)
    lbl_phone.grid(row=10, sticky=W)
    lbl_email = Label(ContactUpdateForm, text="Email", font=('times', 20), bd=5)
    lbl_email.grid(row=11, sticky=W)
    lbl_website = Label(ContactUpdateForm, text="Website", font=('times', 20), bd=5)
    lbl_website.grid(row=12, sticky=W)

    # ===================ENTRY===============================
    firstname = Entry(ContactUpdateForm, textvariable=FIRSTNAME, font=('times', 17))
    firstname.grid(row=0, column=1)
    lastname = Entry(ContactUpdateForm, textvariable=LASTNAME, font=('times', 17))
    lastname.grid(row=1, column=1)
    Radiobutton(ContactUpdateForm, text="Male", variable=GENDER, value="Male", font=('times', 14)).grid(row=2, column=1, sticky=W)
    Radiobutton(ContactUpdateForm, text="Female", variable=GENDER, value="Female", font=('times', 14)).grid(row=2, column=1, sticky=E)
    age = Entry(ContactUpdateForm, textvariable=AGE, font=('times', 17))
    age.grid(row=3, column=1)
    address_unit = Entry(ContactUpdateForm, textvariable=ADDRESS_UNIT, font=('times', 17))
    address_unit.grid(row=4, column=1)
    address_civic = Entry(ContactUpdateForm, textvariable=ADDRESS_CIVIC, font=('times', 17))
    address_civic.grid(row=5, column=1)
    address_street = Entry(ContactUpdateForm, textvariable=ADDRESS_STREET, font=('times', 17))
    address_street.grid(row=6, column=1)
    address_city = Entry(ContactUpdateForm, textvariable=ADDRESS_CITY, font=('times', 17))
    address_city.grid(row=7, column=1)
    address_province = Entry(ContactUpdateForm, textvariable=ADDRESS_PROVINCE, font=('times', 17))
    address_province.grid(row=8, column=1)
    address_postal_code = Entry(ContactUpdateForm, textvariable=ADDRESS_POSTAL_CODE, font=('times', 17))
    address_postal_code.grid(row=9, column=1)
    phone = Entry(ContactUpdateForm, textvariable=PHONE, font=('times', 17))
    phone.grid(row=10, column=1)
    email = Entry(ContactUpdateForm, textvariable=EMAIL, font=('times', 17))
    email.grid(row=11, column=1)
    website = Entry(ContactUpdateForm, textvariable=WEBSITE, font=('times', 17))
    website.grid(row=12, column=1)

    
    # Button to update data
    btn_update = Button(ContactUpdateForm, text="Update", font=('arial bold italic', 10), width=10, bg="Sky blue", command=lambda: SubmitUpdatedData(firstname, lastname, GENDER, age, address_unit, address_civic, address_street, address_city, address_province, address_postal_code, phone, email, website, member_id))
    btn_update.grid(row=14, columnspan=2, pady=10)


def SubmitUpdatedData(entry_firstname, entry_lastname, entry_gender, entry_age, entry_address_unit, entry_address_civic, entry_address_street, entry_address_city, entry_address_province, entry_address_postal_code, entry_phone, entry_email, entry_website, member_id):
    
   
    print(str(entry_firstname.get()), str(entry_lastname.get()), str(entry_gender.get()), int(entry_age.get()), str(entry_address_unit.get()),
            str(entry_address_civic.get()), str(entry_address_street.get()), str(entry_address_city.get()), str(entry_address_province.get()),
            str(entry_address_postal_code.get()), str(entry_phone.get()), str(entry_email.get()), str(entry_website.get()), member_id)
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute(
         "UPDATE `member` SET firstname=?, lastname=?, gender=?, age=?, address_unit=?, address_civic=?, address_street=?, address_city=?, address_province=?, address_postal_code=?, phone=?, email=?, website=? WHERE mem_id=?",
        (
            str(entry_firstname.get()), str(entry_lastname.get()), str(entry_gender.get()), int(entry_age.get()), str(entry_address_unit.get()),
            str(entry_address_civic.get()), str(entry_address_street.get()), str(entry_address_city.get()), str(entry_address_province.get()),
            str(entry_address_postal_code.get()), str(entry_phone.get()), str(entry_email.get()), str(entry_website.get()), member_id
        )
    )
    conn.commit()
    cursor.close()
    conn.close()
    tkMessageBox.showinfo('', 'Contact updated successfully!')

def OnSelected(event):
    global mem_id
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    mem_id = selecteditem[0]
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    ADDRESS_UNIT.set("")
    ADDRESS_CIVIC.set("")
    ADDRESS_STREET.set("")
    ADDRESS_CITY.set("")
    ADDRESS_PROVINCE.set("")
    ADDRESS_POSTAL_CODE.set("")
    PHONE.set("")
    EMAIL.set("")
    WEBSITE.set("")
    FIRSTNAME.set(selecteditem[1])
    LASTNAME.set(selecteditem[2])
    GENDER.set(selecteditem[3])
    AGE.set(selecteditem[4])
    ADDRESS_UNIT.set(selecteditem[5])
    ADDRESS_CIVIC.set(selecteditem[6])
    ADDRESS_STREET.set(selecteditem[7])
    ADDRESS_CITY.set(selecteditem[8])
    ADDRESS_PROVINCE.set(selecteditem[9])
    ADDRESS_POSTAL_CODE.set(selecteditem[10])
    PHONE.set(selecteditem[11])
    EMAIL.set(selecteditem[12])
    WEBSITE.set(selecteditem[13])


def DeleteData():
    if not tree.selection():
        result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn = sqlite3.connect("pythontut.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `member` WHERE `mem_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()

def getData():
    # Replace this select command with hardcoded values for now
    # In real implementation, you'll use the selected contact's ID to fetch data
    selected_contact_id = 1  # Example ID
    select_query = "SELECT * FROM `member` WHERE mem_id = ?"
    
    # Open a database connection
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    
    # Execute the select query
    cursor.execute(select_query, (selected_contact_id,))
    
    # Fetch the result
    selected_contact_data = cursor.fetchone()
    
    # Close cursor and connection
    cursor.close()
    conn.close()

    return selected_contact_data

def AddNewWindow():
    global mem_id
    mem_id = None  # Reset mem_id when adding a new contact
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    ADDRESS_UNIT.set("")
    ADDRESS_CIVIC.set("")
    ADDRESS_STREET.set("")
    ADDRESS_CITY.set("")
    ADDRESS_PROVINCE.set("")
    ADDRESS_POSTAL_CODE.set("")
    PHONE.set("")
    EMAIL.set("")
    WEBSITE.set("")
    NewWindow = Toplevel()
    NewWindow.title("Contact List")
    width = 850
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width / 2)) - (width /2)
    y = ((screen_height / 2) ) - (height / 2)
    NewWindow.resizable(True, True)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()

    # ===================FRAMES==============================
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)

    # ===================LABELS==============================
    lbl_title = Label(FormTitle, text="Add New Contact", font=('arial bold italic', 25), bg="Sky blue", width=400)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="First Name", font=('times', 20), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="Last Name", font=('times', 20), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('times', 20), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="Age", font=('times', 20), bd=5)
    lbl_age.grid(row=3, sticky=W)
    lbl_address_unit = Label(ContactForm, text="Unit Number", font=('times', 20), bd=5)
    lbl_address_unit.grid(row=4, sticky=W)
    lbl_address_civic = Label(ContactForm, text="Civic Number", font=('times', 20), bd=5)
    lbl_address_civic.grid(row=5, sticky=W)
    lbl_address_street = Label(ContactForm, text="Street", font=('times', 20), bd=5)
    lbl_address_street.grid(row=6, sticky=W)
    lbl_address_city = Label(ContactForm, text="City", font=('times', 20), bd=5)
    lbl_address_city.grid(row=7, sticky=W)
    lbl_address_province = Label(ContactForm, text="Province", font=('times', 20), bd=5)
    lbl_address_province.grid(row=8, sticky=W)
    lbl_address_postal_code = Label(ContactForm, text="Postal Code", font=('times', 20), bd=5)
    lbl_address_postal_code.grid(row=9, sticky=W)
    lbl_phone = Label(ContactForm, text="Phone", font=('times', 20), bd=5)
    lbl_phone.grid(row=10, sticky=W)
    lbl_email = Label(ContactForm, text="Email", font=('times', 20), bd=5)
    lbl_email.grid(row=11, sticky=W)
    lbl_website = Label(ContactForm, text="Website", font=('times', 20), bd=5)
    lbl_website.grid(row=12, sticky=W)

    # ===================ENTRY===============================
    firstname = Entry(ContactForm, textvariable=FIRSTNAME, font=('times', 17))
    firstname.grid(row=0, column=1)
    lastname = Entry(ContactForm, textvariable=LASTNAME, font=('times', 17))
    lastname.grid(row=1, column=1)
    Radiobutton(ContactForm, text="Male", variable=GENDER, value="Male", font=('times', 14)).grid(row=2, column=1, sticky=W)
    Radiobutton(ContactForm, text="Female", variable=GENDER, value="Female", font=('times', 14)).grid(row=2, column=1, sticky=E)
    age = Entry(ContactForm, textvariable=AGE, font=('times', 17))
    age.grid(row=3, column=1)
    address_unit = Entry(ContactForm, textvariable=ADDRESS_UNIT, font=('times', 17))
    address_unit.grid(row=4, column=1)
    address_civic = Entry(ContactForm, textvariable=ADDRESS_CIVIC, font=('times', 17))
    address_civic.grid(row=5, column=1)
    address_street = Entry(ContactForm, textvariable=ADDRESS_STREET, font=('times', 17))
    address_street.grid(row=6, column=1)
    address_city = Entry(ContactForm, textvariable=ADDRESS_CITY, font=('times', 17))
    address_city.grid(row=7, column=1)
    address_province = Entry(ContactForm, textvariable=ADDRESS_PROVINCE, font=('times', 17))
    address_province.grid(row=8, column=1)
    address_postal_code = Entry(ContactForm, textvariable=ADDRESS_POSTAL_CODE, font=('times', 17))
    address_postal_code.grid(row=9, column=1)
    phone = Entry(ContactForm, textvariable=PHONE, font=('times', 17))
    phone.grid(row=10, column=1)
    email = Entry(ContactForm, textvariable=EMAIL, font=('times', 17))
    email.grid(row=11, column=1)
    website = Entry(ContactForm, textvariable=WEBSITE, font=('times', 17))
    website.grid(row=12, column=1)

    # ==================BUTTONS==============================
    btn_addcon = Button(ContactForm, text="SAVE", font=('arial bold italic', 10), width=50, bg= "Sky blue", command=SubmitData)
    btn_addcon.grid(row=13, columnspan=2, pady=10)
    btn_addcon = Button(ContactForm, text="SAVE", font=('arial bold italic', 10), width=50, bg="Sky blue",
                        command=SubmitData)
    btn_addcon.grid(row=13, columnspan=2, pady=10)

def updateData():
    global mem_id
    mem_id = None  # Reset mem_id when adding a new contact
    FIRSTNAME.set("")
    LASTNAME.set("")
    GENDER.set("")
    AGE.set("")
    ADDRESS_UNIT.set("")
    ADDRESS_CIVIC.set("")
    ADDRESS_STREET.set("")
    ADDRESS_CITY.set("")
    ADDRESS_PROVINCE.set("")
    ADDRESS_POSTAL_CODE.set("")
    PHONE.set("")
    EMAIL.set("")
    WEBSITE.set("")
    NewWindow = Toplevel()
    NewWindow.title("updateData")
    width = 850
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width / 2)) - (width /2)
    y = ((screen_height / 2) ) - (height / 2)
    NewWindow.resizable(True, True)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()

    # ===================FRAMES==============================
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)

    # ===================LABELS==============================
    lbl_title = Label(FormTitle, text="Add New Contact", font=('arial bold italic', 25), bg="Sky blue", width=400)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="First Name", font=('times', 20), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="Last Name", font=('times', 20), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('times', 20), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="Age", font=('times', 20), bd=5)
    lbl_age.grid(row=3, sticky=W)
    lbl_address_unit = Label(ContactForm, text="Unit Number", font=('times', 20), bd=5)
    lbl_address_unit.grid(row=4, sticky=W)
    lbl_address_civic = Label(ContactForm, text="Civic Number", font=('times', 20), bd=5)
    lbl_address_civic.grid(row=5, sticky=W)
    lbl_address_street = Label(ContactForm, text="Street", font=('times', 20), bd=5)
    lbl_address_street.grid(row=6, sticky=W)
    lbl_address_city = Label(ContactForm, text="City", font=('times', 20), bd=5)
    lbl_address_city.grid(row=7, sticky=W)
    lbl_address_province = Label(ContactForm, text="Province", font=('times', 20), bd=5)
    lbl_address_province.grid(row=8, sticky=W)
    lbl_address_postal_code = Label(ContactForm, text="Postal Code", font=('times', 20), bd=5)
    lbl_address_postal_code.grid(row=9, sticky=W)
    lbl_phone = Label(ContactForm, text="Phone", font=('times', 20), bd=5)
    lbl_phone.grid(row=10, sticky=W)
    lbl_email = Label(ContactForm, text="Email", font=('times', 20), bd=5)
    lbl_email.grid(row=11, sticky=W)
    lbl_website = Label(ContactForm, text="Website", font=('times', 20), bd=5)
    lbl_website.grid(row=12, sticky=W)

    # ===================ENTRY===============================
    firstname = Entry(ContactForm, textvariable=FIRSTNAME, font=('times', 17))
    firstname.grid(row=0, column=1)
    lastname = Entry(ContactForm, textvariable=LASTNAME, font=('times', 17))
    lastname.grid(row=1, column=1)
    Radiobutton(ContactForm, text="Male", variable=GENDER, value="Male", font=('times', 14)).grid(row=2, column=1, sticky=W)
    Radiobutton(ContactForm, text="Female", variable=GENDER, value="Female", font=('times', 14)).grid(row=2, column=1, sticky=E)
    age = Entry(ContactForm, textvariable=AGE, font=('times', 17))
    age.grid(row=3, column=1)
    address_unit = Entry(ContactForm, textvariable=ADDRESS_UNIT, font=('times', 17))
    address_unit.grid(row=4, column=1)
    address_civic = Entry(ContactForm, textvariable=ADDRESS_CIVIC, font=('times', 17))
    address_civic.grid(row=5, column=1)
    address_street = Entry(ContactForm, textvariable=ADDRESS_STREET, font=('times', 17))
    address_street.grid(row=6, column=1)
    address_city = Entry(ContactForm, textvariable=ADDRESS_CITY, font=('times', 17))
    address_city.grid(row=7, column=1)
    address_province = Entry(ContactForm, textvariable=ADDRESS_PROVINCE, font=('times', 17))
    address_province.grid(row=8, column=1)
    address_postal_code = Entry(ContactForm, textvariable=ADDRESS_POSTAL_CODE, font=('times', 17))
    address_postal_code.grid(row=9, column=1)
    phone = Entry(ContactForm, textvariable=PHONE, font=('times', 17))
    phone.grid(row=10, column=1)
    email = Entry(ContactForm, textvariable=EMAIL, font=('times', 17))
    email.grid(row=11, column=1)
    website = Entry(ContactForm, textvariable=WEBSITE, font=('times', 17))
    website.grid(row=12, column=1)

    # ==================BUTTONS==============================
    btn_addcon = Button(ContactForm, text="SAVE", font=('arial bold italic', 10), width=50, bg= "Sky blue", command=SubmitData)
    btn_addcon.grid(row=13, columnspan=2, pady=10)
    btn_addcon = Button(ContactForm, text="SAVE", font=('arial bold italic', 10), width=50, bg="Sky blue",
                        command=SubmitData)
    btn_addcon.grid(row=13, columnspan=2, pady=10)

# ============================FRAMES======================================
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
Bottom = Frame(root, width=500, bd=1, relief=SOLID)
Bottom.pack(side=BOTTOM)
Mid = Frame(root, width=500, bg="white")
Mid.pack(side=BOTTOM)
MidLeft = Frame(Bottom, width=100)
MidLeft.pack(side=LEFT)
MidLeftPadding = Frame(Bottom, width=500, bg="white")
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Bottom, width=100)
MidRight.pack(side=RIGHT)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
# ============================LABELS======================================
lbl_title = Label(Top, text="Contact Management System", font=('arial bold italic', 40), bg="Light grey", width=500)
lbl_title.pack(fill=X)

# ============================BUTTONS=====================================
btn_add = Button(MidLeft, text="ADD NEW", font=('arial bold italic', 15),  bg="green", command=AddNewWindow)
btn_add.pack(side=BOTTOM)
btn_delete = Button(MidRight, text="DELETE",font=('arial bold italic', 15),  bg="red", command=DeleteData)
btn_delete.pack(side=BOTTOM)
btn_update = Button(Mid, text="UPDATE", font=('arial bold italic', 15),  bg="blue", command=UpdateContact)
btn_update.pack(side=BOTTOM)

# ============================TABLES======================================
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin,
                    columns=("ID", "FIRST NAME", "LAST NAME", "GENDER", "AGE", "ADDRESS UNIT", "ADDRESS CIVIC",
                             "ADDRESS STREET", "ADDRESS CITY", "ADDRESS PROVINCE", "ADDRESS POSTAL CODE", "PHONE",
                             "EMAIL", "WEBSITE"),
                    height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('ID', text="ID", anchor=W)
tree.heading('FIRST NAME', text="FIRST NAME", anchor=W)
tree.heading('LAST NAME', text="LAST NAME", anchor=W)
tree.heading('GENDER', text="GENDER", anchor=W)
tree.heading('AGE', text="AGE", anchor=W)
tree.heading('ADDRESS UNIT', text="ADDRESS UNIT", anchor=W)
tree.heading('ADDRESS CIVIC', text="ADDRESS CIVIC", anchor=W)
tree.heading('ADDRESS STREET', text="ADDRESS STREET", anchor=W)
tree.heading('ADDRESS CITY', text="ADDRESS CITY", anchor=W)
tree.heading('ADDRESS PROVINCE', text="ADDRESS PROVINCE", anchor=W)
tree.heading('ADDRESS POSTAL CODE', text="ADDRESS POSTAL CODE", anchor=W)
tree.heading('PHONE', text="PHONE", anchor=W)
tree.heading('EMAIL', text="EMAIL", anchor=W)
tree.heading('WEBSITE', text="WEBSITE", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.column('#6', stretch=NO, minwidth=0, width=90)
tree.column('#7', stretch=NO, minwidth=0, width=90)
tree.column('#8', stretch=NO, minwidth=0, width=90)
tree.column('#9', stretch=NO, minwidth=0, width=90)
tree.column('#10', stretch=NO, minwidth=0, width=90)
tree.column('#11', stretch=NO, minwidth=0, width=150)
tree.column('#12', stretch=NO, minwidth=0, width=150)
tree.column('#13', stretch=NO, minwidth=0, width=150)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)

# ============================INITIALIZATION==============================
if __name__ == '__main__':
    Database()
    root.mainloop()
