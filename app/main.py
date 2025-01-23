def create_report(data_file_name: str, report_file_name: str) -> None:
    try:
        total_supply = 0
        total_buy = 0

        with open(data_file_name, "r") as data_file:
            for line in data_file:
                if not line.strip():
                    continue

                operation, amount = line.strip().split(",")
                amount = int(amount)

                if operation == "supply":
                    total_supply += amount
                elif operation == "buy":
                    total_buy += amount

        result = total_supply - total_buy

        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{total_supply}\n")
            report_file.write(f"buy,{total_buy}\n")
            report_file.write(f"result,{result}\n")

        print(f"Report created: {report_file_name}")

    except FileNotFoundError:
        print(f"Error: File {data_file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
