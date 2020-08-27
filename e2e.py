from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from time import sleep
from selenium.webdriver.chrome.options import Options

print("test")


def test_score_webservice():
    #ALL PRINT() FOR WATCH ALL STEP
    print(1)

    #Enter URL for the file we need read
    Url = "http://127.0.0.1:8777"
    print(2)
    #Option Chrome_option its for that's work with Jenkins
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    #Call the Webdriver (here Chrome)
    driver = webdriver.Chrome(executable_path='C:\chromedriver.exe', options=chrome_options)
    print(3)
    #Call the Url in chromedriver
    driver.get(Url)

    sleep(1)
    #take the score and test if that an int or no
    res = driver.find_element_by_id("score")
    test = int(res.text)
    print(4)
    #if test is int bigger that 1 and smaller that 1000 that's OK
    if test >= 1 and test <= 1000:
        print("True")
        return True
    else:
        print("False")
        return False
#Call Test score in the web
def main_test() :

        test = test_score_webservice()
        print(0)


main_test()
