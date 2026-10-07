def create_report(data_file_name: str, report_file_name: str) -> None:
    buff = {}
    with open(data_file_name, "r") as data_file:
        while True:
            line = data_file.readline()
            if not line:
                break
            name, value = line.split(",")
            if name not in buff:
                buff[name] = int(value)
            else:
                buff[name] += int(value)

    buff["result"] = buff["supply"] - buff["buy"]
    new_f = open(report_file_name, "w")
    supply = buff["supply"]
    buy = buff["buy"]
    result = supply - buy

    new_f.write(f"supply,{supply}\n")
    new_f.write(f"buy,{buy}\n")
    new_f.write(f"result,{result}\n")

    new_f.close()
