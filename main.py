import requests
def is_chinese(char):
    if '\u4e00' <= char <= '\u9fff':
        return True
    else:
        return False
def literal_translation(sentence):
    result = ""
    for i in sentence:
        json = {'kw': i}
        url = "https://fanyi.baidu.com/sug"
        data = requests.post(url, data=json, timeout=8)
        content = data.json()
        try:
            data = content['data'][0]['v']
        except:
            continue
        word = ""
        flag = False
        for i in data:
            if i == '[':
                flag = True
            if i == ']':
                flag = False
                continue
            if flag == True:
                continue
            if not 'a' <= i <= 'z' and word != '':
                break
            if 'a' <= i <= 'z':
                word += i
        if result:
            result += ' ' + word
        else:
            result += word
    return result
def translate(word):
    result = ""
    json = {'kw': word}
    url = "https://fanyi.baidu.com/sug"
    data = requests.post(url, data=json, timeout=8)
    content = data.json()
    try:
        data = content['data'][0]['v']
    except:
        return ""
    word = ""
    for i in data:
        if not is_chinese(i) and word != '':
            break
        if is_chinese(i):
            word += i
    if result:
        result += ' ' + word
    else:
        result += word
    return result
if __name__ == "__main__":
    while True:
        sentence = input("请输入要翻译的句子:")
        new_sentence = literal_translation(sentence)
        result = ""
        for i in new_sentence.split(" "):
            result += translate(i)
        print("直译后的英语句:",new_sentence,"\n直译后:",result)