import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    buy_sum = 0
    supply_sum = 0

    with open(data_file_name, "r") as file:
        reader = csv.reader(file)
        data_csv = list(reader)

        for line in data_csv:
            if line[0] == "buy":
                buy_sum += int(line[1])
            elif line[0] == "supply":
                supply_sum += int(line[1])

    file.close()

    result_sum = supply_sum - buy_sum

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply_sum}\n")
        file.write(f"buy,{buy_sum}\n")
        file.write(f"result,{result_sum}\n")

    file.close()
