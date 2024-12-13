def filter_by_state(list_dict: list[dict[str, any]], state: str = "EXECUTED") -> list[dict[str, any]]:
    """Функция,возвращающая новый список словарей, содержащий только те словари, у которых ключ соответствует
    указанному значению"""

    new_dict = []
    for i in list_dict:
        if i["state"] == state:
            new_dict.append(i)
    return new_dict


def sort_by_date(list_dict: list[dict[str, any]], sort: bool = True) -> list[dict[str, any]]:
    """Функция возвращающая список отсортированный по дате"""

    sorted_list_dict = sorted(list_dict, key=lambda i: i["date"], reverse=sort)
    return sorted_list_dict
