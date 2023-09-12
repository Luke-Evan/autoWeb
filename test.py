from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

ACCOUNT = "221250170"
PASSWORD = "rlbnjdx3312"

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Edge()

wd.get("https://xk.nju.edu.cn/")
wd.implicitly_wait(10)
account = wd.find_element(By.ID, "loginName")
account.send_keys(ACCOUNT)
password = wd.find_element(By.ID, "loginPwd")
password.send_keys(PASSWORD)
input()
titles = wd.find_elements(By.CSS_SELECTOR, "ul#cvPageHeadTab li")
for title in titles:
    if "收藏" in title.get_attribute('outerHTML'):
        title.click()
while True:
    finish = True
    while finish:
        sleep(0.5)
        wd.refresh()
        courses = wd.find_elements(By.CSS_SELECTOR, "div table tbody tr")
        for course in courses:
            try:
                if (("已满" not in course.get_attribute("outerHTML"))
                        and "仙林校区" in course.get_attribute("outerHTML")):
                    # and ("乒乓球" in course.get_attribute("outerHTML") or "羽毛球" in course.get_attribute("outerHTML"))
                    star = course.find_element(By.CSS_SELECTOR, "a.cv-choice")
                    wd.execute_script("arguments[0].scrollIntoView();", course)
                    star.click()
                    finish = False
                    break
            except:
                break
        print(1)
    make_sure = wd.find_element(By.CSS_SELECTOR, "div#cvDialog  div.cv-foot div.cv-sure")
    make_sure.click()
    t = input()
    if t == 1:
        break