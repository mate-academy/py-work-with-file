def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as file:
        d = {}
        for info in file:
            values = info.rstrip("\n").split(",")
            d.setdefault(values[0], []).append(int(values[1]))

    supply, buy = sum(d["supply"]), sum(d["buy"])

    with open(report_file_name, "w") as info_file:
        info_file.write(f"supply,{supply}" + "\n")
        info_file.write(f"buy,{buy}" + "\n")
        info_file.write(f"result,{supply - buy}" + "\n")
