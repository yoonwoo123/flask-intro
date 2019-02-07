from flask import Flask, render_template, request, redirect
import datetime
import csv

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
    
@app.route('/hi')    
def hi():
    return '안녕, 지원'

# 5월 20일부터 d-day를 출력하는 것을 만들어주세요.
@app.route('/dday')
def dday():
    now = datetime.datetime.now()
    vacation = datetime.datetime(2019, 5, 20)
    d = vacation - now
    # return은 반드시 string으로 되어야 한다!
    return f'{d.days}일 뒤에 놀러가자'
    
# variable routing
@app.route('/hi/<string:name>')
def greeting(name):
    return render_template('greeting.html', html_name=name)
    
# 세제곱의 결과를 출력해볼게요!
@app.route('/math/<int:num>')
def math(num):
    a = num**3
    return f'{a}이 나옵니다'
    #혹은 return str(a) 로 출력 무조건 string으로 출력해야되기 때문이다.

@app.route('/movie')
def movie():
    movies = ['극한직업', '신비한 동물 사전', '그린북', '그린랜턴']
    return render_template('movie.html', movies=movies)

@app.route('/google')
def google():
    return render_template('google.html')

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/ping')
def ping():
    return render_template('ping.html')
    
    
@app.route('/pong')
def pong():
    # request.args = {'name': '재찬', 'msg' : '안녕'}
    name = request.args.get('name')
    msg = request.args.get('msg')
    return render_template('pong.html', name=name, msg=msg)

@app.route('/opgg')
def opgg():
    return render_template('opgg.html' )

@app.route('/opggresult')
def opggresult():
    return render_template('opggresult.html')
    
@app.route('/timeline')
def timeline():
    # 지금까지 기록되어있는 방명록들을 ('timeline.csv')
    # 보여주자!
    timerecord = []
    with open('timeline.csv', 'r', encoding='utf-8', newline='') as r:
        reader = csv.DictReader(r)
        for row in reader:
            timerecord.append(row)
    return render_template('timeline.html', timerecord=timerecord)
    
@app.route('/timeline/create')
def timeline_create():
    username = request.args.get('username')
    message = request.args.get('message')
    # a : append, w : write
    with open('timeline.csv', 'a', encoding='utf-8', newline='') as f:
        fieldnames= ['username', 'message']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'username': username,
                         'message': message
                         })
        
    #return render_template('timeline_create.html', username=username, message=message)
    return redirect('/timeline')

@app.route('/dictionary/<string:word>')
def dictionary(word):
    dictionarys = {'apple': '사과', 'banana': '바나나'}
    if word in dictionarys:
        return f'{word}은(는) {dictionarys[word]}!'
    else:
        return f'{word}라는 단어가 없습니다.'
    # return render_template('08workshop.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)