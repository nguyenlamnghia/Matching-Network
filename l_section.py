# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass
from math import pi, sqrt, isnan
# import numpy as np
from numpy import divide

def convert_f_unit(f, unit):
    match unit:
        case "Hz":
            return f
        case "KHz":
            return f * 1e3
        case "MHz":
            return f * 1e6
        case "GHz":
            return f * 1e9

# LC HIGHPASS OR LC DC BLOCK
def LCHP(data):
    rs = data[0]
    xs = data[1]
    rl = data[2]
    xl = data[3]
    f = convert_f_unit(data[4],data[8])

    # tinh omega
    w = 2 * pi * f

    # chuyen zl sang rs noi tiep vs c1
    ql = -xl/rl
    c1 = -1/(w*xl) if xl != 0 else float('inf')

    # chuyen zs sang rp song song voi l1
    qs = xs/rs
    l1 = ((1 + qs ** 2) * xs)/(w * qs ** 2) if qs != 0 else float('inf')

    print(c1,l1)
    rp = (1 + qs ** 2) * rs
    rs = rl

    # kiem tra rs < rp thi chay khong thi tra ve non
    if (rs > rp):
        return float('nan'), float('nan'), float('nan')
    else:
        # Tinh Q
        Q = sqrt(rp / rs - 1)

        # Tinh lp
        lp = rp/(w*Q)

        # tinh lc
        cs = 1/(Q*w*rs)

        # kiem tra neu xl = 0 thi tra ve c luon
        if xl == 0:
            c = cs * 1e12
        else:
            if c1 == cs:
                c = float('inf')
            # do c nt c1
            else:
                c = ((c1 * cs) / (c1 - cs)) * 1e12

        # kiem tra neu xs = 0 thi tra ve l luon
        if xs == 0:
            l = lp * 1e9
        else:
            if l1 == lp:
                l = float('inf')
            # do l1 // l
            else:
                l = ((lp * l1) / (l1 - lp)) * 1e9

        lchpcval = c
        lchpqval = abs(Q)
        lchplval = l
        return (lchpqval, lchpcval, lchplval, "LCHP")

# CL LOWPASS OR CL DC FEED
def CLLP(data):
    rs = data[0]
    xs = data[1]
    rl = data[2]
    xl = data[3]
    f = convert_f_unit(data[4],data[8])

    # tinh omega
    w = 2 * pi * f

    # chuyen zl sang rs noi tiep vs l1
    ql = xl / rl
    l1 = xl / w;

    # chuyen zs sang rp song song voi c1
    qs = -xs / rs
    rp = rs * (1+qs**2)
    c1 = qs / (rp*w)

    rs = rl

    # Kiem tra neu rs < rl thi chay
    if (rs > rp):
        return float('nan'), float('nan'), float('nan')
    else:
        Q = sqrt(rp / rl - 1);

        # tinh cp
        cp = Q/(rp*w)
        # do c // c1
        c = (cp - c1) * 1e12;

        # tinh ls
        ls = (Q * rl) / w
        # do l1 nt l
        l = (ls - l1) * 1e9

        return (Q, l, c, "CLLP")

# LC LOWPASS OR LC DC FEED
# Giong CLLP nhung load va source duoc hoan doi
def LCLP(data):
    rs = data[2]
    xs = data[3]
    rl = data[0]
    xl = data[1]
    f = convert_f_unit(data[4],data[8])

    w = 2 * pi * f

    # chuyen zl sang rs noi tiep vs l1
    ql = xl / rl
    l1 = xl / w;

    # chuyen zs sang rp song song voi c1
    qs = -xs / rs
    rp = rs * (1+qs**2)
    c1 = qs / (rp*w)

    rs = rl

    # Kiem tra neu rs < rl thi chay
    if (rs > rp):
        return float('nan'), float('nan'), float('nan')
    else:
        Q = sqrt(rp / rl - 1);

        # tinh cp
        cp = Q/(rp*w)
        # do c // c1
        c = (cp - c1) * 1e12;

        # tinh ls
        ls = (Q * rl) / w
        # do l1 nt l
        l = (ls - l1) * 1e9
        return (Q, l, c, "LCLP")

# CL HIGHPASS OR CL DC BLOCK
def CLHP(data):
    # Giong LCHP nhung thay source bang load
    rs = data[2]
    xs = data[3]
    rl = data[0]
    xl = data[1]
    f = convert_f_unit(data[4],data[8])

    # tinh omega
    w = 2 * pi * f

    # chuyen zl sang rs noi tiep vs c1
    ql = -xl/rl
    c1 = -1/(w*xl) if xl != 0 else float('inf')

    # chuyen zs sang rp song song voi l1
    qs = xs/rs
    l1 = ((1 + qs ** 2) * xs) / ( w * qs ** 2) if qs != 0 else float('inf')

    rp = (1 + qs ** 2) * rs
    rs = rl

    # kiem tra rs < rp thi chay khong thi tra ve non
    if (rs > rp):
        return float('nan'), float('nan'), float('nan')
    else:
        # Tinh Q
        Q = sqrt(rp / rs - 1)

        # Tinh lp
        lp = rp/(w*Q)

        # tinh lc
        cs = 1/(Q*w*rs)

        # kiem tra neu xl = 0 thi tra ve c luon
        if xl == 0:
            c = cs * 1e12
        else:
            if c1 == cs:
                c = float('inf')
            # do c nt c1
            else:
                c = ((c1 * cs) / (c1 - cs)) * 1e12

        # kiem tra neu xs = 0 thi tra ve l luon
        if xs == 0:
            l = lp * 1e9
        else:
            if l1 == lp:
                l = float('inf')
            # do l1 // l
            else:
                l = ((lp * l1) / (l1 - lp)) * 1e9

        clhpcval = c
        clhpqval = abs(Q)
        clhplval = l
        return(clhpqval,clhplval,clhpcval,"CLHP")

def check_input(data):
    # neu rs = rl && xs = xl
    if (data[0] == data[2] and data[1] == -data[3]):
        return False
    else:
        return True

def dc_feed_handler(data):
    if check_input(data):
        result = CLLP(data)
        if not (isnan(result[0]) or isnan(result[1]) or isnan(result[2])):
            return result
        else:
            result = LCLP(data)
            return result
    else:
        return [1,0,0,"L Section"]

def dc_block_handler(data):
    if check_input(data):
        result = CLHP(data)
        if not (isnan(result[0]) or isnan(result[1]) or isnan(result[2])):
            return result
        else:
            result = LCHP(data)
            return result
    else:
        return [1,0,0,"L Section"]


#DC BLOCK = HIGHPASS
#DC FEED = LOWPASS
