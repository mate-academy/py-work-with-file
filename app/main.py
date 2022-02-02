def create_report(data_file_name: str, report_file_name: str):
    data_dict = {}

    with open(data_file_name, "r") as data_file:
        data = data_file.read()
        data = data.split()
        for iterator, value in enumerate(data):
            temp = data[iterator].split(",")

            if temp[0] in data_dict:
                data_dict[temp[0]] += int(temp[1])
            else:
                data_dict[temp[0]] = int(temp[1])

        with open(report_file_name, "w") as report_file:
            result = data_dict["supply"] - data_dict["buy"]

            report_file.write("supply" + "," + str(data_dict["supply"]) + "\n")
            report_file.write("buy" + "," + str(data_dict["buy"]) + "\n")
            report_file.write("result" + "," + str(result) + "\n")
