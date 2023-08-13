import requests
from bs4 import BeautifulSoup
import pandas as pd

#Web sitesinden verileri çekmek için yapılan işlem
url = "https://easycep.com/"
response = requests.get(url)
htmlicerigi = response.content
soup = BeautifulSoup(htmlicerigi, "html.parser")

isim = soup.find_all("div", attrs={"class": "product__typeOne--name"}) #İlan isimini aldırmak için yapılan işlem
fiyat = soup.find_all("div", attrs={"class": "product__typeOne--price"}) #İlan fiyatını aldırmak için yapılan işlem


liste = [] #bilgileri saklamak için liste oluşturma

for i in range(len(isim)):
    isim[i] = (isim[i].text).strip("\n").strip() #isim bilgilerini listenin içine eklemek için yapılan islem
    fiyat[i] = (fiyat[i].text).strip("\n").strip()  #fiyat bilgilerini listenin içine eklemek için yapılan islem
    liste.append([isim[i], fiyat[i]])

cikti = pd.DataFrame(liste, columns=["İlan Adı", "Fiyatlar"]) #bilgileri DataFrama ' ye çevirmek için yapılan işlem

# DataFrame'i ekrana yazdırma için
print(cikti)

# DataFrame'i ilanlar.txt dosyasına kaydetmek için
cikti.to_csv("ilanlar.txt", index=False, sep="\t")

# Ortalama fiyatı hesaplamak için
ortalama_fiyat = cikti["Fiyatlar"].str.replace("[^0-9]", "", regex=True).astype(int).mean()
print(f"Ortalama Fiyat: {ortalama_fiyat:.2f} TL")
