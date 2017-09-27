import bs4 as bs
import urllib.request

def getCodechefData(userName):

    userNameStatus = "/users/" + userName    #for practice questions
    data = []
    
    sauce = urllib.request.urlopen("https://www.codechef.com/users/" + userName).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    body = soup.body

    status = 2
    for x in body.find_all('article'):
        status -= 1
        if not(status == 1 or status == 0):
            break
        for y in x.find_all('a'):
            statusLink = 'https://www.codechef.com' + y.get('href');
            #print(' ', statusLink, end = "\t")

            queName = y.text
            
            game = urllib.request.urlopen(statusLink).read()
            play = bs.BeautifulSoup(game, 'lxml')
            div = play.find_all("div", class_ = "breadcrumb")
            qLink = div[0].find_all('a');
            
            lastLink = qLink[-1].get('href')
            if(lastLink == userNameStatus):
                queLink = 'https://www.codechef.com' + qLink[-2].get('href')
            else:
                queLink = 'https://www.codechef.com' + lastLink
            #print(queLink, end='\t')

            queUrl = urllib.request.urlopen(queLink).read()
            queHtml = bs.BeautifulSoup(queUrl, 'lxml')
            tags = queHtml.find_all('a', class_='problem-tag-small')

            dataRow = [queLink, queName, status, [tag.text.strip() for tag in tags]]
            #for tag in tags:
                #print(tag.text, end = "")
            data.append(dataRow)

    return data


if __name__ == '__main__':
    
    #userName = input("Enter user name ").strip()
    #userName = "utkarsh028"
    print( getCodechefData('tysamurai') )