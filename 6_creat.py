"""
from flask import Flask

app = Flask(__name__)

# 데이터 베이스에 저장함 주로
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]

def template(contents,content):
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href="/">WEB</a></h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href="/create/">create</a></li>
            </ul>
        </body>
    </html>
    '''

def getContents():
    liTags = ''
    for topic in topics:
        liTags = liTags + f'<li><a href="read/{topic["id"]}/">{topic["title"]}</a></li>'    
    return liTags

@app.route('/')
def index():
    return template(getContents(), '<h2>Welcome</h2>Hello, WEB')
    # contents, content

@app.route('/read/<int:id>/')
def read(id):
    print(type(id))
    # 그냥 @app.route('/read/<id>/')하면 문자열임.
    title = ''
    body = ''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
    print(title, body)
    # title하고 body값 잘 나오는 지 확인
    return template(getContents(), f'<h2>{title}</h2>{body}')

@app.route('/create/')
def create():
    # GET이 기본값(자바 프레임워크 할 때와 같음)
    # GET은 URL 보이고 POST은 안보이고
    # http://127.0.0.1:5000/안녕/
    content = '''
        <form action="/안녕/" method="POST"> 
            <p><input type = "text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit" value="create"></p>
        </form>
    '''
    return template(getContents(), content)

app.run(debug=True)
"""