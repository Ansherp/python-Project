import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import random

class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")

        self.index = 0
        self.score = 0

        # Load image
        self.images = os.listdir("图片")
        self.images = random.sample(self.images, 10)
        self.image = Image.open(os.path.join('图片', self.images[self.index]))  # 替换为你的图片路径
        self.image = self.image.resize((200,200))
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.label = tk.Label(root, image=self.photo)
        self.label.place(x=250, y=20)
        self.label.pack(padx=10, pady=10)

        choice = self.images[self.index][:-4].split("&")
        self.random_c = random.sample([0, 1], 2)

        # Buttons
        self.button1_text = tk.StringVar()
        self.button1_text.set(choice[self.random_c[0]])
        self.button1 = tk.Button(root, textvariable=self.button1_text, command=self.button1_click, font=('Arial', 16), width=25)
        self.button1.pack(side=tk.LEFT, padx=10)

        self.button2_text = tk.StringVar()
        self.button2_text.set(choice[self.random_c[1]])
        self.button2 = tk.Button(root, textvariable=self.button2_text, command=self.button2_click, font=('Arial', 16), width=25)
        self.button2.pack(side=tk.RIGHT, padx=10)

        # Center the window and set a fixed size
        window_width = 700
        window_height = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def next_img(self):
        # Load image
        self.image = Image.open(os.path.join('图片', self.images[self.index]))  # 替换为你的图片路径
        self.image = self.image.resize((200,200))
        self.photo = ImageTk.PhotoImage(self.image)

        # Display image
        self.label = tk.Label(root, image=self.photo)
        self.label.place(x=250, y=20)

    def button1_click(self):
        self.index += 1

        self.next_img()
        if self.random_c[0] == 0:
            self.score += 1000
        else:
            messagebox.askyesno("", "You choice the wrong")
            self.root.destroy()
        print(self.score)
        if self.score >= 10000:
            messagebox.showinfo("", "Congratulations！ pass the test")
        choice = self.images[self.index][:-4].split("&")
        self.random_c = random.sample([0, 1], 2)
        self.button1_text.set(choice[self.random_c[0]])
        self.button2_text.set(choice[self.random_c[1]])

    def button2_click(self):
        self.index += 1

        self.next_img()
        if self.random_c[0] == 1:
            self.score += 1000
        else:
            messagebox.askyesno("", "You choice the wrong")
            self.root.destroy()
        if self.score >= 10000:
            messagebox.showinfo("", "Congratulations！ pass the test")
        print(self.score)
        choice = self.images[self.index][:-4].split("&")
        self.random_c = random.sample([0, 1], 2)
        self.button1_text.set(choice[self.random_c[0]])
        self.button2_text.set(choice[self.random_c[1]])


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()
