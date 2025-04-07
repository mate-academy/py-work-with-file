# write your code here
def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data:
        list_of_date = data.readlines()
        dictionary = {}
        for data in list_of_date:
            el, quantity = data.strip().split(",")
            if el in dictionary.keys():
                dictionary[el] += int(quantity)
            else:
                dictionary[el] = int(quantity)
        with open(report_file_name, "w") as report:
            file_string = ""
            for item, quantity in dictionary.items():
                file_string += f"{item},{quantity}\n"
            report.write(file_string)
