def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        data = data_file.read()

        processed_data = {
            "supply": 0,
            "buy": 0
        }

        lines = data.split("\n")

        for line in lines:
            if line:
                operation, amount = line.split(",")
                amount = int(amount)

                if operation == "buy":
                    processed_data["buy"] += amount
                elif operation == "supply":
                    processed_data["supply"] += amount

    result = processed_data["supply"] - processed_data["buy"]

    with open(report_file_name, "w") as report_file:
        for operation_type, amount in processed_data.items():
            report_file.write(f"{operation_type},{amount}\n")
        report_file.write(f"result,{result}\n")


if __name__ == "__main__":
    create_report("data.csv", "data_result.csv")
