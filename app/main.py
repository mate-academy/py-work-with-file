def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {
        "supply": 0,
        "buy": 0,
    }

    try:
        with open(data_file_name, "r") as file_in:
            for line in file_in.readlines():
                key, value = line.split(",")
                report[key] += int(value)

    except FileNotFoundError:
        print("File not found!")

    with open(report_file_name, "a") as file_out:
        for key, value in report.items():
            file_out.write(f"{key},{value}\n")

        file_out.write(f"result,{report['supply'] - report['buy']}\n")
