from bs4 import BeautifulSoup
import urllib2
import csv
import itertools

a=[]
b=[]
c=[]
url = urllib2.urlopen("http://freekaamaal.com")
data=url.read()
soup=BeautifulSoup(data,"lxml")
price=soup.find("div","featuredetail")
detail=[span.string for span in soup.find_all("span","text-13 black-txt prefix-5 suffix-5") ]
price1=[div.string for div in soup.find_all("div","offer-rs orange-text text-16 fltLeft prefix-5 suffix-5 font-bold")]
price2=[div.string for div in soup.find_all("div","old-rs light-txt text-12 fltLeft prefix-42 suffix-5 top-spacing-4")]

f = csv.writer(open("Data.csv", "w"))
combined=zip([detail,price1,price2])
print combined
f.writerow([combined]) 


#for i in detail:
#	d=i.text
#	a.append(d)
#for j in price1:
#	e=j.text
#	b.append(e)
#for k in price2:
#	f=k.text
#	c.append(f)

#f.writerow([combined])

    
    
   