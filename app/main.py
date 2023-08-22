def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        for line in file:
            row = line.split(",")
            if row[0] == "supply":
                supply += int(row[1])
            elif row[0] == "buy":
                buy += int(row[1])

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{supply - buy}\n")
