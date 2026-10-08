# E-Commerce Laptops Web Scraper & Data Extractor

A Python-based web scraper that extracts e-commerce laptop listings, cleans unstructured specs using Regex, and exports formatted structured data into Microsoft Excel (.xlsx).

 Features
#- **Automated Web Scraping:** Uses `requests` and `BeautifulSoup` to scrape live product listings.
#- **Regex Spec Extraction:** Automatically parses RAM and Storage capacities from messy text descriptions into separate clean columns.
- **Excel Export:** Exports cleaned data directly into structured Excel (`.xlsx`) workbooks using `pandas` and `openpyxl`.

##  Tech Stack
- **Language:** Python 3.x
- **Libraries:** Requests, BeautifulSoup4, Pandas, OpenPyXL, Re (Regex)

## Project Structure
- `laptop_scraper.py` - Main Python scraping script.
- `laptops_data_advanced.xlsx` - Cleaned output Excel file.
Python web scraper to extract laptops data (Name, Price, RAM, Storage) into Excel.
