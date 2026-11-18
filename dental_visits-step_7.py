# === Stage 7: Связи между сущностями ===
# Project: DentalVisits
import datetime

PROCEDURE_STATUS = ("completed", "planned", "cancelled")

class Procedure:
    def __init__(self, name, cost, status="planned"):
        self.name = name
        self.cost = cost
        self.status = status

    def __repr__(self):
        return f"Procedure(name={self.name!r}, cost={self.cost}, status={self.status!r})"


class Visit:
    def __init__(self, date, dentist, cost, status="planned"):
        self.date = date
        self.dentist = dentist
        self.cost = cost
        self.status = status
        self.procedures = []

    def add_procedure(self, procedure):
        if not isinstance(procedure, Procedure):
            raise TypeError("procedure must be a Procedure instance")
        self.procedures.append(procedure)

    def get_procedures(self):
        return list(self.procedures)

    def check_integrity(self):
        problems = []

        if self.date is None:
            problems.append("visit has no date")

        valid_date = None
        if isinstance(self.date, str):
            try:
                valid_date = datetime.datetime.strptime(self.date, "%Y-%m-%d")
            except ValueError:
                problems.append(f"invalid date format: {self.date!r}")
        elif not isinstance(self.date, datetime.datetime):
            problems.append(f"date is not a date: {self.date!r}")

        if valid_date is not None:
            for proc in self.procedures:
                if isinstance(proc.status, str) and proc.status not in PROCEDURE_STATUS:
                    problems.append(
                        f"procedure {proc.name!r} has invalid status: {proc.status!r}"
                    )

        total = sum(p.cost for p in self.procedures)
        if total != self.cost:
            problems.append(
                f"cost mismatch: visit={self.cost}, procedures sum={total}"
            )

        return problems


if __name__ == "__main__":
    visit = Visit(
        date="2024-06-01",
        dentist="Dr. Smith",
        cost=1500,
        status="completed",
    )
    visit.add_procedure(Procedure("Cleaning", 600))
    visit.add_procedure(Procedure("Filling", 900))

    procedures = visit.get_procedures()
    print(f"Procedures: {procedures}")

    issues = visit.check_integrity()
    if issues:
        print("Integrity problems:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("Integrity check passed")
