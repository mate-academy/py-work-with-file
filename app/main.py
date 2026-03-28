def create_report(data_file_name: str, report_file_name: str):
    data = {}

    with open(data_file_name, "r") as file_in:
        for line in file_in.readlines():
            line = line.split(",")
            if line[0] not in data:
                data[line[0]] = int(line[1])
            else:
                data[line[0]] += int(line[1])

    with open(report_file_name, "w") as file_out:
        report = f"supply,{data['supply']}\n" \
                 f"buy,{data['buy']}\n" \
                 f"result,{data['supply'] - data['buy']}\n"
        file_out.write(report)
