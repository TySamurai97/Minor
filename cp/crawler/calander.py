# import bs4 as bs
# import urllib.request

# url = "http://clist.by"
# sauce = urllib.request.urlopen(url).read()
# soup = bs.BeautifulSoup(sauce,'lxml')

# print(soup)


# table = soup.find(id='contests')
# l = []
# for tr in range(3,len(table.contents),2):
#     l.append(table.contents[tr])

# head = ['Start/End Time','Duration','Event']
# table = []
# for x in l:
#     a= []
#     dc = {}
#     mydivs = x.find("div", attrs={ "class" : "col-md-5 col-sm-12 start-time" }).text
#     mydivs2 = x.find("div", attrs={ "class" : "col-md-3 col-sm-6 duration" })
#     mydivs4 = x.find("div", attrs={ "class" : "col-md-7 col-sm-8 event" }) 
#     p=[]
#     q=[]
#     r=[]
#     s=[]
    
#     for string in mydivs2.strings:
#         q.append(string)   
#     for string in mydivs4.strings:
#         s.append(string) 
#     dc['Start/End Time'] = str(mydivs.strip())
#     dc['Duration']= str(q[0])
#     dc['Event']=str(s[2])                     
#     table.append(dc)

# for x in table:
#     print(x)
