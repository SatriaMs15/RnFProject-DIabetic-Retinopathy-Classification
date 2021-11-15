from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.geometry('540x380')
root.title("Predict Diabetic Renopathy")


def add_image():
    print("aaaaaa")


# Frame
Title = Label(root, text="Predict Diabetic Renopaty", font=12)
Title.pack(pady=10)

imageFrame = Frame(root)
imageFrame.pack(pady=30)

buttonFrame = Frame(root)
buttonFrame.pack(padx=20, pady=20)

Photo = Image.open("IDRiD_004.jpg")
Photo = Photo.resize((150,150))
Photo = ImageTk.PhotoImage(Photo)
photo = Label(imageFrame,image=Photo)
photo.pack(side=LEFT,padx=30)

PredictResult = Entry(imageFrame, textvariable="Diabetic/Normal", width=6, font=('Helvatixa',32))
PredictResult.pack(side=LEFT,padx=30)

btn_play = Button(buttonFrame, text="Add your Image", command=add_image, font=('Calibri',14))
btn_play.pack(side=LEFT, padx=50, pady=10)

btn_predict = Button(buttonFrame, text="Predict", command=add_image, font=('Calibri',14))
btn_predict.pack(side=LEFT, padx=50, pady=10)

root.mainloop()
