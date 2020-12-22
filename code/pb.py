#!/usr/bin/env python
'''
Check price of chair
If price drop is detected, send email
'''
from datetime import datetime

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from send_to_gmail import send_to_gmail

opts = Options()
opts.headless = True
browser = Firefox(options=opts)

url = 'https://www.pbteen.com/products/sherpa-ivory-faux-fur-groovy-swivel-chair'
browser.get(url)
div = browser.find_elements_by_class_name('pip-summary')[0]
results = div.find_elements_by_class_name('price-amount')
for result in results:
    if not result.text:
        continue

    price = float(result.text)
    if price < 100:
        # shipping price
        continue
    # most likely, this is the price
    break

if price < 399:
    subject = "Price drop"
else:
    subject = "Same price"
browser.close()

message = f"The item at {url} is priced at ${price}"
print(f"{datetime.now()}: {subject}: {message}")
send_to_gmail(subject, message)
