# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

from middleware import convert_f_unit, pi_l_section_convert_to_ui
from math import pi, sqrt

def CLC(rs, xs, rl, xl, Q, f):
    rv = min(rs, rl) * (Q * Q + 1)
    w = 2 * pi * f

    #cs-l-cl t network matching
    q = sqrt(rv / rs - 1) #start source matching
    cs = 1 / w / rs / q
    if (xs != 0):
        if (cs == -1 / w / xs):
            cs = float('inf')
        else:
            cs = (cs * (-1 / w / xs)) / (cs + 1 / w / xs)
    cs = cs * 1e12
    # return cs

    ls = rv / w / q
    q = sqrt(rv / rl - 1) #start load matching
    cl = 1 / w / rl / q
    if (xl != 0) :
        if (cl == -1 / w / xs) :
          cl = float('inf')
        else :
          cl = (cl * (-1 / w / xs)) / (cl + 1 / w / xs)
    cl = cl * 1e12
    #return cl

    ll = rv / w / q
    l = (ll * ls) / (ll + ls)
    l = l * 1e9
    #return l

    return [cs,l,cl,"CLC_T_Section"]

def LCL(rs, xs, rl, xl, Q, f):
    rv = min(rs, rl) * (Q * Q + 1)
    w = 2 * pi * f

    # ls-c-ll t network matching
    q = sqrt(rv / rs - 1) #start source matching
    ls = (q * rs) / w - xs / w
    ls = ls * 1e9
    # return ls

    cs = q / w / rv
    q = sqrt(rv / rl - 1) #start load matching
    ll = (q * rl) / w - xl / w
    ll = ll * 1e9
    # return ll

    cl = q / w / rv
    c = cs + cl
    c = c * 1e12
    # return c

    return [ls,c,ll,"LCL_T_Section"]


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
        result.append(CLC(rs, xs, rl, xl, Q, f))
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
        result.append(LCL(rs, xs, rl, xl, Q, f))
        return pi_l_section_convert_to_ui(result)
