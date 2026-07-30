from pathlib import Path


def create_report(data_file_name: str, report_file_name: str) -> None:
    script_dir = Path(__file__).parent
    file_path = script_dir.parent / data_file_name

    data_file = open(file_path)
    data = [el.rstrip("\n") for el in data_file.readlines()]
    report = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }

    for item in data:
        key, value = item.split(",")
        report[key] = report.get(key, 0) + int(value)

    report["result"] = report["supply"] - report["buy"]

    data_file.close()

    report_file = open(f"../{report_file_name}", "w")
    for item, total in report.items():
        line_to_write = f"{item},{total}\n"
        report_file.write(line_to_write)

    report_file.close()
