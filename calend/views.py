from django.shortcuts import render, redirect
from datetime import datetime


def events(request):
    mn = datetime.now().month
    yr = datetime.now().year
    return render(request, '{0}-cal/{1}-{2}.html'.format(str(yr), str(mn), str(yr)), context=None)


def nxt(request):
    mn = datetime.now().month
    year = datetime.now().year
    next_month = mn + 1
    print(next_month)
    print('{0}-cal/{1}-{2}'.format(str(year), str(next_month), str(year)))
    return render(request, '{0}-cal/{1}-{2}.html'.format(str(year), str(next_month), str(year)), context=None)


def prev(request):
    mn = datetime.now().month
    year = datetime.now().year
    prev_month = mn - 1
    print(prev_month)
    if prev_month == 0:
        prev_month = 12
        year-= 1
    return render(request, '{0}-cal/{1}-{2}.html'.format(str(year), str(prev_month), str(year)), context=None)


def detail(request):
    return render(request, '2016-cal/events.html', context=None)