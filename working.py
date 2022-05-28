import shopify
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


def all_products():
    products = shopify.Product.find()
    return products


def product_by_id(product_id):
    product = shopify.Product.find(product_id)
    return product


def create_product():
    # product creates OK but default variant stays
    product = shopify.Product()
    product.title = 'Pls SUB Hoody'
    product.save()
    print(product.id)
    sizes = ['Small', 'Medium', 'Large', 'X-Large']
    for size in sizes:
        variant = shopify.Variant()
        variant.option1 = size
        variant.title = size
        variant.price = 25.00
        product.variants.append(variant)
    product.save()
    print(product.variants)


def discount_item(product_id, discountPrice):
    product = shopify.Product.find(product_id)
    for item in product.variants:
        print(item)
        item.compare_at_price = item.price
        item.price = discountPrice
        print(item.price)
        item.save()


def main():
    session = shopify.Session(os.getenv("shopurl"), "2022-04", os.getenv("app_password"))
    shopify.ShopifyResource.activate_session(session)
    # items = all_products()
    # print(items[0].id)
    # discount_item(items[0].id, 12)
    # create_product()
    item = product_by_id(7360092078278)
    print(item)
    discount_item(item.id, 12)
    shopify.ShopifyResource.clear_session()


if __name__ == '__main__':
    configure()
    main()
