from collections import OrderedDict


def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
            open(data_file_name, "r") as file1,
            open(report_file_name, "w") as file2):
        dic = {}
        for line in file1:
            clean_line = line.strip()
            if not clean_line:
                continue
            operation, count = clean_line.split(",")
            count = int(count)
            dic[operation] = dic.get(operation, 0) + count

        dic = OrderedDict(dic)
        if "supply" in dic:
            dic.move_to_end("supply", last=False)

        for key, value in dic.items():
            context = f"{key},{value}\n"
            file2.write(context)
        result_value = dic.get("supply", 0) - dic.get("buy", 0)
        file2.write(f"result,{result_value}\n")
