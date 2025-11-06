import csv
# data_file_name read from this
# report_file_name write to this

def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    # file = open(data_file_name, "r")
    # a = csv.reader(data_file_name, delimiter=',', quotechar='|')
    # for row in a:
    #     print(a)
    with open(data_file_name, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            print(row)


create_report("../apples.csv", "../bananas.csv")



