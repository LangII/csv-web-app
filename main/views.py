
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



def csvUploadView(_request):

    template = "main/main.html"
    context = {'debug': {}, 'table': []}

    # context['debug']['request method'] = _request.method
    # context['debug']['request files'] = _request.FILES

    if _request.method == 'POST' and 'file' in _request.FILES:

        file_in = _request.FILES['file']

        # Check that 'file_in' is '.csv' before proceeding.  Else return error message.
        context['file_name'] = str(file_in)
        if not context['file_name'].endswith('.csv'):
            context['not_csv'] = 'file uploaded is not a csv'
            return render(_request, template, context)

        package = io.StringIO(file_in.read().decode('ascii'))
        context['table'] = [ i for i in csv.reader(package, delimiter=',') ]

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
