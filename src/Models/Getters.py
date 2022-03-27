class CarDetails:

    def __init__(self, id, title, price, dictionar):
        self.id = id
        self.title = title
        self.price = price
        self.dictionar = dictionar

    def GetId(self):
        for x in self.id:
            return x.text.strip()

    def GetTitle(self):
        # ceva = self.title.findAll("div", {"class": "offer-summary"})
        for title in self.title:
            current_title = title.find("span", {"class": "offer-title big-text fake-title"})
            return current_title.text.strip()

    def GetPrice(self):
        for pret in self.price:
            pretSelect = pret.find_all("span", {"class": "offer-price__number"})
            # cv = pret.select("span.offer-price__number")
            return pretSelect[0].text.strip().replace("        EUR", "a").replace(" ", ".").replace("a", " €")

    def GetBrand(self):
        if "Marca" in self.dictionar:
            return self.dictionar['Marca']
        return ""

    def GetModel(self):
        if "Model" in self.dictionar:
            return self.dictionar['Model']
        return ""

    def GetYear(self):
        if "Anul" in self.dictionar:
            return self.dictionar['Anul']
        return ""

    def GetKm(self):
        if "Km" in self.dictionar:
            return self.dictionar['Km'].replace(" km", "").replace(" ", ".")
        return ""

    def GetFuelType(self):
        if "Combustibil" in self.dictionar:
            return self.dictionar['Combustibil']
        return ""

    def GetHorsePower(self):
        if "Putere" in self.dictionar:
            return self.dictionar['Putere']
        return ""

    def GetCm3(self):
        if "Capacitate cilindrica" in self.dictionar:
            return self.dictionar['Capacitate cilindrica'].replace(" cm3", "").replace(" ", ".")
        return ""

    def GetTransmission(self):
        if "Transmisie" in self.dictionar:
            return self.dictionar['Transmisie']
        return ""

    def GetGearBox(self):
        if "Cutie de viteze" in self.dictionar:
            return self.dictionar['Cutie de viteze']
        return ""

    def GetBodyTypes(self):
        if "Tip Caroserie" in self.dictionar:
            return self.dictionar['Tip Caroserie']
        return ""
