function HP1() {
  rs = parseFloat(document.circuit.rs.value);

  xs = parseFloat(document.circuit.xs.value);

  rl = parseFloat(document.circuit.rl.value);

  xl = parseFloat(document.circuit.xl.value);

  Q = parseFloat(document.circuit.q.value);

  f = parseFloat(document.circuit.f.value);

  with (Math) {
    w = 2 * PI * f;

    q = xs / rs;

    rp = (1 + q * q) * rs;

    rv = sqrt(rp * rl);

    if (rp > rv) {
      qs = sqrt(rp / rv - 1);

      ql = sqrt(rv / rl - 1);

      lp = rp / w / q;

      c = 1 / w / rv / qs;

      document.circuit.hp1cs.value = c * 1e12;

      l = rp / w / qs;

      if (xs != 0) {
        if (lp == l) {
          l = Number.POSITIVE_INFINITY;
        } else {
          l = (1 * lp) / (lp - l);
        }
      }

      document.circuit.hp1ls.value = l * 1e9;

      cs = -1 / w / xl;

      l = rv / w / ql;

      document.circuit.hp1ll.value = l * 1e9;

      c = 1 / w / rl / ql;

      if (xl != 0) {
        if (cs == c) {
          c = Number.POSITIVE_INFINITY;
        } else {
          c = (c * cs) / (cs - c);
        }
      }

      document.circuit.hp1cl.value = c * 1e12;
    } else {
      document.circuit.hp1cs.value = Number.NaN;

      document.circuit.hp1ls.value = Number.NaN;

      document.circuit.hp1cl.value = Number.NaN;

      document.circuit.hp1ll.value = Number.NaN;
    }
  }
}

function HP2() {
  rl = parseFloat(document.circuit.rs.value);

  xl = parseFloat(document.circuit.xs.value);

  rs = parseFloat(document.circuit.rl.value);

  xs = parseFloat(document.circuit.xl.value);

  Q = parseFloat(document.circuit.q.value);

  f = parseFloat(document.circuit.f.value);

  with (Math) {
    w = 2 * PI * f;

    q = xs / rs;

    rp = (1 + q * q) * rs;

    rv = sqrt(rp * rl);

    if (rp > rv) {
      qs = sqrt(rp / rv - 1);

      ql = sqrt(rv / rl - 1);

      lp = rp / w / q;

      c = 1 / w / rv / qs;

      document.circuit.hp2cs.value = c * 1e12;

      l = rp / w / qs;

      if (xs != 0) {
        if (lp == l) {
          l = Number.POSITIVE_INFINITY;
        } else {
          l = (1 * lp) / (lp - l);
        }
      }

      document.circuit.hp2ls.value = l * 1e9;

      cs = -1 / w / xl;

      l = rv / w / ql;

      document.circuit.hp2ll.value = l * 1e9;

      c = 1 / w / rl / ql;

      if (xl != 0) {
        if (cs == c) {
          c = Number.POSITIVE_INFINITY;
        } else {
          c = (c * cs) / (cs - c);
        }
      }

      document.circuit.hp2cl.value = c * 1e12;
    } else {
      document.circuit.hp2cs.value = Number.NaN;

      document.circuit.hp2ls.value = Number.NaN;

      document.circuit.hp2cl.value = Number.NaN;

      document.circuit.hp2ll.value = Number.NaN;
    }
  }
}

function LP1() {
  rs = parseFloat(document.circuit.rs.value);

  xs = parseFloat(document.circuit.xs.value);

  rl = parseFloat(document.circuit.rl.value);

  xl = parseFloat(document.circuit.xl.value);

  Q = parseFloat(document.circuit.q.value);

  f = parseFloat(document.circuit.f.value);

  with (Math) {
    w = 2 * PI * f;

    q = -xs / rs;

    rp = (1 + q * q) * rs;

    rv = sqrt(rp * rl);

    if (rp > rv) {
      qs = sqrt(rp / rv - 1);

      ql = sqrt(rv / rl - 1);

      cp = q / w / rp;

      c = qs / w / rp - cp;

      document.circuit.lp1cs.value = c * 1e12;

      l = (qs * rv) / w;

      document.circuit.lp1ls.value = l * 1e9;

      l = (rl * ql) / w - xl / w;

      document.circuit.lp1ll.value = l * 1e9;

      c = ql / w / rv;

      document.circuit.lp1cl.value = c * 1e12;
    } else {
      document.circuit.lp1cs.value = Number.NaN;

      document.circuit.lp1ls.value = Number.NaN;

      document.circuit.lp1cl.value = Number.NaN;

      document.circuit.lp1ll.value = Number.NaN;
    }
  }
}

function LP2() {
  rl = parseFloat(document.circuit.rs.value);

  xl = parseFloat(document.circuit.xs.value);

  rs = parseFloat(document.circuit.rl.value);

  xs = parseFloat(document.circuit.xl.value);

  Q = parseFloat(document.circuit.q.value);

  f = parseFloat(document.circuit.f.value);

  with (Math) {
    w = 2 * PI * f;

    q = -xs / rs;

    rp = (1 + q * q) * rs;

    rv = sqrt(rp * rl);

    if (rp > rv) {
      qs = sqrt(rp / rv - 1);

      ql = sqrt(rv / rl - 1);

      cp = q / w / rp;

      c = qs / w / rp - cp;

      document.circuit.lp2cs.value = c * 1e12;

      l = (qs * rv) / w;

      document.circuit.lp2ls.value = l * 1e9;

      l = (rl * ql) / w - xl / w;

      document.circuit.lp2ll.value = l * 1e9;

      c = ql / w / rv;

      document.circuit.lp2cl.value = c * 1e12;
    } else {
      document.circuit.lp2cs.value = Number.NaN;

      document.circuit.lp2ls.value = Number.NaN;

      document.circuit.lp2cl.value = Number.NaN;

      document.circuit.lp2ll.value = Number.NaN;
    }
  }
}

function BP1() {
  rs = parseFloat(document.circuit.rs.value);

  xs = parseFloat(document.circuit.xs.value);

  rl = parseFloat(document.circuit.rl.value);

  xl = parseFloat(document.circuit.xl.value);

  Q = parseFloat(document.circuit.q.value);

  f = parseFloat(document.circuit.f.value);

  with (Math) {
    w = 2 * PI * f;

    q = xs / rs;

    rp = (1 + q * q) * rs;

    rv = sqrt(rp * rl);

    if (rp > rv) {
      qs = sqrt(rp / rv - 1);

      ql = sqrt(rv / rl - 1);

      lp = rp / w / q;

      c = 1 / w / rv / qs;

      document.circuit.bp1cs.value = c * 1e12;

      l = rp / w / qs;

      if (xs != 0) {
        if (lp == l) {
          l = Number.POSITIVE_INFINITY;
        } else {
          l = (1 * lp) / (lp - l);
        }
      }

      document.circuit.bp1ls.value = l * 1e9;

      l = (ql * rl) / w - xl / w;

      document.circuit.bp1ll.value = l * 1e9;

      c = ql / w / rv;

      document.circuit.bp1cl.value = c * 1e12;
    } else {
      document.circuit.bp1cs.value = Number.NaN;

      document.circuit.bp1ls.value = Number.NaN;

      document.circuit.bp1cl.value = Number.NaN;

      document.circuit.bp1ll.value = Number.NaN;
    }
  }
}

function BP2() {
  rl = parseFloat(document.circuit.rs.value);

  xl = parseFloat(document.circuit.xs.value);

  rs = parseFloat(document.circuit.rl.value);

  xs = parseFloat(document.circuit.xl.value);

  Q = parseFloat(document.circuit.q.value);

  f = parseFloat(document.circuit.f.value);

  with (Math) {
    w = 2 * PI * f;

    q = xs / rs;

    rp = (1 + q * q) * rs;

    rv = sqrt(rp * rl);

    if (rp > rv) {
      qs = sqrt(rp / rv - 1);

      ql = sqrt(rv / rl - 1);

      lp = rp / w / q;

      c = 1 / w / rv / qs;

      document.circuit.bp2cs.value = c * 1e12;

      l = rp / w / qs;

      if (xs != 0) {
        if (lp == l) {
          l = Number.POSITIVE_INFINITY;
        } else {
          l = (1 * lp) / (lp - l);
        }
      }

      document.circuit.bp2ls.value = l * 1e9;

      l = (ql * rl) / w - xl / w;

      document.circuit.bp2ll.value = l * 1e9;

      c = ql / w / rv;

      document.circuit.bp2cl.value = c * 1e12;
    } else {
      document.circuit.bp2cs.value = Number.NaN;

      document.circuit.bp2ls.value = Number.NaN;

      document.circuit.bp2cl.value = Number.NaN;

      document.circuit.bp2ll.value = Number.NaN;
    }
  }
}

function BP3() {
  rs = parseFloat(document.circuit.rs.value);

  xs = parseFloat(document.circuit.xs.value);

  rl = parseFloat(document.circuit.rl.value);

  xl = parseFloat(document.circuit.xl.value);

  Q = parseFloat(document.circuit.q.value);

  f = parseFloat(document.circuit.f.value);

  with (Math) {
    w = 2 * PI * f;

    q = -xs / rs;

    rp = (1 + q * q) * rs;

    rv = sqrt(rp * rl);

    if (rp > rv) {
      qs = sqrt(rp / rv - 1);

      ql = sqrt(rv / rl - 1);

      cp = q / w / rp;

      c = qs / w / rp - cp;

      document.circuit.bp3cs.value = c * 1e12;

      l = (qs * rv) / w;

      document.circuit.bp3ls.value = l * 1e9;

      l = rv / w / ql;

      document.circuit.bp3ll.value = l * 1e9;

      cs = -1 / w / xl;

      c = 1 / w / rl / ql;

      if (xl != 0) {
        if (cs == c) {
          c = Number.POSITIVE_INFINITY;
        } else {
          c = (c * cs) / (cs - c);
        }
      }

      document.circuit.bp3cl.value = c * 1e12;
    } else {
      document.circuit.bp3cs.value = Number.NaN;

      document.circuit.bp3ls.value = Number.NaN;

      document.circuit.bp3cl.value = Number.NaN;

      document.circuit.bp3ll.value = Number.NaN;
    }
  }
}

function BP4() {
  rl = parseFloat(document.circuit.rs.value);

  xl = parseFloat(document.circuit.xs.value);

  rs = parseFloat(document.circuit.rl.value);

  xs = parseFloat(document.circuit.xl.value);

  Q = parseFloat(document.circuit.q.value);

  f = parseFloat(document.circuit.f.value);

  with (Math) {
    w = 2 * PI * f;

    q = -xs / rs;

    rp = (1 + q * q) * rs;

    rv = sqrt(rp * rl);

    if (rp > rv) {
      qs = sqrt(rp / rv - 1);

      ql = sqrt(rv / rl - 1);

      cp = q / w / rp;

      c = qs / w / rp - cp;

      document.circuit.bp4cs.value = c * 1e12;

      l = (qs * rv) / w;

      document.circuit.bp4ls.value = l * 1e9;

      l = rv / w / ql;

      document.circuit.bp4ll.value = l * 1e9;

      cs = -1 / w / xl;

      c = 1 / w / rl / ql;

      if (xl != 0) {
        if (cs == c) {
          c = Number.POSITIVE_INFINITY;
        } else {
          c = (c * cs) / (cs - c);
        }
      }

      document.circuit.bp4cl.value = c * 1e12;
    } else {
      document.circuit.bp4cs.value = Number.NaN;

      document.circuit.bp4ls.value = Number.NaN;

      document.circuit.bp4cl.value = Number.NaN;

      document.circuit.bp4ll.value = Number.NaN;
    }
  }
}

function Pi() {
  rs = parseFloat(document.circuit.rs.value);

  xs = parseFloat(document.circuit.xs.value);

  rl = parseFloat(document.circuit.rl.value);

  xl = parseFloat(document.circuit.xl.value);

  Q = parseFloat(document.circuit.q.value);

  f = parseFloat(document.circuit.f.value);

  with (Math) {
    if (Q < 0) {
      document.circuit.cspi.value = Number.NaN;

      document.circuit.clpi.value = Number.NaN;

      document.circuit.lpi.value = Number.NaN;

      document.circuit.lspi.value = Number.NaN;

      document.circuit.llpi.value = Number.NaN;

      document.circuit.cpi.value = Number.NaN;
    } else {
      if (Q == 0 && rs == rl) {
        document.circuit.cspi.value = 0;

        document.circuit.clpi.value = 0;

        document.circuit.lpi.value = 0;

        document.circuit.lspi.value = 0;

        document.circuit.llpi.value = 0;

        document.circuit.cpi.value = 0;
      } else {
        if (Q < sqrt(max(rs, rl) / min(rs, rl) - 1)) {
          document.circuit.cspi.value = Number.NaN;

          document.circuit.clpi.value = Number.NaN;

          document.circuit.lpi.value = Number.NaN;

          document.circuit.lspi.value = Number.NaN;

          document.circuit.llpi.value = Number.NaN;

          document.circuit.cpi.value = Number.NaN;
        } else {
          rv = max(rs, rl) / (Q * Q + 1);

          //document.circuit.rvpi.value=rv

          w = 2 * PI * f;

          qs = -xs / rs; //find parallel circuits

          ql = -xl / rl;

          rps = rs * (1 + qs * qs);

          rpl = rl * (1 + ql * ql);

          //cs-l-cl pi network matching

          cps = qs / rps / w;

          cpl = ql / rpl / w;

          q = sqrt(rps / rv - 1); //start source matching

          cs = q / w / rps - cps;

          document.circuit.cspi.value = cs * 1e12;

          ls = (q * rv) / w;

          q = sqrt(rpl / rv - 1); //start load matching

          cl = q / w / rpl - cpl;

          document.circuit.clpi.value = cl * 1e12;

          ll = (q * rv) / w;

          l = ls + ll;

          document.circuit.lpi.value = l * 1e9;

          //ls-c-ll pi network matching

          q = sqrt(rps / rv - 1); //start source matching

          ls = rps / w / q;

          if (qs != 0) {
            lps = rps / qs / w;

            ls = (ls * lps) / (ls - lps);
          }

          document.circuit.lspi.value = ls * 1e9;

          cs = 1 / w / q / rv;

          q = sqrt(rpl / rv - 1); //start load matching

          ll = rpl / w / q;

          if (ql != 0) {
            lpl = rpl / ql / w;

            ll = (ll * lpl) / (ll - lpl);
          }

          document.circuit.llpi.value = ll * 1e9;

          cl = 1 / w / q / rv;

          c = (cl * cs) / (cl + cs);

          document.circuit.cpi.value = c * 1e12;
        }
      }
    }
  }
}

function Tnet() {
  rs = parseFloat(document.circuit.rs.value);

  xs = parseFloat(document.circuit.xs.value);

  rl = parseFloat(document.circuit.rl.value);

  xl = parseFloat(document.circuit.xl.value);

  Q = parseFloat(document.circuit.q.value);

  f = parseFloat(document.circuit.f.value);

  with (Math) {
    if (Q < 0) {
      document.circuit.cst.value = Number.NaN;

      document.circuit.clt.value = Number.NaN;

      document.circuit.lt.value = Number.NaN;

      document.circuit.lst.value = Number.NaN;

      document.circuit.llt.value = Number.NaN;

      document.circuit.ct.value = Number.NaN;
    } else {
      if (Q == 0 && rs == rl) {
        document.circuit.cst.value = 0;

        document.circuit.clt.value = 0;

        document.circuit.lt.value = 0;

        document.circuit.lst.value = 0;

        document.circuit.llt.value = 0;

        document.circuit.ct.value = 0;
      } else {
        if (Q < sqrt(max(rs, rl) / min(rs, rl) - 1)) {
          document.circuit.cst.value = Number.NaN;

          document.circuit.clt.value = Number.NaN;

          document.circuit.lt.value = Number.NaN;

          document.circuit.lst.value = Number.NaN;

          document.circuit.llt.value = Number.NaN;

          document.circuit.ct.value = Number.NaN;
        } else {
          rv = min(rs, rl) * (Q * Q + 1);

          //document.circuit.rvt.value=rv

          w = 2 * PI * f;

          //cs-l-cl t network matching

          q = sqrt(rv / rs - 1); //start source matching

          cs = 1 / w / rs / q;

          if (xs != 0) {
            if (cs == -1 / w / xs) {
              cs = Number.POSITIVE_INFINITY;
            } else {
              cs = (cs * (-1 / w / xs)) / (cs + 1 / w / xs);
            }
          }

          document.circuit.cst.value = cs * 1e12;

          ls = rv / w / q;

          q = sqrt(rv / rl - 1); //start load matching

          cl = 1 / w / rl / q;

          if (xl != 0) {
            if (cl == -1 / w / xs) {
              cl = Number.POSITIVE_INFINITY;
            } else {
              cl = (cl * (-1 / w / xs)) / (cl + 1 / w / xs);
            }
          }

          document.circuit.clt.value = cl * 1e12;

          ll = rv / w / q;

          l = (ll * ls) / (ll + ls);

          document.circuit.lt.value = l * 1e9;

          //ls-c-ll t network matching

          q = sqrt(rv / rs - 1); //start source matching

          ls = (q * rs) / w - xs / w;

          document.circuit.lst.value = ls * 1e9;

          cs = q / w / rv;

          q = sqrt(rv / rl - 1); //start load matching

          ll = (q * rl) / w - xl / w;

          document.circuit.llt.value = ll * 1e9;

          cl = q / w / rv;

          c = cs + cl;

          document.circuit.ct.value = c * 1e12;
        }
      }
    }
  }
}

function LCLP() {
  // This is the same as CLLP except the source and load are swapped

  rs = parseFloat(document.circuit.rl.value);

  xs = parseFloat(document.circuit.xl.value);

  rl = parseFloat(document.circuit.rs.value);

  xl = parseFloat(document.circuit.xs.value);

  f = parseFloat(document.circuit.f.value);

  w = 2 * Math.PI * f;

  qs = -xs / rs;

  ql = xl / rl;

  rp = rs * (1 + qs * qs);

  c1 = qs / rp / w;

  l1 = xl / w;

  if (rl > rp) {
    document.circuit.lclpcval.value = Number.NaN;

    document.circuit.lclpqval.value = Number.NaN;

    document.circuit.lclplval.value = Number.NaN;
  } else {
    Q = Math.sqrt(rp / rl - 1);

    cp = Q / rp / w;

    c = (cp - c1) * 1e12;

    ls = (Q * rl) / w;

    l = (ls - l1) * 1e9;

    document.circuit.lclpcval.value = c;

    document.circuit.lclpqval.value = Math.abs(Q);

    document.circuit.lclplval.value = l;
  }
}

function CLLP() {
  // This is a comment

  rs = parseFloat(document.circuit.rs.value);

  xs = parseFloat(document.circuit.xs.value);

  rl = parseFloat(document.circuit.rl.value);

  xl = parseFloat(document.circuit.xl.value);

  f = parseFloat(document.circuit.f.value);

  w = 2 * Math.PI * f;

  qs = -xs / rs;

  ql = xl / rl;

  rp = rs * (1 + qs * qs);

  c1 = qs / rp / w;

  l1 = xl / w;

  if (rl > rp) {
    //alert("Load Resistance is larger than source resistance. Cannot use C para, L series");

    document.circuit.cllpcval.value = Number.NaN;

    document.circuit.cllpqval.value = Number.NaN;

    document.circuit.cllplval.value = Number.NaN;
  } else {
    Q = Math.sqrt(rp / rl - 1);

    cp = Q / rp / w;

    c = (cp - c1) * 1e12;

    ls = (Q * rl) / w;

    l = (ls - l1) * 1e9;

    document.circuit.cllpcval.value = c;

    document.circuit.cllpqval.value = Math.abs(Q);

    document.circuit.cllplval.value = l;
  }
}

function LCHP() {
  rs = parseFloat(document.circuit.rs.value);

  xs = parseFloat(document.circuit.xs.value);

  rl = parseFloat(document.circuit.rl.value);

  xl = parseFloat(document.circuit.xl.value);

  f = parseFloat(document.circuit.f.value);

  w = 2 * Math.PI * f;

  ql = -xl / rl;

  qs = xs / rs;

  c1 = -1 / w / xl;

  l1 = ((1 + qs * qs) * xs) / w / qs / qs;

  rp = (1 + qs * qs) * rs;

  rs = rl;

  if (rs > rp) {
    //alert("Load resistance is larger than source resistance. Cannot use LC match")

    document.circuit.lchpcval.value = Number.NaN;

    document.circuit.lchpqval.value = Number.NaN;

    document.circuit.lchplval.value = Number.NaN;
  } else {
    Q = Math.sqrt(rp / rs - 1);

    lp = rp / w / Q;

    cs = 1 / Q / w / rs;

    if (xl == 0) {
      c = cs * 1e12;
    } else {
      if (c1 == cs) {
        c = Number.POSITIVE_INFINITY;
      } else {
        c = ((c1 * cs) / (c1 - cs)) * 1e12;
      }
    }

    if (xs == 0) {
      l = lp * 1e9;
    } else {
      if (l1 == lp) {
        l = Number.POSITIVE_INFINITY;
      } else {
        l = ((lp * l1) / (l1 - lp)) * 1e9;
      }
    }

    document.circuit.lchpcval.value = c;

    document.circuit.lchpqval.value = Math.abs(Q);

    document.circuit.lchplval.value = l;
  }
}

function CLHP() {
  rs = parseFloat(document.circuit.rl.value);

  xs = parseFloat(document.circuit.xl.value);

  rl = parseFloat(document.circuit.rs.value);

  xl = parseFloat(document.circuit.xs.value);

  f = parseFloat(document.circuit.f.value);

  w = 2 * Math.PI * f;

  ql = -xl / rl;

  qs = xs / rs;

  c1 = -1 / w / xl;

  l1 = ((1 + qs * qs) * xs) / w / qs / qs;

  rp = (1 + qs * qs) * rs;

  rs = rl;

  if (rs > rp) {
    //alert("Load resistance is larger than source resistance. Cannot use LC match")

    document.circuit.clhpcval.value = Number.NaN;

    document.circuit.clhpqval.value = Number.NaN;

    document.circuit.clhplval.value = Number.NaN;
  } else {
    Q = Math.sqrt(rp / rs - 1);

    lp = rp / w / Q;

    cs = 1 / Q / w / rs;

    if (xl == 0) {
      c = cs * 1e12;
    } else {
      if (c1 == cs) {
        c = Number.POSITIVE_INFINITY;
      } else {
        c = ((c1 * cs) / (c1 - cs)) * 1e12;
      }
    }

    if (xs == 0) {
      l = lp * 1e9;
    } else {
      if (l1 == lp) {
        l = Number.POSITIVE_INFINITY;
      } else {
        l = ((lp * l1) / (l1 - lp)) * 1e9;
      }
    }

    document.circuit.clhpcval.value = c;

    document.circuit.clhpqval.value = Math.abs(Q);

    document.circuit.clhplval.value = l;
  }
}

function setCircuit() {
  var rs = parseFloat(document.circuit.rs.value);

  var xs = parseFloat(document.circuit.xs.value);

  var rl = parseFloat(document.circuit.rl.value);

  var xl = parseFloat(document.circuit.xl.value);

  Tnet();

  Pi();

  LP1();

  LP2();

  HP1();

  HP2();

  BP1();

  BP2();

  BP3();

  BP4();

  if ((rs == rl) & (xs == -xl)) {
    document.circuit.lchpcval.value = 0;

    document.circuit.lchpqval.value = xs / rs;

    document.circuit.lchplval.value = 0;

    document.circuit.cllpcval.value = 0;

    document.circuit.cllpqval.value = xs / rs;

    document.circuit.cllplval.value = 0;

    document.circuit.lclpcval.value = 0;

    document.circuit.lclpqval.value = xs / rs;

    document.circuit.lclplval.value = 0;

    document.circuit.clhpcval.value = 0;

    document.circuit.clhpqval.value = xs / rs;

    document.circuit.clhplval.value = 0;
  } else {
    LCHP();

    CLLP();

    LCLP();

    CLHP();
  }
}
