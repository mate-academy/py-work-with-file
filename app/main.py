import tests

def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r", encoding="utf-8") as data_file, \
         open(report_file_name, "w", encoding="utf-8") as report_file:

        report = {
            "supply": 0,
            "buy": 0
        }

        for line in data_file:
            if not line.strip():
                continue
            column1, column2 = line.strip().split(",")

            report[column1] += int(column2)

        result = report["supply"] - report["buy"]

        report_file.write(f"supply,{report['supply']}\n")
        report_file.write(f"buy,{report['buy']}\n")
        report_file.write(f"result,{result}\n")




