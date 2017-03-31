from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import requests

# Create your models here.
# models map to datbase files

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    stock = models.IntegerField(default=0)

class Click(models.Model):
	def __init__(self):
		HOST = models.CharField(max_length=200)
		REF = models.CharField(max_length=200)
		USER = models.CharField(max_length=200)
		RIP = models.CharField(max_length=200)
		HNAME = models.CharField(max_length=200)

	def set_meta(request):
		r = request
		self.HOST = r.HTTP_HOST
		self.REF = r.HTTP_REFERER
		self.USER = r.HTTP_USER_AGENT
		self.RIP = r.REMOTE_ADDR
		self.HNAME = r.REMOTE_HOST


class Yeah(models.Model):
    def __init__(self):
        headers = {'Host': 'review.wizehive.com', 'Connection':'keep-alive', 'Content-Length':'434' ,
        'Origin': 'http://review.wizehive.com', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Accept': 'text/javascript, text/html, application/xml, text/xml, */*', 'X-Prototype-Version':'1.7', 'X-Requested-With':'XMLHttpRequest',
        'Referer':'http://review.wizehive.com/voting/bpc-fau', 'Accept-Encoding':'gzip, deflate', 'Accept-Language':'en-US,en;q=0.8'
         }

        cookies = dict(WizeHive='4499r4amar18vejghet4ot73r1',__utmt='1',__utma='142613171.459024429.1490972590.1490972590.1490972590.1',__utmb='142613171.1.10.1490972590',__utmc='142613171',
           __utmz='142613171.1490972590.1.1.utmcsr=business.fau.edu|utmccn=(referral)|utmcmd=referral|utmcct=/centers/adams-center/business-plan-competition/index.aspxAlexaToolbar-ALX_NS_PH: AlexaToolbar/alx-4.0.1'
         )

        payload = {'_method':'POST',
        'data[_Token][key]':'2f6b653e392466b7893b740f64fd39933dd1b0a2',
        'data[Security][key]':'f09a9a32f100069253032d373e391f99',
        'data[SubmissionID]':'',
        'data[GroupID]':'71122',
        'data[PageID]':'4588844',
        'data[FormID]':'-3',
        'data[UploadIDs]':'',
        'data[tcuser_id]':'0',
        'data[Hidden][114721]':'0',
        'data[Form][field][114721]':'1',
        'data[_Token][fields]':'806db26091bb738c12fb87faec5fe0baabd3590b%3ASecurity.key'
        }

        session = requests.Session()
        p = session.post('http://review.wizehive.com/voting/vote/bpc-fau/45141/4588844.json' , headers=headers, cookies=cookies, data=payload)
        print(p.text)
