import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence
import time
import os
import random

image_file = None
class ImageApp:
    def __init__(self, root):

        root.title("Image Viewer")
        self.window = root
        self.index = 0
        self.score = 0
        # Center the window and set a fixed size
        window_width = 700
        window_height = 500
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        root.configure(bg='white')

        # Load image
        self.images = os.listdir("图片")
        self.images = random.sample(self.images, 10)

        global image_file
        image_file = tk.PhotoImage(file=os.path.join('图片', self.images[self.index]))
        self.canvas = tk.Canvas(root, bg='white', width=200, height=200)  # width=图片的长 height=图片的长(不替换，写在等于号的后面)
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=image_file)  # 这里的width/2和height/2分别替换为长的二分之一和高的二分之一
        self.canvas.config(highlightthickness=0)
        self.canvas.pack(padx=10, pady=10)

        choice = self.images[self.index][:-4].split("&")
        self.random_c = random.sample([0, 1], 2)

        # Buttons
        self.button1_text = tk.StringVar()
        self.button1_text.set(choice[self.random_c[0]])
        self.button1 = tk.Button(root, textvariable=self.button1_text, command=self.button1_click, font=('Arial', 16), width=25)
        # self.button1.place(x=480, y=550)
        self.button1.pack(side=tk.LEFT, padx=10)

        self.button2_text = tk.StringVar()
        self.button2_text.set(choice[self.random_c[1]])
        self.button2 = tk.Button(root, textvariable=self.button2_text, command=self.button2_click, font=('Arial', 16), width=25)
        # self.button2.place(x=20, y=550)
        self.button2.pack(side=tk.RIGHT, padx=10)

    def next_img(self):
        # Load image
        global image_file
        image_file = tk.PhotoImage(file=os.path.join('图片', self.images[self.index]))
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=image_file)  # 这里的width/2和height/2分别替换为长的二分之一和高的二分之一

        # Display image

    def button1_click(self):
        self.index += 1
        if self.random_c[0] == 0:
            self.score += 1000
            im = Image.open(r"gif/good.gif")
            # GIF图片流的迭代器
            iter = ImageSequence.Iterator(im)
            # frame就是gif的每一帧，转换一下格式就能显示了
            self.canvas.delete(self.image)
            for frame in iter:
                frame = frame.resize((200, 140))
                pic = ImageTk.PhotoImage(frame)
                self.canvas.create_image(0, 0, anchor='nw', image=pic)
                time.sleep(0.05)
                self.window.update_idletasks()  # 刷新
                self.window.update()
        else:
            im = Image.open(r"gif/wrong.gif")
            # GIF图片流的迭代器
            iter = ImageSequence.Iterator(im)
            self.canvas.delete(self.image)
            # frame就是gif的每一帧，转换一下格式就能显示了
            for frame in iter:
                frame = frame.resize((200, 200))
                pic = ImageTk.PhotoImage(frame)
                self.canvas.create_image(0, 0, anchor='nw', image=pic)
                time.sleep(0.1)
                self.window.update_idletasks()  # 刷新
                self.window.update()
            # messagebox.askyesno("", "You choice the wrong")
            self.root.destroy()
        print(self.score)
        if self.score >= 10000:

            self.canvas.delete(self.image)
            # frame就是gif的每一帧，转换一下格式就能显示了
            while True:
                im = Image.open(r"gif/结束.gif")
                # GIF图片流的迭代器
                iter = ImageSequence.Iterator(im)
                for frame in iter:
                    frame = frame.resize((200, 200))
                    pic = ImageTk.PhotoImage(frame)
                    self.canvas.create_image(0, 0, anchor='nw', image=pic)
                    time.sleep(0.1)
                    self.window.update_idletasks()  # 刷新
                    self.window.update()
            # messagebox.showinfo("", "Congratulations！ pass the test")
        choice = self.images[self.index][:-4].split("&")
        self.random_c = random.sample([0, 1], 2)
        self.button1_text.set(choice[self.random_c[0]])
        self.button2_text.set(choice[self.random_c[1]])
        self.next_img()

    def button2_click(self):
        self.index += 1
        if self.random_c[0] == 1:
            self.score += 1000
            im = Image.open(r"gif/good.gif")
            # GIF图片流的迭代器
            iter = ImageSequence.Iterator(im)
            self.canvas.delete(self.image)
            # frame就是gif的每一帧，转换一下格式就能显示了
            for frame in iter:
                frame = frame.resize((200, 200))
                pic = ImageTk.PhotoImage(frame)
                self.canvas.create_image(0, 0, anchor='nw', image=pic)
                time.sleep(0.05)
                self.window.update_idletasks()  # 刷新
                self.window.update()
        else:
            im = Image.open(r"gif/wrong.gif")
            # GIF图片流的迭代器
            iter = ImageSequence.Iterator(im)
            # frame就是gif的每一帧，转换一下格式就能显示了
            self.canvas.delete(self.image)
            for frame in iter:
                frame = frame.resize((200, 200))
                pic = ImageTk.PhotoImage(frame)
                self.canvas.create_image(0, 0, anchor='nw', image=pic)
                time.sleep(0.1)
                self.window.update_idletasks()  # 刷新
                self.window.update()
            # messagebox.askyesno("", "You choice the wrong")
            self.root.destroy()
        if self.score >= 10000:

            self.canvas.delete(self.image)
            # frame就是gif的每一帧，转换一下格式就能显示了
            while True:
                im = Image.open(r"gif/结束.gif")
                # GIF图片流的迭代器
                iter = ImageSequence.Iterator(im)
                for frame in iter:
                    frame = frame.resize((200, 200))
                    pic = ImageTk.PhotoImage(frame)
                    self.canvas.create_image(0, 0, anchor='nw', image=pic)
                    time.sleep(0.1)
                    self.window.update_idletasks()  # 刷新
                    self.window.update()
            # messagebox.showinfo("", "Congratulations！ pass the test")
        print(self.score)
        choice = self.images[self.index][:-4].split("&")
        self.random_c = random.sample([0, 1], 2)
        self.button1_text.set(choice[self.random_c[0]])
        self.button2_text.set(choice[self.random_c[1]])
        self.next_img()


if __name__ == "__main__":
    window = tk.Tk()
    ImageApp(window)
    window.mainloop()
