from tkinter import *
import pyautogui
import time


class AutoClicker:
    def __init__(self, window_size, bg_color, button_size, button_color, title, sleep_time, click_option):
        self.button = None
        self.window = Tk()
        self.window.title(title)
        self.button_color = button_color
        self.button_size = button_size
        self.sleep_time = sleep_time
        self.click_option = click_option
        self.window.geometry(f'{window_size[0]}x{window_size[1]}')
        self.window.config(background=bg_color)
        self.window.attributes("-topmost", True)
        self.create_gui()
        self.window.mainloop()

    def create_gui(self):
        self.button = Button(self.window, text='start', bg=self.button_color, height=self.button_size[0],
                             width=self.button_size[1], command=self.click)
        self.button.pack(pady=30)

    def click(self):
        if self.button.cget('text') == 'start':
            self.button.config(text='stop')
            pyautogui.moveTo(600, 600)

            while self.button.cget('text') == 'stop':
                if self.click_option == 'triple click':
                    pyautogui.tripleClick()
                elif self.click_option == 'double click':
                    pyautogui.doubleClick()
                else:
                    pyautogui.click()

                self.window.update()
                time.sleep(self.sleep_time)
        else:
            self.button.config(text='start')


auto_clicker = AutoClicker((300, 100), 'black', (5, 10), 'white', 'auto_clicker', 0.001, 'triple click')
