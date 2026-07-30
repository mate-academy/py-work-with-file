import csv


def create_report(data_file_name: str,
                  report_file_name: str
                  ) -> None:
    result_supply = 0
    result_buy = 0
    result = 0

    with open(data_file_name) as data_file:
        reader = csv.reader(data_file)
        for line in reader:
            if not line:
                continue
            if line[0] == "supply":
                result_supply += int(line[1])
            elif line[0] == "buy":
                result_buy += int(line[1])

        result += (result_supply - result_buy)
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{result_supply}\n"
                          f"buy,{result_buy}\n"
                          f"result,{result}\n")
