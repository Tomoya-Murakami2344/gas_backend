import os

from flask import Flask
from selenium import webdriver
from flask_cors import CORS
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# import chromedriver_autoinstaller

# chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

# options = Options()
# options.add_argument("--headless")  # ヘッドレスモードで実行
# options.add_argument("--no-sandbox")  # サンドボックスを無効化
# options.add_argument("--disable-dev-shm-usage")  # /dev/shmパーティションの使用を避ける
# options.add_argument("--disable-software-rasterizer")
# options.add_argument('--window-size=90,80')
# options.add_argument("--disable-gpu")  # GPUハードウェアアクセラレーションを無効化
# options.add_argument("--remote-debugging-port=9222")  # デバッグポートを指定
# options.add_argument("--disable-features=VizDisplayCompositor")

app = Flask(__name__)
CORS(app)

@app.route("/<user_id>/<user_password>")
def hello_world(user_id, user_password):
    print("hello world")
    # options = webdriver.ChromeOptions()
    # driver = webdriver.Remote(
    #          command_executor = 'http://selenium:4444/wd/hub',
    #          options = options
    #          )
    # driver.implicitly_wait(10)
    # driver = webdriver.Chrome()
    # driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
             command_executor = 'http://localhost:4444/wd/hub',
             options = options
             )
    
    # user_id = "chizukimmppab11000@gmail.com"
    # user_password = "5055062339@"
    print(user_id)
    print(user_password)
    name = os.environ.get("NAME", "World")
    driver.get("https://www.buyma.com/login/")
    
    id = driver.find_element('id','txtLoginId') 
    password = driver.find_element('id','txtLoginPass') 
    submit = driver.find_element('id','login_do')
    id.clear()
    password.clear()
    
    id.send_keys(user_id)
    password.send_keys(user_password)
    
    submit.click()
    time.sleep(10.0)
    
    driver.get("https://www.buyma.com/my/favitems/")
    time.sleep(10.0)
    with open("test.txt", "w") as f:
        f.write(driver.page_source)
    time.sleep(10.0)
    rule = driver.find_element(By.CLASS_NAME,'my-page-profile__name').text.strip()
    driver.quit()
    
    return f"Hello {name}! {rule}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)