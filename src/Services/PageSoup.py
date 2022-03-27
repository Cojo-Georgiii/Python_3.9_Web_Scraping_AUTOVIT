from urllib.request import urlopen as urlReq
from bs4 import BeautifulSoup


class SoupPage:
    def __init__(self, page):
        self.page = page
        self.uClient = urlReq(self.page)
        self.pageHtml = self.uClient.read()
        self.uClient.close()
        self.sopu = BeautifulSoup(self.pageHtml, "lxml")  # SCRAPING THE TEXTS

    def ImageSoup(self):
        return self.sopu.find("div", {"class": "offer-photos"}).find_all("img", src=True)

    def TitleSoup(self):
        return self.sopu.findAll("div", {"class": "offer-summary"})

    def PriceSoup(self):
        return self.sopu.findAll("section", {"class": "offer-header"})

    def IdSoup(self):
        return self.sopu.find("div", {"class": "offer-meta"}).find_all("span", {"id": "ad_id"})

    def filterData(self):
        scrap = self.sopu.find("div", class_="offer-params").find_all("li", {"class": "offer-params__item"})
        key1 = []  # CREATING A LIST FOR THE KEYS
        values1 = []  # CREATING A LIST FOR THE VALUES
        for detail in scrap:
            valori = detail.find("div", {"class": "offer-params__value"})  # GETTING THE VALUES FROM THE HTML CODE
            keyD = detail.find("span", {"class": "offer-params__label"})  # GETTING THE KEYS FROM THE HTML CODE
            values = valori.text.strip()  # GETTING RID OF WHITE SPACES AND HTML COMMANDS
            key = keyD.text.strip()  # GETTING RID OF WHITE SPACES AND HTML COMMANDS
            key1.append(key)  # GETTING RID OF WHITE SPACES AND HTML COMMANDS
            values1.append(values)
        return dict(zip(key1, values1))  # {key1: values1 for key1, values1 in zip(key1, values1)}
# return a dictionary with the car's main values
