def create_report(data_file_name: str,
                  report_file_name: str) -> None:

    with open(data_file_name, "r") as data, \
            open(report_file_name, "w") as report:
        data_dict = {}
        for i in data:
            new = [i.rstrip("\n").split(",")]
            for name in new:
                if name[0] not in data_dict:
                    data_dict[name[0]] = int(name[1])
                else:
                    data_dict[name[0]] += int(name[1])
        data_dict["result"] = data_dict["supply"] - data_dict["buy"]

        report.write(f"supply,{data_dict['supply']}\n"
                     f"buy,{data_dict['buy']}\n"
                     f"result,{data_dict['result']}\n")
