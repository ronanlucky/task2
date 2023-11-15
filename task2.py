import requests
from bs4 import BeautifulSoup

def scrape_flipkart_mobile(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract name and brand
        name = soup.find('span', {'class': '_35KyD6'}).get_text(strip=True)
        brand = soup.find('span', {'class': 'B_NuCI'}).get_text(strip=True)

        # Extracting specifications
        specifications = {}
        specs_rows = soup.find_all('tr', {'class': '_1s_Smc row'})
        for row in specs_rows:
            key = row.find('td', {'class': '_1hKmbr col col-3-12'}).get_text(strip=True)
            value = row.find('td', {'class': '_1hKmbr col col-9-12'}).get_text(strip=True)
            specifications[key] = value

        # Print the results
        print(f"Name: {name}")
        print(f"Brand: {brand}")
        print("Specifications:")
        for key, value in specifications.items():
            print(f"{key}: {value}")
    else:
        print(f"Failed to retrieve the page. Status Code: {response.status_code}")

# Example URL of a mobile phone on Flipkart
url = 'https://www.flipkart.com/samsung-galaxy-s21-fe-5g-snapdragon-888-navy-128-gb/p/itmcb8fc8eb2e82b?pid=MOBGTKQG8T9ZHJMM&lid=LSTMOBGTKQG8T9ZHJMMA4D1AC&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_e5c00873-7089-49cb-880c-7f149a3162e8_1_1BUWY8OBA8L9_MC.MOBGTKQG8T9ZHJMM&ppt=browse&ppn=browse&otracker=clp_pmu_v2_Latest%2BSamsung%2Bmobiles%2B_3_1.productCard.PMU_V2_Samsung%2BGalaxy%2BS21%2BFE%2B5G%2Bwith%2BSnapdragon%2B888%2B%2528Navy%252C%2B128%2BGB%2529_samsung-mobile-store_MOBGTKQG8T9ZHJMM_neo%2Fmerchandising_2&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Latest%2BSamsung%2Bmobiles%2B_LIST_productCard_cc_3_NA_view-all&cid=MOBGTKQG8T9ZHJMM'
scrape_flipkart_mobile(url)
