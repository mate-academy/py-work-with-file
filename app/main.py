def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as data:
        aggregated = {"supply": [], "buy": []}
        for string in data.readlines():
            if "supply," in string:
                aggregated["supply"].append(int(string.replace("supply,", "")))
            if "buy," in string:
                aggregated["buy"].append(int(string.replace("buy,", "")))
    with open(report_file_name, "w") as report:
        supply = sum(aggregated['supply'])
        buy = sum(aggregated['buy'])
        report.write(f"supply,{supply}\n"
                     f"buy,{buy}\n"
                     f"result,{supply - buy}\n"
                     )
