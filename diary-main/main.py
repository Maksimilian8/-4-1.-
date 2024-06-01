# Импорт
from flask import Flask, render_template, request, redirect
# Подключение библиотеки баз данных
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Подключение SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Создание db
db = SQLAlchemy(app)

# Задание №1. Создай класс под комментарием "Задание №1"
class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)

    # Задание №3. Функция для вывода объектов по id
    def __repr__(self):
        return f'<Card {self.id}>'

# Задание №2. Создай способ записи данных в БД
@app.route('/form_create', methods=['GET', 'POST'])
def form_create():
    if request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        text = request.form['text']

        # Создание объекта и запись в БД
        card = Card(title=title, subtitle=subtitle, text=text)
        db.session.add(card)
        db.session.commit()

        return redirect('/')
    else:
        return render_template('create_card.html')

# Задание №2. Отобразить объекты из БД в index.html
@app.route('/')
def index():
    cards = Card.query.all()
    return render_template('index.html', cards=cards)

# Задание №2. Отобразить нужную карточку по id
@app.route('/card/<int:id>')
def card(id):
    card = Card.query.get_or_404(id)
    return render_template('card.html', card=card)

# Запуск страницы c созданием карты
@app.route('/create')
def create():
    return render_template('create_card.html')

if __name__ == "__main__":
    app.run(debug=True)