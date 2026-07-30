def read_file(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        result = []
        for line in file.readlines():
            if len(line) != 0:
                result.append(line)
        return result


def write_file(file_name: str, data: dict[str]) -> None:
    with open(file_name, "a") as file:
        for key, value in data.items():
            file.write(f"{key},{value}\n")


def calculate_report(data_list: list[str]) -> dict[str]:
    result_dict = {"supply": 0,
                   "buy": 0}
    for data in data_list:
        operation, number = data.replace("\n", "").split(",")
        result_dict[operation] += int(number)

    result_dict["result"] = result_dict["supply"] - result_dict["buy"]
    return result_dict


def create_report(data_file_name: str, report_file_name: str) -> None:
    data_list = read_file(data_file_name)
    report = calculate_report(data_list)
    write_file(report_file_name, report)
