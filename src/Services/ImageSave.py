import sys
import requests
import os


class ImageDownload:
    def __init__(self, img, id):
        self.images = img
        self.id = id

    def GetLinks(self):
        return [x['src'] for x in self.images]

    def SaveToDisk(self):
        try:
            # creating the folder based on their ids
            os.makedirs(f"C://Users/cojoc/PycharmProjects/scraping/photos/{self.id}")
            for i, image in enumerate(self.GetLinks()):  # using enumerate to index through the links of photos
                r = requests.get(image, stream=True)  # reuqesting to get the image
                # This will allow us to save the images in the folder based by their ids
                with open(f'C://Users/cojoc/PycharmProjects/scraping/photos/{self.id}/image_' + str(i) + '.jpg',
                          'wb') as f:
                    for chunk in r:
                        f.write(chunk)
        except:
            print("The Folder already exists")
            sys.exit()  # exiting the program if the folder with the car's id already exist
