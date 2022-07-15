# %%
print("mainが実行されます。")

import os
import sys
from pathlib import Path

on_py = False
try:  # .py
    path_file_dir = str(Path(__file__).resolve().parent)  # get_ipython().__class__.__name__ で判断させてもOK
    print("Hello, .py")
    on_py = True

except:  # .ipynb
    from IPython import get_ipython

    # 外部オリジナルモジュール変更時自動リロード
    # %reload_ext autoreload
    # %autoreload 2

    path_file_dir = str(Path().resolve())
    print("Hello, .ipynb")

sys.path.append(path_file_dir)
sys.path.append(str(Path(path_file_dir).resolve().parent))
sys.path.append(os.path.join(str(Path(path_file_dir).resolve().parent), "module"))  # 自作モジュール置き場のパスを追加

import pprint

print("path一覧")
pprint.pprint(sys.path)

# herokuで動かす場合
on_heroku = False
if "HEROKU_RUN" in os.environ:  # herokuの環境変数に HEROKU_RUN を設定しておく
    print("Hello, Heroku")
    on_heroku = True

# %%
import time
from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), "JST")
today = datetime.now(JST).strftime("%y%m%d")

# %%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.alert import Alert

# ChromeDriverをダウンロードしなくていいようにするライブラリ pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

# download_dir = "xxxxxxxxxxxx"
# savefile_dir = "xxxxxxxxxxxx"
# prefs = {
#     "download.default_directory": download_dir,  # ダウンロード先のディレクトリ
#     "savefile.default_directory": savefile_dir,  # 印刷保存先のディレクトリ
# }
# options.add_experimental_option("prefs", "")  # ファイルと印刷保存先を変更

# options.add_experimental_option("detach", True)  # プログラムが終わってもブラウザを起動したままにする
# options.add_argument("--kiosk-printing")  # 印刷ダイアログを表示せずそのまま印刷する

# profile_dir = "xxxxxxxxxxxx"  # プロファイルのディレクトリ
# options.add_argument("--user-data-dir=" + profile_dir) # プロファイルを変更

if on_heroku == True:
    # Headless Chromeをあらゆる環境で起動させるオプション
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument('--proxy-server="direct://"')
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
time.sleep(1)

# %%
# gspread Google スプレッドシート / pip install gspread
# https://docs.gspread.org/
# oauth2client は非推奨となったので使わない

import gspread

SPREADSHEET_KEY_PATH = "./xxxxxxxxx.json"  # スプレッドシートのキー(.json)のパス
SPREADSHEET_KEY = "xxxxxxxxxxxx"  # スプレッドシートのキー(URL/d/の後の文字列)

gc = gspread.service_account(filename=SPREADSHEET_KEY_PATH)
workbook = gc.open_by_key(SPREADSHEET_KEY)
worksheet = workbook.sheet1  # 一番左のシートを指定

# %%
# xlwings Excel / pip install xlwings
# https://docs.xlwings.org/
# 必要に応じて xlwings addin install でアドオンをインストールすること

import xlwings as xw

workbook = xw.Book("./xxxxxxxxx.xlsx")  # Excelファイル(.xlsx/.xls)のパス
worksheet = workbook.sheets[0]  # 一番左のシートを指定

# %%
driver.get("https://www.yahoo.co.jp/")
time.sleep(1)

# %%
driver.quit()
sys.exit

