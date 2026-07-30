def create_report(data_file_name: str, report_file_name: str) -> None:
    parsed_data = []
    try:
        with open(data_file_name, "r") as data_file_obj:
            data = data_file_obj.readlines()
            for line in data:
                row = line.strip().split(",")
                parsed_data.append(row)
        with open(report_file_name, "w") as report_file_obj:
            values = {"buy": 0, "supply": 0}
            for item in parsed_data:
                key = item[0]
                value = item[1]
                if key == "buy":
                    values["buy"] += int(value)
                if key == "supply":
                    values["supply"] += int(value)
            values_to_str = {key: str(value) for key, value in values.items()}
            result = values["supply"] - values["buy"]
            report_file_obj.write("supply"
                                  + ","
                                  + values_to_str["supply"]
                                  + "\n")
            report_file_obj.write("buy" + "," + values_to_str["buy"] + "\n")
            report_file_obj.write("result" + "," + str(result) + "\n")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Data file was not found")

    except IOError as e:
        print(f"Error: {e}")
        print("Read/write error happened")
