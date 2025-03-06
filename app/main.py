def create_report(data_file_name: str,report_file_name: str) -> None:

    with open(data_file_name, "r") as fruits:
        supply = 0
        buy = 0
        for fruit in fruits:
            parts = fruit.strip().split(",")
            operation = parts[0]
            amount = int(parts[1])
            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount
        result = supply - buy
        str_result = str(result)

        with open(report_file_name, "a") as report:
            report.write(f"supply,{supply}\n")
            report.write(f"buy,{buy}\n")
            report.write(f"result,{str_result}\n")
