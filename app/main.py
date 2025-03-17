def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as data_file:

        for line in data_file.read().splitlines():
            line_split = line.split(",")
            print(line_split)

            if line_split[0] == "supply":
                supply += int(line_split[1])

            if line_split[0] == "buy":
                buy += int(line_split[1])

    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )
