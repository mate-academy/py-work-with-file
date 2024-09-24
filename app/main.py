def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as file:
        dict_result = {}
        for info in file:
            values = info.rstrip("\n").split(",")
            dict_result.setdefault(values[0], []).append(int(values[1]))

    supply, buy = sum(dict_result["supply"]), sum(dict_result["buy"])

    with open(report_file_name, "w") as info_file:
        info_file.write(f"supply,{supply}" + "\n")
        info_file.write(f"buy,{buy}" + "\n")
        info_file.write(f"result,{supply - buy}" + "\n")
