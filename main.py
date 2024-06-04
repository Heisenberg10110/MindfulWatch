import os
import sys
import time
import logging
import warnings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from tqdm import tqdm
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


logging.basicConfig(level=logging.CRITICAL)


warnings.filterwarnings("ignore")


original_stdout = sys.stdout
original_stderr = sys.stderr


sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')


options = Options()
options.add_argument("--log-level=3")  # 设置日志级别为3，抑制大部分日志信息


service = Service(log_path=os.devnull)


driver = webdriver.Edge(service=service, options=options)

base_url = 'https://lms.sysu.edu.cn/mod/fsresource/view.php?id='
initial_id = 71621



driver.get(
    'https://cas.sysu.edu.cn/cas/login?service=https%3A%2F%2Flms.sysu.edu.cn%2Flogin%2Findex.php%3FauthCAS%3DCAS')

sys.stdout = original_stdout
sys.stderr = original_stderr

num_videos_per_batch = int(input("请完成验证后，输入你想一次看的视频数后(和电脑性能匹配)，按Enter继续..."))
sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')

total_videos = 71755 - 71621 + 1
for i in range(0, total_videos, num_videos_per_batch):
    mmm = (i/total_videos)*100
    sys.stdout = original_stdout
    sys.stderr = original_stderr
    print(f"你正在看第{i+1}~{i+num_videos_per_batch}个视频，已完成{mmm:.2f}%")
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.devnull, 'w')
    video_ids = range(initial_id + i, initial_id + i + num_videos_per_batch)

    # TODO.....


    sys.stdout = original_stdout
    sys.stderr = original_stderr
    print("正在观看视频，等待6分钟...")

    for _ in tqdm(range(395), desc="观看进度"):
        time.sleep(1)
    print("\n")
    # 重定向标准输出和标准错误以抑制日志信息
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open(os.devnull, 'w')


    for handle in driver.window_handles[1:]:
        driver.switch_to.window(handle)
        driver.close()
    driver.switch_to.window(driver.window_handles[0])

driver.quit()