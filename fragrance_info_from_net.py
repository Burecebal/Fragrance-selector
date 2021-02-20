import os
from googlesearch import search
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import json
import smtplib
from email.message import EmailMessage


def get_fragrance_site(fragrance):
    perfume_search = 'fragrantica:' + fragrance
    for url in search(perfume_search, tld='com', stop=1, lang='en'):
        return url


def get_info(url):
    os.environ['WDM_LOG_LEVEL'] = '0'
    os.environ['WDM_PRINT_FIRST_LINE'] = 'False'
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--ignore-certificate-errors')
    options.headless = True
    service = ChromeDriverManager(cache_valid_range=0).install()
    driver = webdriver.Chrome(service, options=options)
    try:
        driver.get(url)
        lst = []
        name = driver.find_element(By.XPATH, "//h1[contains(@class,'text-center medium-text-left')]").text
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH, '//*[@id="main-content'
                                                                                  '"]/div[1]/div['
                                                                                  '1]/div/div[2]/div['
                                                                                  '4]/div[2]/div/div['
                                                                                  '1]/div[3]/div/div')))
        ratings = driver.find_elements(By.XPATH,
                                       './/div[@style="width: 100%; height: 0.3rem; border-radius: 0.2rem; '
                                       'background: rgba(204, 224, 239, 0.4);"]')
        votes = driver.find_element(By.XPATH, "//span[contains(@itemprop,'ratingCount')]").text
        for style in ratings:
            lst.append(style.find_element(By.TAG_NAME, 'div').get_attribute('style'))
        driver.quit()
        return name, lst, votes
    except:
        driver.quit()
        raise


def seasons_ratings(lst):
    ratings = []
    for i in lst[len(lst):len(lst) - 7:-1]:
        percentage = i.split(';')[3]
        per = float(percentage.replace(' width: ', '').replace('%', ''))
        ratings.append(per)
    return ratings


class Fragrance:
    def __init__(self, name, winter, spring, summer, fall, day, night, total_votes, url):
        self.name = name
        self.winter = winter
        self.spring = spring
        self.summer = summer
        self.fall = fall
        self.day = day
        self.night = night
        self.url = url
        self.total_votes = total_votes


def save_fragrance(fragrance):
    try:
        x = 0
        with open("fragrances.json", "r") as file:
            data = json.load(file)
            for i in data:
                if i['name'] == fragrance.name:
                    x = 1
        if x:
            print('Fragrance already added.')
        else:
            data.append(fragrance.__dict__)
            with open('fragrances.json', 'w') as file:
                json.dump(data, file)
    except FileNotFoundError:
        with open("fragrances.json", 'w') as file:
            json.dump([fragrance.__dict__], file)


def delete_fragrance(fragrance_name):
    try:
        with open('fragrances.json', 'r') as file:
            data = json.load(file)
            for i in data:
                if i['name'] == fragrance_name:
                    data.remove(i)
        with open('fragrances.json', 'w') as file:
            json.dump(data, file)
        print('Fragrance deleted.')
    except FileNotFoundError:
        print('You do not have any fragrances added.')


def show_all():
    try:
        with open('fragrances.json', 'r') as file:
            data = json.load(file)
            for i in data:
                print(i)
    except FileNotFoundError:
        print('You do not have any fragrances added.')


def kill_all():
    try:
        data = []
        with open('fragrances.json', 'w') as file:
            json.dump(data, file)
        print('All deleted.')
    except FileNotFoundError:
        print('You do not have any fragrances added.')


def send_email(choice,yomail):
    email = EmailMessage()
    email['from'] = #name here
    email['to'] = yomail
    email['subject'] = 'Your fragrance random choice'
    email.set_content(f'The random fragrance choice for today is: {choice}')
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login#(your mail here, your password here)
        smtp.send_message(email)
        print('Email sent!')
