from django.http import HttpResponse

from TestModel.models import Test

# 数据库操作
def testdb(request):
    test1 = Test(name = 'runoob')
    test1.save()
    return HttpResponse("<p>添加数据成功! </p>")

# 获取数据
def gettest(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects这个模型管理器all()获取所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id = 1)

    # 获取单个对象
    response3 = Test.objects.get(id = 1)

    # 限制返回的数据相当于SQL中的OFFSET 0 LIMIT 2
    Test.objects.order_by('name')[0:2]

    # 上面的方法可以连锁使用
    Test.objects.filter(name = 'runoob').order_by('id')