def create_report(data_file_name: str, report_file_name: str) -> None:
    info = {}
    with (open(data_file_name)) as read_file:
        for line in read_file:
            split_line = line.split(",")
            info[split_line[0]] = (info.get(split_line[0], 0)
                                   + int(split_line[1]))

    info["result"] = info["supply"] - info["buy"]
    order = ["supply", "buy", "result"]
    with (open(report_file_name, "w")) as write_file:
        write_file.writelines(f"{key},{info[key]}\n" for key in order)
