def create_report(data_file_name: str, report_file_name: str):
    data = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as file_in, \
         open(report_file_name, "w") as file_out:
        for row in file_in:
            row = row.replace("\n", "").split(",")
            operation_type = row[0]
            amount = int(row[1])
            data[operation_type] += amount
        data["result"] = data["supply"] - data["buy"]
        file_out.write(f"supply,{data['supply']}\n"
                       f"buy,{data['buy']}\n"
                       f"result,{data['result']}\n")
