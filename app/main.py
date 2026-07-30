def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    supply = 0
    buy = 0

    with open(data_file_name) as file:
        for line in file:
            line = line.split(",")

            if line[0] == "supply":
                supply += int(line[-1])
            elif line[0] == "buy":
                buy += int(line[-1])

    with open(report_file_name, "a") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{supply - buy}\n")
