from tkinter import Tk
from tkinter import filedialog
from tkinter import dialog
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk, ImageDraw

root  = Tk()
root.title('Watermarkly.com')
root.geometry('600x600')
root.resizable(False, False)


picture_path = ''
img_photo = None

img = ttk.Label(root)
img.grid(column=1, row=2, columnspan=2, rowspan=2)

def chooseFile():
    global picture_path, img_photo
    picture_path = filedialog.askopenfilename(
        title='Choose your Picture',
        filetypes=[('Bilder', "*.png *.jpg *.jpeg")]
    )
    if picture_path:
        pil_img = Image.open(picture_path)
        pil_img = pil_img.resize((300, 300))  
        img_photo = ImageTk.PhotoImage(pil_img)
        img.config(image=img_photo)
button = ttk.Button(master=root, padding=5,  text='Choose your Picture', style='Fun.TButton', command=chooseFile)
button.grid(column=0, row=0)

entry = ttk.Entry(textvariable='Enter your Text', width=50)
entry.grid(column=1, row=0, columnspan=2, padx=20, pady=0)
watermarked_image = None

def addWatermark():
    global img_photo, watermarked_image
    image = Image.open(picture_path)
    image = image.resize((300, 300))
    draw = ImageDraw.Draw(image)
    text = entry.get()
    font_size = 40
    try:
        from PIL import ImageFont
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = None
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (image.width - text_width) // 2
    y = (image.height - text_height) // 2
    draw.text((x, y), text, font=font, fill="black")
    img_photo = ImageTk.PhotoImage(image)
    img.config(image=img_photo)
    watermarked_image = image

confirmButton = ttk.Button(master=root, padding=5, text='Confirm', style='Fun.TButton', command=addWatermark)
confirmButton.grid(column=3, row=0, padx=20, pady=20)

def savePicture():
    global watermarked_image
    save_path = filedialog.asksaveasfilename(title='Save your Watermarked Picture',defaultextension='.png',
    filetypes=[('PNG files', '*.png'), ('JPEG files', '*.jpg *.jpeg')])
    if save_path and watermarked_image:
        watermarked_image.save(save_path)
    



saveButton = ttk.Button(padding=5, text='Save Picture', style='Fun.TButton', width=50, command=savePicture)
saveButton.grid(column=1, row=9)






root.mainloop()