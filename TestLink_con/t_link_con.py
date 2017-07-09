# -*- coding: utf-8 -*-

import xml_model
import get_values

print('请输入开始的用例ID,后续用例将自动顺序生成')
t_id = input()
t_Values = get_values.t_Values()
values = t_Values.get_values(t_id)
for k, v in values.items():
    print(k, v)

T_link = xml_model.Tlink()
# name_input=, importance_input=,actions_input=,expectedresults_input=
model = T_link.model
T_link.initial()
for k, v in values.items():
    done = model.format(t_id=t_id, name_input=v[0], importance_input=v[1], actions_input=v[2],
                        expectedresults_input=v[3])
    done = bytes(done, encoding="utf8")
    T_link.to_file(done)
T_link.fin()
