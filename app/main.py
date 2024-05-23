def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "w") as file_out):
        text = file_in.read().split()
        result_dict = {}

        for item in text:
            key, value = item.split(",")
            value = int(value)

            if key in result_dict:
                result_dict[key] += value
            else:
                result_dict[key] = value

        file_out.write(
            f"supply,{str(result_dict["supply"])}\n"
            f"buy,{str(result_dict["buy"])}\n"
            f"result,{result_dict["supply"] - result_dict["buy"]}\n"
        )
