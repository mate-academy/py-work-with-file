def create_report(data_file_name: str, report_file_name: str) -> None:
    file_data = open(data_file_name, "r")
    rep_data = {}
    for line in file_data.readlines():
        if line.strip() != "":
            columns = line.split(",")
            name = columns[0]
            value = int(columns[1])
            if name not in rep_data:
                rep_data[name] = value
            else:
                rep_data[name] += value

    file_data.close()

    result = rep_data["supply"] - rep_data["buy"]

    file_report = open(report_file_name, "w")
    file_report.write(f"supply,{rep_data['supply']}\n")
    file_report.write(f"buy,{rep_data['buy']}\n")
    file_report.write(f"result,{result}\n")

    file_report.close()
