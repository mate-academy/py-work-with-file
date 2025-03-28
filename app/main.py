def create_report(data_file_name: str, report_file_name: str) -> None:
    csv_dict = {
        "supply": 0,
        "buy": 0
    }

    with open(data_file_name) as data_file:
        for line in data_file.readlines():
            if line != "":
                key, value = line.split(",")
                csv_dict[key] += int(value[:len(value) - 1])

    with open(report_file_name, "w") as report_file:
        for key, value in csv_dict.items():
            report_file.writelines([key, ",", str(value), "\n"])

        report_file.writelines(["result,",
                                str(csv_dict["supply"] - csv_dict["buy"]),
                                "\n"])
