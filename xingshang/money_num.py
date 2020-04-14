#! /usr/bin/python
# - coding: utf-8 -*-
"""现有i张10元纸币, j 张5元纸币, k张两元纸币, 购物后要支付n元(n为整数),
要求编写一个时间复杂度为O(1)的函数FindSolution(i, j, k, n), 功能是算出是否能用现在手上拥有的纸币拼凑成n元, 而不需要找零.
如：共有5张10元纸币，5张5元纸币，5张2元纸币，许凑齐27元，需2张10元纸币，1张5元纸币，1张2元纸币
    共有5张10元纸币，5张5元纸币，5张2元纸币，需凑齐100元，无法凑齐
"""


def find_solution(i: int, j: int,  k: int, n: int):
    if n % 2 == 0:    # n是偶数
        ten_page = n // 10
        if ten_page <= i:
            five_page = 0       # 当10元纸币够用时，n为偶数时，5元纸币用不上
            remain_num = n - ten_page % 10
            two_page = remain_num // 2
            if two_page <= k:
                return '共有{0}张10元纸币，{1}张5元纸币，{2}张2元纸币，要凑齐{3}元，' \
                       '需{4}张10元纸币，{5}张5元纸币，{6}张2元纸币'.format(i, j, k, n, ten_page, five_page, two_page)
            else:
                return '共有{0}张10元纸币，{1}张5元纸币，{2}张2元纸币，要凑齐{3}元，无法凑齐'\
                    .format(i, j, k, n)
        else:    # 当10元纸币不够用时，用两张5元凑10元
            remain_num = n - ten_page * 10
            five_page = remain_num // 5
            if five_page <= j:      # 当5元纸币足够时，且组为偶数张
                if five_page % 2 == 0:       # 偶数张5元纸币
                    pass
                else:                       # 基数张5元纸币
                    five_page -= 1

                remain_num_2 = remain_num - 5 * five_page
                two_page = remain_num_2 // 2
                if two_page <= j:
                    return '共有{0}张10元纸币，{1}张5元纸币，{2}张2元纸币，要凑齐{3}元，' \
                           '需{4}张10元纸币，{5}张5元纸币，{6}张2元纸币'.format(i, j, k, n, ten_page, five_page, two_page)
                else:
                    return '共有{0}张10元纸币，{1}张5元纸币，{2}张2元纸币，要凑齐{3}元，无法凑齐'.format(i, j, k, n)
            else:       # 5元纸币不够时
                if five_page % 2 == 0:
                    five_page = j
                else:
                    five_page = j - 1

                remain_num_2 = remain_num - 5 * five_page
                two_page = remain_num_2 // 2
                if two_page <= j:
                    return '共有{0}张10元纸币，{1}张5元纸币，{2}张2元纸币，要凑齐{3}元，' \
                           '需{4}张10元纸币，{5}张5元纸币，{6}张2元纸币'.format(i, j, k, n, ten_page, five_page, two_page)
                else:
                    return '共有{0}张10元纸币，{1}张5元纸币，{2}张2元纸币，要凑齐{3}元，无法凑齐'.format(i, j, k, n)
    else:           # n为基数时
        if j == 0:      # 只有10元纸币和2元纸币凑不到基数
            return '共有{0}张10元纸币，{1}张5元纸币，{2}张2元纸币，要凑齐{3}元，无法凑齐'.format(i, j, k, n)
        elif n in (1, 3):       # 1，3为基数，但是凑不到
            return '共有{0}张10元纸币，{1}张5元纸币，{2}张2元纸币，要凑齐{3}元，无法凑齐'.format(i, j, k, n)
        else:
            ten_page = n // 10
            if ten_page <= i:           # 10元够用
                remain_num = n - ten_page * 10
                if remain_num < 5:
                    ten_page -= 1
                    remain_num = n - ten_page * 10

                five_page = 1
                remain_num_2 = remain_num - 5
                two_page = remain_num_2 // 2
                if two_page <= j:
                    return '共有{0}张10元纸币，{1}张5元纸币，{2}张2元纸币，要凑齐{3}元，' \
                       '需{4}张10元纸币，{5}张5元纸币，{6}张2元纸币'.format(i, j, k, n, ten_page, five_page, two_page)
                else:
                    return '共有{0}张10元纸币，{1}张5元纸币，{2}张2元纸币，要凑齐{3}元，无法凑齐'.format(i, j, k, n)
            else:       # 10元不够用时
                ten_page = i
                remain_num = n - ten_page * 10
                five_page = remain_num // 5
                if five_page <= j:        # 5元够用时且为基数张
                    remain_num_2 = remain_num - five_page * 5
                    if remain_num_2 < 5:
                        five_page -= 1
                        remain_num_2 = remain_num - five_page * 5
                    two_page = remain_num_2 // 2
                    if two_page <= j:
                        return '共有{0}张10元纸币，{1}张5元纸币，{2}张2元纸币，要凑齐{3}元，' \
                               '需{4}张10元纸币，{5}张5元纸币，{6}张2元纸币'.format(i, j, k, n, ten_page, five_page, two_page)
                    else:
                        return '共有{0}张10元纸币，{1}张5元纸币，{2}张2元纸币，要凑齐{3}元，无法凑齐'.format(i, j, k, n)
                else:       # 5元不够用
                    five_page = j
                    if five_page % 2 == 0:      # j必须为基数
                        five_page -= 1
                    remain_num_2 = remain_num - five_page * 5
                    two_page = remain_num_2 // 2
                    if two_page <= j:
                        return '共有{0}张10元纸币，{1}张5元纸币，{2}张2元纸币，要凑齐{3}元，' \
                               '需{4}张10元纸币，{5}张5元纸币，{6}张2元纸币'.format(i, j, k, n, ten_page, five_page, two_page)
                    else:
                        return '共有{0}张10元纸币，{1}张5元纸币，{2}张2元纸币，要凑齐{3}元，无法凑齐'.format(i, j, k, n)


if __name__ == '__main__':
    for i in range(5, 100, 2):
        print(find_solution(3, 10, 10, i))
