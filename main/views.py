
import io
import csv
import ast
from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, HttpResponse
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

    # context['debug']['request'] = _request
    # context['debug']['request type'] = str(type(_request))
    context['debug']['request method'] = _request.method
    # context['debug']['request files'] = _request.FILES

    if _request.method == 'POST':

        if 'template_download' in _request.POST:

            cdc_headers = [
                'CompanyName', 'FirstName', 'LastName', 'Address1', 'Address2', 'City', 'State',
                'Zip', 'Country', 'Phone', 'Fax', 'Email', 'ShippingMethod', 'ShippingAccount',
                'ShippingNotes', 'Notes', 'PartNumber1', 'Quantity1', 'PartNumber2', 'Quantity2',
                'PartNumber3', 'Quantity3', 'PartNumber4', 'Quantity4', 'PartNumber5', 'Quantity5'
            ]

            response_ = HttpResponse(content_type='text/csv')
            response_['Content-Disposition'] = 'attachment; filename="cdc_format.csv"'
            writer = csv.writer(response_, delimiter=',')
            writer.writerow(cdc_headers)

            return response_

        if 'csv_upload' in _request.FILES:

            # Check that 'csv_upload' is '.csv' before proceeding.  Else return error message.
            context['file_name'] = str(_request.FILES['csv_upload'])
            if not context['file_name'].endswith('.csv'):
                context['not_csv'] = 'file uploaded is not a csv'
                return render(_request, template, context)

            # Use 'io.StringIO' and 'csv.reader' to store contents of 'file' as list-of-lists.
            package = io.StringIO(_request.FILES['csv_upload'].read().decode('ascii'))
            context['table'] = [ i for i in csv.reader(package, delimiter=',') ]

            context['debug']['table'] = context['table']

        if 'submitting' in _request.POST:

            # Convert string to list-of-lists.
            submitting = ast.literal_eval(_request.POST.get('submitting'))
            # Slice 'submitting' to avoid headers.
            for line in submitting[1:]:
                _, submission = tblPackageShipments.objects.update_or_create(
                    companyid=line[0],
                    requesteddatetime=datetime.now(),
                    attention=line[1],
                    freightcost=line[2],
                    fulfillmentcost=line[3]
                )

    # context['debug']['context'] = context

    return render(_request, template, context)
