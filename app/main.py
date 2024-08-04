def create_report(data_file_name: str, report_file_name: str) -> str:
    account = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 2:
                continue
            key, value = parts
            account[key] += int(value)
    account["result"] = account["supply"] - account["buy"]

    with open(report_file_name, "w") as file:
        for key, value in account.items():
            file.write(f"{key}, {value}\n")
    return f"Report created: {report_file_name}"
