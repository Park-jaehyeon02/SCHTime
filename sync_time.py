#-*- coding: utf-8 -*-
import urllib.request
def sync_time(url_num=0):
    month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06',
        'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

    url = ['http://www.google.com', 'http://www.naver.com']
    date = urllib.request.urlopen(url[url_num]).headers['Date'][5:-4]
    d, m, y, hour, min, sec = date[:2], month[date[3:6]], date[7:11], date[12:14], date[15:17], date[18:]
    time_list = [d,date[3:6],y,hour,min,sec,month[date[3:6]],url[url_num]]
    return time_list

if __name__ =='__main__':
    time_list = sync_time(0)
    print(f'[{time_list[-1]}]의 서버시간\n{time_list[0]}년 {time_list[6]}월 {time_list[2]}일 {time_list[3]}시 {time_list[4]}분 {time_list[5]}초')
