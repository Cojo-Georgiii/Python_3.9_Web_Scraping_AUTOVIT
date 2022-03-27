import tkinter
from src.Models import Getters
from src.DBRepository import sqlCon
from src.Services import PageSoup
from src.Services import ImageSave


class Window:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Web Scraping")
        self.window.geometry("650x150+560+150")

        self.url = tkinter.Label(self.window, text="Enter the url")
        self.url.pack()

        self.entry = tkinter.Text(self.window, width="90", height="1")
        self.entry.pack()

        self.btn = tkinter.Button(self.window, command=lambda: [self.buttonClick(), self.GetInput()], text="Parse")
        self.btn.pack()

        self.window.mainloop()

    def GetInput(self):
        result = self.entry.get("1.0", "end")
        return result

    def buttonClick(self):
        souping = PageSoup.SoupPage(self.GetInput())
        get = Getters.CarDetails(souping.IdSoup(), souping.TitleSoup(), souping.PriceSoup(), souping.filterData())
        con = sqlCon.DataBaseConnect("{SQL SERVER};", "DESKTOP-IKGLTSA\SPARTA;", "Scraping;", "yes;")
        con.Inserting(get)
        img = ImageSave.ImageDownload(souping.ImageSoup(), get.GetId())
        img.SaveToDisk()
# pyreverse -o png <UI>