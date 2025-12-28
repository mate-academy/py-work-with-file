import os


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    data_file_path = os.path.join(os.getcwd(), data_file_name)
    report_file_path = os.path.join(os.getcwd(), report_file_name)

    try:
        data_file = open(data_file_path, "r")
        for line in data_file:
            if line.strip():
                operation, amount = line.strip().split(",")
                if operation == "supply":
                    supply_total += int(amount)
                elif operation == "buy":
                    buy_total += int(amount)
    except FileNotFoundError:
        print("File not found")

    result = supply_total - buy_total

    report_file = open(report_file_path, "w")
    report_file.write(f"supply,{supply_total}\n")
    report_file.write(f"buy,{buy_total}\n")
    report_file.write(f"result,{result}\n")
