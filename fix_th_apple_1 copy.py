import json
import requests
# идея была в том что бы сначала достать все телефоны из API и потом достать только нужные на 256гб
url = 'https://api.technodom.kz/katalog/api/v1/products/category/smartfony?city_id=5f5f1e3b4c8a49e692fefd70&limit=24&brands=apple&cl-smartphones-memory-13=256&sorting=score&price=0'
response = requests.get(url)
data = response.json()
apple = data['payload'][:20]
filter1 = []
for phone in apple:
    filter2 = {
        'sku': phone['sku'],
        'title': phone['title'],
        'price': phone['price'],
        'color': phone['color']['title']
    }
    filter1.append(filter2)
with open('apple.json', 'w', encoding='utf-8') as file:
    json.dump(filter1, file, ensure_ascii=False)

print("Телефоны найдены")
