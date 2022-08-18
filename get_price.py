import os
import re
import csv

html_path = r"C:\Users\dsnkb\Desktop\Bored_Ape_Yacht_Club\html_Bored_Ape"
filter_last_sale_block = r"Last sale price for this NFT\" (.*)Last Sale \(Contract\)"
filter_last_sale_price = r"Displaying current value; (.+?) \(\$"

price_dict = dict()
for item in os.listdir(html_path):
    if item.endswith("html"):
        with open(os.path.join(html_path, item), "r", encoding='utf-8') as f:
            text = f.read()
            result_block = re.findall(filter_last_sale_block, text, re.S)
            result_price = re.findall(filter_last_sale_price, result_block[0])
            if len(result_price) == 1:
                price_dict[item] = result_price[0]
            else:
                price_dict[item] = 'NA'

with open(os.path.join(html_path, "Last_Sale_Price.csv"), "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['NFT_Name', 'Last_Sale_Price'])
    for i in price_dict:
        name = i.strip(".html")
        price = price_dict[i]
        writer.writerow([name, price])