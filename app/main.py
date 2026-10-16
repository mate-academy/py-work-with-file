def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as f:
        for line in f:
            line = line.strip()

            if line == "":
                continue
            name, num = line.split(",")

            if name == "supply":
                supply += int(num)

            elif name == "buy":
                buy += int(num)

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{supply - buy}\n")
