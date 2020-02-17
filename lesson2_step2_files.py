import os
from selenium import webdriver
import time

try:
	link = 'http://suninjuly.github.io/file_input.html'
	browser = webdriver.Chrome()
	browser.get(link)


	current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла
	file_path = os.path.join(current_dir, 'file.txt') # добавляем к этому пути имя файла

	find_file = browser.find_element_by_id("file")
	find_file.send_keys(file_path)

	print(os.path.abspath(__file__))
	print(os.path.abspath(os.path.dirname(__file__)))

	# ждем загрузки страницы
	time.sleep(1)

finally:
 	# ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()