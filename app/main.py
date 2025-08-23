def create_report(dn, rn):
    try:
        lines = open(dn, encoding="utf-8").read().splitlines()
    except FileNotFoundError:
        lines = open("../" + dn, encoding="utf-8").read().splitlines()
    s = b = 0
    for l in lines:
        if not l:
            continue
        op, amt = l.split(",", 1)
        if op == "supply":
            s += int(amt)
        else:
            b += int(amt)
    open(rn, "w", encoding="utf-8").write(f"supply,{s}\nbuy,{b}\nresult,{s-b}\n")
