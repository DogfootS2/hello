from django.http.response import HttpResponse
from django.shortcuts import render

from os import name
import urllib.request
month = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', \
    'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

def getServertime():
    url = 'http://www.president.go.kr'
    date = urllib.request.urlopen(url).headers['Date'][5:-4]
    d, m, y, hour, min, sec = date[:2], month[date[3:6]], date[7:11], date[12:14], date[15:17], date[18:]
    return (url, y, m, d, hour, min, sec)

# Create your views here.
def index(request):
    # return render(request, 'main/time.html')
    time = getServertime()
    return HttpResponse(f'{time[0]}의 서버시간\n{time[1]}년 {time[2]}월 {time[3]}일 {time[4]}시 {time[5]}분 {time[6]}초')