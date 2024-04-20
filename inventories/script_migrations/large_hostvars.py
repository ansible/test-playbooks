#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import random
import string


UNICODE_LETTERS = string.ascii_letters + ("읤僪䠱빨胀콩厺殜赬镗צּ䂕ᆑ䭆蜅펵ꂢ綌靸縹聂傈㟩륯Ȳ北벊렙ぶ逖ϥ谺艣뒉摳")


random_str = "".join([random.choice(UNICODE_LETTERS) for _ in range(10)])

inv = {
    "somegroup{0}".format(random_str): dict(
        hosts=["somehost{0}".format(random_str)],
        vars=dict(
            ansible_host="127.0.0.1", ansible_connection="local", cruft="x" * 1024 ** 2
        ),
    )
}

print(json.dumps(inv))
