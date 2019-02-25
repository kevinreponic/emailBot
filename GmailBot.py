from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests

class GmailBot:

    def __init__ (self) :
        self.driver = webdriver.Firefox()
    

    def start(self) :
        driver = self.driver
        driver.get('https://gmx.com')
        time.sleep(4)
        create_account = driver.find_element_by_xpath("//*[@id='signup-button']")
        create_account.click()
        time.sleep(4)
        email_elem = driver.find_element_by_xpath('/html/body/onereg-app/div/onereg-form/div/div/form/section/section[1]/onereg-alias-check/fieldset/onereg-progress-meter/div[2]/div[2]/div/pos-input[1]/input')
        email_elem.clear()
        email_elem.send_keys('reponicbot')
        gender_elem = driver.find_element_by_xpath('/html/body/onereg-app/div/onereg-form/div/div/form/section/section[2]/onereg-progress-meter/onereg-personal-info/fieldset/div/div/onereg-radio-wrapper[1]/pos-input-radio/label/i')
        gender_elem.click()
        time.sleep(2)
        password_elem = driver.find_element_by_xpath('/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-password/fieldset/onereg-progress-meter/onereg-form-row[1]/div/div/pos-input/input')
        password_elem.send_keys('reponic1')
        time.sleep(2)
        password_confirm_elem = driver.find_element_by_xpath('/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-password/fieldset/onereg-progress-meter/onereg-form-row[2]/div/div/pos-input/input')
        password_confirm_elem.send_keys('reponic1')
        time.sleep(2)
        first_name_elem = driver.find_element_by_xpath('/html/body/onereg-app/div/onereg-form/div/div/form/section/section[2]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[1]/div/div[2]/pos-input/input')
        last_name_elem = driver.find_element_by_xpath('/html/body/onereg-app/div/onereg-form/div/div/form/section/section[2]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[2]/div/div[2]/pos-input/input')
        first_name_elem.clear()
        last_name_elem.clear()
        first_name_elem.send_keys('TestOne')
        last_name_elem.send_keys('TestTwo')
        time.sleep(2)
        country_elem = driver.find_element_by_xpath('/html/body/onereg-app/div/onereg-form/div/div/form/section/section[2]/onereg-progress-meter/onereg-personal-info/fieldset/fieldset/onereg-form-row[1]/div/div/pos-input/select')
        country_elem.send_keys('Venezuela')
        time.sleep(2)
        month_elem = driver.find_element_by_xpath('/html/body/onereg-app/div/onereg-form/div/div/form/section/section[2]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[3]/div/div/div/onereg-dob-wrapper/pos-input-dob/pos-input[1]/input')
        day_elem = driver.find_element_by_xpath('/html/body/onereg-app/div/onereg-form/div/div/form/section/section[2]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[3]/div/div/div/onereg-dob-wrapper/pos-input-dob/pos-input[2]/input')
        year_elem = driver.find_element_by_xpath('/html/body/onereg-app/div/onereg-form/div/div/form/section/section[2]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[3]/div/div/div/onereg-dob-wrapper/pos-input-dob/pos-input[3]/input')
        day_elem.clear()
        month_elem.clear()
        year_elem.clear()
        day_elem.send_keys('26')
        month_elem.send_keys('11')
        year_elem.send_keys('1990')
        time.sleep(2)
        sms_check_elem = driver.find_element_by_xpath('/html/body/onereg-app/div/onereg-form/div/div/form/section/section[4]/onereg-password-recovery/fieldset/onereg-progress-meter/div[3]/onereg-checkbox-wrapper/pos-input-checkbox/label')
        sms_check_elem.click()
        recovery_check = driver.find_element_by_xpath('/html/body/onereg-app/div/onereg-form/div/div/form/section/section[4]/onereg-password-recovery/fieldset/onereg-progress-meter/div[4]/onereg-checkbox-wrapper/pos-input-checkbox/label')
        recovery_check.click()
        time.sleep(2)
        recovery_email = driver.find_element_by_xpath('/html/body/onereg-app/div/onereg-form/div/div/form/section/section[4]/onereg-password-recovery/fieldset/onereg-progress-meter/onereg-form-row[2]/div/div[2]/pos-input/input')
        recovery_email.send_keys('kevin@reponic.org')
        time.sleep(2)
        recaptcha_key = '6Lc7GmIUAAAAAKDjVWk0q9Y5HhN5bNr1ctLZDmnw'
        service_key = 'a92be1cd15a740797a055dd80ce7a532'
        page_url = 'https://signup.gmx.com/?edition=us&lang=en#.1559516-header-signup2-1'
        request_url = 'http://2captcha.com/in.php?key=' + service_key + '&method=userrecaptcha&googlekey=' + recaptcha_key + '&pageurl=' + page_url
        resp = requests.get(request_url)
        if resp.text[0:2] != 'OK':
            quit('Service Error: error code ' + resp.text)
        captcha_id = resp.text[3:]
        fetch_url = 'http://2captcha.com/res.php?key=' + service_key + '&action=get&id=' + captcha_id
        time.sleep(5)
        print('Waiting for captcha solution...')
        for i in range (1, 10) :
            time.sleep(5)
            resp = requests.get(fetch_url)
            if resp.text[0:2] == 'OK' :
                break
        
        print('Captcha solved')        
        google_token = resp.text[3:]
        print(google_token)
        time.sleep(2)
        script = driver.execute_script('___grecaptcha_cfg.clients[0].Gq.X.callback("' + google_token + '");')
        time.sleep(2)
        submit_button = driver.find_element_by_xpath('/html/body/onereg-app/div/onereg-form/div/div/form/section/section[5]/onereg-terms-and-conditions/onereg-progress-meter/fieldset/div[3]/div/button')
        submit_button.submit()
        time.sleep(2)
kevinGmail = GmailBot()
kevinGmail.start()