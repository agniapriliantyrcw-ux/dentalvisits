# === Stage 1: Каркас модуля ===
# Project: DentalVisits
from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List


class VisitStatus(str, Enum):
    SCHEDULED = "запланирован"
    COMPLETED = "завершён"
    CANCELLED = "отменён"


@dataclass
class Visit:
    date: date
    doctor: str
    cost: float
    status: VisitStatus = VisitStatus.SCHEDULED

    def __post_init__(self) -> None:
        if self.cost < 0:
            raise ValueError("Стоимость визита не может быть отрицательной")


def create_demo_visits() -> List[Visit]:
    return [
        Visit(date(2025, 1, 15), "Иванов И.И.", 3500.0, VisitStatus.SCHEDULED),
        Visit(date(2025, 1, 10), "Петрова А.С.", 8200.0, VisitStatus.COMPLETED),
        Visit(date(2025, 1, 20), "Сидоров К.В.", 1500.0, VisitStatus.CANCELLED),
    ]


def main() -> None:
    visits = create_demo_visits()
    print("Демо-записи визитов к стоматологу:")
    for visit in visits:
        print(f"  {visit.date} | {visit.doctor} | {visit.cost} ₽ | {visit.status.value}")


if __name__ == "__main__":
    main()
