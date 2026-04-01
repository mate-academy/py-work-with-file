def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r")
          as file_in, open(report_file_name, "a") as file_out):

        data = file_in.read()
        new_str = data.replace("\n", " ").replace(",", " ")
        lst = new_str.split(" ")

        supply = 0
        buy = 0
        for i in range(len(lst) - 1):
            if lst[i] == "supply":
                supply += int(lst[i + 1])
            if lst[i] == "buy":
                buy += int(lst[i + 1])

        report = ("supply," + str(supply) + "\n"
                  + "buy," + str(buy) + "\n"
                  + "result," + str(supply - buy) + "\n")

        file_out.write(report)
