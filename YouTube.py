import pickle, os, json, time, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

def startChrome():
    # enable automation
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # do not load images (makes it faster)
    prefs = {'profile.managed_default_content_settings.images': 1}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--lang=en-US")
    # open in incognito
    options.add_argument("--incognito")
    try:
        path = ChromeDriverManager().install()
    except:
        path = './chromedriver.exe'
    wd = webdriver.Chrome(executable_path=path, options=options)
    wait = WebDriverWait(wd, 30)
    wd.get("chrome://version")
    elem = wd.find_element_by_xpath("//td[@id='profile_path']")
    Path = elem.text[:-7]
    wd.quit()

    options.add_argument('user-data-dir='+Path)
    return webdriver.Chrome(executable_path=path, options=options)


def scroll(driver):
    #try:
        while(True):
            height = driver.execute_script("return document.body.scrollHeight")
            time.sleep(random.randint(0,10))
            driver.find_element_by_tag_name('body').send_keys(Keys.END)
            if int(height)==0:
                break
        time.sleep(1)
    #except:
        ""


def run_query(video_ID):
    video_arrays = []
    driver = startChrome()
    for i in range(2):
        try:
            yt = 'https://www.youtube.com/watch?v='+ video_ID
            driver.get(yt)
            wait = WebDriverWait(driver, 20)


            scroll(driver)

            wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[@href]")))
            elems = driver.find_elements_by_xpath("//a[@href]")

            for e in elems:
                link = e.get_attribute("href")
                if 'watch?v=' in link:
                    l = link.replace('https://www.youtube.com/watch?v=', '')
                    if l[:11] not in video_arrays:
                        video_arrays.append(l[:11])
                        video_ID = l[:11]
                        break
        except:
            ""
        
    print(video_arrays)

run_query("S9CexoeVpa4")