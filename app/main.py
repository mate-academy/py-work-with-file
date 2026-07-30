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

    result_string = ("supply," + str(stuff["supply"]) + "\nbuy,"
                     + str(stuff["buy"]) + "\nresult,"
                     + str(stuff["result"]) + "\n")

    new_file.write(result_string)

    new_file.close()
