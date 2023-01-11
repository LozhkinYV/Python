str1 = '5*x^3 + 57*x^2 + 3*x - 4 = 0'
str2 = '5*x^2 + x = 0'

str3 = str1[:str1.find('=')] + ' + ' + str2[:str2.find(' =')]
str3 = str3.replace('+ -', '- ')
str3 = str3.replace(' - ', ' -')
str3 = str3.replace('+', '')
str3_list = str3.split()

unique = list(set(str3_list))
out_dict = {}
potential = 0

for item in unique:
    k = len([i for i in range(0, len(str3_list)) if str3_list[i]==item])
    if item[0] == '-':
        potential = -1
        item = item[1:]
    else:
        potential = 1
    if '*' in item:
        k2 = item[:item.find('*')]
        item = item[item.find('*') + 1:]
    else:
        k2 = 1
    if item in out_dict.keys():
        out_dict[item] += k * int(k2) * potential
    else:
        out_dict[item] = k * int(k2) * potential

out_str = ''
for key in list(out_dict.keys()):
    out_str += str(out_dict[key]) + '*' + key + ' + '
out_str = out_str[:-3]
out_str = out_str.replace('1*', '')
out_str = out_str.replace(' + -', ' - ')

print(out_str)