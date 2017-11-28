import bs4 as bs
import urllib.request
def spojRank( str ):
  url = "http://www.spoj.com/users/"+str+"/"
  sauce = urllib.request.urlopen(url).read()
  soup = bs.BeautifulSoup(sauce,'lxml')

  table = soup.find(id='user-profile-left')
  l=[]
  for node in table.findAll('p'):
     l.append(''.join(node.findAll(text=True)))
  return(l[2].split("#")[-1].split("(")[0])

print(spojRank("utkarsh028"))

