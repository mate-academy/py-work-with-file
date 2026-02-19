def create_report(data_file_name: str, report_file_name: str) -> None:
    res = {"supply" : 0, "buy" : 0, "result" : 0}
    input_file = open(data_file_name)
    for line in input_file.readlines():
        data = line.split(",")
        res[data[0]] = res.get(data[0], 0) + int(data[1])
    res["result"] = res["supply"] - res["buy"]
    res = "\n".join([f"{key},{val}"for key, val in res.items()]) + "\n"
    input_file.close()
    output_file = open(report_file_name, "w")
    output_file.write(res)
    output_file.close()


if __name__ == "__main__":
    pass
