def create_report(
        data_file_name: str,
        report_file_name: str,
) -> None:
    supply = 0
    buy = 0

    with open(data_file_name,) as data_file:
        for line in data_file:
            if not line.strip():
                continue

            split_line = line.split(",")

            if "supply" in split_line:
                supply += int(split_line[1])

            else:
                buy += int(split_line[1])

    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{result}\n"
        )
