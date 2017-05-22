from flask import Markup
import os
import yaml

def GenChapterDict():
    ReturnDict = {}
    for item in os.listdir('static/story/'):
        with open('static/story/'+ item) as yamlfile:
            datadict = yaml.load(yamlfile.read())
            itemname = item.replace('.yml', '')
            ReturnDict[itemname] = datadict
    return ReturnDict

def GenChapterIndex(chapterdict, VW):
    ReturnString = ''
    if VW:
        ReturnString = '<a href="/vwstory/all">All Chapters</a></br>\n'
        for x in range(1,len(chapterdict)+1):
            ReturnString += '<a href=vwstory/' + str(x) + '>' + chapterdict[str(x)]['title'] + '</a></br>\n'
    else:
        ReturnString = '<a href="/story/all">All Chapters</a></br>\n'
        for x in range(1,len(chapterdict)+1):
            ReturnString += '<a href=story/' + str(x) + '>' + chapterdict[str(x)]['title'] + '</a></br>\n'
    return Markup(ReturnString)

def GenAllStory(chapterdict):
    ReturnString = ''
    for x in range(1,len(chapterdict)+1):
        ReturnString += '<h2>' + chapterdict[str(x)]['title'] + '</h2></br>\n'
        ReturnString += chapterdict[str(x)]['content'] + '</br></br>\n'
    return Markup(ReturnString)

def GenStoryFootLinks(chapterdict, VW):
    ReturnDict = {}
    for item in chapterdict:
        NewString = ''
        itemnum = int(item)
        beforenum = itemnum - 1
        afternum = itemnum + 1
        if not VW:
            if str(beforenum) in chapterdict:
                NewString += '<p id="left"><a href=/story/' + str(beforenum) + '>' + '<img src="/static/PrevButton.png"> </a></p>'
            if str(afternum) in chapterdict:
                NewString += '<p id="right"><a href=/story/' + str(afternum) + '>' + '<img src="/static/NextButton.png"> </a></p>'
            ReturnDict[item] = Markup(NewString)
        if VW:
            if str(beforenum) in chapterdict:
                NewString += '<p id="left"><a href=/vwstory/' + str(beforenum) + '>' + '<img src="/static/VWPrevButton.png"> </a></p>'
            if str(afternum) in chapterdict:
                NewString += '<p id="right"><a href=/vwstory/' + str(afternum) + '>' + '<img src="/static/VWNextButton.png"> </a></p>'
            ReturnDict[item] = Markup(NewString)
    return ReturnDict

def GenWallofFame(filename):
    userlist = []
    returnstring = '<p>'
    with open(filename, 'r') as readfile:
        for line in readfile:
            splitline = line.split(',', 1)
            username = splitline[0]
            role = splitline[1].replace('"','').strip()
            userlist.append((username, role))
    for item in userlist:
        returnstring += item[0] + '</br>' + item[1] + '</br></br>'
    returnstring += '</p>'
    return returnstring
