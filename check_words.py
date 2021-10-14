def word_count():
    count = 0
    with open("Users\\moshe_ogalbo\\Downloads\\file.txt") as f:
        data = f.readLines()
        for line in data:
            words = line.split()
            for word in words:
                if word == "Alex":
                    count += 1
    return  count
