import datetime


def log(massege: str):
    time = datetime.datetime.now().strftime('%D %H:%M:%S')
    with open('Seminar7\log.txt', 'a', encoding="utf-8") as file:
        file.write(f'{time}: {massege}\n')