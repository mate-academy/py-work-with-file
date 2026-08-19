def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with open(data_file_name, "r") as file:
        supply = 0
        buy = 0
        for line in file.readlines():
            if not line.strip():
                continue
            parts = line.split(",")
            amount = int(parts[1].strip())
            if parts[0] == "supply":
                supply += amount
            elif parts[0] == "buy":
                buy += amount
        result = supply - buy
        with open(report_file_name, "w") as file:
            file.write(f"supply,{supply}\n")
            file.write(f"buy,{buy}\n")
            file.write(f"result,{result}\n")
