# Imports for prediction
#from predict import initialize, predict_image
from tkinter import *
from PIL import Image, ImageTk
import os
import random
import requests
import json

discocytes = "C:/Users/hammb/Dateien/Datasets/Portraits_png/Discocytes-Test"
echinocytes = "C:/Users/hammb/Dateien/Datasets/Portraits_png/Echinocytes-Test"
spherocytes = "C:/Users/hammb/Dateien/Datasets/Portraits_png/Spherocytes-Test"

images = []

def sendFrameForProcessing(imagePath, imageProcessingEndpoint):
    headers = {'Content-Type': 'application/octet-stream'}

    with open(imagePath, mode="rb") as test_image:
        try:
            response = requests.post(imageProcessingEndpoint, headers = headers, data = test_image)
            print("Response from classification service: (" + str(response.status_code) + ") " + json.dumps(response.json()) + "\n")
        except Exception as e:
            print(e)
            print("No response from classification service")
            return None

    return json.dumps(response.json())

def get_images():
    
    images.append(get_rand_image())
    images.append(get_rand_image())
    images.append(get_rand_image())
    images.append(get_rand_image())
    images.append(get_rand_image())
    images.append(get_rand_image())
    images.append(get_rand_image())
    images.append(get_rand_image())
    images.append(get_rand_image())

def button_click(number):
    
    current = e.get()
    e.delete(0, END)
    
    #p = predict_image(Image.open(images[number]))
    
    p = sendFrameForProcessing(images[number], "http://192.168.0.52/image")
    
    p = dict(json.loads(p))
    
    predictions = {}
    
    predictions[p["predictions"][0]["tagName"]] = p["predictions"][0]["probability"]
    predictions[p["predictions"][1]["tagName"]] = p["predictions"][1]["probability"]
    predictions[p["predictions"][2]["tagName"]] = p["predictions"][2]["probability"]
    
    e.insert(0, max(predictions, key=predictions.get))

def get_rand_image():
    
    path = [discocytes, echinocytes, spherocytes][random.randint(0,2)]
    
    return os.path.join(path, os.listdir(path)[random.randint(0, len(os.listdir(path)) - 1)])

def reload_images():
    
    for key in range(len(images)):
        images[key] = get_rand_image()
    
    image0 = ImageTk.PhotoImage(file=images[0])
    image1 = ImageTk.PhotoImage(file=images[1])
    image2 = ImageTk.PhotoImage(file=images[2])
    image3 = ImageTk.PhotoImage(file=images[3])
    image4 = ImageTk.PhotoImage(file=images[4])
    image5 = ImageTk.PhotoImage(file=images[5])
    image6 = ImageTk.PhotoImage(file=images[6])
    image7 = ImageTk.PhotoImage(file=images[7])
    image8 = ImageTk.PhotoImage(file=images[8])
    
    button_0.configure(image=image0)
    button_1.configure(image=image1)
    button_2.configure(image=image2)
    button_3.configure(image=image3)
    button_4.configure(image=image4)
    button_5.configure(image=image5)
    button_6.configure(image=image6)
    button_7.configure(image=image7)
    button_8.configure(image=image8)
    
    button_0.image = image0
    button_1.image = image1
    button_2.image = image2
    button_3.image = image3
    button_4.image = image4
    button_5.image = image5
    button_6.image = image6
    button_7.image = image7
    button_8.image = image8
    
    
global image0, image1, image2, image3, image4, image5, image6, image7, image8
    
if __name__ == '__main__':
    # Load and intialize the model
    #initialize()
    
    image = get_rand_image()
    
    #prediction = predict_image(image)

    root = Tk()
    root.title("Bloodcell prediction")
    
    e = Entry(root, width=35, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    
    get_images()
    
    image0 = ImageTk.PhotoImage(file=images[0])
    image1 = ImageTk.PhotoImage(file=images[1])
    image2 = ImageTk.PhotoImage(file=images[2])
    image3 = ImageTk.PhotoImage(file=images[3])
    image4 = ImageTk.PhotoImage(file=images[4])
    image5 = ImageTk.PhotoImage(file=images[5])
    image6 = ImageTk.PhotoImage(file=images[6])
    image7 = ImageTk.PhotoImage(file=images[7])
    image8 = ImageTk.PhotoImage(file=images[8])
    # Define Buttons
    
    button_0 = Button(root,  image=image0, command=lambda: button_click(0))
    button_1 = Button(root,  image=image1, command=lambda: button_click(1))
    button_2 = Button(root,  image=image2, command=lambda: button_click(2))
    button_3 = Button(root,  image=image3, command=lambda: button_click(3))
    button_4 = Button(root,  image=image4, command=lambda: button_click(4))
    button_5 = Button(root,  image=image5, command=lambda: button_click(5))
    button_6 = Button(root,  image=image6, command=lambda: button_click(6))
    button_7 = Button(root,  image=image7, command=lambda: button_click(7))
    button_8 = Button(root,  image=image8, command=lambda: button_click(8))
    
    button_reload = Button(root,  text = "New Images", command=lambda: reload_images())
    
    button_0.image = image0
    button_1.image = image1
    button_2.image = image2
    button_3.image = image3
    button_4.image = image4
    button_5.image = image5
    button_6.image = image6
    button_7.image = image7
    button_8.image = image8
    
    # Put the buttons on the screen
    
    button_0.grid(row=3, column=0)
    button_1.grid(row=3, column=1)
    button_2.grid(row=3, column=2)
    
    button_3.grid(row=2, column=0)
    button_4.grid(row=2, column=1)
    button_5.grid(row=2, column=2)
    
    button_6.grid(row=1, column=0)
    button_7.grid(row=1, column=1)
    button_8.grid(row=1, column=2)
    
    button_reload.grid(row=4, column=1)
    
    root.mainloop()
