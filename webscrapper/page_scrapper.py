from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from . import text_cleaning as tc

def get_max_pages(url):
    options = Options()
    options.add_argument('--headless=new')
    browser = webdriver.Chrome(options=options)
    browser.get(url)
    page = browser.page_source
    soup = BeautifulSoup(page, 'html.parser')
    pages = soup.find_all('span', class_='button__content heading-5')
    num_pages = tc.get_page_numbers(pages)
    return num_pages
