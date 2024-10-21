import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file_path = os.path.join(BASE_DIR, "..", data_file_name)
    report_file_path = report_file_name  #os.path.join(BASE_DIR, "..", report_file_name)

    if not os.path.exists(data_file_path):
        raise FileNotFoundError(f"The data file '{data_file_path}' does not exist.")

    total_supply = 0
    total_buy = 0

    file = open(data_file_path, "r")
    for line in file:
        if not line.strip():
            continue

        operation, amount = line.strip().split(",")
        amount = int(amount)

        if operation == "supply":
            total_supply += amount
        elif operation == "buy":
            total_buy += amount

    file.close()

    report_file = open(report_file_path, "w")
    report_file.write(f"supply,{total_supply}\n")
    report_file.write(f"buy,{total_buy}\n")
    report_file.write(f"result,{total_supply - total_buy}\n")

    report_file.close()
