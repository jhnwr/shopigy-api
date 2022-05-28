import shopify
from dotenv import load_dotenv
import os

load_dotenv()

session = shopify.Session(os.getenv("shopurl"), "2022-04", os.getenv("app_password"))
shopify.ShopifyResource.activate_session(session)
# product = shopify.Product()
# product.title = "Test From API 5x"
# print(product.id)  # => 292082188312
# product.save()                      # => True
# shopify.Product.exists(product.id)  # => True
# product = shopify.Product.find()
# print(product)
# Resource holding our newly created Product object
# Inspect attributes with product.attributes
# product.price = 19.99
# product.save()

# price updates
#product = shopify.Product.find(6155673338054)
#for item in product.variants:
#    print(item)
#    item.compare_at_price = 20.00
#    item.price = 15.00
#    item.save()

# add a variant:
product = shopify.Product.find(7280634888390)
v = shopify.Variant()
v.title = 'test_variant_by_byob'
v.option1 = 'test varaiants '
product.variants.append(v)
product.save()


# clear session as we are not using a context manager
shopify.ShopifyResource.clear_session()
