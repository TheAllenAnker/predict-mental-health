import json
import re
import pyexcel

sheet = pyexcel.get_sheet(file_name="user_ids.xlsx")
id_str = json.dumps(sheet.to_array())
id_list = re.compile('"(.*?)"').findall(id_str)
id_str = ""
for user_id in id_list:
    if not user_id:
        break
    id_str += '\"' + user_id + '\"' + ','

print(id_str[0:-1])

