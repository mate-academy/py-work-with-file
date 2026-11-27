def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with open(data_file_name, "r") as data_file:
        supply = 0
        buy = 0
        for line in data_file:
            clean_line = line.strip()
            if clean_line:
                operation, count_str = clean_line.split(",")
                count = int(count_str)
                if operation == "supply":
                    supply += count
                elif operation == "buy":
                    buy += count
        result = supply - buy
    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{supply}\nbuy,{buy}\nresult,{result}\n"
        )
