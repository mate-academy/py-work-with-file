import os


def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:

    data_dict = {"result": 0,
                 "supply": 0,
                 "buy": 0}

    with open(os.path.abspath(
            data_file_name), "r") as file:

        for line in file:
            if line.rstrip():

                data = line.split(",")
                key = data[0]
                value = int(data[1][:-1])

                if key in data_dict:
                    data_dict[key] += value
                else:
                    data_dict.update({key: value})
        file.close()

    data_dict["result"] += data_dict["supply"]
    data_dict["result"] -= data_dict["buy"]

    with open(os.path.abspath(report_file_name),
              "a") as report:

        report.write(f"supply,{str(data_dict['supply'])}\n")
        report.write(f"buy,{str(data_dict['buy'])}\n")
        report.write(f"result,{str(data_dict['result'])}\n")

        report.close()
