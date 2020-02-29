import unittest

from challenge_4.app.challenge_4 import sort_vouchers


class VoucherTests(unittest.TestCase):

    def test_sort_vouchers_function_exists(self):
        voucher_string=\
            "190112:Available:aaaa," \
            "190112:Activated:bbbb," \
            "190111:Available:cccc,"\
            "190110:Redeemed:dddd," \
            "190110:Expired:eeee," \
            "190111:Activated:ffff"
        self.assertTrue(sort_vouchers(voucher_string))

    def test_can_sort_supplied_data(self):
        voucher_string = \
            "190112:Available:aaaa," \
            "190112:Activated:bbbb," \
            "190111:Available:cccc,"\
            "190110:Redeemed:dddd," \
            "190110:Expired:eeee," \
            "190111:Activated:ffff"
        sorted_voucher_string = \
            "190111:Activated:ffff," \
            "190111:Available:cccc,"\
            "190112:Activated:bbbb," \
            "190112:Available:aaaa," \
            "190110:Redeemed:dddd," \
            "190110:Expired:eeee"
        self.assertEqual(sorted_voucher_string, sort_vouchers(voucher_string))

    def test_can_sort_only_avail(self):
        voucher_string = \
            "202003:Available:aaaa," \
            "202004:Activated:bbbb," \
            "202005:Available:cccc,"\
            "202006:Activated:zzzz," \
            "202009:Available:eeee," \
            "190111:Activated:ffff"
        sorted_voucher_string =\
            "190111:Activated:ffff,"\
            "202003:Available:aaaa,"\
            "202004:Activated:bbbb,"\
            "202005:Available:cccc,"\
            "202006:Activated:zzzz,"\
            "202009:Available:eeee"
        self.assertEqual(sorted_voucher_string, sort_vouchers(voucher_string))

    def test_can_sort_vouchers_same_status_and_same_date(self):
        voucher_string = \
            "202003:Redeemed:dddc," \
            "202003:Redeemed:ddda," \
            "202003:Redeemed:dddb," \
            "202003:Expired:cccc," \
            "202003:Expired:cccb," \
            "202003:Expired:ccca," \
            "202003:Available:fffc," \
            "202003:Available:fffb," \
            "202003:Available:fffa," \
            "202003:Activated:gggc," \
            "202003:Activated:ggga," \
            "202003:Activated:gggb"
        sorted_voucher_string =\
            "202003:Activated:ggga,"\
            "202003:Activated:gggb," \
            "202003:Activated:gggc,"\
            "202003:Available:fffa,"\
            "202003:Available:fffb,"\
            "202003:Available:fffc,"\
            "202003:Redeemed:ddda,"\
            "202003:Redeemed:dddb,"\
            "202003:Redeemed:dddc,"\
            "202003:Expired:ccca,"\
            "202003:Expired:cccb,"\
            "202003:Expired:cccc"
        self.assertEqual(sorted_voucher_string, sort_vouchers(voucher_string))

    def test_current_vouchers_returned_in_chronological_order(self):
        voucher_string= \
            "202003:Available:dddc," \
            "202004:Available:ddda," \
            "202005:Available:dddb," \
            "202005:Activated:ccca," \
            "202003:Activated:cccc," \
            "202004:Activated:cccb"
        sorted_voucher_string = \
            "202003:Activated:cccc," \
            "202003:Available:dddc," \
            "202004:Activated:cccb," \
            "202004:Available:ddda," \
            "202005:Activated:ccca," \
            "202005:Available:dddb"
        self.assertEqual(sorted_voucher_string, sort_vouchers(voucher_string))

    def test_non_current_vouchers_returned_in_reverse_chronological_order(self):
        voucher_string= \
            "202003:Redeemed:dddc," \
            "202004:Redeemed:ddda," \
            "202005:Redeemed:dddb," \
            "202003:Expired:cccc," \
            "202004:Expired:cccb," \
            "202005:Expired:ccca"
        sorted_voucher_string =\
            "202005:Redeemed:dddb,"\
            "202005:Expired:ccca," \
            "202004:Redeemed:ddda,"\
            "202004:Expired:cccb,"\
            "202003:Redeemed:dddc,"\
            "202003:Expired:cccc"
        self.assertEqual(sorted_voucher_string, sort_vouchers(voucher_string))

    def test_handles_empty_string(self):
        voucher_string = ""
        with self.assertRaises(RuntimeError):
            sort_vouchers(voucher_string)


if __name__ == '__main__':
    unittest.main()
