def read_lines(filename="", nb_lines=0):
    i = 0
    with open(filename) as fhandle:
        for line in fhandle:
            nb_lines += 1
            if i <= nb_lines and nb_lines > 0:
                print(line, end="")
            elif nb_lines <= 0:
                print(line, end="")
