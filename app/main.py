def create_report(data_file_name: str, report_file: str) -> None:
    store = {}

    with open(data_file_name, "r") as file:
        for line in file.readlines():
            line = line.strip()
            if not line:
                continue

            key, value = line.split(",")
            if key not in store:
                store[key] = int(value)
            else:
                store[key] += int(value)

    with open(report_file, "w") as result_file:
        result_file.write(f"supply,{store['supply']}\n")
        result_file.write(f"buy,{store['buy']}\n")

        result = store["supply"] - store["buy"]
        result_file.write(f"result,{result}\n")
