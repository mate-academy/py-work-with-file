def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as source_file:
        supply = 0
        buy = 0

        data = source_file.read().split("\n")

        for line in data:
            if len(line) > 3:
                operation, amount = line.split(",")

                if operation == "supply":
                    supply += int(amount)
                if operation == "buy":
                    buy += int(amount)

        with open(report_file_name, "w") as report_file:
            output = f"supply,{supply}\nbuy,{buy}\nresult,{supply - buy}\n"
            report_file.write(output)
