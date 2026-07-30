def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:

    tmp_dict = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }

    with (open(data_file_name, "r") as source,
          open(report_file_name, "a") as report_file):

        for line in source.readlines():
            if line.strip():
                process_data, amount_data = line.strip().split(",")

                key_data = process_data.strip()
                val_data = int(amount_data.strip())

                tmp_dict[key_data] = tmp_dict[key_data] + val_data

        tmp_dict["result"] = tmp_dict["supply"] - tmp_dict["buy"]

        # write into report file
        for key_data, val_data in tmp_dict.items():
            line = f"{key_data},{val_data}\n"
            report_file.write(line)
