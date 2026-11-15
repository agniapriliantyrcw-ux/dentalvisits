# === Stage 5: Удаление и восстановление ===
# Project: DentalVisits
from datetime import datetime


class Visit:
    def __init__(self, visit_id, patient_id, procedure_id, doctor, date, cost,
                 status="completed"):
        self.visit_id = visit_id
        self.patient_id = patient_id
        self.procedure_id = procedure_id
        self.doctor = doctor
        self.date = date
        self.cost = cost
        self.status = status
        self.deleted = False
        self.deleted_at = None

    def soft_delete(self):
        self.deleted = True
        self.deleted_at = datetime.now()

    def restore(self):
        self.deleted = False
        self.deleted_at = None

    @property
    def is_deleted(self):
        return self.deleted

    def to_dict(self):
        return {
            "visit_id": self.visit_id,
            "patient_id": self.patient_id,
            "procedure_id": self.procedure_id,
            "doctor": self.doctor,
            "date": self.date,
            "cost": self.cost,
            "status": self.status,
            "deleted": self.deleted,
            "deleted_at": self.deleted_at.isoformat() if self.deleted_at else None,
        }


class VisitRepository:
    def __init__(self):
        self._visits = []

    def add(self, visit):
        self._visits.append(visit)

    def get(self, visit_id):
        for visit in self._visits:
            if visit.visit_id == visit_id:
                return visit
        return None

    def hard_delete(self, visit_id):
        for visit in self._visits:
            if visit.visit_id == visit_id:
                self._visits.remove(visit)
                return True
        return False

    def soft_delete(self, visit_id):
        visit = self.get(visit_id)
        if visit:
            visit.soft_delete()
            return True
        return False

    def restore(self, visit_id):
        visit = self.get(visit_id)
        if visit:
            visit.restore()
            return True
        return False

    def get_active(self):
        return [v for v in self._visits if not v.is_deleted]

    def get_deleted(self):
        return [v for v in self._visits if v.is_deleted]
