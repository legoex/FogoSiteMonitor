import urllib.request

ruUrls = [
    'https://fogo.ua/ru/produkcija/',
    'https://fogo.ua/ru/product-category/dizelnye-jelektrostancii/',
    'https://fogo.ua/ru/product-category/benzinovye-jelektrostancii/',
    'https://fogo.ua/ru/product-category/traktornie-generatory/',
    'https://fogo.ua/ru/product-category/dizelnye-jelektrostancii/s-dvigatelem-mitsubishi/',
    'https://fogo.ua/ru/product-category/dizelnye-jelektrostancii/s-dvigatelem-iveco/',
    'https://fogo.ua/ru/product-category/dizelnye-jelektrostancii/s-dvigatelem-scania/',
    'https://fogo.ua/ru/product-category/dizelni-elektrostancii/z-dvigunom-doosan/',
    'https://fogo.ua/ru/product-category/dizelnye-jelektrostancii/s-dwigatelem-scania/',
]

ukrUrls = [
    'https://fogo.ua/produkcija/',
    'https://fogo.ua/product-category/dizelnye-jelektrostancii/',
    'https://fogo.ua/product-category/benzinovye-jelektrostancii/',
    'https://fogo.ua/product-category/traktornie-generatory/',
    'https://fogo.ua/product-category/dizelnye-jelektrostancii/s-dvigatelem-mitsubishi/',
    'https://fogo.ua/product-category/dizelnye-jelektrostancii/s-dvigatelem-iveco/',
    'https://fogo.ua/product-category/dizelnye-jelektrostancii/s-dvigatelem-scania/',
    'https://fogo.ua/product-category/dizelni-elektrostancii/z-dvigunom-doosan/',
    'https://fogo.ua/product-category/dizelnye-jelektrostancii/s-dwigatelem-scania/',
]
print("Check the ru status code:")
for url in ruUrls:
    try:
        print(str(url) + " -> " + str(urllib.request.urlopen(url).getcode()))
    except:
        print(str(url) + " -> BROKEN!!!!!!!!")
print("Check the ukr status code:")
for url in ukrUrls:
    try:
        print(str(url) + " -> " + str(urllib.request.urlopen(url).getcode()))
    except:
        print(str(url) + " -> BROKEN!!!!!!!!")
