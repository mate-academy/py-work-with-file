import os


def create_report(
        data_file_name: str,
        report_file_name: str) -> None:
    current_dir = os.path.dirname(__file__)
    data_file_path = os.path.join(current_dir, "..", data_file_name)

    with open(data_file_path, "r") as file:
        lines = file.read().splitlines()

    result = {}

    for line in lines:
        if not line.strip():
            continue
        parts = line.split(",")
        operation_type, amount = parts[0], int(parts[1])

        if operation_type in result:
            result[operation_type] += amount
        else:
            result[operation_type] = amount

    sorted_result = dict(
        sorted(
            result.items(),
            key=lambda x: x[1],
            reverse=True))

    with open(report_file_name, "w") as w:
        for i in sorted_result:
            w.write(f"{i},{sorted_result[i]}\n")

    result_line = (
        f"result,"
        f"{sorted_result.get('supply', 0) - sorted_result.get('buy', 0)}"
    )
    with open(report_file_name, "a") as report_file:
        report_file.write(f"{result_line}\n")
