def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        while (line := (file.readline()).split(",")) != [""]:
            if "buy" in line:
                buy += int(line[1])
            else:
                supply += int(line[1])

    with open(report_file_name, "w") as file:
        file.write(
            f"supply,{supply}\n"
        )
        file.write(
            f"buy,{buy}\n"
        )
        file.write(
            f"result,{supply - buy}\n"
        )
