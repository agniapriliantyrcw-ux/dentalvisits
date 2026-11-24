# === Stage 9: Фильтрация записей ===
# Project: DentalVisits
from datetime import date, datetime


def filter_visits_by_dentist(visits, dentists):
    return [visit for visit in visits if visit["dentist"] in dentists]


def filter_visits_by_date_range(visits, start_date, end_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    return [
        visit
        for visit in visits
        if start_date <= visit["date"] <= end_date
    ]


def filter_visits(visits, dentists=None, start_date=None, end_date=None):
    result = visits
    if dentists:
        result = filter_visits_by_dentist(result, dentists)
    if start_date or end_date:
        result = filter_visits_by_date_range(
            result, start_date, end_date
        )
    return result


def parse_date(value):
    return datetime.strptime(value, "%Y-%m-%d").date()


def format_date(value):
    return value.strftime("%Y-%m-%d") if isinstance(value, date) else value
