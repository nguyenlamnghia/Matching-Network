# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

# DC FEED: CLC, LLC, CLL
# DC BLOCK: LCL, LCC, CCL

from math import pi, sqrt
from middleware import pi_l_section_convert_to_ui, convert_f_unit

def CLC(rs, xs, rl, xl, Q, f):
    rv = max(rs, rl) / (Q ** 2 + 1)
    w = 2 * pi * f
    # find parallel circuits
    qs = -xs / rs
    ql = -xl / rl
    rps = rs * (1 + qs * qs)
    rpl = rl * (1 + ql * ql)

    # cs-l-cl pi network matching
    cps = qs / rps / w
    cpl = ql / rpl / w

    # start source matching
    print(rps, rv)
    q = sqrt(rps / rv - 1)
    cs = q / w / rps - cps
    cs = cs * 1e12
    # return cs

    ls = (q * rv) / w
    q = sqrt(rpl / rv - 1)
    cl = q / w / rpl - cpl
    cl = cl * 1e12
    #return cl

    ll = (q * rv) / w;
    l = ls + ll
    l = l * 1e9
    #return l

    return [cs, cl, l , "CLC_PI_Section"]

def LCL(rs, xs, rl, xl, Q, f):
    rv = max(rs, rl) / (Q ** 2 + 1)
    w = 2 * pi * f
    # find parallel circuits
    qs = -xs / rs
    ql = -xl / rl
    rps = rs * (1 + qs * qs)
    rpl = rl * (1 + ql * ql)

    # ls-c-ll pi network matching
    q = sqrt(rps / rv - 1)
    ls = rps / w / q
    if (qs != 0):
        lps = rps / qs / w
        ls = (ls * lps) / (ls - lps)
    ls = ls * 1e9
    #return ls

    cs = 1 / w / q / rv
    q = sqrt(rpl / rv - 1)
    ll = rpl / w / q
    if (ql != 0):
        lpl = rpl / ql / w
        ll = (ll * lpl) / (ll - lpl)
    ll = ll * 1e9
    # return ll

    cl = 1 / w / q / rv
    c = (cl * cs) / (cl + cs)
    c = c * 1e12
    # return c

    return [ls, ll, c, "LCL_PI_Section"]


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
        return pi_l_section_convert_to_ui(result)
