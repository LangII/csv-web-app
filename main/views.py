
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



# dummy = [
#     {
#         'this': 'whatsagiga',
#         'that': {
#             'huh': 'farfignooget',
#             'really': 'criminal',
#             'ok': 'BAM'
#         }
#     },
#     {
#         'this': 'craptastic',
#         'that': {
#             'huh': 'sciencefictionation',
#             'really': 'fakeblood',
#             'ok': 'HOOYA'
#         }
#     },
# ]

# args = {'data': dummy}
