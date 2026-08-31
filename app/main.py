import csv


def create_report(data_file_name: str, report_file_name: str) -> None:

    supply_list = []
    buy_list = []

    sum_of_supply = 0
    sum_of_buy = 0
    result = 0

    with open(data_file_name, "r") as file:
        read_data = csv.reader(file)

        for i in read_data:
            print(i)
            if i[0] == "supply":
                supply_list.append(i[1])
            else:
                buy_list.append(i[1])

        sum_of_supply += sum((list(map(int, supply_list))))
        sum_of_buy += sum(list(map(int, buy_list)))

        result += sum_of_supply - sum_of_buy

    report_content = [
        ["supply", sum_of_supply],
        ["buy", sum_of_buy],
        ["result", result],
    ]

    with open(report_file_name, "w") as file:
        write_data = csv.writer(file)

        write_data.writerows(report_content)
