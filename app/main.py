def create_report(data_file_name: str, report_file_name:str) -> None:
    data_file = open(data_file_name, "r")
    supply_sum = 0
    buy_sum = 0

    for f in data_file:
        if f == "":
            break
        for line in f:
            operator, number = line.split(",")
            number = int(number)
            if operator == "supply":
                supply_sum += number
            if operator == "buy":
                buy_sum += number
        new_number = open(report_file_name, "w")
        data_file.close()
        new_number.close()








