import requests
from bs4 import BeautifulSoup

# 特別注意的一個點，這裡的requests.get()函式多加一個參數「verify」
# 原因是當程式在向SSL 網站傳送HTTP Request 時，程式會在當前執行環境尋找儲存該網站的安全憑證
# 所以要跳過這個步驟，只要在這用函式時，加入參數「verify」且設為「False」(此步驟可省略)
url = "https://csie.asia.edu.tw/project/semester-103"
req = requests.get(url, verify = False)
req.encoding = "utf8"

if req.status_code == 200:
    soup = BeautifulSoup(req.text, "lxml")

    fp = open("academic_year_103.txt", "w",encoding="utf8")

    # 從原始碼可以得知有兩個表(<table>)的資料要撈，所以使用find_all() 把兩個table 撈出來
    # 再來每個table 有多個行，所以撈tr 也是用find_all()
    # 最後td 的部分，是因為在輸出的時候利用縮進"\t" 來分隔各項資料    
    for table in soup.find_all("table"):

        for row in table.find_all("tr"):

            for cell in row.find_all("td"):

                t = cell.text.replace("\t", "").replace("\n", "")
                
                fp.write(t + "\t")

            fp.write("\n")

        fp.write("\n")

    fp.close()

else:
    print("No page!")
