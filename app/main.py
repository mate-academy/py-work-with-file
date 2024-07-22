def create_report(data_file_name: str, report_file_name: str) -> None:
    try:
        file_to_read = open(data_file_name)
    except FileNotFoundError:
        print("No such file in the directory")
    except PermissionError:
        print("You do not have an access to this file")
    else:
        supply = 0
        buy = 0
        for line in file_to_read:
            if line:
                splitted = line.split(",")
                if splitted[0] == "supply":
                    supply += int(splitted[1])
                else:
                    buy += int(splitted[1])
        result = supply - buy
    finally:
        file_to_read.close()
    try:
        file_to_write = open(report_file_name, "w")
    except FileNotFoundError:
        print("No such file in the directory")
    except PermissionError:
        print("You do not have an access to this file")
    else:
        file_to_write.write(
            "supply" + "," + str(supply) + "\n"
            + "buy" + "," + str(buy) + "\n"
            + "result" + "," + str(result) + "\n"
        )
    finally:
        file_to_write.close()
