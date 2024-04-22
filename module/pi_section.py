# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

# DC FEED: CLC, LLC, CLL
# DC BLOCK: LCL, LCC, CCL

from math import pi, sqrt
from middleware import pi_l_section_convert_to_ui, convert_f_unit

def CLC(rs, xs, rl, xl, Q, f):

    # tim r virtual
    rv = max(rs, rl) / (Q ** 2 + 1)
    w = 2 * pi * f

    # chuyen zl sang rpl song song voi cpl
    # chuyen zs sang rps song song voi cps
    qs = -xs / rs
    ql = -xl / rl

    rps = rs * (1 + qs * qs)
    rpl = rl * (1 + ql * ql)
    cps = qs / rps / w
    cpl = ql / rpl / w

    # tinh c1, l1 tu q1
    q = sqrt(rps / rv - 1)
    c1 = q / w / rps - cps
    c1 = c1 * 1e12
    # return c1
    l1 = (q * rv) / w

    # tinh c2, l2 tu q2
    q = sqrt(rpl / rv - 1)
    c2 = q / w / rpl - cpl
    c2 = c2 * 1e12
    #return c2
    l2 = (q * rv) / w
    l = l1 + l2
    l = l * 1e9
    #return l

    return [c1, l, c2 , "CLC_PI_Section"]


def LCL(rs, xs, rl, xl, Q, f):
    # tim r virtual
    rv = max(rs, rl) / (Q ** 2 + 1)
    w = 2 * pi * f


    # chuyen zl sang rpl song song voi lpl
    # chuyen zs sang rps song song voi lps
    qs = -xs / rs
    ql = -xl / rl
    rps = rs * (1 + qs * qs)
    rpl = rl * (1 + ql * ql)

    # tinh l1, c1 tu q1
    q = sqrt(rps / rv - 1)
    l1 = rps / w / q
    if (qs != 0):
        lps = rps / qs / w
        l1 = (l1 * lps) / (l1 - lps)
    l1 = l1 * 1e9
    #return l1
    c1 = 1 / w / q / rv

    # tinh l1, c2 tu q2
    q = sqrt(rpl / rv - 1)
    l2 = rpl / w / q
    if (ql != 0):
        lpl = rpl / ql / w
        l2 = (l2 * lpl) / (l2 - lpl)
    l2 = l2 * 1e9
    # return l2
    c2 = 1 / w / q / rv

    c = (c2 * c1) / (c1 + c2)
    c = c * 1e12
    # return c

    return [l1, c, l2, "LCL_PI_Section"]

def LCLC(rs, xs, rl, xl, Q, f):
    # tim r virtual
    rv = max(rs, rl) / (Q ** 2 + 1)
    w = 2 * pi * f

    # chuyen zl sang rpl song song voi cpl
    # chuyen zs sang rps song song voi lps

    qs = -xs / rs
    ql = -xl / rl
    rps = rs * (1 + qs * qs)
    rpl = rl * (1 + ql * ql)
    cpl = qs / rpl / w

    # tinh c1, l1 tu q1
    q = sqrt(rps / rv - 1)
    l1 = rps / w / q
    if (qs != 0):
        lps = rps / qs / w
        l1 = (l1 * lps) / (l1 - lps)
    l1 = l1 * 1e9
    #return l1
    # tinh zc1
    zc1 = q * rv

    # tinh c2, l2 tu q2
    q = sqrt(rpl / rv - 1)
    c2 = q / w / rpl - cpl
    c2 = c2 * 1e12
    #return c2
    # tinh zl2
    zl2 = q * rv
    
    # so sanh zl2 va zc1 de xac dinh la C hay L
    if (zl2 > zc1):
        l = (zl2 - zc1) / w
        l = l * 1e9
        return [l1, l , c2, "LLC_PI_Section"]
    if (zl2 < zc1):
        c = 1 / (zc1 - zl2) / w
        c = c * 1e12
        return [l1, c, c2, "LCC_PI_Section"]
    else:
        pass

def CLCL(rs, xs, rl, xl, Q, f):
    # tim r virtual
    rv = max(rs, rl) / (Q ** 2 + 1)
    w = 2 * pi * f

    # chuyen zl sang rpl song song voi lpl
    # chuyen zs sang rps song song voi cps

    qs = -xs / rs
    ql = -xl / rl

    rps = rs * (1 + qs * qs)
    rpl = rl * (1 + ql * ql)

    # lpl = rpl / ql / w
    cps = qs / rps / w

    # tinh l1, c1 tu q1
    q = sqrt(rps / rv - 1)
    c1 = q / w / rps - cps
    c1 = c1 * 1e12
    # return c1
    # tinh zl1
    zl1 = q * rv

    # tinh l2, c2 tu q2
    q = sqrt(rpl / rv - 1)
    l2 = rpl / w / q
    if (ql != 0):
        lpl = rpl / ql / w
        l2 = (l2 * lpl) / (l2 - lpl)
    l2 = l2 * 1e9
    # return l2
    # tinh zc2
    zc2 = q * rv

    # so sanh zc2 va zl1 de xac dinh la C hay L
    if (zc2 < zl1):
        l = (zl1 - zc2) / w
        l = l * 1e9
        return [c1, l, l2, "CLL_PI_Section"]
    if (zc2 > zl1):
        c = 1 / (zc2 - zl1) / w
        c = c * 1e12
        return [c1, c, l2, "CCL_PI_Section"]
    else:
        pass

def dc_block_handler(data):
    rs = data[0]
    xs = data[1]
    rl = data[2]
    xl = data[3]
    Q = data[5]
    f = convert_f_unit(data[4],data[8])
    # Check input
    if (Q < 0):
        return []
    elif (Q == 0 and rs == rl):
        return [[0,0,0,"LCL"], [0,0,0,"LCC"], [0,0,0,"CCL"]]
    elif (Q < sqrt(max(rs, rl) / min(rs, rl) - 1)):
        return []
    else:
        result = []
        result.append(LCL(rs, xs, rl, xl, Q, f))
        clcl_result = CLCL(rs, xs, rl, xl, Q, f)
        lclc_result = LCLC(rs, xs, rl, xl, Q, f)
        if clcl_result[3] == "CCL_PI_Section":
            result.append(clcl_result)
        if lclc_result[3] == "LCC_PI_Section":
            result.append(lclc_result)
        return pi_l_section_convert_to_ui(result)

def dc_feed_handler(data):
    rs = data[0]
    xs = data[1]
    rl = data[2]
    xl = data[3]
    Q = data[5]
    f = convert_f_unit(data[4],data[8])
    # Check input
    if (Q < 0):
        return []
    elif (Q == 0 and rs == rl):
        return [[0,0,0,"LCL"], [0,0,0,"LCC"], [0,0,0,"CCL"]]
    elif (Q < sqrt(max(rs, rl) / min(rs, rl) - 1)):
        return []
    else:
        result = []
        result.append(CLC(rs, xs, rl, xl, Q, f))
        clcl_result = CLCL(rs, xs, rl, xl, Q, f)
        lclc_result = LCLC(rs, xs, rl, xl, Q, f)
        if clcl_result[3] == "CLL_PI_Section":
            result.append(clcl_result)
        if lclc_result[3] == "LLC_PI_Section":
            result.append(lclc_result)
        return pi_l_section_convert_to_ui(result)
