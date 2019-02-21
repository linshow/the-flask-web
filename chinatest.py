import re

def c2n(c_str):
    if c_str == '':
        return u'0'
    stc = u'零一二三四五六七八九'
    dst = u'0123456789'
    for i, c in enumerate(stc):
        c_str = c_str.replace(c,dst[i])
    return c_str

def get_gewei(c_str):
    if u'百零' in c_str:
        return c2n(c_str.split(u'十百零')[1])
    elif u'十' in c_str:
        return c2n(c_str.split(u'十')[1])
    elif u'千零' in c_str:
        return c2n(c_str.split(u'千零')[1])
    else:
        return '0'

def get_shiwei(c_str):
    if u'百零' in c_str:
        return u'0'
    elif u'百' in c_str:
        return c2n(c_str.split(u'百')[0].split(u'十')[0])
    elif u'千零' in c_str and u'十' in c_str:
        return c2n(c_str.split(u'千零')[0].split(u'十')[0])
    elif u'十' in c_str:
        if c_str.split(u'十')[0] == '':
            return u'1'
        return c2n(c_str.split(u'十')[0])
    else:
        return u'0'

def get_complex(c_str):
    gewei = get_gewei(c_str)
    shiwei = get_shiwei(c_str)
    c_str = shiwei+gewei
    return c_str

def check_whether_special(c_str):
    for i in u'十百千':
        if i in c_str:
            return False
    return True

def convert_section(c_str):
    if check_whether_special(c_str):
        return c2n(c_str)
    else:
        return get_complex(c_str)

def convert_all(c_str):
    if check_whether_special(c_str):
        return c2n(c_str)
    result=''
    flag=0
    float_part = ''
    if u'萬' in c_str:
        flag=4
        i = c_str.split(u'萬')[0]
        c_str = c_str.split(u'萬')[1]
        if c_str=='':
            result+='0000'
            return result
    right = get_complex(c_str)
    return result + '0'*(flag-len(get_complex(c_str)))+right+float_part
    



def convertCharacter2Dight(string):
    global sub_str
    chinese_numbers = re.findall(u'[零一二三四五六七八九十百]{1,}', string,re.S)
    sub_str = re.sub(u'[零一二三四五六七八九十百千]{1,}','_',string)
  
    for chinese_number in chinese_numbers:
        digit = convert_all(chinese_number)
        sub_str = sub_str.replace('_',digit,1)
    # print('原句子:',string)
    # print(sub_str)
    return sub_str

# convertCharacter2Dight('臺北市信義區虎林街二二二巷七十九號一樓')
# convertCharacter2Dight('臺北市大安區仁愛路四段２６６巷十五弄十八號１樓')
# convertCharacter2Dight('臺北市中山區北安路六四九號一樓')
# convertCharacter2Dight('臺北市大安區師大路五十九巷十三號一樓')
# print(sub_str)

