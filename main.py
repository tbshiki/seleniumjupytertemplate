# %%
print('mainが実行されます。')

import sys
from pathlib import Path

try: #.ipynb
    get_ipython().__class__.__name__
    path_file_dir = str(Path().resolve())

except NameError: # .py
    path_file_dir = str(Path(__file__).resolve().parent)

sys.path.append(str(Path(path_file_dir).resolve().parent))
sys.path.append(str(Path(path_file_dir).resolve().parent) + '\\module')
sys.path.append(path_file_dir)

import pprint
print('path一覧')
pprint.pprint(sys.path)

# %%
import os
import time

on_heroku = False
if 'HEROKU_RUN' in os.environ: # herokuの環境変数に HEROKU_RUN を設定しておく
    print('Hello, Heroku')
    on_heroku = True

# %%
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

options = Options()

if on_heroku == True:
    # Headless Chromeをあらゆる環境で起動させるオプション
    options.add_argument('--disable-gpu');
    options.add_argument('--disable-extensions');
    options.add_argument('--proxy-server="direct://"');
    options.add_argument('--proxy-bypass-list=*');
    options.add_argument('--start-maximized');
    options.add_argument('--headless');

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
time.sleep(1)

# %%
driver.get('https://www.yahoo.co.jp/')
time.sleep(1)

# %%
driver.quit()
sys.exit


