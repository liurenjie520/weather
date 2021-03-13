#!/usr/bin/python3
#coding=utf-8
#本项目不建议使用server酱，因为不够直观
import requests, json
import time

spkey = '88806f3e51f72337714104837f800677'          #CoolPush酷推
def get_iciba_everyday():
    icbapi = 'http://open.iciba.com/dsapi/'
    eed = requests.get(icbapi)
    bee = eed.json()               #返回的数据
    english = eed.json()['content']
    zh_CN = eed.json()['note']
    str = '\n【每日一句】\n' + english + '\n' + zh_CN
    return str
print(get_iciba_everyday())

def main():
    api = 'http://t.weather.itboy.net/api/weather/city/'             #API地址，必须配合城市代码使用
    city_code = '101020100'               #进入https://where.heweather.com/index.html查询你的城市代码
    tqurl = api + city_code
    response = requests.get(tqurl)
    d = response.json()         #将数据以json形式返回，这个d就是返回的json数据

    if(d['status'] == 200):     #当返回状态码为200，输出天气状况
        parent = d["cityInfo"]["parent"]  # 省
        city = d["cityInfo"]["city"]  # 市
        update_time = d["time"]  # 更新时间
        date = d["data"]["forecast"][0]["ymd"]  # 日期
        week = d["data"]["forecast"][0]["week"]  # 星期
        weather_type = d["data"]["forecast"][0]["type"]  # 天气
        wendu_high = d["data"]["forecast"][0]["high"]  # 最高温度
        wendu_low = d["data"]["forecast"][0]["low"]  # 最低温度
        shidu = d["data"]["shidu"]  # 湿度
        pm25 = str(d["data"]["pm25"])  # PM2.5
        pm10 = str(d["data"]["pm10"])  # PM10
        quality = d["data"]["quality"]  # 天气质量
        fx = d["data"]["forecast"][0]["fx"]  # 风向
        fl = d["data"]["forecast"][0]["fl"]  # 风力
        ganmao = d["data"]["ganmao"]  # 感冒指数
        tips = d["data"]["forecast"][0]["notice"]  # 温馨提示

        cpurl = 'https://push.xuthus.cc/ww/'+spkey
        #自己改发送方式，我专门创建了个群来收消息，所以我用的group
        tdwt = get_iciba_everyday() + "\n-----------------------------------------" + "\n【今日份天气】\n城市： " + parent + city + \
               "\n日期： " + date + "\n星期: " + week + "\n天气: " + weather_type + "\n温度: " + wendu_high + " / " + wendu_low + "\n湿度: " + \
               shidu + "\nPM25: " + pm25 + "\nPM10: " + pm10 + "\n空气质量: " + quality + \
               "\n风力风向: " + fx + fl + "\n感冒指数: " + ganmao + "\n温馨提示： " + tips + "\n更新时间: " + update_time

        requests.post(cpurl,tdwt.encode('utf-8'))         #把天气数据转换成UTF-8格式，不然要报错。
    else:

        error = '【出现错误】\n　　今日天气推送错误，请检查服务或网络状态！'
        print(error)

def main_handler(event, context):
    return main()

if __name__ == '__main__':
    main()

