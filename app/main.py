import re


def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {"supply": 0, "buy": 0}

    with open(data_file_name, "r", encoding="UTF-8") as file:
        file_open = file.read().strip()
        make_list = re.split(r"[\n,]", file_open)

        for index in range(0, len(make_list) - 1, 2):
            key = make_list[index].strip().lower()
            try:
                value = int(make_list[index + 1].strip())
            except ValueError:
                continue

            if key in report:
                report[key] += value

    supply_sum = report["supply"]
    buy_sum = report["buy"]

    result = supply_sum - buy_sum

    with open(report_file_name, "x") as write_file:
        write_file.write(f"supply,{supply_sum}\n")
        write_file.write(f"buy,{buy_sum}\n")
        write_file.write(f"result,{result}\n")
