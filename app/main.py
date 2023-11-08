def create_report(data_file_name: str,
                  report_file_name: str
                  ) -> None:

    dict_in = {"supply": 0, "buy": 0}

    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):

        for line_text in file_in:
            if line_text == "\n":
                continue
            operation_type, amount = line_text.split(",")
            dict_in[operation_type] += int(amount)
        dict_in["result"] = dict_in["supply"] - dict_in["buy"]

        for key, value in dict_in.items():
            file_out.write(f"{key},{value}\n")
