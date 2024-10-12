import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    # read file
    file_read = open(data_file_name)
    csv_content = csv.reader(file_read)

    # handle file
    result_dict = {"supply": 0, "buy": 0}
    for row in csv_content:
        if row[0] == "supply":
            result_dict["supply"] = result_dict.get("supply") + int(row[1])
        if row[0] == "buy":
            result_dict["buy"] = result_dict.get("buy") + int(row[1])

    result_dict.update(
        {"result": result_dict.get("supply") - result_dict.get("buy")}
    )

    file_read.close()

    result_list = []
    for action, number in result_dict.items():
        result_list.append([action, str(number)])

    # write file
    file_write = open(report_file_name, "w")
    writer = csv.writer(file_write)
    for row in result_list:
        writer.writerow(row)

    file_write.close()
