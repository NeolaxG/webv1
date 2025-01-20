from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Функция для чтения комментариев из файла
def read_comments():
    try:
        with open('comments.txt', 'r', encoding='utf-8') as f:
            comments = f.readlines()
        return [comment.strip() for comment in comments]
    except FileNotFoundError:
        return []


# Функция для записи комментариев в файл
def write_comment(comment):
    with open('comments.txt', 'a', encoding='utf-8') as f:
        f.write(comment + '\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/comments', methods=['GET', 'POST'])
def comments():
    if request.method == 'POST':
        comment = request.form['comment']
        write_comment(comment)
        return redirect(url_for('comments'))

    comments = read_comments()
    return render_template('comments.html', comments=comments)


if __name__ == '__main__':
    app.run(debug=True)