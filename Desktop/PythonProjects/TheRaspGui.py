import tkinter as tk
from tkinter import font as tkfont
import requests
from weather import Weather,Unit
import time
import threading
import random


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
        for F in (StartPage, PageOne, PageTwo,PageThree):
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
        label = tk.Label(self, text="Raspberry PI Info Desk", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="BTC Price",
                            command=lambda: controller.show_frame("PageOne"), bg='red',font=controller.title_font)
        button2 = tk.Button(self, text="Weather",
                            command=lambda: controller.show_frame("PageTwo"),bg ='blue',font=controller.title_font)
        button3 = tk.Button(self, text="Advice of the day",
                            command=lambda: controller.show_frame("PageThree"), bg='blue', font=controller.title_font)


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
        weather_Result = textF +" " + dateF+" " + highF +"°C"

        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=weather_Result, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageThree(tk.Frame):



    def __init__(self, parent, controller):
        def test():
            threading.Timer(5.0, test).start()
            r2 = requests.get(' http://api.adviceslip.com/advice')
            advice_result = r2.json()
            label3.config(text=advice_result)
            return advice_result
        def reloadapi():
            theRoll = ['http://api.adviceslip.com/advice','http://api.adviceslip.com/advice','http://api.adviceslip.com/advice']
            threading.Timer(5.0, reloadapi ).start()
            r2 = requests.get(random.choice(theRoll))
            advice_result = r2.json()
            return advice_result



        tk.Frame.__init__(self, parent)
        self.controller = controller
        label3 = tk.Button(self, text=reloadapi(), font=controller.title_font, command=reloadapi())
        print("test")
        label3.pack(side="top", fill="x", pady=10)
        button3= tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button3.pack()






if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
