from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Image Viewer")
root.iconbitmap(r"C:\Users\LENOVO\Desktop\python\icon.ico")

my_img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\LENOVO\Desktop\python\images\img 1.png"))
my_img2 = ImageTk.PhotoImage(Image.open(r"C:\Users\LENOVO\Desktop\python\images\img 2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open(r"C:\Users\LENOVO\Desktop\python\images\img 3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open(r"C:\Users\LENOVO\Desktop\python\images\img 4.png"))
my_img5 = ImageTk.PhotoImage(Image.open(r"C:\Users\LENOVO\Desktop\python\images\img 5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open(r"C:\Users\LENOVO\Desktop\python\images\img 6.png"))
my_img7 = ImageTk.PhotoImage(Image.open(r"C:\Users\LENOVO\Desktop\python\images\img 7.jpg"))
my_img8 = ImageTk.PhotoImage(Image.open(r"C:\Users\LENOVO\Desktop\python\images\img 8.png"))
my_img9 = ImageTk.PhotoImage(Image.open(r"C:\Users\LENOVO\Desktop\python\images\img 9.jpg"))
my_img10 = ImageTk.PhotoImage(Image.open(r"C:\Users\LENOVO\Desktop\python\images\img 10.png"))

my_list = [my_img1,my_img2,my_img3,my_img4,my_img5,my_img6,my_img7,my_img8,my_img9,my_img10]
img_number=1
status = Label(root,text="Image " + str(img_number) +" of " + str(len(my_list)), bd=1 , relief=SUNKEN,anchor=E)


my_Label = Label(image=my_img1)
my_Label.grid(row=0,column=0,columnspan=3)

def forward(img_number):
    global my_Label
    global button_forward
    global button_back

    my_Label.grid_forget()
    my_Label = Label(image=my_list[img_number-1])
    my_Label.grid(row=0, column=0, columnspan=3)
    button_forward = Button(root, text=">>", command=lambda: forward(img_number+1))
    button_forward.grid(row=1, column=2)
    button_back = Button(root, text="<<", command=lambda: back(img_number-1))
    button_back.grid(row=1, column=0)

    if img_number == 10:
        button_forward=Button(root,text=">>",state=DISABLED)
        button_forward.grid(row=1, column=2)

    status = Label(root, text="Image " + str(img_number) + " of " + str(len(my_list)), bd=1, relief=SUNKEN,anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)

def back(img_number):
    global my_Label
    global button_forward
    global button_back

    my_Label.grid_forget()
    my_Label = Label(image=my_list[img_number - 1])
    my_Label.grid(row=0, column=0, columnspan=3)
    button_forward = Button(root, text=">>", command=lambda: forward(img_number + 1))
    button_forward.grid(row=1, column=2)
    button_back = Button(root, text="<<", command=lambda: back(img_number - 1))
    button_back.grid(row=1, column=0)

    if img_number == 1:
        button_back=Button(root,text="<<",state=DISABLED)
        button_back.grid(row=1, column=0)

    status = Label(root,text="Image " + str(img_number) +" of " + str(len(my_list)), bd=1 , relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)





button_back=Button(root,text="<<",command=back,state = DISABLED)
button_back.grid(row=1,column=0)
button_forward=Button(root,text=">>",command=lambda: forward(2))
button_forward.grid(row=1,column=2)
button_exit= Button(root,text="Exit",command=root.quit)
button_exit.grid(row=1,column=1,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)
root.mainloop()
