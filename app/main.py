def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    data_file = open("data_file_name.csv", "r")
    for line in data_file:
            if line.strip():
                parts = line.strip().split(",")
                operation = parts[0]
                amount = int(parts[1])

                if operation == "supply":
                    supply += amount
                elif operation == "buy":
                    buy += amount
                data_file.close()
    data2_file = open("report_file_name", "w")
    data2_file.write(f"supply,{supply}\n")
    data2_file.write(f"buy,{buy}\n")
    data2_file.write(f"result,{supply - buy}\n")
    data2_file.close()
