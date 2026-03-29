def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(report_file_name, "w") as report_file:
        write_dict = {}
        for line in open(data_file_name).read().split("\n"):
            if line == "":
                break
            elif line.split(",")[0] not in write_dict:
                write_dict[line.split(",")[0]] = int(line.split(",")[1])
            else:
                write_dict[line.split(",")[0]] += int(line.split(",")[1])
        write_dict["result"] = write_dict["supply"] - write_dict["buy"]
        report_file.write(f"supply,{write_dict['supply']}\nbuy,"
                          f"{ write_dict['buy']}\nresult,"
                          f"{write_dict['result']}\n")
