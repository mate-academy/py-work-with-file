def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file1:
        for line in file1:
            if line.strip():
                parts = line.strip().split(",")
                operation = parts[0]
                amount = int(parts[1])

                if operation == "supply":
                    supply += amount
                elif operation == "buy":
                    buy += amount

    with open(report_file_name, "w") as file2:
        file2.write(f"supply,{supply}\n")
        file2.write(f"buy,{buy}\n")
        file2.write(f"result,{supply - buy}\n")
