import os


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    base_path = os.path.dirname(__file__)
    input_path = os.path.join(base_path, "..", data_file_name)

    with open(input_path) as file:
        for line in file:
            if line.strip() == "":
                continue
            operation, amount = line.strip().split(",")
            if operation == "supply":
                supply += int(amount)
            elif operation == "buy":
                buy += int(amount)

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{supply - buy}\n")
