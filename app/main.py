def create_report(data_file_name: str, report_file_name: str) -> None:
    file_read = open(data_file_name)
    file_write = open(report_file_name, "w")

    res_dict = {
        "buy": [],
        "supply": []
    }

    for line in file_read:
        arr = line.split(",")
        res_dict[arr[0]].append(int(arr[1]))

    file_read.close()

    supply = sum(res_dict["supply"])
    buy = sum(res_dict["buy"])
    result = supply - buy

    res = "\n".join([
        "supply," + str(supply),
        "buy," + str(buy),
        "result," + str(result) + "\n"]
    )

    file_write.write(res)
    file_write.close()
