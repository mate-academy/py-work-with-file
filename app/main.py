def create_report(data_file_name: str, report_file_name: str) -> None:
    counter = {}
    with open(data_file_name, "r") as file:
        for line in file:
            if not line.strip():
                continue
            key, value = line.strip().split(",")
            counter[key] = counter.get(key, 0) + int(value)

    counter["result"] = counter.get("supply", 0) - counter.get("buy", 0)

    with open(report_file_name, "a") as file_to_write:
        output_order = ["supply", "buy", "result"]
        for key in output_order:
            if key in counter:
                file_to_write.write(f"{key},{counter[key]}\n")
