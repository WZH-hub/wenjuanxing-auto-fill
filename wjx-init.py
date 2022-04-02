import time
import random
from selenium import webdriver
chrome_driver = "C:\Python39\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"

browser = webdriver.Chrome(executable_path=chrome_driver)
# 这行代码的作用是将webdriver这个属性置为undefined，防止问卷星反爬
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
                        'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})

url = '问卷星问卷网址'
browser.get(url)
time.sleep(0.5)

i = 0
# np.random.seed(0)
answers = browser.find_elements_by_css_selector('.div_question')
for answer in answers:
    try:
        # 先找到标签
        browser.execute_script("arguments[0].scrollIntoView();", answer)
        # 找到一个回答
        # 随机点击标签
        ans = answer.find_elements_by_css_selector('li')
        # print(len(ans))
        # 如果没有获取到
        if not ans:
            trs = answer.find_elements_by_css_selector('tr')
            if not trs:
                text_area = answer.find_element_by_css_selector(
                    'textarea')  # 填空框
                text_area.send_keys("无")
            else:
                for tr in trs[1:]:
                    tds = tr.find_elements_by_css_selector('td')  # 一框多选择那种
                    td = random.choice(tds)
                    td.click()
            continue
        li = random.choice(ans)
        li.click()
    except Exception as e:
        print(e)
submit_button = browser.find_element_by_css_selector('#submit_button')
submit_button.click()


button = browser.find_element_by_xpath(
    '//*[@id = "alert_box"]/div[2]/div[2]/div[2]/button')
button.click()
rect = browser.find_element_by_xpath('//*[@id = "rectTop"]')
rect.click()
time.sleep(5)
browser.quit()  # 运行完毕自动关闭浏览器
