def word_count():
    count = 0

    with open("Users\\moshe_ogalbo\\Jenkins-Projects-Final-1\\file.txt") as f:
        data = f.readlines()
        for line in data:
            words = line.split()
            for word in words:
                if word == "moshe":
                    count += 1
    return count