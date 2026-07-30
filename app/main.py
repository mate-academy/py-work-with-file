def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as input_file:
        input_csv = input_file.readlines()

    for line in input_csv:
        current_line = line.strip().split(",")
        if len(current_line) >= 2:
            if current_line[0] == "supply":
                supply += int(current_line[1])
            elif current_line[0] == "buy":
                buy += int(current_line[1])

    with open(report_file_name, "w") as output_csv:
        output_csv.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )
