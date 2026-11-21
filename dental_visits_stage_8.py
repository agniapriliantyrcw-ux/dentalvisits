# === Stage 8: Генерация идентификаторов ===
# Project: DentalVisits
PROJECT_PREFIX = "DVL"


def generate_unique_id(prefix=PROJECT_PREFIX, length=8, characters="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """Генерирует уникальный идентификатор с указанным префиксом и проверяет коллизии.

    Использует модуль secrets для генерации криптографически стойких случайных значений.
    Проверяет, что сгенерированный идентификатор не существует в переданном словаре.
    """
    import secrets

    while True:
        random_suffix = "".join(secrets.choice(characters) for _ in range(length))
        candidate = f"{prefix}-{random_suffix}"

        if candidate not in prefix_to_id:
            prefix_to_id[candidate] = True
            return candidate


prefix_to_id = {}


if __name__ == "__main__":
    id_1 = generate_unique_id()
    id_2 = generate_unique_id()
    print(id_1)
    print(id_2)
    print(id_1 != id_2)
