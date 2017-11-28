# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 18:36:30 2017

@author: Tanay Saxena
"""

import bs4 as bs
import urllib.request

nameTable = list() # details of all submissions done by the user
Problems = list()

def verifyCF(userHandle):
    url = "http://codeforces.com/profile/" + userHandle
    sauce = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(sauce,'lxml')
    return not len(soup.find_all('div',class_="user-rank"))==0

def getTags(s):
    sauce = urllib.request.urlopen(s)
    soup = bs.BeautifulSoup(sauce,'lxml')
    roundBox = soup.find_all('div',class_='caption titled')
    
    #print(type(roundBox[1]))
    ''' 1st tag inside roundBox is the <div> for problem tags '''
    if(len(roundBox)>1):
        tagBox = roundBox[1].next_sibling.next_sibling
        #print(tagBox)
        tagList = []
        for childTag in tagBox.find_all('span'):
            tag = childTag.string
            if not tag==None:
                tag = tag.strip()
            tagList.append(tag)
        tagList = tagList[:-1]
        return tagList
    return ['']

def getPageList(s):
    sauce = urllib.request.urlopen(s)
    soup = bs.BeautifulSoup(sauce,'lxml')
    table = soup.find_all('table',class_ ='status-frame-datatable' )
    x = 0
    for tr in table:
        x = tr
    table = x
    x = []
    i=0
    for tr in table:
        if i%2==1:
            x.append(tr)
        i+=1

    table = list()
    for h in range(len(x)):
        i=0
        element = list()
        for el in x[h]:
            if i==7 or i==11:
                element.append(el)
            i+=1
        table.append(element)
    table = table[1:]
    x=0
    i=0
    for i in range(len(table)):
        lst = list()
        for url in table[i][0].find_all('a'):
            lst.append('http://codeforces.com' + url.get('href'))
            problemName = str(url.text)
            lst.append(problemName.strip())
        
        for span in table[i][1].find_all('span',class_='submissionVerdictWrapper'):
            if(span.text == 'Accepted'):
                lst.append(1)
            else:
                lst.append(0)
        '''
            Do not use getTags for all the submitted problems instead call it for solvedand
            unsolved problems individually for optimallity and speed 
        '''
        #lst.append(getTags( lst[0]))  
        nameTable.append( lst )


def createList(s):
    sauce = urllib.request.urlopen('http://codeforces.com/submissions/' + s)
    soup = bs.BeautifulSoup(sauce,'lxml')
    maxPage = 1
    span = soup.find_all('div',class_='pagination')
    
    if(len(span) == 2):
        ls = list()
        for li in span[1].find_all('li'):
            ls.append(li.text)
        
        ls = ls[-2]
        maxPage = int(ls.strip())
    maxPage+=1
    link = 'http://codeforces.com/submissions/' + s + '/page/'
    for i in range(1,maxPage):
        currLink = link + str(i)
        getPageList(currLink)
    
    dct = {}
    
    for i in range(len(nameTable)):
        if nameTable[i][1] in dct.keys():
            key = nameTable[i][1]
            if( nameTable[i][2] == 1 and dct[key][2] == 0 ):
                dct[key][2] == 1    
        else:
            dct[nameTable[i][1]] = nameTable[i]
    #print(dict)
    for i in dct.values():
        if i[2] == 0:
            Problems.append(i)
    i=0
    for prob in Problems:
        Problems[i].append( getTags(Problems[i][0]) )
        i+=1
    dct = {}
    
    for problem in nameTable:
        if (not problem[1] in dct.keys()) and problem[2]==1:
            dct[problem[1]] = problem
    #solvedProblems = list(dct.values())
    for prob in dct.values():
        Problems.append(prob)
    i=0
    for prob in Problems:
        Problems[i].append( getTags(Problems[i][0]) )
        i+=1
    return Problems
    #print(solvedProblems)


if __name__ == '__main__':
    
    # print(createList('cool_head'))
    print(getTags('http://codeforces.com/problemset/problem/859/B'))