import shutil
from subprocess import call

import requests
from prestashop_api import PrestashopApi


def to_link(name: str):
    return "-".join(name.lower().split())


call(["python", "../scraping algorithm/scraper.py"])

token = open('token.txt', 'r').read()

API_PATH = "https://localhost/api/"
api = PrestashopApi("https://localhost/api", token)

products = open("../scraping algorithm/products.csv", "r", encoding="UTF8").read().split('\n')
products.pop(0)

el_split = '\\'

manufacturers = dict()
res = api.get('manufacturers')
for m in res['manufacturers']['manufacturer']:
    manufacturers[api.get('manufacturers/' + m['@id'])['manufacturer']['name']] = m['@id']

categories = {
    "Buty": 3, "Odzież": 6, "Akcesoria": 9, "Sneakersy": 4, "Bieganie": 5, "Piłka nożna": 11,
    "Koszulki i topy sportowe": 7, "Bluzy": 8, "Spodnie": 12, "Skarpetki": 13, "Nakrycia głowy": 14,
    "Torby i plecaki": 15
}
# print(requests.get(API_PATH + 'categories/4', auth=(token, ""), verify=False).text)
# print(api.get('categories/4')['category']['nb_products_recursive'])
# exit(0)

for p in products:
    p = p.split('|')
    if len(p) <= 1:
        continue

    print(f"""----------------------------------------------------------------------------
    nazwa: {p[2]}
    kategorie: {p[3].split(el_split)}
    cena: {p[4]}
    marka: {p[5]}
    podsumowanie: {p[6]}
    opis: {p[7]}
    ilość: {p[8]}
    podatek: {p[10]}
    dostawca: {p[11]}""")

    imgs = p[1].split(el_split)

    res = api.add('products',
                  {'product':
                      {
                          "id_manufacturer": manufacturers[p[5]],
                          "id_supplier": p[11],
                          "id_category_default": categories[p[3].split(el_split)[0]],
                          "price": format(float(p[4]) / 1.23, '.6f'),
                          "name": p[2],
                          "description": p[7],
                          "description_short": p[6],
                          "link_rewrite": to_link(p[2]),

                          "id_tax_rules_group": 1,
                          "visibility": "both",
                          "active": 1,
                          "state": 1
                      }
                   }
                  )['product']

    for img in imgs:
        resource = requests.get(img, stream=True)
        if resource.status_code == 200:
            with open("img.jpg", 'wb') as f:
                shutil.copyfileobj(resource.raw, f)
        api.add_image("products/" + res['id'], "img.jpg")
