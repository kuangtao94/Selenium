from selenium import webdriver
import time as t

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://videojs.com/")
driver.implicitly_wait(10)

video = driver.find_element_by_id("preview-player_html5_api")
#js 定位到视频
js = "return arguments[0].currentSrc"
driver.execute_script(js,video)
t.sleep(10)

#视频播放
play_js = "return arguments[0].play()"
driver.execute_script(play_js,video)
t.sleep(2)

#视频暂停
pause_js = "return arguments[0].pause()"
driver.execute_script(pause_js,video)
t.sleep(2)
driver.quit()