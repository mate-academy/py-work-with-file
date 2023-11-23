def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as csv_data:
        data_lines = csv_data.readlines()
        data_store = dict()
        data_split = [line.strip().split(",") for line in data_lines]
        for data in data_split:
            if not data[0] in data_store:
                data_store[data[0]] = int(data[1])
            else:
                data_store[data[0]] += int(data[1])

        data_store["result"] = data_store.get("supply") - data_store.get("buy")

    with open(report_file_name, "a") as report:
        report.write(
            f"supply,{data_store.get('supply')}\n"
            f"buy,{data_store.get('buy')}\n"
            f"result,{data_store.get('result')}\n"
        )
