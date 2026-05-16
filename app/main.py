from __future__ import annotations


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as input_file:
        for line in input_file:
            cleaned_line = line.strip()
            if not cleaned_line:
                continue

            operation_type, amount_str = cleaned_line.split(",")
            amount = int(amount_str)

            if operation_type == "supply":
                total_supply += amount
            elif operation_type == "buy":
                total_buy += amount

    result_value = total_supply - total_buy

    with open(report_file_name, "w") as output_file:
        output_file.write(f"supply,{total_supply}\n")
        output_file.write(f"buy,{total_buy}\n")
        output_file.write(f"result,{result_value}\n")
