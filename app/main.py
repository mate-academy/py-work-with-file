import os

def create_report(data_file_name: str, report_file_name: str) -> str:
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(current_script_dir)
    data_full_path = os.path.join(base_dir, data_file_name)
    report_full_path = os.path.join(base_dir, report_file_name)

    supply_total = 0
    buy_total = 0

    input_file = open(data_full_path, "r")
    for line in input_file:
        line = line.strip()
        if not line:
            continue
        operation, amount = line.split(",")
        amount = int(amount)
        if operation == "supply":
            supply_total += amount
        elif operation == "buy":
            buy_total += amount
    input_file.close()

    result = supply_total - buy_total
    report_file = open(report_full_path, "w")
    report_file.write(f"supply,{supply_total}\n")
    report_file.write(f"buy,{buy_total}\n")
    report_file.write(f"result,{result}\n")
    report_file.close()


create_report("apples.csv", "report.csv")
