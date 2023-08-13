import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://easycep.com/"
response = requests.get(url)
htmlicerigi = response.content
soup = BeautifulSoup(htmlicerigi, "html.parser")
isim = soup.find_all("div", attrs={"class": "product__typeOne--name"}) 
fiyat = soup.find_all("div", attrs={"class": "product__typeOne--price"})

liste = []

for i in range(len(isim)):
    isim[i] = (isim[i].text).strip("\n").strip()
    fiyat[i] = (fiyat[i].text).strip("\n").strip()

    liste.append([isim[i], fiyat[i]])

cikti = pd.DataFrame(liste, columns=["İlan Adı", "Fiyatlar"])

# DataFrame'i ekrana yazdırma
print(cikti)

# DataFrame'i ilanlar.txt dosyasına kaydetme
cikti.to_csv("ilanlar.txt", index=False, sep="\t")

# Ortalama fiyatı hesaplama
ortalama_fiyat = cikti["Fiyatlar"].str.replace("[^0-9]", "", regex=True).astype(int).mean()
print(f"Ortalama Fiyat: {ortalama_fiyat:.2f} TL")
