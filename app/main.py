def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as source, \
            open(report_file_name, "a") as target:
        data = {}
        for line in source.readlines():
            line = [line.split(",")[0], int(line.split(",")[1])]
            if line[0] in data:
                data[line[0]] += line[1]
            else:
                data[line[0]] = line[1]

        data["result"] = data["supply"] - data["buy"]

        target.write(f"supply,{data['supply']}\n")
        target.write(f"buy,{data['buy']}\n")
        target.write(f"result,{data['result']}\n")
