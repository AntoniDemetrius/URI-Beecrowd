while True:
    try:
        N, R = [int(x) for x in input().strip().split(' ')]

        VLT = [False for i in range(N + 1)]

        for MERG in [int(x) for x in input().strip().split(' ')]:
            VLT[MERG] = True

        if(N == R):
            print('*')
        else:
            for i in range(1, N + 1):
                if(not VLT[i]):
                    print(f'{i} ', end='')
            print()
    except EOFError:
        break
