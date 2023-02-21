from typing import List


def convert_file_names(file_names: List[str]) -> List[str]:
    max_length = len(max(file_names, key=lambda file_name: len(file_name)))
    clear_names = [''.join(sorted(set(file_name), key=file_name.index)) for file_name in file_names]
    return ['{prefix}{postfix}'.format(prefix='_'*(max_length - len(file_name)),
                                       postfix=file_name)
            for file_name in clear_names]