from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import logging
import rumeno_paths
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from PIL import Image

driver = webdriver.Chrome()


def csv_write(res):
    csv_file = 'rumeno.csv'
    with open(csv_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(res.keys())
        writer.writerow(res.values())


def open_rumeno():
    driver.maximize_window()

    driver.get("http://rumeno.in/")
    # print(driver.current_url)
    time.sleep(3)


def rumeno_home():
    driver.get("http://rumeno.in/home")
    time.sleep(2)


def scroll_home():

    scroll_1 = driver.find_element(By.XPATH,"//*[@id='root']/section/div[1]")
    scroll_2 = driver.find_element(By.XPATH,"//*[@id='about']/div")
    scroll_3 = driver.find_element(By.XPATH,"//*[@id='root']/section/div[3]")
    scroll_4 = driver.find_element(By.XPATH,"//*[@id='training']")
    scroll_5 = driver.find_element(By.XPATH,"//*[@id='root']/section/div[4]")

    Scroll_pages = (scroll_1,scroll_2,scroll_3,scroll_4,scroll_5)

    for i in Scroll_pages:
        driver.execute_script("arguments[0].scrollIntoView();", i)
        time.sleep(3)


def rumeno_product():
    driver.get("http://rumeno.in/products")
    time.sleep(1)


def scroll_product():
    p_1 = driver.find_element(By.XPATH, "//*[@id='root']/div[4]/img")
    p_2 = driver.find_element(By.XPATH, "//*[@id='root']/div[5]")
    p_3 = driver.find_element(By.XPATH, "//*[@id='root']/div[5]/div[2]/div")
    p_4 = driver.find_element(By.XPATH, "//*[@id='root']/div[6]")
    list_p = [p_1, p_2, p_3, p_4]

    for i in list_p:
        driver.execute_script("arguments[0].scrollIntoView();", i)
        time.sleep(3)


def rumeno_service():
    driver.get("https://rumeno.in/Services")
    time.sleep(1)


def scroll_service():
    sp_1 = driver.find_element(By.XPATH, "//*[@id='root']/section[1]")
    sp_2 = driver.find_element(By.XPATH, "//*[@id='root']/section[1]/div[5]/div")
    sp_3 = driver.find_element(By.XPATH, "//*[@id='root']/div[4]/div[1]")
    sp_4 = driver.find_element(By.XPATH, "//*[@id='root']/div[4]/div[3]")
    sp_5 = driver.find_element(By.XPATH, "//*[@id='root']/section[2]/div")
    sp_6 = driver.find_element(By.XPATH,"//*[@id='root']/div[5]")

    sp = [sp_1, sp_2, sp_3, sp_4, sp_5, sp_6]

    for r in sp:
        driver.execute_script("arguments[0].scrollIntoView();", r)
        time.sleep(3)


def rumeno_contact():
    driver.get("https://rumeno.in/contactus")
    time.sleep(1)


def scroll_contact():
    c_1 = driver.find_element(By.XPATH,"//*[@id='root']/section/div")
    c_2 = driver.find_element(By.XPATH,"//*[@id='root']/div[5]")

    cn = [c_1,c_2]
    for c in cn:
        driver.execute_script("arguments[0].scrollIntoView();", c)
        time.sleep(3)


def create_id():

    driver.find_element(By.XPATH, rumeno_paths.create_rumeno_id['open']).click()

    driver.find_element(By.XPATH, rumeno_paths.create_rumeno_id['create_new']).click()

    driver.find_element(By.XPATH, rumeno_paths.create_rumeno_id['enter_name']).send_keys('mohammad noor')
    time.sleep(1)

    driver.find_element(By.XPATH, rumeno_paths.create_rumeno_id['mobile_no']).send_keys('9859779')
    time.sleep(1)

    driver.find_element(By.XPATH, rumeno_paths.create_rumeno_id['email']).send_keys('khan786@gmail.com')
    time.sleep(1)

    driver.find_element(By.XPATH, rumeno_paths.create_rumeno_id['password']).send_keys('956887er')
    time.sleep(1)

    driver.find_element(By.XPATH,rumeno_paths.create_rumeno_id['country']).click()
    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR,"#react-select-2-option-100").click()

    driver.find_element(By.XPATH, rumeno_paths.create_rumeno_id['state']).click()
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR,"#react-select-3-option-19").click()

    driver.find_element(By.XPATH, rumeno_paths.create_rumeno_id['city']).click()
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "#react-select-4-option-102").click()

    driver.find_element(By.XPATH, rumeno_paths.create_rumeno_id['address']).send_keys('indore')
    time.sleep(1)

    driver.find_element(By.XPATH, rumeno_paths.create_rumeno_id['sign_in']).click()
    time.sleep(3)


def login_id():
    driver.find_element(By.XPATH,rumeno_paths.login_rumeno_id['open_login_button']).click()

    driver.find_element(By.XPATH,rumeno_paths.login_rumeno_id['user_name']).send_keys('mohammad noor')
    time.sleep(2)

    driver.find_element(By.XPATH,rumeno_paths.login_rumeno_id['password']).send_keys('956887er')
    time.sleep(2)

    driver.find_element(By.XPATH,rumeno_paths.login_rumeno_id['submit']).click()
    time.sleep(3)


def add_product():

    test_case1()

    driver.find_element(By.XPATH,rumeno_paths.product_click['click']).click()

    p_1 = driver.find_element(By.XPATH, "//*[@id='root']/div[4]/img")
    p_2 = driver.find_element(By.XPATH, "//*[@id='root']/div[5]")

    list = [p_1,p_2]

    for i in list:

        driver.execute_script("arguments[0].scrollIntoView();", i)
        time.sleep(3)

    driver.find_element(By.XPATH,"//*[@id='root']/div[5]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[6]/button").click()
    time.sleep(2)

    driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/div/div[1]/form/div[1]/input").send_keys("demo7")
    time.sleep(1)

    driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/div/div[1]/form/div[2]/input").send_keys("demo1234567")
    time.sleep(1)

    driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[2]/div/div/div[1]/form/div[3]/button").click()
    time.sleep(1)

    driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/button").click()
    time.sleep(1)

    driver.find_element(By.XPATH,"//*[@id='root']/div[5]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[6]/button").click()
    time.sleep(2)

    driver.find_element(By.XPATH,"//*[@id='login']").click()
    time.sleep(3)

    driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/button").click()
    time.sleep(3)

    p_1 = driver.find_element(By.XPATH, "//*[@id='root']/div[4]/img")
    p_2 = driver.find_element(By.XPATH, "//*[@id='root']/div[5]")
    p_3 = driver.find_element(By.XPATH,"//*[@id='root']/div[5]/div[2]/div/div[2]/div[2]/div")

    list = [p_1, p_2, p_3]

    for i in list:

        driver.execute_script("arguments[0].scrollIntoView();", i)
        time.sleep(3)

    driver.find_element(By.XPATH,"//*[@id='root']/div[5]/div[2]/div/div[2]/div[2]/div/div/div[2]/div[6]/button").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//*[@id='login']").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/button").click()

    p_1 = driver.find_element(By.XPATH, "//*[@id='root']/div[4]/img")
    p_2 = driver.find_element(By.XPATH, "//*[@id='root']/div[5]")
    p_3 = driver.find_element(By.XPATH, "//*[@id='root']/div[5]/div[2]/div/div[2]/div[2]/div")
    p_4 = driver.find_element(By.XPATH, "//*[@id='root']/div[5]/div[2]/div/div[2]/div[3]/div")

    list = [p_1, p_2, p_3, p_4]

    for i in list:

        driver.execute_script("arguments[0].scrollIntoView();", i)
        time.sleep(3)

    driver.find_element(By.XPATH,"//*[@id='root']/div[5]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[6]/button").click()

    driver.find_element(By.XPATH, "//*[@id='login']").click()
    time.sleep(3)
    
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/button").click()
    time.sleep(2)


def test_case1():
    try:
        open_rumeno()
        driver.find_element(By.XPATH, rumeno_paths.Choose_lang_path['english']).click()
        driver.find_element(By.XPATH, rumeno_paths.submit_button['button']).click()
        time.sleep(3)

        rumeno_home()

        result_dict = {}
        result_dict["testcase1"] = "Success"
        print("button clicked succesfull")
        csv_write(result_dict)
        return ("pass")

    except Exception as e:
        print("error in test case 1",e)

        result_dict = {}
        result_dict["testcase1"] = "failed"
        return ("failed")


# def test_case2():


def test_case3():
    try:
        test_case1()
        create_id()
        result_dict = {}
        result_dict["testcase3"] = "Success"
        print("test case 3 succesfull")
        csv_write(result_dict)
        return ("pass")

    except Exception as e:
        print("error in test case 3", e)

        result_dict = {}
        result_dict["testcase3"] = "failed"
        return ("failed")


def test_case4():
    try:
        test_case1()
        login_id()

        result_dict = {}
        result_dict["testcase4"] = "Success"
        print("test case 4 succesfull")
        csv_write(result_dict)
        return ("pass")

    except Exception as e:
        print("error in test case 4", e)

        result_dict = {}
        result_dict["testcase4"] = "failed"
        return ("failed")


def test_case5():
    try:
        test_case1()
        scroll_home()

        result_dict = {}
        result_dict["testcase5"] = "Success"
        print("test case 5 succesfull")
        csv_write(result_dict)
        return ("pass")

    except Exception as e:
        print("error in test case 5", e)

        result_dict = {}
        result_dict["testcase5"] = "failed"
        return ("failed")


def test_case6():
    try:
        test_case1()
        driver.find_element(By.XPATH, rumeno_paths.product_click['click']).click()
        rumeno_product()
        scroll_product()

        result_dict = {}
        result_dict["testcase6"] = "Success"
        print("test case 6 succesfull")
        csv_write(result_dict)
        return ("pass")

    except Exception as e:
        print("error in test case 6", e)

        result_dict = {}
        result_dict["testcase6"] = "failed"
        return ("failed")


def test_case7():
    try:
        test_case1()
        driver.find_element(By.XPATH, rumeno_paths.service_click['click']).click()
        rumeno_service()
        scroll_service()

        result_dict = {}
        result_dict["testcase7"] = "Success"
        print("test case 7 succesfull")
        csv_write(result_dict)
        return ("pass")

    except Exception as e:
        print("error in test case 7",e)

        result_dict = {}
        result_dict["testcase7"] = "failed"
        return ("failed")


def test_case8():
    try:
        test_case1()
        driver.find_element(By.XPATH, rumeno_paths.contact_link['click']).click()
        rumeno_contact()
        scroll_contact()

        result_dict = {}
        result_dict["testcase8"] = "Success"
        print("test cae 8 succesfull")
        csv_write(result_dict)
        return ("pass")

    except Exception as e:
        print("error in test case 8", e)

        result_dict = {}
        result_dict["testcase8"] = "failed"
        return ("failed")


def test_case9():
    try:
        test_case1()

        driver.find_element(By.XPATH, rumeno_paths.add_to_cart['open']).click()
        time.sleep(1)

        driver.find_element(By.XPATH, rumeno_paths.add_to_cart['close']).click()
        time.sleep(1)

        result_dict = {}
        result_dict["testcase9"] = "Success"
        print("tset case 9 succesfull")
        csv_write(result_dict)
        return ("pass")

    except Exception as e:
        print("error in test case 9", e)

        result_dict = {}
        result_dict["testcase9"] = "failed"
        return ("failed")


def check_product_name():
    try:
        test_case1()

        driver.find_element(By.XPATH, rumeno_paths.product_click['click']).click()
        p_1 = driver.find_element(By.XPATH, "//*[@id='root']/div[4]/img")
        p_2 = driver.find_element(By.XPATH, "//*[@id='root']/div[5]")

        list = [p_1, p_2]

        for i in list:
            driver.execute_script("arguments[0].scrollIntoView();", i)
            time.sleep(3)
        dict = {"Animal Supplement":"Micro Floratone","Farmhouse":"Farm House Floor Burner","Amazon":"Castrator","Human":"Rumeno Goat Milk Powder",
                "crop":"Goat"}

        driver.find_element(By.XPATH,"//*[@id='menu']/li[1]/div").click()
        time.sleep(1)

        txt = driver.find_element(By.XPATH,"//*[@id='root']/div[5]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]").text
        if dict["Animal Supplement"] == txt:
            print('1:',txt)

        else:
            print("Failed")

        driver.find_element(By.XPATH,"//*[@id='menu']/li[2]/div/span").click()
        time.sleep(2)

        txt1 = driver.find_element(By.XPATH,"//*[@id='root']/div[5]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]").text

        if dict["Farmhouse"] == txt1:
            print('2:',txt1)

        else:
            print("Failed")

        driver.find_element(By.XPATH,"//*[@id='menu']/li[3]/div/span").click()
        time.sleep(2)

        txt2 = driver.find_element(By.XPATH,"//*[@id='root']/div[5]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]").text
        if dict["Amazon"] == txt2:
            print('3:',txt2)

        else:
            print("Failed")

        driver.find_element(By.XPATH,"//*[@id='menu']/li[4]/div/span").click()
        time.sleep(1)

        txt3 = driver.find_element(By.XPATH,"//*[@id='root']/div[5]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]").text

        if dict["Human"] == txt3:
            print('4:',txt3)

        else:
            print('failed')

        driver.find_element(By.XPATH,"//*[@id='menu']/li[5]/div/span").click()
        time.sleep(1)

        txt4 = driver.find_element(By.XPATH,"//*[@id='root']/div[5]/div[2]/div/div[2]/div/div/div/div[2]/div[1]").text

        if dict["crop"] == txt4:
            print('5:',txt4)

        else:
            print("321")

        result_dict = {}
        result_dict["product name"] = "Success"
        print("check product name sucsesfull")
        csv_write(result_dict)
        return ("pass")

    except Exception as e:
        print("error in product name", e)

        result_dict = {}
        result_dict["check product name"] = "failed"
        return ("failed")


def check_product():
    try:

        test_case1()

        scroll_1 = driver.find_element(By.XPATH, "//*[@id='root']/section/div[1]")
        scroll_2 = driver.find_element(By.XPATH, "//*[@id='about']/div")
        scroll_3 = driver.find_element(By.XPATH, "//*[@id='root']/section/div[3]")

        scrll = [scroll_1,scroll_2,scroll_3]

        for i in scrll:
            driver.execute_script("arguments[0].scrollIntoView();", i)
            time.sleep(3)

        driver.find_element(By.XPATH,"//*[@id='#home']/div[3]/div[3]/div[1]/div/div/img").click()
        time.sleep(1)

        driver.find_element(By.XPATH,"//*[@id='#home']/div[3]/div[3]/div[1]/div/div/div/a/button").click()
        time.sleep(3)

        driver.find_element(By.XPATH,"//*[@id='navbarSupportedContent']/ul/li[1]/a").click()
        time.sleep(1)

        scroll_1 = driver.find_element(By.XPATH, "//*[@id='root']/section/div[1]")
        scroll_2 = driver.find_element(By.XPATH, "//*[@id='about']/div")
        scroll_3 = driver.find_element(By.XPATH, "//*[@id='root']/section/div[3]")

        scrll = [scroll_1, scroll_2, scroll_3]

        for i in scrll:
            driver.execute_script("arguments[0].scrollIntoView();", i)
            time.sleep(3)

        driver.find_element(By.XPATH,"//*[@id='#home']/div[3]/div[3]/div[2]/div/div/img").click()
        time.sleep(1)

        driver.find_element(By.XPATH,"//*[@id='#home']/div[3]/div[3]/div[2]/div/div/div/a/button").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//*[@id='navbarSupportedContent']/ul/li[1]/a").click()
        time.sleep(1)

        scroll_1 = driver.find_element(By.XPATH, "//*[@id='root']/section/div[1]")
        scroll_2 = driver.find_element(By.XPATH, "//*[@id='about']/div")
        scroll_3 = driver.find_element(By.XPATH, "//*[@id='root']/section/div[3]")

        scrll = [scroll_1, scroll_2, scroll_3]

        for i in scrll:
            driver.execute_script("arguments[0].scrollIntoView();", i)
            time.sleep(3)

        driver.find_element(By.XPATH,"//*[@id='#home']/div[3]/div[3]/div[3]/div/div/img").click()
        time.sleep(1)

        driver.find_element(By.XPATH,"//*[@id='#home']/div[3]/div[3]/div[3]/div/div/div/a/button").click()
        time.sleep(2)

        result_dict = {}
        result_dict["check product"] = "Success"
        print("check product succesfull")
        csv_write(result_dict)
        return ("pass")

    except Exception as e:
        print("error in check product", e)

        result_dict = {}
        result_dict["check product"] = "failed"
        return ("failed")


def check_pages():
    try:
        test_case1()

        scroll_home()
        dict = {"home": "https://rumeno.in/home",
                "about": "https://rumeno.in/home#about",
                "product": "https://rumeno.in/products",
                "training": "https://rumeno.in/home#training"}

        driver.find_element(By.XPATH,"//*[@id='#home']/div[4]/div/div[2]/div[2]/ul/li[1]/a").click()
        time.sleep(1)

        home = driver.current_url

        if dict["home"] == home:
            print("success",home)

        else:
            print("failed")

        scroll_home()
        driver.find_element(By.XPATH,"//*[@id='#home']/div[4]/div/div[2]/div[2]/ul/li[2]/a").click()
        time.sleep(1)

        about = driver.current_url

        if dict["about"] == about:
            print("success",about)

        else:
            print("failed")

        scroll_2 = driver.find_element(By.XPATH, "//*[@id='about']/div")
        scroll_3 = driver.find_element(By.XPATH, "//*[@id='root']/section/div[3]")
        scroll_4 = driver.find_element(By.XPATH, "//*[@id='training']")
        scroll_5 = driver.find_element(By.XPATH, "//*[@id='root']/section/div[4]")

        Scroll_pages = (scroll_2, scroll_3, scroll_4, scroll_5)

        for i in Scroll_pages:
            driver.execute_script("arguments[0].scrollIntoView();", i)
            time.sleep(3)

        driver.find_element(By.XPATH,"//*[@id='#home']/div[4]/div/div[2]/div[2]/ul/li[3]/a").click()
        time.sleep(2)

        product = driver.current_url

        if dict["product"] == product:
            print("success",product)

        else:
            print("failed")

        driver.find_element(By.XPATH, "//*[@id='navbarSupportedContent']/ul/li[1]/a").click()
        time.sleep(1)

        scroll_home()
        driver.find_element(By.XPATH,"//*[@id='#home']/div[4]/div/div[2]/div[2]/ul/li[4]/a").click()
        time.sleep(1)

        training = driver.current_url

        if dict["training"] == training:
            print("success",training)

        else:
            print("failed")


        result_dict = {}
        result_dict["check pages"] = "Success"
        print("check pages succesfull")
        csv_write(result_dict)
        return ("pass")

    except Exception as e:
        print("error in check pages", e)

        result_dict = {}
        result_dict["check pages"] = "failed"
        return ("failed")


def check_training():
    try:
        test_case1()

        dict = {"Goat farming":"Personal information",
                "Advance farmhouse":"Advance Farmhouse Training",
                "Pro training":"Pro-Training for Commercial Goat Farming",
                "Webinar":"Coming soon"}

        scroll_1 = driver.find_element(By.XPATH, "//*[@id='root']/section/div[1]")
        scroll_2 = driver.find_element(By.XPATH, "//*[@id='about']/div")
        scroll_3 = driver.find_element(By.XPATH, "//*[@id='root']/section/div[3]")
        scroll_4 = driver.find_element(By.XPATH, "//*[@id='training']")

        Scroll_pages = (scroll_1, scroll_2, scroll_3, scroll_4)

        for i in Scroll_pages:
            driver.execute_script("arguments[0].scrollIntoView();", i)
            time.sleep(3)

        driver.find_element(By.XPATH,"//*[@id='v-pills-home-tab']").click()

        driver.save_screenshot("image.png")
        image = Image.open("image.png")
        image.show()

        # txt = driver.find_element(By.XPATH,"//*[@id='v-pills-home']/h4[1]").text
        #
        # if dict["Goat farming"] == txt:
        #     print("1",txt, ":True")
        #
        # else:
        #     print("False")

        driver.find_element(By.XPATH,"//*[@id='v-pills-profile-tab']").click()
        time.sleep(1)
        driver.save_screenshot("image.png")
        image1 = Image.open("image.png")
        image1.show()

        # txt1 = driver.find_element(By.XPATH,"//*[@id='v-pills-profile']/h4").text
        #
        # if dict["Advance farmhouse"] == txt1:
        #     print("2",txt1, ":True")
        #
        # else:
        #     print("Failed")

        driver.find_element(By.XPATH,"//*[@id='v-pills-messages-tab']").click()
        time.sleep(1)
        driver.save_screenshot("image.png")
        image2 = Image.open("image.png")
        image2.show()

        # txt2 = driver.find_element(By.XPATH,"//*[@id='v-pills-messages']/h4").text
        #
        # if dict["Pro training"] == txt2:
        #     print("3",txt2, ":True")
        #
        # else:
        #     print("False")

        driver.find_element(By.XPATH,"//*[@id='v-pills-settings-tab']").click()
        time.sleep(1)
        driver.save_screenshot("image.png")
        image3 = Image.open("image.png")
        image3.show()

        # txt3 = driver.find_element(By.XPATH,"//*[@id='v-pills-settings']/h4").text
        #
        # if dict["Webinar"] == txt3:
        #     print("4",txt3, ":True")
        #
        # else:
        #      print("False")


        result_dict = {}
        result_dict["check training"] = "Success"
        print("check training succesfull")
        csv_write(result_dict)
        return ("pass")

    except Exception as e:
        print("error in check training", e)

        result_dict = {}
        result_dict["check training"] = "failed"
        return ("failed")


def product_pages():
    try:
        test_case1()
        driver.find_element(By.XPATH,rumeno_paths.product_click['click']).click()
        scroll_product()

        dict = {"page 1 ":"Neonato", "page 2":"Digesto Plus", "page 3":"Rumeno Micro Flora"}
        driver.find_element(By.XPATH,"//*[@id='root']/div[5]/div[2]/div/div[2]/ul/li[6]/a").click()

        p1 = driver.find_element(By.XPATH,"//*[@id='root']/div[5]/div[2]/div/div[2]/div[3]/div")
        p2 = driver.find_element(By.XPATH,"//*[@id='root']/div[5]/div[2]/div/div[2]/div[2]/div")
        p3 = driver.find_element(By.XPATH,"//*[@id='root']/div[5]/div[2]/div/div[2]/div[1]/div")

        p = [p1, p2, p3]

        for i in p:
            driver.execute_script("arguments[0].scrollIntoView();", i)
            time.sleep(3)

        txt = driver.find_element(By.XPATH,"//*[@id='root']/div[5]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]").text

        if dict["page 1 "] == txt:
            print(txt)

        else:
            print("Failed")

        p1 = driver.find_element(By.XPATH, "//*[@id='root']/div[5]/div[2]/div/div[2]/div[1]/div")
        p2 = driver.find_element(By.XPATH, "//*[@id='root']/div[5]/div[2]/div/div[2]/div[2]/div")
        p3 = driver.find_element(By.XPATH, "//*[@id='root']/div[5]/div[2]/div/div[2]/div[3]/div")

        p = [p1, p2, p3]

        for i in p:
            driver.execute_script("arguments[0].scrollIntoView();", i)
            time.sleep(3)

        driver.find_element(By.XPATH, "//*[@id='root']/div[5]/div[2]/div/div[2]/ul/li[6]/a").click()

        p1 = driver.find_element(By.XPATH, "//*[@id='root']/div[5]/div[2]/div/div[2]/div[3]/div")
        p2 = driver.find_element(By.XPATH, "//*[@id='root']/div[5]/div[2]/div/div[2]/div[2]/div")
        p3 = driver.find_element(By.XPATH, "//*[@id='root']/div[5]/div[2]/div/div[2]/div[1]/div")

        p = [p1, p2, p3]

        for i in p:
            driver.execute_script("arguments[0].scrollIntoView();", i)
            time.sleep(3)

        txt1 = driver.find_element(By.XPATH,"//*[@id='root']/div[5]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]").text

        if dict["page 2"] == txt1:
            print(txt1)

        else:
            print("Failed")

        p1 = driver.find_element(By.XPATH, "//*[@id='root']/div[5]/div[2]/div/div[2]/div[1]/div")
        p2 = driver.find_element(By.XPATH, "//*[@id='root']/div[5]/div[2]/div/div[2]/div[2]/div")
        p3 = driver.find_element(By.XPATH, "//*[@id='root']/div[5]/div[2]/div/div[2]/div[3]/div")

        p = [p1, p2, p3]

        for i in p:
            driver.execute_script("arguments[0].scrollIntoView();", i)
            time.sleep(3)

        driver.find_element(By.XPATH,"//*[@id='root']/div[5]/div[2]/div/div[2]/ul/li[6]/a").click()

        p1 = driver.find_element(By.XPATH, "//*[@id='root']/div[5]/div[2]/div/div[2]/div[2]/div")
        p2 = driver.find_element(By.XPATH, "//*[@id='root']/div[5]/div[2]/div/div[2]/div[1]/div")

        p = [p1, p2]

        for i in p:
            driver.execute_script("arguments[0].scrollIntoView();", i)
            time.sleep(3)

        txt2 = driver.find_element(By.XPATH,"//*[@id='root']/div[5]/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]").text

        if dict["page 3"] == txt2:
            print(txt2)

        else:
            print("Failed")

        result_dict = {}
        result_dict["product pages"] = "Success"
        print("product pages succesfull")
        csv_write(result_dict)
        return ("pass")

    except Exception as e:
        print("error in product pages", e)

        result_dict = {}
        result_dict["product pages"] = "failed"
        return ("failed")


def check():
    test_case1()
    scroll_home()
    get = driver.find_element(By.XPATH,"//img[@class='ps-4 logo']").get_attribute("src")
    print(get)


if __name__ == "__main__":
    # test_case1()
    # test_case3()
    # test_case4()
    # test_case5()
    # test_case6()
    # test_case7()
    # test_case8()
    # test_case9()
    # add_product()
    # check_product_name()
    # check_product()
    # check_pages()
    # check_training()
    # product_pages()
    check()