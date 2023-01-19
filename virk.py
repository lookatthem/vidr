def func1(arg1, arg2):
    var57 = func2(arg2, arg1)
    var58 = 1845293322 & 401
    var59 = arg1 ^ arg2
    var60 = ((var59 ^ arg1) | var59) ^ arg1
    var61 = ((213 | arg2) - var59) ^ arg2
    var62 = (var57 & var57) ^ var58 | var57
    var63 = var58 | 763829537 + var58
    var64 = (var63 & var57 + var62) & var59
    var65 = (var57 ^ var60 - var63) + var59
    var66 = ((var60 ^ arg2) - 1477707065) ^ var58
    var67 = var60 - var63
    if var61 < var63:
        var68 = var65 - var60 | var60 + 974722561
    else:
        var68 = (var59 + var65) + var62 & arg2
    if var60 < arg1:
        var69 = var67 | var58
    else:
        var69 = var67 - var59 ^ 45
    var70 = var60 | var60
    var71 = (arg2 + (var63 & var58)) + var62
    var72 = var66 - var67 + var57 - var62
    result = arg1 + 946697916 | var63
    return result
def func2(arg3, arg4):
    var5 = 0
    for var56 in [(-4 | arg4) | arg3 for i in func3(arg4, -1)]:
        if arg4 < arg3:
            var5 += (var5 & var56) + var5
        else:
            var5 += var5 | arg3
    return var5
def func4(arg8, arg9):
    var41 = func5(arg9, arg8)
    if arg9 < arg8:
        var42 = ((184 ^ (-254 & arg8 + var41 & (2082144381 + arg9 | (908310052 ^ (var41 | 97450081))) - ((508200691 & (((var41 + arg9) | arg9 | arg9) & -1436357683)) ^ arg9)) ^ arg9 & 133 - -1651365767) | 856 - 1086423016) | -632
    else:
        var42 = (arg9 - arg8 & 630 ^ 1957902512 - ((950 - (arg8 - arg9 & (476307630 - -807 + arg9)) + (arg8 & arg9 - 1638295391 ^ arg8 - var41)) - arg8 | arg8 | -722 | arg8 | -592) ^ -978) - -382
    var43 = 156805409 ^ var41 | arg8
    var44 = arg8 | arg8
    result = var41 | var44 - arg9
    return result
def func7(arg12, arg13):
    if arg12 < arg12:
        var18 = class8()
    else:
        var18 = class10()
    for var19 in range(45):
        var20 = var18.func9
        var20(arg12, var19)
    var21 = (-567 - -729080987 - arg12) & arg13
    var22 = var21 | (260 ^ 312) & arg13
    var23 = ((290 | 1334929601) - arg12) | var22
    var24 = (var22 | var23 + arg13) | 149
    var25 = arg12 ^ 340
    var26 = (var23 + var23) - arg13 + var25
    var27 = -264960823 & var25 - 931 + var21
    var28 = (arg12 | -216 ^ -616) + 823
    var29 = var25 | var26
    var30 = var26 + var25 ^ -2124578094 - 735
    var31 = 1916752612 - arg13 + var29 + var25
    var32 = var28 | arg13
    var33 = ((arg13 + arg12) + var30) ^ var28
    var34 = arg12 + arg12 ^ var27 | arg12
    if var28 < arg12:
        var35 = var26 - var22
    else:
        var35 = var22 - var30 | var21 + var32
    var36 = ((arg12 & var34) + var30) - var21
    var37 = (arg12 | var27) | var34 - var36
    var38 = var25 - var34
    var39 = var26 + 709 ^ var29 - var26
    result = var34 + ((var32 & var37 + var32) - arg12)
    return result
class class10(object):
    def func9(self, arg16, arg17):
        return 0
class class8(object):
    def func9(self, arg14, arg15):
        result = 666117287 & 1 + (((arg15 - arg15) | arg14) - arg14) - 0
        return result
def func3(arg6, arg7):
    var45 = func4(189924079, -107)
    yield var45
    var46 = arg6 - arg6 + arg6 - arg7
    yield var46
    var47 = (-611 + arg7) + arg7 & var46
    yield var47
    var48 = arg6 + arg7
    yield var48
    var49 = var48 ^ arg6
    yield var49
    var50 = var49 & var49
    yield var50
    var51 = ((var47 ^ var49) | var50) + -881
    yield var51
    var52 = 1907322133 - var51
    yield var52
    var53 = var47 & (531490367 + var49)
    yield var53
    var54 = 919 ^ var48 ^ arg7
    yield var54
    var55 = var47 ^ ((447555241 - var49) ^ var50)
    yield var55
def func5(arg10, arg11):
    def func6(acc, rest):
        var40 = func7(acc, -2)
        if acc == 0:
            return var40
        else:
            result = func6(acc - 1, var40)
            return result
    result = func6(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 12'
    print 'arg_number: 73'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
