#!/usr/bin/env python
'''
Check price of chair
If price drop is detected, send email
'''

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from send_to_gmail import send_to_gmail

opts = Options()
opts.headless = True
browser = Firefox(options=opts)

url = 'https://www.pbteen.com/products/sherpa-groovy-swivel-chair/'
browser.get(url)
results = browser.find_elements_by_class_name('price-amount')
price = float(results[0].text)
if price < 399:
    subject = "Price drop"
else:
    subject = "Same price"
browser.close()

message = f"The item at {url} is priced at ${price}"
send_to_gmail(subject, message)
