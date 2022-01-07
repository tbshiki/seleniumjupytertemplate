# %%
print('mainが実行されます。')

import sys
from pathlib import Path


try: # get_ipython().__class__.__name__ で判断させてもOK
    # .py
    path_file_dir = str(Path(__file__).resolve().parent)

except:
    #.ipynb
    path_file_dir = str(Path().resolve())

sys.path.append(str(Path(path_file_dir).resolve().parent))
sys.path.append(str(Path(path_file_dir).resolve().parent) + '\\module') # 自作モジュールのパスを追加
sys.path.append(path_file_dir)

import pprint
print('path一覧')
pprint.pprint(sys.path)

# %%
import os
import time

# herokuで動かす場合
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
# gspread スプレッドシートを
# https://docs.gspread.org/
# pip install gspread
# oauth2client は非推奨となったので使わない

import gspread

SPREADSHEET_KEY_PATH = './xxxxxxxxx.json' # スプレッドシートのキー(.json)のパス
SPREADSHEET_KEY = 'xxxxxxxxxxxx' # スプレッドシートのキー(URL/d/の後の文字列)

gc = gspread.service_account(filename = SPREADSHEET_KEY_PATH)
workbook = gc.open_by_key(SPREADSHEET_KEY)
worksheet = workbook.sheet1 # 一番左のシートを指定

# %%
# xlwings Excel
# https://docs.xlwings.org/
# pip install xlwings

import xlwings as xw

workbook = xw.Book('./xxxxxxxxx.xlsx') # Excelファイル(.xlsx/.xls)のパス
worksheet = workbook.sheets[0] # 一番左のシートを指定

# %%
driver.get('https://www.yahoo.co.jp/')
time.sleep(1)

# %%
driver.quit()
sys.exit


