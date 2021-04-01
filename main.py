from bs4 import BeautifulSoup
import requests


# TODO 1 Set values here:
site_of_product = "https://www.amazon.co.uk/Xbox-Wireless-Controller-Carbon-Black/dp/B08SRMPBRF/ref=pd_bxgy_img_2/261-1920978-6264915?_encoding=UTF8&pd_rd_i=B07SDFLVKD&pd_rd_r=de8c487a-4908-41c7-bcdf-aa196769fe58&pd_rd_w=k0vJi&pd_rd_wg=c4gjN&pf_rd_p=dcf35746-0212-418b-a148-30395d107b2d&pf_rd_r=6X9MNF4YN1XKC66XFWDT&refRID=6X9MNF4YN1XKC66XFWDT&th=1"
price_i_want_to_pay = 40

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"
}
response = requests.get(url=site_of_product, headers=header)
soup = BeautifulSoup(response.text, "html.parser")
name_of_item = soup.find(class_="product-title-word-break").getText().strip()
try:
    price_of_item = float(soup.find(class_="a-color-price").getText().split("£")[1])
except IndexError:
    print(f"There aren't any active offerings for {name_of_item}")
    price_of_item = 999999909099009099090
else:
    difference = price_of_item - price_i_want_to_pay


def price_check():
    if price_of_item <= price_i_want_to_pay:
        print(f"{name_of_item} is now £{price_of_item}. Consider buying it.")
    else:
        print(f"{name_of_item} is now £{price_of_item}. It's £{difference} more than you wanted to pay.")


if price_of_item == 999999909099009099090:
    pass
else:
    price_check()