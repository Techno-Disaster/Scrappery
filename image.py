from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

search = input("Enter Search Term: ")

params = {"q": search}
r = requests.get("https://www.bing.com/images/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
links = soup.findAll("a", {"class": "thumb"})
for item in links:
    img_obg = requests.get(item.attrs["href"])
    print("Getting Image")
    title = item.attrs["href"].split("/")[-1]
    img = Image.open(BytesIO(img_obg.content))
    img.save("./Downloaded_Images/" + title, img.format)

