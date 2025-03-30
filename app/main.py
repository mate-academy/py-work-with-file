

def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as FileToRead:
        amount_supply = 0
        amount_buy = 0
        for line in FileToRead:
            if len(line) == 0:
                continue

            operation_type, amount = linecd

            try:
                if operation_type == "supply":
                    amount_supply += int(amount)
                if operation_type == "buy":
                    amount_buy += int(amount)

            except ValueError:
                raise "!ERROR TYPE!"


    with open(report_file_name, "w") as FileToWrite:
        FileToWrite.write("supply," + str(amount_supply))
        FileToWrite.write("buy," + str(amount_buy))
        result = amount_supply - amount_buy
        FileToWrite.write("result," + str(result))