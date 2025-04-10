def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data:
        list_of_date = data.readlines()
        dictionary = {}
        for data in list_of_date:
            el, quantity = data.strip().split(",")
            if el in dictionary:
                dictionary[el] += int(quantity)
            else:
                dictionary[el] = int(quantity)

        with open(report_file_name, "w") as report:
            file_string = ""
            file_string += f"supply,{dictionary["supply"]}\n"
            file_string += f"buy,{dictionary["buy"]}\n"
            file_string += (
                f"result,{dictionary["supply"] - dictionary["buy"]}\n"
            )
            report.write(file_string)
            print(file_string)
