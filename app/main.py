def create_report(data_file_name: str, report_file_name: str) -> None:
    buy = 0
    supply = 0
    with open(data_file_name, "r") as file:
        for line in file:
            if line.startswith("buy"):
                buy += int(line[4:])
            else:
                supply += int(line[7:])

    with open(report_file_name, "w") as new_file:
        new_file.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )
