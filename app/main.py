import os


def create_report(data_file_name: str, report_file_name: str) -> None:
    if not os.path.exists(data_file_name):
        return
    report_data = {}
    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as report_file
    ):
        for line in data_file:
            data = line.split(",")
            if len(data) != 2:
                return

            key, value = data
            report_data[key] = int(value) + report_data.get(key, 0)
        if not report_data.get("supply") or not report_data.get("buy"):
            return
        report_file.write(
            f"supply,{report_data['supply']}"
            + "\n" + f"buy,{report_data['buy']}"
            + "\n" + f"result,{report_data['supply'] - report_data['buy']}"
            + "\n"
        )
