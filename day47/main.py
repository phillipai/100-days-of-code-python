import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import smtplib

load_dotenv(".env")
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

URL = "https://www.amazon.com/Resistance-INNELO-Workout-Exercise-Stackable/dp/B092HT8TL2/ref=sr_1_2?keywords=" \
      "work%2Bfrom%2Bhome%2Bfitness&pd_rd_r=caad6e53-d0a0-417d-a68f-ce8f4b163fda&pd_rd_w=qvoAu&pd_rd_wg=" \
      "s58LM&pf_rd_p=d6dae0b5-d3cf-4be0-8934-83385f36bcc9&pf_rd_r=A19XTC1PF3S9R4XDW3BE&qid=1647285684&sr=8-2&th=1"
http_headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/99.0.4844.51 Safari/537.36",
}
response = requests.get(URL, headers=http_headers)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

price = float(soup.find(name="span", class_="a-offscreen").getText()[1:])
product_name = " ".join(
    soup.find(name="span", class_="a-size-large product-title-word-break", id="productTitle").getText().split())

if price < 25.00:
    with smtplib.SMTP("smtp.outlook.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject: Alert: Amazon Price Tracker\n\n{product_name}\nis now ${price}.\n\n{URL}",
        )
