def split_fileB(line):
    kv = line.replace(" ",",").split(",")
    return (kv[1], kv[0] + " " + kv[2])
