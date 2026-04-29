from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
driver = webdriver.Chrome()
url = "https://www.producthunt.com/search?q=mental+health+ai"
driver.get(url)
#TIME TO LOAD
time.sleep(10)
#CSS selector is complete
elements = driver.find_elements(By.CSS_SELECTOR, 'a[data-test="post-name"]')
app_names = []
for item in elements:
    app_names.append({"name": item.text})
with open('products.json', 'w') as f:
    json.dump(app_names, f, indent=4)
driver.quit()
print('done')
