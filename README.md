# wdasec-announcement-crawler
技能檢定中心公告爬蟲  
可以爬取技檢中心的公告資訊，特別適合爬取技能競賽的題目  

## 注意 Notice
僅支援Python3

## 相依套件 Require Modules
 - requests `pip3 install requests`
 - BeautifulSoup4 `pip3 install beautifulsoup4`

## 使用方法 Usages
### 取得搜尋列表
```python
wdasec.search(url)
```
### 取得公告內容
```python
wdasec.announcement(url)
```

## 範例 Examples
> 範例程式在 [這裡](examples/example.py)
### 取得搜尋列表
```python
wdasec.search("https://www.wdasec.gov.tw/News.aspx?n=12FE9C104388A457&sms=FDDD385F34312990")
```
返回結果
```python
[{'post_date': '110-06-03',
  'title': '[全國賽]110第51屆全國技能競賽－賽前公告試題資料',
  'url': 'https://www.wdasec.gov.tw/News_Content.aspx?n=12FE9C104388A457&sms=FDDD385F34312990&s=CC6C5A2E2C03DD6B',
  'views': '10011'},
 {'post_date': '110-08-11',
  'title': '[全國賽暨國手選拔賽]行動應用開發等5個新職類第51屆全...',
  'url': 'https://www.wdasec.gov.tw/News_Content.aspx?n=12FE9C104388A457&sms=FDDD385F34312990&s=9805C9CBAC56EE33',
  'views': '477'},
 {'post_date': '110-05-10',
  'title': '[分區賽]110第51屆分區技能競賽－正式賽試題',
  'url': 'https://www.wdasec.gov.tw/News_Content.aspx?n=12FE9C104388A457&sms=FDDD385F34312990&s=AD62BD52354CD607',
  'views': '2683'},
 {'post_date': '110-01-28',
  'title': '[分區賽]110第51屆分區技能競賽－賽前公告試題資料',
  'url': 'https://www.wdasec.gov.tw/News_Content.aspx?n=12FE9C104388A457&sms=FDDD385F34312990&s=3D42933DA696DA8C',
  'views': '57066'},
 {'post_date': '109-10-07',
  'title': '[全國賽]109第50屆全國技能競賽－正式賽試題',
  'url': 'https://www.wdasec.gov.tw/News_Content.aspx?n=12FE9C104388A457&sms=FDDD385F34312990&s=9B0EF91382ED99AD',
  'views': '6810'},
 {'post_date': '109-06-11',
  'title': '[身障賽]109第16屆全國身心障礙者技能競賽暨第10屆...',
  'url': 'https://www.wdasec.gov.tw/News_Content.aspx?n=12FE9C104388A457&sms=FDDD385F34312990&s=AD53C2E5B0B36441',
  'views': '866'},
 {'post_date': '109-01-14',
  'title': '[達人盃]109年全國職場達人盃木漆花藝類群創作技能競賽...',
  'url': 'https://www.wdasec.gov.tw/News_Content.aspx?n=12FE9C104388A457&sms=FDDD385F34312990&s=B0D1879B2399D421',
  'views': '361'},
 {'post_date': '108-02-20',
  'title': '歷屆技能競賽試題索取申請表',
  'url': 'https://www.wdasec.gov.tw/News_Content.aspx?n=12FE9C104388A457&sms=FDDD385F34312990&s=4B927814698B3A4F',
  'views': '8128'}]
  ```
### 取得公告內容
```python
wdasec.announcement("https://www.wdasec.gov.tw/News_Content.aspx?n=5279F68BA6EBB1E2&sms=DD855C7DF840A224&s=4C34600FB55F226E")
```
返回結果
```python
{'content': '<div class="p"> <p><span><br/><p>有關本次培訓應注意事項，說明如下：</p> <p '
            'align="left">一、時間:110年10月16、17日(星期六、日) '
            '共計2天；參加培訓應於當日上午9時整前完成報到（第一節課遲到15分鐘以上或中途缺課者，以未全程參與論）。</p> <p '
            'align="left">二、地點:臺南市南英高級商工職業學校(臺南市永福路一段149號)，餐飲管理大樓B1視聽教室(校區有提供停車)。</p> '
            '<p align="left">三、培訓通知函於9月10日以掛號郵寄通訊地址，請注意查收。</p> <p '
            'align="left">四、由於課程內容較多，請參訓人員務必提前研讀技術士技能檢定與發證辦法、技術士技能檢定</p> '
            '<p>作業及試場規則等2法規與監評人員有關部分、監評人員從事監評工作標準作業程序、場地</p> <p '
            'align="left">自評表、應檢人參考資料等資料，以利結訓測試(紙筆測試)作答。</p> <p '
            'align="left">五、為確認參加人員身分，請務必攜帶通知函及身分證明文件供查驗。</p> '
            '<p>六、適逢嚴重特殊傳染性肺炎(COVID-19)防疫期間，凡經防疫單位要求進行居家隔離、居家檢疫、加強自主健康管理、自主健康管理之一或會議當日有發燒等不適症狀者，請一律請假勿與會；至出席人員部分，出席時請配合單位出入口之體溫量測，自行攜帶口罩與會，並於活動進行中全程佩戴。</p> '
            '<p>七、依行政院環保政策規定，不提供紙杯，請自備杯具。</p> '
            '<p>八、基於衛生及安全考量，請參訓人員依技術士技能檢定食物製備職類單一級術科測試參考資料之監評人員應注意事項，自備白色工作服（長身、有袖、廚服或實驗衣型即可），並於進入廚房時務必著穿，相關事項說明如下：</p> '
            '<p '
            'align="left">(一)依講師授課需要，本次培訓授課地點分別為視聽教室及廚房，參訓人員進廚房時若未穿著規定服裝者，將不得進場，視同未全程參訓。</p> '
            '<p>(二)模擬監評測試時，參訓人員未穿著規定服裝者，視為嚴重缺失，不得進場應試，該項成績以不及格論。</p>\n'
            '</span></p> </div>',
 'files': [{'files': [{'type': 'zip',
                       'url': 'https://ws.wda.gov.tw/Download.ashx?u=LzAwMS9VcGxvYWQvMzE1L3JlbGZpbGUvOTc2Ny8xMzM2NTYvZjk3OGIyZjQtODJjMC00YTdjLTkzZDktZmNhYWUxYTNlM2I3LnppcA%3d%3d&n=MjE4MDDpo5%2fnianoo73lgpnogbfpoZ7ooZvnlJ%2flsIjplbfooZPnp5HmuKzoqabnm6PoqZXkurrlk6Hos4fmoLzln7noqJMuemlw'}],
            'name': '21800食物製備職類衛生專長術科測試監評人員資格培訓'}],
 'info': {'check_date': '110-09-10',
          'post_date': '110-09-10',
          'update_date': '110-09-10',
          'views': '24'},
 'title': '公告110年度技術士技能檢定「食物製備」職類衛生專長術科測試監評人員資格培訓課程資料'}
  ```
