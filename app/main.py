def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as file:
        lines = file.readlines()

        supply = 0
        buy = 0

        for line in lines:
            line = line.strip()
            if line:
                op_type, amount = line.split(",")
                amount = int(amount)

                if op_type == "supply":
                    supply += amount
                elif op_type == "buy":
                    buy += amount

        result = (supply - buy)
        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{supply}\n")
            report_file.write(f"buy,{buy}\n")
            report_file.write(f"result,{result}\n")
