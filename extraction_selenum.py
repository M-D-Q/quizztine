import pytest
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