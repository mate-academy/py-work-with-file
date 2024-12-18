# def create_report(data_file_name: str,
#                   report_file_name: str
#                   ) -> None:
#     data_dict = {"supply": 0, "buy": 0}
#
#     with open(data_file_name) as file:
#         for line in file.readlines():
#             if line:
#                 name, value = line.split(",")
#                 data_dict[name] += int(value)
#
#         data_dict["result"] = data_dict["supply"] - data_dict["buy"]
#
#     with open(report_file_name, "a") as report:
#         report.write(f"supply,{data_dict["supply"]}\n")
#         report.write(f"buy,{data_dict["buy"]}\n")
#         report.write(f"result,{data_dict["result"]}\n")
def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            if not line.strip():
                continue
            try:
                operation, amount = line.strip().split(",")
                amount = int(amount)
            except ValueError:
                continue
            if operation == "buy":
                buy += amount
            elif operation == "supply":
                supply += amount
    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n"
                          f"buy,{buy}\n"
                          f"result,{result}\n")