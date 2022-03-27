import sys
import pypyodbc


class DataBaseConnect:
    def __init__(self, drive1, server_name1, db_name1, Trust_Connection):
        self.driver = drive1
        self.server_name = server_name1
        self.db_name = db_name1
        self.Trust_Connection = Trust_Connection

    def GetConnection(self):  # connecting to the database server
        return pypyodbc.connect(f'Driver={self.driver}' f'Server={self.server_name}' f'Database={self.db_name}' 
                                f'Trusted_Connection={self.Trust_Connection}')

    def Inserting(self, get):
        conn = self.GetConnection().cursor()  # opening the connection to the database
        conn.execute(f"SELECT id FROM AutoVitScraping WHERE id ={(get.GetId())}")  # tryin to see if the id exists in db
        data = conn.fetchall()
        if len(data) == 0: # if the id already exists in the database it will not add the new value
            conn.execute("INSERT INTO AutoVitScraping VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)", (get.GetId(), get.GetTitle(),
                                                                                           get.GetPrice(),
                                                                                           get.GetBrand(),
                                                                                           get.GetModel(),
                                                                                           get.GetYear(),
                                                                                           get.GetKm(),
                                                                                           get.GetFuelType(),
                                                                                           get.GetHorsePower(),
                                                                                           get.GetCm3(),
                                                                                           get.GetTransmission(),
                                                                                           get.GetGearBox(),
                                                                                           get.GetBodyTypes()))
        else:  # if the id exists in the database it will close the application after displaying a message
            print("The ID already exists")
            sys.exit()
        conn.commit()  # ending the connection to the database
