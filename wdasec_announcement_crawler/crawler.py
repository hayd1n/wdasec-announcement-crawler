import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def search(url: str) -> list:
    """
    獲取搜尋列表

    Args:
        url (str): 搜尋網址

    Returns:
        list: 搜尋結果
    """
    soup = _getHTML(url)
    table = soup.select("div.area-table.rwd-straight table tbody tr")
    result = list()
    for announcement in table:
        title = announcement.select("[data-title=" + "標題" + "]")[0].select("span > a")[0]
        title_text = title.text
        title_link = title.get("href")
        post_date = announcement.select("[data-title=" + "發布日期" + "]")[0].select("span")[0].text
        views = announcement.select("[data-title=" + "點閱人氣" + "]")[0].select("span")[0].text
        result.append({
            "url": urljoin(url, title_link),
            "title": title_text,
            "post_date": post_date,
            "views": views
        })
    return result

def announcement(url: str) -> dict:
    """
    獲取公告內容

    Args:
        url (str): 公告網址

    Returns:
        dict: 公告內容
    """
    soup = _getHTML(url)
    title_text = soup.select("div.title span")[0].text
    post_date_text = soup.select("div[title=發布日期] .p span")[0].text
    views_text = soup.select("div[title=點閱人氣] .p span")[0].text
    content_text = str(soup.select("div.area-essay.page-caption-p div.div[title=''] div.p")[0])
    result = {
        "title": title_text,
        "info": {
            "post_date": post_date_text,
            "views": views_text
        },
        "content": content_text
    }
    publisher = soup.select("div[title=發布單位] .p span")
    if len(publisher) != 0:
        publisher_text = publisher[0].text
        result['info']['publisher'] = publisher_text
    check_date = soup.select("div[title=檢核日期] .p span")
    if len(check_date) != 0:
        check_date_text = check_date[0].text
        result['info']['check_date'] = check_date_text
    update_date = soup.select("div[title=更新日期] .p span")
    if len(update_date) != 0:
        update_date_text = update_date[0].text
        result['info']['update_date'] = update_date_text
    files_list = soup.select("div.group-list.file-download-multiple .in .ct .in ul li div.list-text.file-download-multiple")
    if len(files_list) != 0:
        files = list()
        for file in files_list:
            name_text = file.find("div", attrs={"data-index": "0"}).select("span a")[0].text
            in_files_list = file.find("ul", attrs={"data-index": "1"}).select("li")
            in_files = list()
            for in_file in in_files_list:
                in_file_info = in_file.select("span a")[0]
                in_file_url = in_file_info.get("href")
                in_file_type = in_file_info.text
                in_files.append({
                    "url": in_file_url,
                    "type": in_file_type
                })
            files.append({
                "name": name_text,
                "files": in_files
            })
        result['files'] = files
    links_list = soup.select("div.list-text.file-download .ct ul li")
    if len(links_list) != 0:
        links = list()
        for link in links_list:
            name = link.select("span a")
            name_text = name[0].text
            url = name[0].get("href")
            links.append({
                "name": name_text,
                "url": url
            })
        result['links'] = links
    return result

def _getHTML(url: str) -> BeautifulSoup:
    """
    解析頁面內容

    Args:
        url (str): 網址

    Returns:
        BeautifulSoup: 解析結果
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    return soup