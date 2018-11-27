def get_ngram(file, n):
    f = open(file, "r").readlines()
    out_f = []
    for k, line in enumerate(f):
        out_f.append([])
        tokens = line.split()
        for token in tokens:
            out_f[-1].append([])
            lens = len(token)
            for i in range(1, n+1):
                for j in range(lens):
                    if j + i <= lens:
                        sub = token[j:j+i]
                        out_f[-1][-1].append(sub)
    return out_f

def get_dict(n_grams):
    dict2 = {}
    for n_gram in n_grams:
        for token in n_gram:
            for n_g in token:
                if n_g in dict2:
                    dict2[n_g] += 1
                else:
                    dict2[n_g] = 1
    return dict2

def output_dict(d, out):
    f = open(out, "w")
    for key in d:
        f.write(key + " " + str(d[key]) + "\n")
    print("Output to dict {}!".format(d))

def out_train_file(n_grams, train_file):
    f = open(train_file, "w")
    for n_gram in n_grams:
        f.write(str(n_gram) + "\n")
    print("Output to file {}!".format(train_file))

def main(input, out_train, out_dict, n=4):
    n_grams = get_ngram(input, n=n)
    d = get_dict(n_grams)
    out_train_file(n_grams, out_train)
    output_dict(d, out_dict)



if __name__ == '__main__':
    import sys
    main(sys.argv[0],
         sys.argv[1],
         sys.argv[2],
         int(sys.argv[3]))