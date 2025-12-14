from bs4 import BeautifulSoup
import requests


give_url=input("paste URL:  ")
target_class=input("paste class you want:  ")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
}
url=requests.get(give_url ,headers=headers)
data= url.text
soup= BeautifulSoup(data,"html.parser")

page_title = soup.title.text.strip() if soup.title else "No Title Found"
print(page_title)

class_items = soup.find_all(class_=target_class)
class_texts = [item.get_text(strip=True) for item in class_items]
print(class_texts)

images = soup.find_all("img")
image_links = [img.get("src") for img in images if img.get("src")]
for img in image_links:
    print(img)