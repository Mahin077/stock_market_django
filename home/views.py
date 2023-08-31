from django.shortcuts import render
import json
# Create your views here.
def index(request):
    with open('static/stock_market_data.json') as json_file:
        data = json.load(json_file)
        total = len(data)
    return render(request,'index.html', {'data': data,'total':total})