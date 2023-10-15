import csv


def create_report(data_file_name, report_file_name):

    f = open(f"{data_file_name}", "r")
    reader = csv.reader(f)
    list = []
    for line in reader:
        list.append(line)
    supply = 0
    for elements in list:
        if elements[0] == 'supply':
            supply += int(elements[1])
    buy = 0
    for elements in list:
        if elements[0] == 'buy':
            buy += int(elements[1])

    result = supply - buy

    final = open(f"{report_file_name}", "w")
    final.write(f"supply,{supply}\n"
                f"buy,{buy}\n"
                f"result,{result}\n"
                )
