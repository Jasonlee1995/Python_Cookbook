import multiprocessing


def engine(arr):
    gpu, test_per_gpu = arr
    print(f'gpu : {gpu}    {len(test_per_gpu)} {test_per_gpu}')


if __name__ == '__main__':
    gpus = list(range(4))
    test = list(range(30))

    num_per_gpu  = len(test) // len(gpus)
    test_gpus = []
    for i in range(len(gpus) - 1):
        test_gpus.append(test[num_per_gpu * i : num_per_gpu * (i+1)])
    test_gpus.append(test[num_per_gpu * (i+1) : ])

    with multiprocessing.Pool(len(gpus)) as p:
        p.map(engine, zip(gpus, test_gpus))


    '''print result
    gpu : 0    7 [0, 1, 2, 3, 4, 5, 6]
    gpu : 1    7 [7, 8, 9, 10, 11, 12, 13]
    gpu : 2    7 [14, 15, 16, 17, 18, 19, 20]
    gpu : 3    9 [21, 22, 23, 24, 25, 26, 27, 28, 29]
    '''