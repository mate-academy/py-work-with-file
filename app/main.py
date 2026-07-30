def create_report(data_file_name: str, report_file_name: str) -> None:
    temp = get_data_from_file(data_file_name)
    difference = get_difference(temp)
    temp["result"] = difference
    make_report_file(temp, report_file_name, "supply", "buy", "result")


def make_report_file(
        data: dict,
        file_name: str,
        supply:str, buy:
        str, result: str) -> None:
    with open(file_name, "w") as file:
        file.write(f"{supply},{data[supply]}\n")
        file.write(f"{buy},{data[buy]}\n")
        file.write(f"{result},{data[result]}\n")


def get_difference(data: dict) -> int:
    values = list(data.values())
    difference = max(values) - min(values)
    return difference


def get_data_from_file(file_name: str) -> dict:
    out = {}
    with open(file_name, "r") as file:
        for line in file:
            if not line.strip():
                continue

            row = line.split(",")
            key = row[0].strip()
            value = int(row[1].strip())

            if key not in out:
                out[key] = value
            else:
                old_value = out.get(key)
                new_value = old_value + value
                out.update({key: new_value})

    return out
