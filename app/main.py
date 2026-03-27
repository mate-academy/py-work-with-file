def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        supply = 0
        buy = 0
        for line in data_file:
            if line:
                operation, amount = line.strip().split(",")
                amount = int(amount)
                if operation == "supply":
                    supply += amount
                elif operation == "buy":
                    buy += amount
        result = supply - buy
        comma = ","
        report_file.write(f"supply{comma}{supply}\n"
                          f"buy{comma}{buy}\n"
                          f"result{comma}{result}\n")
