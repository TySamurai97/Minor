import bs4 as bs
import urllib.request
import pandas as pd

def validateSpoj(userHandle):
    url = "http://www.spoj.com/users/" + userHandle
    sauce = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(sauce,'lxml')
    return "@" + userHandle.strip() == soup.find_all('h4')[0].text.strip()

def createList(userName):
	#3D array: i = table number, j = row, k = column
    tables = pd.read_html('http://www.spoj.com/users/' + userName + "/")

    if(len(tables) == 0):
        quit()

    data = []

    #print("\nSolved Problems: \n")
    getTableContent(userName,tables[0], data, 1)
    
    #print("\nUnsolved Problems: \n")
    getTableContent(userName,tables[1], data, 0)

    return data

def getTableContent(userName,table, data, status):
    rows = 7
    columns = len(table[0])
    for i in range (rows):
        for j in range (columns):
            if( str(table[i][j]) != "nan" ):

            	queName = str(table[i][j])

            	queLink = "http://www.spoj.com/problems/" + queName + "/"
            	statusLink = "http://www.spoj.com/status/" + queName +"," + userName + "/"
            	print("\n", table[i][j], "\t", queLink , "\t", statusLink, end="")

            	sauce = urllib.request.urlopen(queLink).read()
            	soup = bs.BeautifulSoup(sauce, 'lxml')

            	div = soup.find_all("div", id = "problem-tags")
            	TAG = ""
            	for tag in div:
            		if(len(tag.text) > 0):
            			TAG = tag.text
            			break;

            	tg = str(TAG).split('\n')
            	T = []
            	for x in tg:
            		if(x.find('#') == 0):
            			T.append( x[1:] )
            	dataRow = [queLink, queName, status, T]
            	data.append(dataRow)


if __name__ == '__main__':
    
    #userName = input("Enter user name ").strip()
    #userName = "utkarsh028"

    #print("\nProblem Name and Tags\t\tProblem Link\t\tProblem Status\n")
    print( getSpojData('ty_samurai97') )

    


