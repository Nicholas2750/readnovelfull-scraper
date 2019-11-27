from selenium.webdriver import Chrome
import pandas as pd
import sys
import os


url         = input('Enter URL of first chapter     : ')
output_name = input('Enter name of scraping result  : ')
content     = ''

webdriver   = 'drivers/linux-chrome-driver'
browser     = Chrome(webdriver)
browser.get(url)


while True:
    next_chapter    = browser.find_element_by_id('next_chap')
    chapter_content = browser.find_element_by_id('chr-content')

    content += chapter_content.text

    if next_chapter.get_attribute('title'):
        content += os.linesep * 4
        next_chapter.click()
    else:
        browser.quit()
        break


output_file = open('results/' + output_name + '.txt', 'w')
output_file.write(content)
output_file.close()
