def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as first:
        read = first.read()
        list_first = read.split()
        supply_count = 0
        buy_count = 0
        resulto = 0

        for i in list_first:
            operatcie, quantity = i.split(",")
            if operatcie == "supply":
                supply_count += int(quantity)
            elif operatcie == "buy":
                buy_count += int(quantity)

        resulto = supply_count - buy_count
        text_to_file = "".join(("supply,", str(supply_count), "\n",
                                "buy,", str(buy_count), "\n",
                                "result,", str(resulto), "\n"))

        with open(report_file_name, "w") as second:
            second.write(text_to_file)
