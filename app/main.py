def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as input_file:
        for row in input_file:
            row = row.strip()
            if not row:
                continue
            parts = row.split(",")
            if "supply" in parts:
                supply += int(parts[1])
            elif "buy" in parts:
                buy += int(parts[1])

    with open(report_file_name, "w") as result_file:
        result_file.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )
