from flask import Flask, render_template, request

# 초기화
app = Flask(__name__)

@app.route('/home')
def home() :
    a = 10
    print(a)
    return '''
        <h1>hello world</h1>
    '''

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login_check', methods=['POST', 'get'])
def login_check():
    print('로그인 체크 시작')

    # 1/0
    
    print('request.method', request.method)

    # 파라메터 받기
    id = ''
    pw = ''
    # GET 방식
    if request.method == 'GET' :
        id = request.args.get('id')
        print('[GET] id : ', id)

    # POST 방식
    elif request.method == 'POST' :
        pw = request.form.get('pw')
        print('[POST] pw : ', pw)

    # return f'입력한 id:{id}, pw:{pw}'
    return render_template('main.html', id2=id, d={'k':'v'}, l=[1,2,3,4])

# 서버 구동
# 기본 포트 : 5000
app.run(port=5000, debug=True)
