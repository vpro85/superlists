import ipdb as ipdb
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://localhost:8000')
# ipdb.set_trace()
assert 'Congratulations' in browser.title