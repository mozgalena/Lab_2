import re
import requests


def get_address(new_addr, uniq):
    value = [
             q
             for i in range(len(new_addr))
             for text in requests.get(new_addr[i]).text.split(' ')
             for q in re.findall('href="/index.php.+"', text)
            ]

    value = {
             'http://www.toipkro.ru/' + value[i][7:len(value[i]) - 1] + '/'
             for i in range(len(value))
            }

    new_addr = [x for x in value if x not in uniq]
    for x in value:
        if x not in uniq:
            uniq.append(x)
            print(x)
    print(len(new_addr))

    if len(new_addr) > 97:
        get_address(new_addr, uniq)
    else:
        put = open("all_addresses.txt", "w", encoding='utf-8')
        put.write('\n'.join(uniq))
        put.close()
        mail_address(uniq)


def mail_address(c):
    value = {
             q
             for gr_1 in range(len(c))
             for text in requests.get(c[gr_1]).text.split(' ')
             for q in re.findall('[\w.][\w.]+@\w+\.\w+', text)
            }
    v = open("mail_address.txt", "w", encoding='utf-8')
    v.write('\n'.join(value))
    v.close()



get_address(new_addr=['http://www.toipkro.ru'], uniq=['http://www.toipkro.ru/'])