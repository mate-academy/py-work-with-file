def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        for line in file:
            data = line.strip().split(",")

            if data[0] == "supply":
                supply += int(data[1])
            else:
                buy += int(data[1])

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\n"
                   f"buy,{buy}\n"
                   f"result,{supply - buy}\n")
