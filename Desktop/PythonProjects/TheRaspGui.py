import tkinter as tk
from tkinter import font as tkfont
import requests
from weather import Weather,Unit
import time
import sys
import os,subprocess
import py_compile


class SampleApp(tk.Tk):



    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        def tick():
            time_string = time.strftime("%H:%M:%S")
            clock.config(text=time_string)
            clock.after(200,tick)


        tk.Frame.__init__(self, parent)
        self.controller = controller
        clock = tk.Label(self, text="fdf",font=("times",100,"bold"), bg="CadetBlue3")
        clock.pack(side="top", fill="x", pady=11)
        tick()
        label = tk.Label(self, text="Daniel Gorgis", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="BTC Price",
                            command=lambda: controller.show_frame("PageOne"), bg='red',font=controller.title_font)
        button2 = tk.Button(self, text="Weather",
                            command=lambda: controller.show_frame("PageTwo"),bg ='blue',font=controller.title_font)
        button3 = tk.Button(self, text="New Func")
        button1.pack()
        button2.pack()
        button3.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        def updateBtc():
            label.after(200, updateBtc())
            updateBtc()
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        BTC_result = 'The current price of bitcoin is: $' + r.json()['bpi']['USD']['rate']
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=BTC_result, font=controller.title_font,bg='red')
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        weather = Weather(unit=Unit.CELSIUS)

        location = weather.lookup_by_location('copenhagen')
        forecasts = location.forecast
        for forecast in forecasts:
            textF =(forecast.text)
            dateF = (forecast.date)
            highF = (forecast.high)
            break
        weather_Result = textF +" " + dateF+" " + highF +" Grader"

        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=weather_Result, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
