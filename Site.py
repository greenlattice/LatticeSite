from flask import Flask, render_template, Markup, send_from_directory, request
import os
import yaml
import supportFuncs

APP = Flask(__name__, static_folder='static')

ChapterDict = supportFuncs.GenChapterDict()
ChapterIndex = supportFuncs.GenChapterIndex(ChapterDict, False)
StoryFootLinks = supportFuncs.GenStoryFootLinks(ChapterDict, False)
VWChapterIndex = supportFuncs.GenChapterIndex(ChapterDict, True)
VWStoryFootLinks = supportFuncs.GenStoryFootLinks(ChapterDict, True)
AllStory = supportFuncs.GenAllStory(ChapterDict)
WallList = supportFuncs.GenWallofFame('static/walloffame.csv')
links = '<p>LINKS: <a href=/>INDEX</a> <a href=/story>STORY</a> <a href=/wall>WALL OF FAME</a> <a href=/experience>EXPERIENCE</a> </p>'

@APP.route('/robots.txt')
@APP.route('/favicon.ico')
def site_extra_stuff():
    return send_from_directory(APP.static_folder, request.path[1:])

@APP.route('/<vw>')
@APP.route('/')
def index(vw = ''):
    '''Returns the index template'''
    title = 'THIS IS THE HOME PAGE'
    return render_template(vw + 'index.html', title=title)

@APP.route('/<vw>story')
@APP.route('/story')
def story(vw = ''):
    '''Returns the story template'''
    title = 'We\'re Your Friends Now <h2>A History of the Friendships That Made The Green Lattice Great</h2>'
    title = Markup(title)
    if vw:
        return render_template(vw + 'story.html', title=title, index=VWChapterIndex)
    else:
        return render_template(vw + 'story.html', title=title, index=ChapterIndex)

@APP.route('/<vw>story/<chapter>')
@APP.route('/story/<chapter>')
def storypart(chapter, vw = ''):
    '''Returns the chapter template'''
    if chapter in ChapterDict:
        title = ChapterDict[chapter]['title']
        content = Markup(ChapterDict[chapter]['content'])
    else:
        title = 'PAGE NOT FOUND'
        content = 'NOTHING TO SEE HERE'
    if vw:
        return render_template('vwchapter.html', title=title, chapter=content, footlinks=VWStoryFootLinks[chapter])
    else:
        return render_template('chapter.html', title=title, chapter=content, footlinks=StoryFootLinks[chapter])

@APP.route('/<vw>story/all')
@APP.route('/story/all')
def allstory(vw = ''):
    '''Returns the chapter template'''
    title = 'The Complete Story of the Green Lattice'
    if vw:
        return render_template('vwchapter.html', title=title, chapter=AllStory, footlinks='')
    else:
        return render_template('chapter.html', title=title, chapter=AllStory, footlinks='')

@APP.route('/<vw>wall')
@APP.route('/wall')
def wall(vw = ''):
    '''Returns the wall of fame template'''
    title = 'ALL IN ALL YOU\'RE JUST ANOTHER PIXEL IN THE LATTICE'
    if vw:
        return render_template('vwwall.html', title=title, wall=Markup(WallList))
    else:
        return render_template('wall.html', title=title, wall=Markup(WallList))

@APP.route('/<vw>experience')
@APP.route('/experience')
def experience(vw = ''):
    '''Returns the individual experience template'''
    title = 'NOW THIS IS SOMEONE ELSE\'S STORY ALL ABOUT HOW'
    if vw:
        return render_template('vwexperience.html', title=title)
    else:
        return render_template('experience.html', title=title)

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=8080)
