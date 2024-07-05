def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with open(data_file_name) as input_file:
        supply = 0
        buy = 0
        for row in input_file:
            if not row:
                continue
            row = row.strip().split(",")
            if "supply" in row:
                supply += int(row[1])
            if "buy" in row:
                buy += int(row[1])

    with open(report_file_name, "w") as result_file:
        result_file.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )
