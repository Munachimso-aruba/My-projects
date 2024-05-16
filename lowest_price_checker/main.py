import requests
from bs4 import BeautifulSoup
import smtplib
import lxml
url ="https://www.amazon.com/Apple-iPhone-13-Pro-Graphite/dp/B09LP77GDL/ref=sr_1_2?crid=RWMFGBR855KN&dib=eyJ2IjoiMSJ9.FmEQ6tzUzg6aiM8W5jePWEu8nw80Tvmp44Jb8IP6-BvgLFVszLLN852u3sXz3f0myQqKuvvvJnADUsfS5YbmMDd2m2tcjwSpXTYXdulZjFy3MLZk-WgmPe6qkJOX44lRDi6OI_fSOSmdkEz80ul1AP-8rUsV3iYqL9wzRGgIjGjt8yMt0h9goiqqJXiZgtZO4RF6DagzJNgslHkRgSydUnZSMgis-Oheh4E39WIc1do.1RCUOPNIoYsYYNKN5l6xVle1JMz9VzPtD2K30rh5tNY&dib_tag=se&keywords=iphone%2B13%2Bpro&qid=1715822268&sprefix=iphone%2B13%2Bpro%2Caps%2C103&sr=8-2&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
amazon_html = requests.get(url=url, headers=header)
amazon_html.raise_for_status()

soup = BeautifulSoup(amazon_html.text, "lxml")
price = float(soup.find("span", class_="a-offscreen").get_text().strip("$"))
if price<480.00:
    connection = smtplib.SMTP_SSL("smtp.gmail.com")
    email = "arubalezem@gmail.com"
    password = "dxzt wnfp spmq wupc"
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email,
                        to_addrs="blaizemuna@gmail.com",
                        msg="Subject:Amazon Iphone 13 pro price alert\n\n"
                            "The Iphone 13 is at an astronomically low price. Get it now "
                            f"at \n{url}")