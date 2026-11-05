# === Stage 2: Проверка полей ===
# Project: DentalVisits
import datetime


VALID_STATUSES = {"запланирован", "выполнен", "отменён", "в ожидании"}


def normalize_date(value):
    """Нормализует строку даты в объект datetime.date."""
    if isinstance(value, datetime.date) and not isinstance(value, datetime.datetime):
        return value
    if isinstance(value, datetime.datetime):
        return value.date()
    if value is None or value.strip() == "":
        return None
    text = str(value).strip()
    formats = ("%d.%m.%Y", "%d/%m/%Y", "%Y-%m-%d", "%m.%m.%Y", "%m/%m/%Y")
    for fmt in formats:
        try:
            return datetime.datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    raise ValueError("Не удалось распознать дату «{value}». Ожидался формат ДД.ММ.ГГГГ".format(value=value))


def normalize_status(value):
    """Нормализует статус визита к допустимому набору значений."""
    if value is None or str(value).strip() == "":
        return None
    key = str(value).strip().lower()
    if key in VALID_STATUSES:
        return key
    raise ValueError("Неизвестный статус «{value}». Допустимые значения: {options}".format(
        value=value, options=", ".join(sorted(VALID_STATUSES))))


def validate_visit(visit):
    """Валидирует сущность «визит» и возвращает список сообщений об ошибках."""
    errors = []

    date = normalize_date(visit.get("дата"))
    if date is None:
        errors.append("Дата визита обязательна и должна быть в формате ДД.ММ.ГГГГ")
    elif date > datetime.date.today():
        errors.append("Дата визита не может быть в будущем")

    doctor = str(visit.get("врач") or "").strip()
    if not doctor:
        errors.append("Укажите врача, который проводит визит")

    cost = visit.get("стоимость")
    try:
        cost_value = float(cost)
    except (TypeError, ValueError):
        errors.append("Стоимость должна быть числовым значением")
    else:
        if cost_value < 0:
            errors.append("Стоимость визита не может быть отрицательной")

    status = normalize_status(visit.get("статус"))
    if status is None:
        errors.append("Укажите статус визита: запланирован, выполнен, отменён или в ожидании")

    return errors
