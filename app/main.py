def create_report(data_file_name: str, report_file_name: str) -> None:
    file_r = open(data_file_name, "r")
    data = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }
    for line in file_r.read().split("\n"):
        if len(line) == 0:
            break
        line_parts = line.split(",")
        data[line_parts[0]] = data[line_parts[0]] + int(line_parts[1])
    data.update({"result": data["supply"] - data["buy"]})
    file_r.close()

    file_w = open(report_file_name, "w")
    for key in data:
        file_w.write(f"{key},{data[key]}\n")
    file_w.close()
