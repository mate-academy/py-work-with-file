from app.constants import report_view, result, supply, buy


def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    with open(data_file_name) as file:
        data = file.read()
    for current_name in report_view:
        count = 0
        for line in data.split("\n"):
            if line and current_name in line:
                count += int(line.split(",")[-1])
        report_view[current_name] = count
    report_view[result] = report_view[supply] - report_view[buy]
    with open(report_file_name, "w") as report:
        for action, report_value in report_view.items():
            report.write(f"{action},{report_value}\n")

