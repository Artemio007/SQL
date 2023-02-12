
def concat(*fields):
    con = ""
    for field in fields:
        con += field[0]
    return con