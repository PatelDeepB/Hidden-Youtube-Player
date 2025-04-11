from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import datetime
import logging
import warnings
import undetected_chromedriver as uc
from pytube import YouTube
import _thread
import ssl
from selenium.webdriver.remote.remote_connection import RemoteConnection
import json
import os

ssl._create_default_https_context = ssl._create_unverified_context

# Function to save session details
def save_session(driver, filename="session.json"):
    session_data = {
        "session_id": driver.session_id,
        "executor_url": driver.command_executor._url
    }
    with open(filename, 'w') as f:
        json.dump(session_data, f)

# Function to load session details
def load_session(filename="session.json"):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            session_data = json.load(f)
        return session_data['session_id'], session_data['executor_url']
    return None, None

def yt_video_download(current_url, title):
    try:
        yt = YouTube(current_url)
        save_path = f"/home/pragnakalpl40/Downloads/{title}.mp4"
        yt.streams.filter(progressive=True, file_extension="mp4") \
           .order_by("resolution").desc().first().download(filename=save_path)
    except Exception as e:
        print(e)

logging.basicConfig(level=logging.ERROR)
warnings.filterwarnings("ignore", category=DeprecationWarning)

chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = uc.Chrome(options=chrome_options)
driver.maximize_window()

query = "Aasma ko chhu kar dekha"
driver.get("https://www.youtube.com/results?search_query=" + query)

videos = driver.find_elements(By.CSS_SELECTOR, ".yt-simple-endpoint.style-scope.ytd-video-renderer")
first_video = videos[0]
first_video.click()

for i in range(1000000):
    time.sleep(1)
    try:
        skip_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ytp-ad-skip-button-container"))
        )
        skip_button.click()
    except:
        pass
    try:
        print("code found")
        var2 = input(
            "0 for start/stop script:\n"
            "1 for next script:\n"
            "2 to close script:\n"
            "3 for auto next on/off:\n"
            "4 for previous script:\n"
            "5 for add 5 s time sleep:\n"
            "6 for remove 5 s time sleep:\n"
            "7 to find related script:\n"
            "8 to skip unwanted script:\n"
            "9 to search the script:\n"
            "10 get the url and title:\n"
            "11 to decrease the frequency:\n"
            "12 to increase the frequency:\n"
            "14 to Download script:\n"
            "15 for next small script:\n"
            "16 for previous small script:\n"
            "17 refresh script:\n"
            "100 for Screenshot of Running element:\nEnter Number:"
        )
        if var2 == "0":
            play_button = driver.find_element(By.CSS_SELECTOR, ".ytp-play-button")
            driver.execute_script("arguments[0].click();", play_button)
            print("stop/start code executed")
        if var2 == "1":
            next_button = driver.find_element(By.CSS_SELECTOR, ".ytp-next-button")
            driver.execute_script("arguments[0].click();", next_button)
            print("Next code executed")
        if var2 == "2":
            driver.quit()
            break
        if var2 == "3":
            next_button = driver.find_element(By.CSS_SELECTOR, ".ytp-autonav-toggle-button-container")
            driver.execute_script("arguments[0].click();", next_button)
            print("auto on/off code executed")
        if var2 == "4":
            driver.back()
            print("Previous code executed")
        if var2 == "5":
            times = int(input("How many time you want to add time sleep:"))
            for i in range(times):
                actions = ActionChains(driver)
                actions.send_keys(Keys.ARROW_RIGHT + Keys.ALT).perform()
            print("jumped to ", times*5, " line")
        if var2 == "6":
            times = int(input("How many time you want to add time sleep:"))
            for j in range(times):
                actions = ActionChains(driver)
                actions.send_keys(Keys.ARROW_LEFT + Keys.ALT).perform()
            print("reversed to ", times*5, " line")
        if var2 == "7":
            try:
                playlist_button = driver.find_element(By.CSS_SELECTOR, 'a#title')
                playlist_button.click()
            except:
                print("Related script not found")
        if var2 == "8":
            try:
                playlist_button = driver.find_element(By.CSS_SELECTOR, ".ytp-skip-ad-button")
                playlist_button.click()
                print("Skip Unwanted script")
            except:
                print("Unwanted script not found")
        if var2 == "9":
            try:
                search_query = input("Which code you want to search:")
                if search_query.lower() not in ["close", ""]:
                    search_box = driver.find_element(By.NAME, "search_query")
                    search_box.clear()
                    search_box.send_keys(search_query)
                    time.sleep(2)
                    search_box.send_keys(Keys.RETURN)
                    time.sleep(2)
                    first_video = driver.find_element(By.XPATH, '//*[@id="contents"]/ytd-video-renderer[1]/div[1]/div')
                    driver.execute_script("arguments[0].click();", first_video)
                    print("founded code and running first code")
                else:
                    print("Search cancelled")
            except:
                print("searched code not found or there is error in the code")
        if var2 == "10":
            try:
                current_url = driver.current_url
                print("Random generated URL :", current_url)
                title_element = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[1]/h1/yt-formatted-string')
                print("Random generated video Title:", title_element.text)
                script_length = driver.find_element(By.CSS_SELECTOR, ".ytp-time-duration")
                print("Script Length:", script_length.text)
            except:
                print("error in getting url")
        if var2 == "11":
            try:
                times = int(input("How much frequency you want to decrease?: "))
                play_button = driver.find_element(By.CSS_SELECTOR, "#movie_player")
                play_button.click()
                play_button.click()
                if times > 5 or times < 0:
                    times = 2
                for i in range(times):
                    actions = ActionChains(driver)
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                print("frequency decreased ", times*5, " %")
            except:
                print("unable to decrease frequency")
        if var2 == "12":
            try:
                times = int(input("How much frequency you want to increase?: "))
                play_button = driver.find_element(By.CSS_SELECTOR, "#movie_player")
                play_button.click()
                play_button.click()
                if times > 5 or times < 0:
                    times = 2
                for i in range(times):
                    actions = ActionChains(driver)
                    actions.send_keys(Keys.ARROW_UP).perform()
                print("frequency increased ", times*5, " %")
            except:
                print("unable to increase frequency")
        if var2 == "13":
            new = True
            last_sub = None
            while new:
                import signal
                def timeout_handler(signum, frame):
                    raise TimeoutError
                timeout_duration = 1
                try:
                    signal.signal(signal.SIGALRM, timeout_handler)
                    signal.alarm(timeout_duration)
                    new = input()
                    signal.alarm(0)
                except TimeoutError:
                    new = True
                try:
                    for i in range(8):
                        subtitle_captions = driver.find_element(By.CSS_SELECTOR, ".ytp-caption-segment")
                        if not last_sub or subtitle_captions != last_sub:
                            if subtitle_captions.text != "English":
                                print(subtitle_captions.text)
                        last_sub = subtitle_captions
                        time.sleep(0.12)
                except:
                    subtitle_button = driver.find_element(By.CSS_SELECTOR, ".ytp-subtitles-button")
                    driver.execute_script("arguments[0].click();", subtitle_button)
                    for i in range(8):
                        subtitle_captions = driver.find_element(By.CSS_SELECTOR, ".ytp-caption-segment")
                        if not last_sub or subtitle_captions != last_sub:
                            if subtitle_captions.text != "English":
                                print(subtitle_captions.text)
                        last_sub = subtitle_captions
                        time.sleep(0.12)
        if var2 == "14":
            try:
                current_url = driver.current_url
                title = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[1]/h1/yt-formatted-string').text
                _thread.start_new_thread(yt_video_download, (current_url, title,))
                print("script added to downloads")
            except Exception as e:
                print("script not downloaded: Error occured")
        if var2 == "15":
            try:
                actions = ActionChains(driver)
                actions.send_keys(Keys.SHIFT + Keys.ARROW_DOWN).perform()
            except Exception as e:
                print("next short script not executed: Error occured")
        if var2 == "16":
            try:
                actions = ActionChains(driver)
                actions.send_keys(Keys.SHIFT + Keys.ARROW_UP).perform()
            except Exception as e:
                print("previous short script not executed: Error occured")
        if var2 == "17":
            try:
                actions = ActionChains(driver)
                actions.send_keys(Keys.CONTROL + "r").perform()
            except:
                pass
        if var2 == "100":
            print("screenshot taken successfully")
            driver.save_screenshot("../current_ss.png")
    except Exception as e:
        print("code not found")
        print(e)

driver.quit()
