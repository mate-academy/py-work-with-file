def amount_counter(row: str) -> int:
    """
    Split string by , and get integer
    :param row:
    :return:
    """
    return int(row.split(",")[1])


def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as report_file
    ):
        rows = data_file.read().split()
        buy_counter, supply_counter = 0, 0

        for row in rows:
            if "buy" in row:
                buy_counter += amount_counter(row)
            if "supply" in row:
                supply_counter += amount_counter(row)

        result = supply_counter - buy_counter
        file_content = (
            f"supply,{supply_counter}\n"
            f"buy,{buy_counter}\n"
            f"result,{result}\n"
        )
        report_file.write(file_content)
