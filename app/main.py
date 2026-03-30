from pathlib import Path


def create_report(data_file_name: str, report_file_name: str) -> None:
    base_dir = Path(__file__).resolve().parent.parent

    input_path = base_dir / data_file_name   # читаем из корня
    output_path = Path(report_file_name)     # пишем в cwd!

    supply = 0
    buy = 0

    with open(input_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            operation, value = line.split(',')
            value = int(value)

            if operation == "supply":
                supply += value
            elif operation == "buy":
                buy += value

    result = supply - buy

    with open(output_path, 'w') as f:
        f.write(f"supply,{supply}\n")
        f.write(f"buy,{buy}\n")
        f.write(f"result,{result}\n")
