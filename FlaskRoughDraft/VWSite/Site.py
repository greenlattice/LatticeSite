from flask import Flask, render_template, Markup
import os
import yaml

APP = Flask(__name__)

def GenChapterDict():
    ReturnDict = {}
    for item in os.listdir('static/story/'):
        with open('static/story/'+ item) as yamlfile:
            datadict = yaml.load(yamlfile.read())
            itemname = item.replace('.yml', '')
            ReturnDict[itemname] = datadict
    return ReturnDict

def GenChapterIndex(chapterdict):
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

def GenStoryFootLinks(chapterdict):
    ReturnDict = {}
    for item in chapterdict:
        NewString = ''
        itemnum = int(item)
        beforenum = itemnum - 1
        afternum = itemnum + 1
        if str(beforenum) in chapterdict:
            NewString += '<p id="left"><a href=/story/' + str(beforenum) + '>' + '<img src="/static/PrevButton.png"> </a></p>'
        if str(afternum) in chapterdict:
            NewString += '<p id="right"><a href=/story/' + str(afternum) + '>' + '<img src="/static/NextButton.png"> </a></p>'
        ReturnDict[item] = Markup(NewString)
    return ReturnDict

ChapterDict = GenChapterDict()
ChapterIndex = GenChapterIndex(ChapterDict)
StoryFootLinks = GenStoryFootLinks(ChapterDict)
AllStory = GenAllStory(ChapterDict)
links = '<p>LINKS: <a href=/>INDEX</a> <a href=/story>STORY</a> <a href=/wall>WALL OF FAME</a> <a href=/experience>EXPERIENCE</a> </p>'

@APP.route('/')
def index():
    '''Returns the index template'''
    title = 'THIS IS THE HOME PAGE'
    return render_template('index.html', title=title)

@APP.route('/story')
def story():
    '''Returns the story template'''
    title = 'We\'re Your Friends Now <h2>A History of the Friendships That Made The Green Lattice Great</h2>'
    title = Markup(title)
    return render_template('story.html', title=title, index=ChapterIndex)

@APP.route('/story/<chapter>')
def storypart(chapter):
    '''Returns the chapter template'''
    if chapter in ChapterDict:
        title = ChapterDict[chapter]['title']
        content = Markup(ChapterDict[chapter]['content'])
    else:
        title = 'PAGE NOT FOUND'
        content = 'NOTHING TO SEE HERE'
    return render_template('chapter.html', title=title, chapter=content, footlinks=StoryFootLinks[chapter])

@APP.route('/story/all')
def allstory():
    '''Returns the chapter template'''
    title = 'The Complete Story of the Green Lattice'
    return render_template('chapter.html', title=title, chapter=AllStory, footlinks='')

@APP.route('/wall')
def wall():
    '''Returns the wall of fame template'''
    title = 'ALL IN ALL YOU\'RE JUST ANOTHER BRICK IN THE LATTICE'
    return render_template('wall.html', title=title)

@APP.route('/experience')
def experience():
    '''Returns the individual experience template'''
    title = 'NOW THIS IS SOMEONE ELSE\'S STORY ALL ABOUT HOW'
    return render_template('experience.html', title=title)

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=8080)
