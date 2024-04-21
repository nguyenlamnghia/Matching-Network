# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

from middleware import convert_f_unit, pi_l_section_convert_to_ui
from math import pi, sqrt

def CLC(rs, xs, rl, xl, Q, f):
    # tim r virtual
    rv = min(rs, rl) * (Q * Q + 1)
    w = 2 * pi * f

    # chuyen zl sang rl noi tiep voi cpl
    # chuyen zs sang rs noi tiep voi cps
    cpl = -1 / w / xl
    cps = -1 / w / xs

    # tinh c1, l1 tu q1
    q = sqrt(rv / rs - 1) #start source matching
    c1 = 1 / w / rs / q
    if (xs != 0):
        if (c1 == cps):
            c1 = float('inf')
        else:
            c1 = (c1 * cps) / (c1 - cps)
    c1 = c1 * 1e12
    # return c1
    l1 = rv / w / q

    # tinh c2, l2 tu q2
    q = sqrt(rv / rl - 1) #start load matching
    c2 = 1 / w / rl / q
    if (xl != 0) :
        if (c2 == cpl) :
            c2 = float('inf')
        else :
          cl = (c2 * cpl) / (c2 - cpl)
    c2 = c2 * 1e12
    # return c2
    l2 = rv / w / q

    l = (l2 * l1) / (l2 + l1)
    l = l * 1e9
    #return l

    return [c1,l,c2,"CLC_T_Section"]

def LCL(rs, xs, rl, xl, Q, f):
    # tim r virtual
    rv = min(rs, rl) * (Q * Q + 1)
    w = 2 * pi * f

    # chuyen zl sang rl noi tiep voi lpl
    # chuyen zs sang rs noi tiep voi lps
    lpl = xl / w
    lps = xs / w

    # tinh l1, c1 tu q1
    q = sqrt(rv / rs - 1) #start source matching
    l1 = (q * rs) / w - lps
    l1 = l1 * 1e9
    # return l1
    c1 = q / w / rv

    # tinh l2, c2 tu q2
    q = sqrt(rv / rl - 1) #start load matching
    l2 = (q * rl) / w - lpl
    l2 = l2 * 1e9
    # return l2
    c2 = q / w / rv

    c = c1 + c2
    c = c * 1e12
    # return c

    return [l1,c,l2,"LCL_T_Section"]

def LCLC(rs, xs, rl, xl, Q, f):
    # tim r virtual
    rv = min(rs, rl) / (Q * Q + 1)
    w = 2 * pi * f

    # chuyen zl sang rl noi tiep voi cpl
    # chuyen zs sang rs noi tiep voi lps
    ql = xl / rl
    qs = xs / rs
    cpl = -1 / w / xl
    lps = xs / w

    # tinh c1, l1 tu q1
    q = sqrt(rv / rs - 1) #start source matching
    l1 = (q * rs) / w - lps
    l1 = l1 * 1e9
    # return l1
    zc1 = rv / q
    # c1 = q / w / rv

    # tinh c2, l2 tu q2
    q = sqrt(rv / rl - 1) #start load matching
    c2 = 1 / w / rl / q
    if (xl != 0) :
        if (c2 == cpl) :
            c2 = float('inf')
        else :
          cl = (c2 * cpl) / (c2 - cpl)
    c2 = c2 * 1e12
    # return c2
    zl2 = rv / q
    # l2 = rv / w / q

    # so sanh zl2 va zc1 de chon l hay c
    z_temp = (zl2 * (-zc1)) / (zl2 - zc1)
    if (z_temp > 0):
        l = z_temp / w
        l = l * 1e9
        return [l1,l,c2,"LLC_T_Section"]
    elif (z_temp < 0):
        c = 1 / w / z_temp
        c = c * 1e12
        return [l1,c,c2,"LCC_T_Section"]

def CLCL(rs, xs, rl, xl, Q, f):
    # tim r virtual
    rv = max(rs, rl) / (Q * Q + 1)
    w = 2 * pi * f

    # chuyen zl sang rl noi tiep voi lpl
    # chuyen zs sang rs noi tiep voi cps
    ql = xl / rl
    qs = xs / rs
    lpl = xl / w
    cps = -1 / w / xs

    # tinh c1, l1 tu q1
    q = sqrt(rv / rs - 1) #start source matching
    c1 = 1 / w / rs / q
    if (xs != 0):
        if (c1 == cps):
            c1 = float('inf')
        else:
            c1 = (c1 * cps) / (c1 - cps)
    c1 = c1 * 1e12
    # return c1
    zl1 = rv / q

    # tinh l2, c2 tu q2
    q = sqrt(rv / rl - 1) #start load matching
    l2 = (q * rl) / w - lpl
    l2 = l2 * 1e9
    # return l2
    zc2 = rv / q

    
    # so sanh zl1 va zc2 de chon l hay c
    z_temp = (zl1 * (-zc2)) / (zl1 - zc2)
    if (z_temp > 0):
        l = z_temp / w
        l = l * 1e9
        return [c1,l,l2,"CLL_T_Section"]
    elif (z_temp < 0):
        c = 1 / w / z_temp
        c = c * 1e12
        return [c1,c,l2,"CCL_T_Section"]




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
        result.append(LCLC(rs, xs, rl, xl, Q, f))
        result.append(CLCL(rs, xs, rl, xl, Q, f))
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
