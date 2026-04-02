from typing import Any


def create_report(data_file_name: str, report_file_name: str) -> Any:
    with open(data_file_name, "r") as f:
        buy = 0
        supply = 0
        for line in f:
            operation_type, amount = line.split(",")
            if operation_type == "buy":
                buy += int(amount)
            if operation_type == "supply":
                supply += int(amount)
        result = supply - buy
    with open(report_file_name, "w") as file_result:
        file_result.write(f"supply,{supply}\n")
        file_result.write(f"buy,{buy}\n")
        file_result.write(f"result,{result}\n")
