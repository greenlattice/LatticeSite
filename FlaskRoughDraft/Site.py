from flask import Flask, render_template
APP = Flask(__name__)

links = '<p>LINKS: <a href=/>INDEX</a> <a href=/story>STORY</a> <a href=/wall>WALL OF FAME</a> <a href=/experience>EXPERIENCE</a> </p>a'


@APP.route('/')
def index():
    '''Returns the guild template'''
    title = 'THIS IS THE HOME PAGE'
    return render_template('index.html', title=title)

@APP.route('/story')
def story():
    '''Returns the story template'''
    title = 'NOW THIS IS A STORY ALL ABOUT HOW'
    return render_template('story.html', title=title)

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
