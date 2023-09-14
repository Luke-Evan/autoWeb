from selenium import webdriver
from selenium.webdriver.common.by import By

LoginName = "13155404501"
PWD = "rlbxxt3312"

wd = webdriver.Edge()
wd.get('http://nju.fanya.chaoxing.com/')
wd.implicitly_wait(10)

# 1. 点击登录，跳转到输入界面
login = wd.find_element(By.XPATH, 'ml/body/div[1]/div[1]/div[4]/p/span/label/input')
login.click()
for handle in wd.window_handles:
    # 先切换到该窗口
    wd.switch_to.window(handle)
    # 得到该窗口的标题栏字符串，判断是不是我们要操作的那个窗口
    if '登录' in wd.title:
        # 如果是，那么这时候WebDriver对象就是对应的该该窗口，正好，跳出循环，
        break

# 2. 输入账号密码登录
loginName = wd.find_element(By.CSS_SELECTOR, '#phone')
loginName.send_keys(LoginName)
Password = wd.find_element(By.CSS_SELECTOR, '#pwd')
Password.send_keys(PWD)
logButton = wd.find_element(By.CSS_SELECTOR, '#phoneLoginBtn')
logButton.click()

# 3. 进入对应课程界面
wd.switch_to.frame('frame_content')
course = wd.find_element(By.XPATH, '//*[@id="course_226013153_79470563"]/div[2]/h3/a/span')
course.click()
for handle in wd.window_handles:
    wd.switch_to.window(handle)
    if '党的纪律建设' in wd.title:
        break

# 4. 进入前逐个检查视频任务点是否完成
chapter = wd.find_element(By.XPATH, '//*[@id="nav_63346"]')
chapter.click()
wd.switch_to.frame('frame_content-zj')
tips = wd.find_elements(By.CLASS_NAME, 'bntHoverTips')
for tip in tips:
    if '已完成' in tip.get_attribute('textContent'):
        tipClick = tip.find_element(By.XPATH, './..')
        tipClick.click()
        break

# 5.进入视频界面后逐个检查任务点是否完成
for handle in wd.window_handles:
    wd.switch_to.window(handle)
    if '学生学习界面' in wd.title:
        break

views = wd.find_elements(By.CLASS_NAME, 'prevHoverTips')
for view in views:
    if '已完成' in view.get_attribute('textContent'):
        viewClick = view.find_element(By.XPATH, './../preceding-sibling::*[1]')
        viewClick.click()
        break

# 6.开始未完成的视频
wd.switch_to.frame("iframe")
wd.switch_to.frame(wd.find_element(By.TAG_NAME, 'iframe'))
beginButton = wd.find_element(By.XPATH, '//*[@id="video"]tton')
beginButton.click()

ariaValue = wd.find_element(By.XPATH, '//*[@id="video"]/div[5]/div[5]/div')
ariaNow = ariaValue.get_attribute('aria-valuenow')
print(type(ariaNow))
print(ariaNow)
