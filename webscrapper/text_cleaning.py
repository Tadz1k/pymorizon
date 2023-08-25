import re

def get_page_numbers(bs4_arr):
    bs4_str = ''.join(str(e) for e in bs4_arr)
    bs4_str = bs4_str.replace('\n', '').replace(' ', '')
    numbers = re.findall(r'>(\d+)<', bs4_str)
    numbers = [int(i) for i in numbers]
    if len(numbers) == 0:
        return 1
    return max(numbers)
