# import unittest
# from selenium import webdriver
#
#
# class test_main(unittest.TestCase):
#
#     def setUp(self):
#
#         gecko = "/Users/ybalgabekov/Downloads/geckodriver"
#         self.browser = webdriver.Firefox(executable_path=gecko)
#
#     def tearDown(self):
#         self.browser.quit()
#
#     def test_main():
#         self.browser.get('http://localhost:8000')
#         print(dir(self.browser))
#
#
# if __name__ == "__main__":
#     unittest.main()