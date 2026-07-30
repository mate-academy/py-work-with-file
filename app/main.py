def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as f:
        for line in f:
            row = line.split(",")
            if row:
                if row[0] == "supply":
                    supply += int(row[1])
                elif row[0] == "buy":
                    buy += int(row[1])
    result = supply - buy

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{result}\n")
