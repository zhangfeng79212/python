from selenium import webdriver
import os,time,sys
chromedriver ="D:/python/testAuto/chromedriver_win32/chromedriver.exe"
os.environ["webdriver.Chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get(sys.argv[1])
driver.refresh()
driver.maximize_window()
print("start....")
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
driver.implicitly_wait(30)
driver.find_elements_by_id("textfield-1018-inputEl")[0].send_keys(sys.argv[2])
driver.find_elements_by_id("textfield-1019-inputEl")[0].send_keys(sys.argv[3])
driver.find_elements_by_id("textfield-1021-inputEl")[0].send_keys(sys.argv[4])