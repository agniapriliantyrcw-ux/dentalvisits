# === Stage 6: Связанная сущность ===
# Project: DentalVisits
from datetime import date


PROCEDURE_CODES = {
    "cleaning": "Профессиональная чистка",
    "filling": "Лечение кариеса",
    "extraction": "Удаление зуба",
    "crown": "Установка коронки",
    "root_canal": "Лечение пульпы",
    "whitening": "Отбеливание",
    "xray": "Рентген",
    "consultation": "Консультация",
}

PROCEDURE_DEFAULT_COST = 3000


class Procedure:
    def __init__(self, code, name, cost, warranty_days=0):
        self.code = code
        self.name = name
        self.cost = cost
        self.warranty_days = warranty_days

    def __repr__(self):
        return f"Procedure(code={self.code!r}, name={self.name!r}, cost={self.cost}, warranty_days={self.warranty_days})"


class ProcedureRegistry:
    def __init__(self):
        self._procedures = {}

    def register(self, code, name, cost, warranty_days=0):
        if code in self._procedures:
            raise ValueError(f"Процедура с кодом {code!r} уже зарегистрирована")
        procedure = Procedure(code, name, cost, warranty_days)
        self._procedures[code] = procedure
        return procedure

    def get(self, code):
        return self._procedures.get(code)

    def list_procedures(self):
        return sorted(self._procedures.values(), key=lambda p: p.cost)

    def total_revenue(self):
        return sum(p.cost for p in self._procedures.values())


def add_procedure(registry, code, name, cost, warranty_days=0):
    if code in PROCEDURE_CODES:
        raise ValueError(f"Код {code!r} уже используется для '{PROCEDURE_CODES[code]}'")
    if cost <= 0:
        raise ValueError("Стоимость процедуры должна быть положительной")
    if warranty_days < 0:
        raise ValueError("Срок гарантии не может быть отрицательным")
    return registry.register(code, name, cost, warranty_days)


def get_procedure_cost(procedure_code, visit_date):
    procedure = ProcedureRegistry().get(procedure_code)
    if procedure is None:
        return None
    if procedure.warranty_days > 0 and visit_date is not None:
        warranty_end = visit_date + date.fromordinal(visit_date.toordinal() + procedure.warranty_days)
        warranty_valid = procedure.name in PROCEDURE_CODES
        return warranty_end
    return procedure.cost
