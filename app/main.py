def create_report(data_file_name: str, report_file_name: str) -> None:
    try:
        with open(data_file_name, "r") as file:
            lines = file.readlines()

            if len(lines) > 1:
                data = [line.strip().split(",") for line in lines[0:]]

                supply_total = sum(int(amount) for op_type, amount
                                   in data if op_type == "supply")
                buy_total = sum(int(amount) for op_type, amount in
                                data if op_type == "buy")

                result = supply_total - buy_total

                with open(report_file_name, "w") as report_file:
                    report_file.write(f"supply,{supply_total}\n")
                    report_file.write(f"buy,{buy_total}\n")
                    report_file.write(f"result,{result}\n")
            else:
                print("Error: CSV file is empty.")

    except FileNotFoundError:
        print(f"Error: File {data_file_name} not found.")


# example of usage
create_report("../apples.csv", "apples_report.csv")
create_report("../bananas.csv", "bananas_report.csv")
create_report("../grapes.csv", "grapes_report.csv")
create_report("../oranges.csv", "oranges_report.csv")
