def create_report(data_file_name: str, report_file_name: str):
    dict1 = {}
    with open("..\\" + data_file_name,
              "r") as input_file, open(report_file_name, "w") as report:
        for i in input_file.read().split():
            operation_type = i.split(",")[0]
            amount = int(i.split(",")[1])
            if operation_type in dict1:
                dict1[operation_type] += amount
            else:
                dict1.update({operation_type: amount})
        final = f"supply,{dict1['supply']}\n"
        final += f"buy,{dict1['buy']}\n"
        final += f"result,{dict1['supply'] - dict1['buy']}\n"
        report.write(final)
