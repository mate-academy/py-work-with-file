def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as f:
        result = f.read().strip().split("\n")

    collected_data = {}

    for el in result:
        key, value = el.split(",")
        if key in collected_data:
            collected_data[key] += int(value)
        else:
            collected_data[key] = int(value)

    collected_data["result"] = collected_data["supply"] - collected_data["buy"]

    keys_order = ["supply", "buy", "result"]
    collected_data = {key: collected_data[key] for key in keys_order}

    report_data = ""
    for key, value in collected_data.items():
        report_data += f"{key},{value}\n"

    with open(report_file_name, "w") as f:
        f.write(report_data)
