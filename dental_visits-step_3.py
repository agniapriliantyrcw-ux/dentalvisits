# === Stage 3: Хранилище в памяти ===
# Project: DentalVisits
import uuid


class Visit:
    def __init__(self, date, doctor, cost, status):
        self.id = uuid.uuid4()
        self.date = date
        self.doctor = doctor
        self.cost = cost
        self.status = status

    def __repr__(self):
        return f"Visit(id={self.id}, date={self.date}, doctor={self.doctor}, cost={self.cost}, status={self.status})"


class VisitStorage:
    def __init__(self):
        self._visits = {}

    def add(self, visit):
        self._visits[visit.id] = visit

    def get(self, visit_id):
        return self._visits.get(visit_id)

    def list(self):
        return list(self._visits.values())


if __name__ == "__main__":
    storage = VisitStorage()

    v1 = Visit("2024-01-15", "Иванов", 5000, "запланирован")
    v2 = Visit("2024-01-16", "Петрова", 8000, "выполнен")
    v3 = Visit("2024-01-17", "Иванов", 3500, "отменён")

    storage.add(v1)
    storage.add(v2)
    storage.add(v3)

    print("Все визиты:")
    for visit in storage.list():
        print(" ", visit)

    print("\nВизит по id:", storage.get(v1.id))

    print("\nПоиск по врачу Иванов:")
    for visit in storage.list():
        if visit.doctor == "Иванов":
            print(" ", visit)
