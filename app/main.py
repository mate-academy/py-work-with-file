def create_report(data_file_name: str, report_file_name: str) -> None:
    source = open(data_file_name, "r")
    source_dict = {}
    for line in source.readlines():
        line = line.strip().split(",")
        key = line[0]
        value = int(line[1])
        source_dict[key] = source_dict.setdefault(key, 0) + value
    source.close()

    report = open(report_file_name, "w")
    report.write(f"supply,{source_dict.get('supply')}\n")
    report.write(f"buy,{source_dict.get('buy')}\n")
    report.write(
        f"result,{source_dict.get('supply') - source_dict.get('buy')}\n"
    )
    report.close()
