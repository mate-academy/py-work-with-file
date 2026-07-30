def create_report(data_file_name: str, report_file_name: str) -> None:
    import os
    if not os.path.exists(data_file_name):
        raise FileNotFoundError(f"File {data_file_name} does not exist.")

    storage = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            if not line.strip():
                continue
            formatted_str = line.strip().split(",")
            key, value = formatted_str[0], formatted_str[1]
            if len(formatted_str) == 2 and key in storage and value.isdigit():
                storage[formatted_str[0]] += int(formatted_str[1])

    storage["result"] = storage["supply"] - storage["buy"]

    with open(report_file_name, "w") as report_file:
        for key, value in storage.items():
            report_file.write(f"{key},{value}\n")
