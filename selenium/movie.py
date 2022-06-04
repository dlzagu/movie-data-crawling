from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('/Users/user/Downloads/chromedriver')

url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=161967'
browser.get(url)

title = browser.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[2]/h3/a').text
print(title)

browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/a').click()
browser.switch_to.frame('pointAfterListIframe')

soup = BeautifulSoup(browser.page_source, 'lxml')
reviews = soup.find('div', attrs={'class':'score_result'}).find_all('li')
for idx, review in enumerate(reviews):
    review_ems = review.find_all('em')
    review_ps = review.find_all('p')
    reviewer_id = review_ems[1].get_text().strip()
    reviewer_date = review_ems[2].get_text()[0].replace('.','')
    star_score = review_ems[0].get_text()
    review_text = review_ps[0].get_text().strip()
    print(reviewer_id, reviewer_date, star_score)
    print(review_text)