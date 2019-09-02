from django.shortcuts import render
import json
from TestModel.models import Test
from HelloWorld.common.response import json_response
# Create your views here.

def index(request):
    context = {}
    if request.POST:
        data = request.POST['data']
        test = Test(name=json.dumps(data), id=2)
        test.save()
        return json_response('保存成功！')
    else:
        data = Test.objects.get(id=2).name
    context['data'] = data
    return render(request, 'index.html', context)