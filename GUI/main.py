import tensorflow as tf
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
from PIL import Image, ImageTk

# Load model machine learning
model = tf.keras.models.load_model('ModelML/ModelDR_Final.h5')
classes = ['Diabetic', 'Normal']

# creating main application window
root = tk.Tk()
root.geometry("720x720")  # size of the top_frame
root.title("Image Classifier")

#  Frame
top_frame = Frame(root, bd=10)
top_frame.pack()

middle_frame = Frame(root, bd=10)
middle_frame.pack()

bottom_frame = Frame(root, bd=10)
bottom_frame.pack()

notification_frame = Frame(root, bd=10)
notification_frame.pack()


# open image file dari hard-disk
def open_image(initialdir='/'):

    file_path = askopenfilename(initialdir=initialdir, filetypes=[('Image File', '*.*')])
    img_var.set(file_path)

    image = Image.open(file_path)
    image = image.resize((320, 180))  # resize image to 32x32
    photo = ImageTk.PhotoImage(image)

    img_label = Label(middle_frame, image=photo, padx=10, pady=10)
    img_label.image = photo  # keep a reference!
    img_label.grid(row=3, column=1)

    return file_path

# Predict Image input
def test_image():
    IMG_SIZE = 612
    #Load path Image input untuk display
    Pred_Path = img_entry.get()

    # membuat path untuk result predict
    Pred_result_Path = "Cache/Prediksi.png"

    # Read Image input
    img = cv2.imread(Pred_Path)

    #Process Image Input
    img_process = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_process = cv2.resize(img_process, (IMG_SIZE, IMG_SIZE))
    img_process = cv2.addWeighted(img_process, 4, cv2.GaussianBlur(img_process, (0, 0), 40), -4, 128)

    # Menyimpan image process kedalam path Pred_result_Path = "Cache/Prediksi.png"
    cv2.imwrite(Pred_result_Path, img_process)

    " Catatan Image Input yang diupload akan di proses terlebih dahulu agar sesuai dengan traning model"
    " Sehingga pada saat predict gambar yang digunakan adalah file gambar upload yang telah di proses"

    #Load Image Process dan bentuk kedalam array
    img_pred = tf.keras.preprocessing.image.load_img(Pred_result_Path, target_size=(150, 150))
    img_array = tf.keras.preprocessing.image.img_to_array(img_pred)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    # Prediksi hasil klassifikasi
    predictions = model.predict(img_array)
    score = tf.nn.sigmoid(predictions[0])
    print(score)
    label = classes[np.argmax(score)]

    result_text = " output class: " + str(label) + " " + "\nConfidence : " + str(int(np.max(score)*100)) + "%"
    test_result_var.set(result_text)


# Koding untuk button upload
btn_img_fopen = Button(top_frame, text='Browse Image', command=lambda: open_image(img_entry.get()), bg="black",
                       fg="white")
btn_img_fopen.grid(row=7, column=1)

img_var = StringVar()
img_var.set("/")
img_entry = Entry(top_frame, textvariable=img_var, width=40)
img_entry.grid(row=7, column=2)

""" middle Frame  """
"Kodingan tampilan tulisan"
ml = Label(middle_frame, font=("Courier", 10), bg="gray", fg="white", text="Browse Image Show Below").grid(row=1,
                                                                                                           column=1)

""" bottom Frame  """
# Koding untuk button predict
btn_test = Button(bottom_frame, text='Test Image', command=test_image, bg="green", fg="white")
btn_test.pack()

test_result_var = StringVar()
test_result_var.set("Your result shown here")
test_result_label = Label(bottom_frame, font=("Courier", 20), height=3, textvariable=test_result_var, bg="white",
                          fg="purple").pack()

# mainloop dari trinket
top_frame.mainloop()
