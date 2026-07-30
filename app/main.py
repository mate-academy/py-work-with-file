import os


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    base_dir = os.path.dirname(os.path.dirname(__file__))
    data_path = os.path.join(base_dir, data_file_name)

    with open(data_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            op, amount = line.split(",")
            amount = int(amount)
            if op == "supply":
                supply += amount
            elif op == "buy":
                buy += amount

    result = supply - buy

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{result}\n")
