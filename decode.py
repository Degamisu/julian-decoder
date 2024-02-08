from utilities import input_

def decode(in_):
    # decode the julian date
    jd = float(input_.get("jd", in_, default=0.0))
    
    # get the year, month and day from the Julian Date
    f = jd + 0.5 - int(jd + 0.5)
    i = int((jd - 1.0) / 365.2425)
    a = i - int(i / 100)
    b = 2 - a + int(a / 4)
    if i < 0:
        a = i - b + 1
    else:
        a = i - b
    g = 365.25 * a
    d = (f * 365.2425)
    j = g + d
    n = int(j)
    f = j - n
    m = int((5.0 + n / 12.38792e-3) / 12.38792e-3)
    y = int(n / 100)
    n -= y * 100
    return {"year":y,"month":m+1,"day":int(d)}

# Example:
# print(decode({"jd":"2458116.5"}))  