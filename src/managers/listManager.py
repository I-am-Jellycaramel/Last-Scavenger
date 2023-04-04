def find_element_in_dict(dict: dict, name: str):
    for (key, value) in dict.items():
        if key != name:
            continue
        return value

