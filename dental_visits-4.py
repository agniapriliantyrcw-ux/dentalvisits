# === Stage 4: Редактирование записей ===
# Project: DentalVisits
from datetime import date


ALLOWED_VISIT_FIELDS = ("date", "doctor", "cost", "status")


class VisitEditable:
    """Редактирование сущности визит по идентификатору.

    Метод update_visits_by_id принимает словарь изменений и применяет
    только те поля, которые присутствуют в ALLOWED_VISIT_FIELDS.
    """

    def __init__(self, visits):
        self._visits = dict(visits)

    def update_visits_by_id(self, visit_id, changes):
        if visit_id not in self._visits:
            return None

        allowed = set(ALLOWED_VISIT_FIELDS)
        if not allowed.issuperset(changes.keys()):
            raise ValueError("Изменены недопустимые поля")

        updated = dict(self._visits[visit_id])
        for field, value in changes.items():
            if field in allowed:
                updated[field] = value

        self._visits[visit_id] = updated
        return updated
