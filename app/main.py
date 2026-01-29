def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    total = {
        "supply": 0,
        "buy": 0
    }
    with open(data_file_name, "r") as file_read:
        for line in file_read.readlines():
            line = line.strip()
            if line != "":
                operation, amount = line.split(",")
                if operation.strip() == "supply":
                    total["supply"] += int(amount.strip())
                elif operation.strip() == "buy":
                    total["buy"] += int(amount.strip())
    total["result"] = total["supply"] - total["buy"]
    with open(report_file_name, "w") as file_write:
        for key, value in total.items():
            file_write.write(f"{key},{value}\n")
