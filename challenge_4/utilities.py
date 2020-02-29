from pprint import pprint as pp

voucher_string=\
    "202003:Available:dddc,"\
    "202004:Available:ddda,"\
    "202005:Available:dddb,"\
    "202005:Activated:ccca,"\
    "202003:Activated:cccc,"\
    "202004:Activated:cccb"


def listify(vouchers_string):
    vouchers = []
    voucher_strings = vouchers_string.split(',')
    for voucher_string in voucher_strings:
        voucher = voucher_string.split(':')
        vouchers.append(voucher)
    return vouchers


if __name__ == "__main__":
    pp(listify(voucher_string))