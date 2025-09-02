
def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open (data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                operation, amount = line.split(",")
                amount = int(amount)
                if operation == "buy":
                    buy += amount
                elif operation == "supply":
                    supply += amount

    result = supply - buy

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\n")
        file.write(f"buy,{buy}\n")
        file.write(f"result,{result}\n")
