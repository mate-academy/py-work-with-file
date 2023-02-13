def create_report(data_file_name: str, report_file_name: str):
    data_to_writing = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as file_read:
        data = file_read.read()
        for row in data.split("\n"):
            if row:
                name, value = row.split(",")
                data_to_writing[name] += int(value)

        data_to_writing["result"] = data_to_writing["supply"] - data_to_writing["buy"]

    with open(report_file_name, "w") as file_write:
        for key, value in data_to_writing.items():
            file_write.write(f"{key},{value}\n")


create_report("oranges.csv", "data.csv")
