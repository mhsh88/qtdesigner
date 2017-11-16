from numpy import unicode

arabic_indic_trans = dict(
    zip((ord(s) for s in u'0123456789'),
        u'\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667\u0668\u0669')
)

for s in u'0123456789', u'33342353', u'88192838743':
    print('{!r} -> {!r}'.format(s, s.translate(arabic_indic_trans)))

for s in 1234567890, 33342353, 88192838743876487602873545683470:
    s = unicode(s)  # Python 2 (s = str(s) for Python 3)
    print('{!r} -> {!r}'.format(s, s.translate(arabic_indic_trans)))


def enToArNumb(number):
    dic = {
        '۰': '0',
        '۱': '1',
        '۲': '2',
        '۳': '3',
        '۴': '4',
        '۵': '5',
        '۶': '6',
        '۷': '7',
        '۸': '8',
        '۹': '9',
        '٫': '.',
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '.': '.',
    }
    temp = [dic.get(num) for num in number]
    return ''.join(temp)


print(enToArNumb('۱۲۳۴۵۶۶،،،،،'))
