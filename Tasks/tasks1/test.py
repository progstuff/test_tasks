from typing import List, Tuple


def get_total_str(data: List[Tuple[str, int, str, str]]) -> str:
    tmp = {}
    for (product, price, name, phone) in data:
        tmp_key = f'{name} {phone}'
        tmp_val = f'{product} - {price}'
        el = tmp.get(tmp_key, None)
        if el is None:
            tmp[tmp_key] = tmp_val
        else:
            tmp[tmp_key] += f'; {tmp_val}'

    result = ''
    for (key, value) in tmp.items():
        result += f'{key}: {value}\n'

    return result[:-1]

