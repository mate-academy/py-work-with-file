import os


def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            operation, amount_str = line.split(",")
            amount = int(amount_str)

            if operation == "supply":
                total_supply += amount
            elif operation == "buy":
                total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, "w") as file:
        file.write(f"supply,{total_supply}\n")
        file.write(f"buy,{total_buy}\n")
        file.write(f"result,{result}\n")


if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, "..", "py-work-with-file")

    for filename in os.listdir(data_dir):
        filename = filename.strip()
        if filename.endswith(".csv") and not filename.endswith("_report.csv"):
            data_file = os.path.join(data_dir, filename)

            if os.path.getsize(data_file) == 0:
                continue

            name_without_ext = os.path.splitext(filename)[0]
            report_filename = f"{name_without_ext}_report.csv"
            report_file = os.path.join(data_dir, report_filename)

            create_report(
                data_file_name=data_file,
                report_file_name=report_file)
