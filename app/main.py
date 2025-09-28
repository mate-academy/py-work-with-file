def create_report(data_file_name: str, report_file_name: str) -> None:
    result1 = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as file1:
        for line in file1:
            line = line.strip()
            if line:
                parts = line.split(",")
                if len(parts) == 2:
                    before_comma = parts[0].strip()
                    after_comma = parts[1].strip()
                    if before_comma in result1:
                        result1[before_comma] += int(after_comma)
    with open(report_file_name, "w") as file2:
        file2.write(f"supply,{result1["supply"]}\n")
        file2.write(f"buy,{result1["buy"]}\n")
        file2.write(f"result,{result1["supply"] - result1["buy"]}\n")
