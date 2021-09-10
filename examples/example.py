import sys
sys.path.append("../")
import wdasec_announcement_crawler as wdasec

from pprint import pprint

pprint(wdasec.search("https://www.wdasec.gov.tw/News.aspx?n=12FE9C104388A457&sms=FDDD385F34312990"))

pprint(wdasec.announcement("https://www.wdasec.gov.tw/News_Content.aspx?n=5279F68BA6EBB1E2&sms=DD855C7DF840A224&s=4C34600FB55F226E"))