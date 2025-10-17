import json

def load_categories():
    with open("data/category.json", encoding="utf-8") as f:
        return json.load(f)

def load_products(q=None):
    with open("data/product.json", encoding="utf-8") as f:
        products = json.load(f)

        if q:
            products = [p for p in products if p["name"].find(q)>=0]

        return products


if __name__ == "__main__":
    print(load_categories())
