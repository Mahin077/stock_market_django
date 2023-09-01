from django.shortcuts import render,HttpResponseRedirect
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
from home.models import StockMarket
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# homepage (2 charts and table of the data)
def index(request):
    #to generate the first line and bar chart taking trade_code, date, close, volume columns
    stMarketFirstChart = StockMarket.objects.values('trade_code', 'date', 'close', 'volume').order_by('date')
    dfFirstChart = pd.DataFrame.from_records(stMarketFirstChart)

    #to add all the unique values of trade_code in the dropdown of index
    tradeCode = StockMarket.objects.values_list('trade_code',flat=True).distinct()
    #creating the first chart(line and bar)
    fig = create_chart(dfFirstChart, dfFirstChart['trade_code'].iloc[0])
    #creating the second chart(candlestick)
    fig2 = second_chart()

    #all the data of stock market
    data = StockMarket.objects.all()
    #total data of stock market
    total=StockMarket.objects.all().count()

    context = {
        'chart': fig.to_html(),
        'chart2': fig2,
        'trade_codes':tradeCode,
        'data': data,
        'total':total,
    }
    return render(request,'index.html', context)


#open the item in a new html file that need to be edit
def update(request,id):
    #searching the particular id for editing
    stMarket = StockMarket.objects.get(id=id)
    context={
        'stMarket' : stMarket,
    }
    return render(request,'update.html',context)


#edit the item in database
def updateRecord(request,id):
    if request.method == "POST":
        date = request.POST['date']
        trade_code = request.POST['trade_code']
        high = request.POST['high']
        low = request.POST['low']
        open = request.POST['open']
        close = request.POST['close']
        volume = request.POST['volume']
        stMarket = StockMarket.objects.get(id=id)
        stMarket.date = date
        stMarket.trade_code=trade_code
        stMarket.high=float(high.replace(',',''))
        stMarket.low=float(low.replace(',',''))
        stMarket.open=float(open.replace(',',''))
        stMarket.close=float(close.replace(',',''))
        stMarket.volume=int(volume.replace(',',''))
        stMarket.save()
        messages.success(request,"The data has been updated")
    return HttpResponseRedirect(reverse('index'))


#after selecting a trade_code from the dropdown this function run to re-render the graph of close and volume(first chart)
def update_chart(request):
    selected_trade_code = request.GET.get('trade_code')

    stMarket = StockMarket.objects.values('trade_code', 'date', 'close', 'volume').order_by('date')
    df = pd.DataFrame.from_records(stMarket)
    
    updated_chart1 = create_chart(df, selected_trade_code)
    chart_html1 = updated_chart1.to_html()

    context = {
        'chart_html1': chart_html1,
    }

    return JsonResponse(context)

#generate the first chart
def create_chart(df, selected_trade_code):
    # filter data by selected_trade_code
    filtered_df = df[df['trade_code'] == selected_trade_code]

    # create a line chart for close
    line_chart = px.line(filtered_df, x='date', y='close', title='Close')

    # create a bar chart for volume
    bar_chart = px.bar(filtered_df, x='date', y='volume', title='Volume')

    # combine the line and bar charts into a multi-axis chart
    fig = go.Figure()

    # add the line chart on the left y-axis
    fig.add_trace(go.Scatter(x=line_chart.data[0]['x'], y=line_chart.data[0]['y'], mode='lines+markers', name='Close', yaxis='y1'))

    # add the bar chart on the right y-axis
    fig.add_trace(go.Bar(x=bar_chart.data[0]['x'], y=bar_chart.data[0]['y'], name='Volume', yaxis='y2'))

    fig.update_layout(
        xaxis=dict(title='Date'),
        yaxis=dict(title='Close', side='left', showgrid=False),
        yaxis2=dict(title='Volume', overlaying='y', side='right', showgrid=False),
        title='multi axis chart of close and volume | First Chart',
    )

    return fig


#generate the second chart(candlestick)
def second_chart():
    #taking date,open,high,low,close only
    data = StockMarket.objects.values('date', 'open', 'high','low','close')
    df = pd.DataFrame.from_records(data)

    # create a candlestick chart
    fig = go.Figure(data=[go.Candlestick(
                    x=df['date'],
                    open=df['open'],
                    high=df['high'],
                    low=df['low'],
                    close=df['close']
    )])

    fig.update_layout(
        title='Candlestick Chart | 2nd Chart',
        xaxis_title='Date',
        yaxis_title='Price',
    )

    return pio.to_html(fig,full_html=False)