import csv
import requests


resp = requests.get("http://makeup-api.herokuapp.com/api/v1/products.json?product_tags=Organic&product_type=bronzer")
respJson = resp.json()

#print(respJson)

print(respJson[0]["id"],respJson[0]["description"])

file = open("organic_product.tsv","a")
file.write("{}\t{}\n".format(respJson[0]["id"], respJson[0]["description"]))
file.write("{}\t{}\n".format(respJson[0]["product_type"],respJson[0]["rating"]))
file.close()