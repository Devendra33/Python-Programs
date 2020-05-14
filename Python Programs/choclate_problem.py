def choclate(cost, choc, wrap):
    c = cost//choc
    w = c
    tot_choc = c
    while w >= wrap:
        rwrap = w % wrap
        rchoc = w // wrap
        tot_choc += rchoc
        w = rwrap + rchoc
    print(tot_choc)
choclate(15, 3, 2)


