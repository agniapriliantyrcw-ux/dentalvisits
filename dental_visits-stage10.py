# === Stage 10: Сортировка записей ===
# Project: DentalVisits
from datetime import datetime

def sort_visits_by_date(visits, ascending=True):
    """Сортирует визиты по дате визита."""
    return sorted(visits, key=lambda v: v['date'], reverse=not ascending)

def sort_visits_by_created_at(visits, ascending=True):
    """Сортирует визиты по дате создания."""
    return sorted(visits, key=lambda v: v['created_at'], reverse=not ascending)

def sort_visits(visits, by_field='date', ascending=True):
    """
    Универсальная сортировка записей «визит».

    by_field: 'date' - по дате визита, 'created_at' - по дате создания.
    ascending: True - по возрастанию, False - по убыванию.
    """
    if by_field == 'created_at':
        key = lambda v: v['created_at']
    elif by_field == 'date':
        key = lambda v: v['date']
    else:
        raise ValueError("Недопустимое поле для сортировки: " + str(by_field))
    return sorted(visits, key=key, reverse=not ascending)

if __name__ == '__main__':
    sample_visits = [
        {'date': datetime(2024, 5, 10), 'created_at': datetime(2024, 5, 1),
         'doctor': 'Иванов', 'cost': 3000.0, 'status': 'запланирован'},
        {'date': datetime(2024, 3, 20), 'created_at': datetime(2024, 4, 15),
         'doctor': 'Петрова', 'cost': 5500.0, 'status': 'завершён'},
        {'date': datetime(2024, 3, 20), 'created_at': datetime(2024, 4, 10),
         'doctor': 'Сидоров', 'cost': 2000.0, 'status': 'в ожидании'},
        {'date': datetime(2024, 1, 5), 'created_at': datetime(2024, 2, 1),
         'doctor': 'Козлова', 'cost': 8000.0, 'status': 'отменён'},
    ]

    print("По дате визита, по возрастанию:")
    for visit in sort_visits(sample_visits, by_field='date', ascending=True):
        print(visit['date'].date(), visit['doctor'])

    print("По дате визита, по убыванию:")
    for visit in sort_visits(sample_visits, by_field='date', ascending=False):
        print(visit['date'].date(), visit['doctor'])

    print("По дате создания, по возрастанию:")
    for visit in sort_visits(sample_visits, by_field='created_at', ascending=True):
        print(visit['created_at'].date(), visit['doctor'])

    print("По дате создания, по убыванию:")
    for visit in sort_visits(sample_visits, by_field='created_at', ascending=False):
        print(visit['created_at'].date(), visit['doctor'])
