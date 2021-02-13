import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class User(Base):
    """Описывает структуру таблицы athelete, содержащую данные об атлетах"""
    __tablename__ = 'user'

    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.Float)

def connect_db():
    """Устанавливает соединение к базе данных, создает таблицы, если их еще нет, и возвращает объект сессии """
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def request_data():
    """Запрашивает у пользователя данные и добавляет их в список users"""
    first_name = input("Введи своё имя: ")
    last_name = input("А теперь фамилию: ")
    email = input("адрес электронной почты: ")
    birthdate = input("дату рождения в формате ГГГГ-ММ-ДД: ")
    gender = input("Выберете пол (Male, Female): ")
    height = input("Ваш рост в метрах (пример: 1.68): ")
    user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        birthdate=birthdate,
        gender=gender,
        height=height
    )
    return user

def main():
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print("данные сохранены!")

if __name__ == "__main__":
    main()