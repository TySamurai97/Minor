import bs4 as bs
import urllib.request

def getCfRating(user):
	url = "http://codeforces.com/profile/" + user.strip()
	sauce = urllib.request.urlopen(url).read()
	soup = bs.BeautifulSoup(sauce,'lxml')

	l = []
	for i in soup.find('div',class_='info').children:
	    l.append(i)
	x=[]
	for i in range(1,len(l),2):
	    x.append(l[i])
	l = x[1]
	x = []
	for i in l.children:
	    x.append(i)
	l = str(x[1].text).strip().split(' ')
	x = []
	for i in l:
	    if not i == '':
	        x.append(i.strip())
	rating = x[2]
	return rating


if __name__ == '__main__':
	print(getCfRating('guptautkarsh028'))