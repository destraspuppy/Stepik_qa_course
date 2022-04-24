from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math


link = "http://suninjuly.github.io/selects1.html"
b = webdriver.Chrome()
b.get(link)

num1 = b.find_element(By.ID, "num1").text
num2 = b.find_element(By.ID, "num2").text
sm = str(int(num1) + int(num2))
print(sm)

select = Select(b.find_element(By.ID, "dropdown"))
select.select_by_value(sm)
b.find_element(By.CSS_SELECTOR, ".btn").click()