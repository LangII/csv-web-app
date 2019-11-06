
import io
import csv
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import permission_required

from django.shortcuts import render
from django.views.generic import ListView
from .models import tblPackageShipments



def mainView(_request):

    ps_data = tblPackageShipments.objects.all()[:5]
    args = {'data': ps_data}

    return render(_request, 'main/main.html', args)



class MainListView(ListView):

    model = tblPackageShipments
    template_name = 'main/main.html'
    context_object_name = 'data'
    ordering = ['companyid']

    # queryset = tblPackageShipments.objects.all()[:10]
    date_range = ['2019-08-01', '2019-08-02']
    queryset = tblPackageShipments.objects.filter(requesteddatetime__range=date_range)



# @permission_required('admin.can_add_log_entry')
def csvUploadView(_request):
    template = "main/main.html"
    context = {'debug': {}, 'table': []}

    context['debug']['request method'] = _request.method
    context['debug']['request files'] = _request.FILES

    # if _request.method == 'GET':  return render(_request, template, context)

    if _request.method == 'POST' and 'file' in _request.FILES:

        file_in = _request.FILES['file']
        # context['debug']['request files contents'] = package

        # package = file_in.read().decode('ascii')
        # context['debug']['data pack type'] = str(type(package))
        # context['debug']['data pack'] = package

        package = io.StringIO(file_in.read().decode('ascii'))

        table = [ i for i in csv.reader(package, delimiter=',') ]
        # for col in csv.reader(package, delimiter=','):
        #     table.append(col)
        context['debug']['table'] = table
        context['table'] = table

        # if not container.name.endswith('.csv'):  messages.error(_request, 'this is not a csv file')

        # data_set = package.read().decode('ascii')
        # io_string = io.StringIO(data_set)
        # next(io_string)
        # for col in csv.reader(io_string, delimiter=','):
        #     _, created = tblPackageShipments.objects.update_or_create(
        #         companyid=col[0],
        #         requesteddatetime=datetime.now(),
        #         attention=col[1],
        #         freightcost=col[2],
        #         fulfillmentcost=col[3]
        #     )

    return render(_request, template, context)
