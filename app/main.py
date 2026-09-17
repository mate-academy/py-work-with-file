def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total: int = 0
    buy_total: int = 0

    try:
        with open(data_file_name, "r") as file_in:
            for line in file_in:
                line = line.strip()
                if not line:
                    continue

                try:
                    operation_type, amount_str = line.split(",")
                    amount: int = int(amount_str)

                    if operation_type == "supply":
                        supply_total += amount
                    elif operation_type == "buy":
                        buy_total += amount
                except (ValueError, IndexError):
                    # Пропускаємо рядки з некоректним форматом
                    continue
    except FileNotFoundError:
        print(f"File {data_file_name} not found.")
        return

    result: int = supply_total - buy_total

    report_content: str = (
        f"supply,{supply_total}\n"
        f"buy,{buy_total}\n"
        f"result,{result}\n"
    )

    with open(report_file_name, "w") as file_out:
        file_out.write(report_content)
