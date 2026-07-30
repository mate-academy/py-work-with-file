def create_report(data_file_name: str,
                  report_file_name: str
                  ) -> None:
    with open(data_file_name, "r") as f:
        supply = 0
        buy = 0
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 2:
                continue

            operation = parts[0].strip()
            amount_str = parts[1].strip()
            if amount_str.isdigit():
                amount = int(amount_str)
                if operation == "supply":
                    supply += amount
                elif operation == "buy":
                    buy += amount

            print(line, end="")

        result = supply - buy
    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\nbuy,{buy}\nresult,{result}\n")
