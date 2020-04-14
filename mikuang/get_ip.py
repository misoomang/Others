#! /usr/bin/python
# -*- coding:utf-8 -*-

from lxml import etree
import requests
import IPy


def get_ip(url):
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
    html = requests.get(url, headers=headers, verify=False)
    html.encoding = 'ut-8'
    html_text = etree.HTML(html.text)
    address_result = html_text.xpath('//dl[@class="list"]/dt | //dl[@class="list"]/dd/span[@class="v_l"] | //dl[@class="list"]/dd/span[@class="v_r"]')
    result_dict = {}
    city_name = None
    item = []
    for result in address_result:
        if '.' not in result.text:
            result_dict[result.text] = []
            city_name = result.text
        else:
            item.append(result.text)
            if len(item) == 2:
                result_dict[city_name].append(item)
                item = []
    print(result_dict)
    return result_dict


def ip_to_int(ip):
    parts = ip.split('.')[::-1]
    n = 0
    for i, j in enumerate(parts):
        n += 256 ** int(i) * int(j)
    return n


def is_edu_ip(ip: str):
    flag = False
    city_name = None
    url = 'http://ipcn.chacuo.net/view/i_CERNET'
    total_ip = get_ip(url)
    for city_name, ips_list in total_ip.items():
        for item in ips_list:
            if ip_to_int(item[0]) <= ip_to_int(ip) <= ip_to_int(item[1]):
                flag = True
        if flag:
            break
    if flag and city_name:
        print('{0}是教育网ip，属于{1}'.format(ip, city_name))
    else:
        print('{0}不是教育网ip'.format(ip))


if __name__ == '__main__':
    url = 'http://ipcn.chacuo.net/view/i_CERNET'
    is_edu_ip('211.86.0.1')
    # print(ip_to_int('7.91.205.21'))
