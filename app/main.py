def create_report(data_file_name: str, report_file_name: str) -> None:
    origin = open(data_file_name)
    new_file = open(report_file_name, "a")
    stuff = {}

    for line in origin.readlines():
        parts = line.split(",")
        if parts[0] not in stuff:
            stuff[parts[0]] = int(parts[1])
        else:
            stuff[parts[0]] += int(parts[1])

    stuff["result"] = stuff["supply"] - stuff["buy"]
    origin.close()

    new_file.write("supply,")
    new_file.write(f"{stuff["supply"]}\n")

    new_file.write("buy,")
    new_file.write(f"{stuff["buy"]}\n")

    new_file.write("result,")
    new_file.write(f"{stuff["result"]}\n")

    new_file.close()
