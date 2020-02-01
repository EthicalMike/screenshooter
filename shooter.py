from selenium import webdriver
DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)
i = 1
fh = open('input.txt')
for line in fh:
    url = line
    driver.get(url)
    name = "screenshots/" + str(i) + "_" + url + ".png"
    name = name.replace("://", "_")
    name = name.replace('\r', '').replace('\n', '')
    screenshot = driver.save_screenshot(name)
    print(name)
    i += 1
fh.close()
driver.quit()