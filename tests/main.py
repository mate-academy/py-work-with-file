def create_report(data_file_name: str, report_file_name: str) -> None:
    object_dictionary = {}
    with open(data_file_name, "r") as read_data_stream:
        for line in read_data_stream:
            separated = line.split(",")
            if len(separated) != 2:
                return
            object_type = separated[0]
            object_value = separated[1]
            if object_dictionary.get(object_type):
                object_dictionary[object_type] += int(object_value)
            else:
                object_dictionary[object_type] = int(object_value)
    with open(report_file_name, "w") as write_data_stream:

        write_data_stream.write("supply" + "," +
                                str(object_dictionary["supply"]) + '\n')
        write_data_stream.write("buy" + "," +
                                str(object_dictionary["buy"]) + '\n')
        write_data_stream.write("result," +
                                str(object_dictionary["supply"] - object_dictionary["buy"]) + '\n')
