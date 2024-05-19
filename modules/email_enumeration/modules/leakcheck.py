# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.chrome.service import Service

# def leakcheck(email):
#     try:
#         options = webdriver.ChromeOptions()
#         options.add_experimental_option('excludeSwitches', ['enable-logging'])
#         options.add_argument("--headless=new")
#         options.add_argument("--disable-notifications")
#         options.add_argument("--disable-popup-blocking")
        
#         PATH = "C:\Program Files (x86)\chromedriver.exe"
#         driver = webdriver.Chrome(options=options, service=Service(PATH))
        
#         driver.get("https://leakcheck.io/")
#         search_box = driver.find_element(By.NAME, "data")
#         search_box.send_keys(email)
#         search_button = driver.find_element(By.ID, "button-search")
#         search_button.click()
#         time.sleep(2)
#         # Check if table exists
#         search_table = driver.find_element(By.ID, "search-table")
#         search_table_body = search_table.find_element(By.TAG_NAME, "tbody")
#         search_table_rows = search_table_body.find_elements(By.TAG_NAME, "tr")
#         data = {}
#         for row in search_table_rows:
#             columns = row.find_elements(By.TAG_NAME, "td")
#             source = columns[0].text
#             last_breach = columns[1].text
#             data[source] = last_breach
#         # Close the driver
#         driver.quit()
#         # Return data
#         return data
#     except Exception as e:
#         error_response = {  "error": str(e)  }
#         return error_response
