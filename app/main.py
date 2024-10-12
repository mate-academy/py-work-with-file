import csv


def create_report(data_file_name: str, report_file_name: str):
    file_read = open(data_file_name)
    # content = file_read.readlines()
    # print(content)
    csv_content = csv.reader(file_read)
    # csv_content = csv.DictReader(file_read)

    result_dict = {"supply": 0, "buy": 0}
    # for row in csv_content:
    #     print(row)
    #     if row[0] not in result_dict:
    #         result_dict.update({row[0]: int(row[1])})
    #     else:
    #         result_dict[row[0]] = result_dict.get(row[0]) + int(row[1])

    for row in csv_content:
        print(row)
        if row[0] == "supply":
            result_dict["supply"] = result_dict.get("supply") + int(row[1])
        if row[0] == "buy":
            result_dict["buy"] = result_dict.get("buy") + int(row[1])

    result_dict.update({"result": result_dict.get("supply") - result_dict.get("buy")})

    # print(result_dict)

    file_read.close()

    result_list = []
    for key, value in result_dict.items():
        print(key, value)
        result_list.append([key, str(value)])

    # print(result_list)

    file_write = open(report_file_name, "w")
    writer = csv.writer(file_write)
    for row in result_list:
        writer.writerow(row)
    file_write.close()


# file_read = "apples.csv"
# file_write = f"result_{file_read}"
# create_report(file_read, file_write)
