# def create_report(data_file_name: str, report_file_name: str) -> None:
#     with open(data_file_name, "r") as f:
#         f_read = f.read()
#         supply_total = 0
#         buy_total = 0
#
#         for line in f_read:
#             operation, number = line.split(",")
#             if operation == "supply":
#                 supply_total += int(number)
#             elif operation == "buy":
#                 buy_total += int(number)
#
#         result = supply_total - buy_total
#
#     with open(report_file_name, "w") as file:
#         file.write(f"supply,{supply_total}\n")
#         file.write(f"buy,{buy_total}\n")
#         file.write(f"result,{result}\n")


def read_csv_file_headless(data_file_name: str) -> list[dict]:
    with open(data_file_name, "r") as f:
        raw_data = f.readlines()
        prepared_data = []
        for line in raw_data:
            tempe = dict()
            row = line.strip().split(",")
            tempe["operation type"] = row[0]
            tempe["amount"] = int(row[1])
            prepared_data.append(tempe)

        return prepared_data


def create_report(data_file_name: str, report_file_name: str) -> None:
    csv_data = read_csv_file_headless(data_file_name)
    report = {"supply": 0, "buy": 0, "result": 0}
    for record in csv_data:
        if record.get("operation type") in report.keys():
            report[record.get("operation type")] += int(record.get("amount"))
        report["result"] = report.get("supply") - report.get("buy")
    with open(report_file_name, "w") as f:
        for key, value in report.items():
            f.write(f"{key},{value}\n")


# def read_csv_file(data_file_name: str) -> list[dict]:
#     with open(data_file_name, "r") as f:
#          raw_data = f.readlines()
#
#          headers = raw_data[0].strip().split(",")
#          prepared_data = []
#
#          for line in raw_data[1:]:
#              tempe = dict()
#              for index, header in enumerate(headers):
#                  tempe[header] = line.strip().split(",")[index]
#              prepared_data.append(tempe)
#
#          return prepared_data
