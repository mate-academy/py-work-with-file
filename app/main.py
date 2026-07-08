def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(f"{data_file_name}", "r") as data_file:

        for line in data_file.readlines():
            line, value = line.strip().split(",")

            if line == "supply":
                supply += int(value)
            elif line == "buy":
                buy += int(value)

    with open(f"{report_file_name}", "w") as report_file:
        result = supply - buy

        report_file.write(f"supply,{supply}\n"
                          f"buy,{buy}\n"
                          f"result,{result}\n")
