# flake8: noqa: E231

def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as data_file_name:

        count_supplies = 0
        count_buys = 0
        list_of_supplies_and_buys = data_file_name.readlines()

        for line in list_of_supplies_and_buys:
            row = line.split(",")[1]
            if "supply" in line:
                count_supplies += int(row)
            if "buy" in line:
                count_buys += int(row)

    amount = count_supplies - count_buys

    with open(report_file_name, "w") as report_file_name:

        report_file_name.write(f"supply,{count_supplies}\n")
        report_file_name.write(f"buy,{count_buys}\n")
        report_file_name.write(f"result,{amount}\n")
