"""
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestcomplet(webdriver.Chrome):
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    super(TestTestcomplet,self).__init__()
    self.implicitly_wait(15)
    self.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testcomplet(self):
    self.driver.get("https://www.briefmenow.org/comptia/which-sysv-init-configuration-file-should-be-modified-to-disable-the-ctrl-alt-delete-key-combination-2/")
    kek = self.driver.find_element(By.CSS_SELECTOR, "#post-content > div").getText()
    print(kek)

kek2 = webdriver.Chrome()

#kekk = TestTestcomplet()

#kekk.test_testcomplet()

kek2.get("https://www.briefmenow.org/comptia/which-sysv-init-configuration-file-should-be-modified-to-disable-the-ctrl-alt-delete-key-combination-2/")
kek = self.driver.find_element(By.CSS_SELECTOR, "#post-content > div").getText()
print(kek)"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver import *
from selenium.webdriver.support.ui import Select
import time
from datetime import date
from selenium.webdriver.chrome.options import Options

xpath1= "/html/body/div/div/section/div[2]/article/header/h1"
xpath2 = "/html/body/div/div/section/div[2]/article/div/p[2]"
xpath3 = "/html/body/div/div/section/div[2]/article/div/p[3]"
xpath4 = "/html/body/div/div/section/div[2]/article/div/p[4]"
xpath5 = "/html/body/div/div/section/div[2]/article/div/p[5]"


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)



"""elements =  browser.find_element(By.XPATH, value=xpath2)
data = elements.get_attribute('innerHTML')
print(data)"""

nbquestion = range(1,120)

for keki in nbquestion :

  browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

  browser.maximize_window()

  browser.get("https://www.briefmenow.org/comptia/which-sysv-init-configuration-file-should-be-modified-to-disable-the-ctrl-alt-delete-key-combination-2/")

  browser.find_element(By.XPATH,value="//*[@id=\"first-step\"]/header/i").click
  xpathquestion = "/html/body/div/div/aside/div[2]/div/ul/li["+str(keki)+"]"
  print(xpathquestion)
  print("kek1")
  xpathquestion = str(xpathquestion)
  print(xpathquestion)
  print("keké")
  browser.find_element(By.XPATH, value=xpathquestion).click
  #browser.find_element(By.CSS_SELECTOR, "nav.navigation:nth-child(1) > div:nth-child(2) > div:nth-child(2) > a:nth-child(1) > strong:nth-child(1)").click


  kek1 = browser.find_element(By.XPATH, value=xpath1).text
  print(kek1)
  kek2 = browser.find_element(By.XPATH, value=xpath2).get_attribute('innerHTML')
  print(kek2)
  kek3 = browser.find_element(By.XPATH, value=xpath3).get_attribute('innerHTML')
  print(kek3)
  kek4 = browser.find_element(By.XPATH, value=xpath4).get_attribute('innerHTML')
  print(kek4)
  kek5 = str(browser.find_element(By.XPATH, value=xpath5).get_attribute('innerHTML'))
  print(kek5)
  print("SUIVANT")

  browser.quit()









