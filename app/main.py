def create_report(data_file_name: str, report_file_name: str) -> None:
    arq = open(data_file_name)
    supply_total = 0
    buy_total = 0
    for line in arq:
        tipo, valor = line.strip().split(",")

        if tipo == "buy":
            buy_total += int(valor)

        if tipo == "supply":
            supply_total += int(valor)
    total = supply_total - buy_total

    arq.close()

    new_arq = open(report_file_name, "w")
    new_arq.write("supply,{}\n".format(supply_total))
    new_arq.write("buy,{}\n".format(buy_total))
    new_arq.write("result,{}\n".format(total))

    new_arq.close()
