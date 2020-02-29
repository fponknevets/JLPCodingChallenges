def sort_vouchers(voucher_string):

    END_DATE = 0
    STATUS = 1
    ID = 2

    status_order = {'Activated': 1, 'Available': 2, 'Redeemed': 3, 'Expired': 4}
    active_statuses = ('Activated', 'Available')
    non_active_statuses = ('Redeemed', 'Expired')

    def _resolve_key(key_value):
        if key_value in status_order:
            return status_order.get(key_value)
        else:
            return key_value

    def _sort_list_by_keys(vouchers, keys):
        for key, rev in keys:
            vouchers.sort(key=lambda voucher: _resolve_key(voucher[key]), reverse=rev)

    def _is_active(voucher):
        return voucher[STATUS] in active_statuses

    def _is_non_active(voucher):
        return voucher[STATUS] in non_active_statuses

    def _get_vouchers(voucher_string):
        if voucher_string in ('', None):
            raise RuntimeError('Empty or none existent voucher string.')
        vouchers = []
        vouchers_data=voucher_string.split(',')
        for voucher_data in vouchers_data:
            voucher=voucher_data.split(':')
            vouchers.append(voucher)
        return vouchers

    def _build_return_string(voucher_list):
        vouchers = []
        for voucher in voucher_list:
            current_voucher_string = ':'.join(voucher)
            vouchers.append(current_voucher_string)
        return ','.join(vouchers)


    try:
        vouchers = _get_vouchers(voucher_string)
    except RuntimeError as err:
        print("Runtime error: {}".format(err))
        raise

    active_vouchers = list(filter(_is_active, vouchers))
    non_active_vouchers = list(filter(_is_non_active, vouchers))

    _sort_list_by_keys(active_vouchers, ((ID, False), (STATUS, False), (END_DATE, False)))
    _sort_list_by_keys(non_active_vouchers, ((ID, False), (STATUS, False), (END_DATE, True)))

    return _build_return_string(active_vouchers + non_active_vouchers)
