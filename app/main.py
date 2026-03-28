def create_report(data_file_name: str, report_file_name: str) -> None:

    groceries = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as file:

        for line in file.readlines():
            grocery_list = line.strip().split(",")
            if len(grocery_list) == 2 and grocery_list[1].isnumeric():
                if grocery_list[0] not in groceries:
                    groceries[grocery_list[0]] = int(grocery_list[1])
                else:
                    groceries[grocery_list[0]] += int(grocery_list[1])

    with open(report_file_name, "w") as file:
        for grocery_key, grocery_value in groceries.items():
            file.write(f"{grocery_key},{grocery_value}\n")

        file.write(f"result,{groceries['supply'] - groceries['buy']}\n")
