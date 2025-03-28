def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as first_file:

        for line in first_file:
            split_line = line.split(",")
            if split_line[0] == "supply":
                supply += int(split_line[1])
            if split_line[0] == "buy":
                buy += int(split_line[1])
    with open(report_file_name, "w") as second_file:
        second_file.write(
            f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n"
        )
