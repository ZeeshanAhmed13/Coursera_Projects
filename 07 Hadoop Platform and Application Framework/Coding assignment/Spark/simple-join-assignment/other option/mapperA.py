def split_fileA(line):
    kv = line.strip().split(",")
    word = kv[0] 
    count = int(kv[1])
    return (word, count)
