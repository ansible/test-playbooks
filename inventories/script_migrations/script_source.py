#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import random
import string


random.seed(29973595994172)


def random_str(non_ascii=True):
    char_list = string.ascii_letters
    if non_ascii:
        char_list += (u"읤僪䠱빨胀콩厺殜赬镗צּ䂕ᆑ䭆蜅펵ꂢ綌靸縹聂傈㟩륯Ȳ北벊렙ぶ逖ϥ谺艣뒉摳")
    return "".join([random.choice(char_list) for _ in range(10)])


inventory = dict()

group_name = "group_%s" % random_str(non_ascii=False)

inventory[group_name] = dict()
inventory[group_name]["hosts"] = list()

for i in range(5):
    inventory[group_name]["hosts"].append("host_%s" % random_str())

inventory[group_name]["vars"] = dict(
    ansible_host="127.0.0.1", ansible_connection="local"
)

print(json.dumps(inventory, ensure_ascii=False))
