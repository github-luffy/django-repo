# coding=gbk
# from django.template.loader import get_template
# from django.template import Context

import csv
import datetime
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
from reportlab.pdfgen import canvas
from cStringIO import StringIO


def hello_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = "attachment;filename=hello.pdf"
    temp = StringIO()   # 使系统的效率最高
    p = canvas.Canvas(temp)
    p.drawString(100, 100, "HelloWorld.")
    p.showPage()
    p.save()
    response.write(temp.getvalue())
    return response


UNRULY_PASSENGERS = [146, 184, 201, 235, 226, 251, 299, 273, 281, 304, 203]  # use for CSV file


def unruly_passengers_csv(request):
    response = HttpResponse(content_type='text/csv')  # content_type is after 1.7 ; tell that file is csv
    # 此句会指示浏览器弹出对话框询问文件存放的位置,并且文明名为unruly.csv
    response['Content-Disposition'] = "attachment; filename=unruly_passengers.csv"
    writer = csv.writer(response)
    writer.writerow(['Year', 'Unruly Airline Passengers'])  # 只写入一行
    for (year, num) in zip(range(1995, 2006), UNRULY_PASSENGERS):
        writer.writerow([year, num])
    return response


def hello(request):
    return HttpResponse("Hello World")


def current_datetime(request):
    now = datetime.datetime.now()
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    return render_to_response('current_datetime.html',
                              {'current_date': now})


def hours_ahead(request, offset):
    try:
        hour_offset = int(offset)
    except ValueError:
        raise Http404("时间差不对")
    update_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
    # t = get_template('hours_ahead.html')
    # html = t.render(Context({'offset': offset, 'update_time': dt}))
    # return HttpResponse(html)
    return render_to_response('hours_ahead.html', locals())


def display_meta(request):
    path_no_domain = request.path
    host_name = request.get_host()
    full_path = request.get_full_path()
    is_secure = request.is_secure()
    key_values = request.META.items()
    key_values.sort()
    return render_to_response('display_meta.html', locals())
