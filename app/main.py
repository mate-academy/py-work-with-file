def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as in_f:
        data_dict = {}
        for line in in_f.readlines():
            if line == "" or line == "\n":
                break
            key, value = line.split(",")
            if key in data_dict.keys():
                data_dict[key] = int(data_dict[key]) + int(value)
            else:
                data_dict[key] = value

    with open(report_file_name, "w") as out_f:
        out_f.write(f"supply, {data_dict["supply"]}\n")
        out_f.write(f"buy, {data_dict["buy"]}\n")
        result = int(data_dict["supply"]) - int(data_dict["buy"])
        out_f.write(f"result, {result}\n")


create_report("apples.csv",
              "apples_report.csv")
