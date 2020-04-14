"""
给一个字符串"123456789",
在任意字符中间插入“+”、“-”、“*”、“/”四种运算符，使最后的计算结果等于50。
例如你可以如此插入：1*2*3*4-56-7+89，使这个式子的最终结果等于50。
输出所有可能的式子结果。
"""


# # 暴力方法
# def make_50(nums: str) -> list:
#     result_list = list()
#     number_str = list(nums)[:-1]
#     operations = ('+', '-', '*', '/', '')
#     all_list = list()
#     for i in number_str:
#         tmp_list = list()
#         for operation in operations:
#             tmp_list.append('{0}{1}'.format(i, operation))
#         all_list.append(tmp_list)
#
#     for a in all_list[0]:
#         for b in all_list[1]:
#             for c in all_list[2]:
#                 for d in all_list[3]:
#                     for e in all_list[4]:
#                         for f in all_list[5]:
#                             for g in all_list[6]:
#                                 for h in all_list[7]:
#                                     calculate = '{0}{1}{2}{3}{4}{5}{6}{7}9'.format(a, b, c, d, e, f, g, h)
#                                     if eval(calculate) == 50:
#                                         result_list.append(calculate)
#     print(result_list)
#     return result_list


# 递归方法
"""
思路：position为插入运算符位置，从前到后插入，插入运算符后
      分为两部分，前半部分带符号，后半部分全是数字，前半部分累积拼接，对后半部分持续加入符号，
      后半部分也分为两部分，带符号部分，全是数字，对全是数字部分持续加入符号...
      以此递归
"""


def make_50(nums: str) -> list:
    result_item = []

    def make(operation, position, remain_num, front_accumulate):
        """
        :param operation: +，-，*，/
        :param position: 添加符号位置
        :param remain_num: 后半纯数字部分，用来递归
        :param front_accumulate: 前半部分累计表达式
        :return:
        """
        remain_num = remain_num.replace(position, position + operation)     # 添加符号，如123456789替换成为1+23456789
        if operation:
            temp = remain_num.split(operation)      # 分为符号部分和纯数字部分，如1， 23456789
            remain_num = temp[1]
            front_accumulate += temp[0] + operation   # 拼接带符号部分，如1+
        if position == '8':     # 到末尾开始执行运算
            calculate = '{0}{1}'.format(front_accumulate, remain_num)
            if eval(calculate) == 50:
                result_item.append(calculate)
            return
        pos = str(int(position) + 1)

        for i in ('+', '-', '*', '/', ''):
            make(i, pos, remain_num, front_accumulate)

    make('', '0', nums, '')
    print(result_item)
    return result_item


# 不要修改下面的部分
if __name__ == "__main__":
    results = make_50("123456789")
    for result in results:
        assert eval(result) == 50
    print("OK")
