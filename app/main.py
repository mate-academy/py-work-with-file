def create_report(data_file_name: str, report_file_name: str) -> None:
    d = {}

    with open(data_file_name, "r") as f:
        for text in f:
            key, value = text.split(",")
            if key not in d:
                d[key] = int(value)
            else:
                d[key] += int(value)

    result = d["supply"] - d["buy"]

    with open(report_file_name, "w") as f:
        f.write(f"supply,{d['supply']}\n"
                f"buy,{d['buy']}\n"
                f"result,{result}\n")
