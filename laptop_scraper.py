import re
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

laptops_list = []

for item in soup.find_all("div", class_="thumbnail"):
    title = item.find("a", class_="title").text.strip()
    price = item.find("h4", class_="price").text.strip()
    description = item.find("p", class_="description").text.strip()

    # 1. RAM nikalna
    ram_match = re.search(r"\b(\d+\s*GB)\b", description, re.IGNORECASE)
    ram = ram_match.group(1) if ram_match else "N/A"

    # 2. Storage nikalna (128GB SSD, 500GB, 1TB wagera ko dhoondna)
    storage_match = re.search(
        r"\b(\d+\s*(?:GB|TB)(?:\s*(?:SSD|HDD|eMMC))?)\b",
        description,
        re.IGNORECASE,
    )

    # Agar storage aur RAM same match ho jayein, toh agla GB match dhoondna
    if storage_match:
        all_matches = re.findall(
            r"\b(\d+\s*(?:GB|TB)(?:\s*(?:SSD|HDD|eMMC))?)\b",
            description,
            re.IGNORECASE,
        )
        if len(all_matches) > 1:
            storage = all_matches[1]  # Doosra GB/TB wala match Storage hai
        else:
            storage = storage_match.group(1)
    else:
        storage = "N/A"

    laptops_list.append({
        "Laptop Name": title,
        "Price": price,
        "RAM": ram,
        "Storage": storage,
        "Full Description": description,
    })

# Save to Excel
df = pd.DataFrame(laptops_list)
df.to_excel("laptops_data_advanced.xlsx", index=False)

print("SUCCESS: Storage aur RAM fixed! Nayi file ready hai!")