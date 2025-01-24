from flask import Flask, render_template, url_for

app = Flask(__name__) #имя текущего файла (app)

@app.route("/") #создаем декоратор (что нужно написать чтобы у нас открылась страница (добавить к ip)

# например так мы откроем с помощью index 
# @app.route("/index") (http://127.0.0.1:5000/index)

def index():
    return render_template('index.html') #подгружем страичку index.html

@app.route("/about")
def about():
    return render_template('about.html') #подгружем страичку about.html


if __name__ == '__main__':
    app.run(debug=True) #возможность при перезагрузке сразу внести изменения на сайт + debug ошибок (для запуска app.py)
