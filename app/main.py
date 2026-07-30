import csv


def create_report(data_file_name: str, report_file_name: str):

    with open(f"{data_file_name}", "r") as file_in, \
            open(f"{report_file_name}", "w") as file_out:

        reader = csv.reader(file_in)

        list_data_file = [file for file in reader]

        dict_data_file = {"supply": 0, "buy": 0, "result": 0}
        for key in list_data_file:
            if dict_data_file.get(key[0]):
                dict_data_file[key[0]] += int(key[1])
            else:
                dict_data_file[key[0]] = int(key[1])
        dict_data_file["result"] = \
            dict_data_file["supply"] - dict_data_file["buy"]

        result = [[key, value] for key, value in dict_data_file.items()]
        writer = csv.writer(file_out, lineterminator='\n')
        writer.writerows(result)
