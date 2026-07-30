from pathlib import Path


def create_report(data_file_name: str, report_file_name: str) -> None:
    project_root = Path(__file__).resolve().parent.parent
    data_path = project_root / data_file_name
    csv_file = open(data_path, "r")
    file_content = csv_file.read()

    supply = 0
    buy = 0

    for line in file_content.strip().splitlines():
        if not line:
            continue
        operation_type, amount = line.split(",")
        if operation_type == "supply":
            supply += int(amount)
        elif operation_type == "buy":
            buy += int(amount)

    result = supply - buy
    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{supply}\n")
    report_file.write(f"buy,{buy}\n")
    report_file.write(f"result,{result}\n")
    csv_file.close()
    report_file.close()
