# -*- coding: utf-8 -*-

"""
技能檢定中心公告爬蟲
~~~~~~~~~~~~~~~~~~~~~

技能檢定中心公告爬蟲
可以爬取技檢中心的公告資訊，特別適合爬取技能競賽的題目

## 使用方式Usages
### 取得搜尋列表
```
wdasec.search(url)
```
### 取得公告內容
```
wdasec.announcement(url)
```

:copyright: (c) 2021 by CRT_HAO.
:license: GPL-3.0 License, see LICENSE for more details.
"""

import requests
from bs4 import BeautifulSoup

from .crawler import search, announcement