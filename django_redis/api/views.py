from django.shortcuts import render

from django.conf import settings
import redis
import datetime

current_date = datetime.datetime.now()

# Connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)

today18pm = current_date.replace(hour=18, minute=0, second=0, microsecond=0)
if current_date < today18pm:
    current_date = datetime.datetime.today() - datetime.timedelta(days=1)
else:
    current_date = datetime.datetime.now()

# Create your views here.

def manage_items(request, *args, **kwargs):
    if request.method == 'GET':
        
        items1 = {}
        count = 0
        for key in redis_instance.keys("*"):
            print("key",key)
            items1[key.decode("utf-8")] = redis_instance.hmget(key,['code','open','high','low','close'])
            count += 1
        response_data = {
           
            'items1': items1
        }
        
        
        return render(request,'index.html',{'getdata':items1,'currentdate':current_date})
    elif request.method == 'POST':
        name = request.POST.get('search_name')
        data = redis_instance.hmget(name,['code','open','high','low','close'])
        response_data = {
            'name': name,
            'code': data[0].decode("utf-8"),
            'open': data[1].decode("utf-8"),
            'high': data[2].decode("utf-8"),
            'low': data[3].decode("utf-8"),
            'close': data[4].decode("utf-8"),
        }
        print(response_data)
        return render(request,'index.html', {'data':response_data,'currentdate':current_date})



