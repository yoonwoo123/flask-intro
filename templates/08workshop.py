from flask import Flask, render_template, request, redirect
import datetime
import csv

app = Flask(__name__)


@app.route('/dictionary/<string:word>')
def dictionary():
    dictionary = {'apple': '사과', 'banana': '바나나'}
    for word in dictionary:
        print(dictionary[word])
    else:
        print('단어가 없습니다.')
    return render_template('08workshop.html')
    
# @app.route('/timeline/create')
# def timeline_create():
#     username = request.args.get('username')
#     message = request.args.get('message')
#     # a : append, w : write
#     with open('timeline.csv', 'a', encoding='utf-8', newline='') as f:
#         fieldnames= ['username', 'message']
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writerow({'username': username,
#                          'message': message
#                          })
        
#     #return render_template('timeline_create.html', username=username, message=message)
#     return redirect('/timeline')