else:
            if dd == 31 or dd == 30:
                dd =  1
            else:
                dd += 1
            if mm == 12:
                mm = 1
                yy += 1
            else:
                mm += 1

            print("{0}/{1}/{3}".format(dd,mm,yy))