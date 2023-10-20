import pyautogui
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk,ImageDraw, ImageFont

# style

# class
class Window(Frame):
    def get_photo(self):
        print('cargando foto ...')
        width,height = pyautogui.size()
        print(width,height)
        # load image
        load = Image.open("screenshot.png")
        load2 = Image.open("./bg.png")
        new_imagen = load2.copy()
        new_imagen.paste(load,((width - 1066), (height-660)))
        # guardar nueva imagen
        new_imagen.save('./rocket_paste.png', quality=95)
        with_disign = Image.open('./rocket_paste.png')
        with_disign.show()
        # renderizado.
        render = ImageTk.PhotoImage(with_disign)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def __init__(self, master=None):
        Frame.__init__(self, master)
    
        self.master = master
        self.pack(fill=BOTH, expand=1)
        # general screenshot
        button=Button(root, text="ScreenShot", command=self.get_screenshot,foreground="#ffffff",background="#424242")
        button.pack(pady=10)
        # close windon.
        button_closed = Button(root, text="Salir", command=root.destroy)
        button_closed.pack(pady=12)
    
    def _interpolate(self,f_co, t_co, interval):
        det_co =[(t - f) / interval for f , t in zip(f_co, t_co)]
        for i in range(interval):
            yield [round(f + det * i) for f, det in zip(f_co, det_co)]

    def create_bg_screenshot(self):
        imgsize=(1920,1080)
        gradient = Image.new('RGBA', imgsize, color=0)
        draw = ImageDraw.Draw(gradient)

        f_co = (253, 46, 216)
        t_co = (23, 214, 255)
        for i, color in enumerate(self._interpolate(f_co, t_co, gradient.width)):
            draw.line([(i, 0), (i, gradient.width)], tuple(color), width=2)
        gradient.save('./bg.png',quallity=95)

    def get_screenshot(self):
        self.create_bg_screenshot()
        # Capturar pantalla.
        screenshot = pyautogui.screenshot()
        # resize
        screenshot.resize((512,512))
        # Guardar imagen.
        screenshot.save("screenshot.png")
        # Mostrar imagen.
        # screenshot.show()
        self.get_photo() 
    

# initial programs
root = Tk()
app = Window(root)
root.wm_title("sp cool")
root.geometry('400x200')
root.mainloop()

