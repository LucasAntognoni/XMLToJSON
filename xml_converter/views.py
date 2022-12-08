from django.http import JsonResponse
from django.shortcuts import render

from xml_converter.converter import convert
from xml_converter.forms import UploadForm


def upload_page(request):

    if request.method == 'POST':

        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            xml_string = request.FILES['file'].read().decode('utf-8')
            result = convert(xml_string)
            return JsonResponse(result)

        else:
            return render(request, 'upload_page.html', {'form': form})

    else:
        form = UploadForm()
        return render(request, 'upload_page.html', {'form': form})
