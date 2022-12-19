from selenium import webdriver
from bs4 import BeautifulSoup

import datetime
import json
import codecs


def color_map(col):
    if col == "Bialy":
        return "Biały"
    elif col == "Bezowy":
        return "Beżowy"
    elif col == "Czern":
        return "Czerń"
    elif col == "Rozowy":
        return "Różowy"
    else:
        return col


pages = {
    "mezczyzni-sneakersy": "Sneakersy\\Buty", "mezczyzni-buty-bieganie": "Bieganie\\Buty", "mezczyzni-buty-pilka_nozna":
    "Piłka nożna\\Buty", "mezczyzni-koszulki": "Koszulki i topy sportowe\\Odzież", "mezczyzni-bluzy_treningowe":
    "Bluzy\\Odzież", "mezczyzni-spodnie": "Spodnie\\Odzież", "mezczyzni-skarpetki": "Skarpetki\\Akcesoria",
    "mezczyzni-nakrycia_glowy": "Nakrycia głowy\\Akcesoria", "mezczyzni-torby": "Torby i plecaki\\Akcesoria"
}
page_size = 48
page_num = 2
page_api = "https://www.adidas.pl/api/plp/content-engine?query="
product_api = "https://www.adidas.pl/api/products/"
offset = "&start="
browser = webdriver.Chrome()
ID = 1

fp = codecs.open('products.csv', 'w', "utf-8")
fp.write(u'\ufeff')
fp.write("ID|obraz URL|nazwa|kategorie|cena brutto|marka|podsumowanie|opis|ilość|widoczność(0)|podatek(1)|dostawca\n")

fc = codecs.open('combinations.csv', 'w', "utf-8")
fc.write(u'\ufeff')
fc.write("ID|Nr zdjęcia|Atrybuty|Wartosci|Ilosc\n")

t = datetime.datetime.now()
for page in pages.keys():
    do_comb = True
    for k in range(page_num):
        browser.get(page_api + page + offset + str(k * page_size))
        content = browser.page_source
        soup = BeautifulSoup(content, "html.parser")
        data = json.loads(soup.find('pre').text)
        data = data['raw']['itemList']['items']

        for p in data:
            browser.get(product_api + p['productId'])
            soup_product = BeautifulSoup(browser.page_source, "html.parser")
            product = json.loads(soup_product.find('pre').text)
            try:
                pods = product['product_description']['subtitle']
            except KeyError:
                pods = p['displayName']
            pods = pods.replace('\n', ' ')
            try:
                desc = product['product_description']['text']
            except KeyError:
                desc = pods
            desc = desc.replace('\n', ' ')

            img = product['view_list'][0]['image_url']
            brand = product['attribute_list']['brand']
            sup = 1
            if pages[page] in ["Skarpetki", "Nakrycia głowy", "Torby i plecaki"]:
                sup = 2

            print(ID)
            if do_comb:
                do_comb = False
                size_cat = "Rozmiar"
                if pages[page] in ["Sneakersy", "Bieganie", "Piłka nożna"]:
                    size_cat = "Rozmiar buta"

                imgs = [img]
                color = color_map(product['attribute_list']['search_color'])
                colors = [color]
                for li in product['product_link_list']:
                    c = color_map(li['search_color'])
                    if c not in colors:
                        colors.append(c)
                        imgs.append(li['image'])

                sizes = [v['size'] for v in product['variation_list']]

                if len(sizes) > 1 and len(colors) > 1:
                    for s in sizes:
                        for i, c in enumerate(colors):
                            fc.write(f"{ID}|{i+1}|{size_cat}\\Kolor|{s}\\{c}|5\n")
                elif len(sizes) > 1:
                    for s in sizes:
                        fc.write(f"{ID}|1|{size_cat}|{s}|5\n")
                elif len(colors) != 0:
                    for i, c in enumerate(colors):
                        fc.write(f"{ID}|{i+1}|Kolor|{c}|5\n")
                else:
                    do_comb = True
                    ID += 1
                    continue

                sign = '\\'
                fp.write(f"{ID}|{sign.join(imgs)}|{p['displayName']}|{pages[page]}|{p['price']}|{brand}|"
                         f"{pods}|{desc}|0|0|1|{sup}\n")
            else:
                fp.write(f"{ID}|{img}|{p['displayName']}|{pages[page]}|{p['price']}|{brand}|"
                         f"{pods}|{desc}|20|0|1|{sup}\n")
            ID += 1

browser.close()
t = datetime.datetime.now() - t
fp.close()
fc.close()
print(t.seconds // 60, "m", t.seconds % 60, "s")
