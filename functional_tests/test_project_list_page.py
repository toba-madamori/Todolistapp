from selenium import webdriver
from note.models import Todo
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestProjectListPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path="C:\geckodriver.exe")

    def tearDown(self):
        self.browser.close()

    def test_no_projects_alert_is_displayed(self):
        self.browser.get(self.live_server_url)
        time.sleep(20)

