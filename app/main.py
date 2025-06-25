def create_report(data_file_name: str, report_file_name: str) -> None:
    content = read_from_file(data_file_name)

    report = build_report(content)

    write_to_file(report_file_name, report)


def read_from_file(data_file_name: str) -> list[str]:
    with open(data_file_name, "r") as file:
        return file.readlines()


def build_report(content: list[str]) -> dict:
    content_dict = {}

    for line in content:
        operation_number = line.replace("\n", "").split(",")

        number_list = content_dict.get(operation_number[0], [])
        number_list.append(int(operation_number[1]))
        content_dict[operation_number[0]] = number_list

    return calc_stats(content_dict)


def calc_stats(content_dict: dict) -> dict:
    stats = {}

    for operation, number_list in content_dict.items():
        num_sum = sum(number_list)
        stats[operation] = num_sum

    stats["result"] = stats.get("supply", 0) - stats.get("buy", 0)

    return stats


def write_to_file(report_file_name: str, report: dict) -> None:
    result_str = (f"supply,{report["supply"]}\n"
                  f"buy,{report["buy"]}\n"
                  f"result,{report["result"]}\n")

    with open(report_file_name, "w") as file:
        file.write(result_str)
