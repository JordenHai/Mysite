from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.
# 建议两个都用
# 类的方式 和 函数

def index(request):
    return render(request,'index.html')
    pass

def userInfo(request):
    if request.method == 'GET':
        user_list = models.UserInfo.objects.all()
        print(user_list.query)
        return render(request,'userInfo.html',{'user_list':user_list})
    if request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('passwd')
        models.UserInfo.objects.create(username=u,password=p)
        return redirect('/app01/user_info/')
    pass

def groupInfo(request):

    return render(request,'groupInfo.html')
    pass

def userDetail(request,nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    # models.UserInfo.objects.get(id=nid)
    return render(request,'userDetail.html',{'obj':obj})
    pass

def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    if request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get("passwd")
        obj = models.UserInfo.objects.filter(username=u,password=p).first()
        if obj:
            return redirect('/app01/index/')
        else:
            return render(request,'login.html')
    else:
        return redirect('/index/')

def loadfile(request):
    if request.method == 'GET':
        return  render(request,'dump.html')
    if request.method == 'POST':
        file = request.FILES.get('files')

        import os
        file_path = os.path.join('upload',file.name)
        f = open(file_path,mode='wb')
        for i in file.chunks():
            f.write(i)
        f.close()

    return render(request,'dump.html')

#数据库操作

def orm(request):
    #增加数据
    # models.UserInfo.objects.create(
    #     username='root',
    #     password='123',
    # )

    # obj = models.UserInfo(username='root',password='123456')
    # obj.save()

    # dic = {'username':'alex','password':666}
    # models.UserInfo.objects.create(**dic)

    #查询
    # data = models.UserInfo.objects.all()
    # print(data)
    # #data,QuerySet=>Djongo=>[]
    # #[obj,obj,obj]
    # for row in data:
    #     print(row.id,row.username,row.password)
    # # 模板语言循环就好了
    # res = models.UserInfo.objects.filter(username='root',password='123')
    # for row in res:
    #     print(row.id,row.username,row.password)

    #删除
    #models.UserInfo.objects.all().delete()
    #models.UserInfo.objects.filter(id=4).delete()

    #更新
    # models.UserInfo.objects.all().update(password=666)
    return HttpResponse('SDASD')



from django.views import View
# cbv方式
# 反射
class Home(View):
    # 调用父类的方法 进行get 或 post或者其他的操作
    def dispatch(self, request, *args, **kwargs):
        # 调用父类中的dispatch方法
        print('before')
        res = super(Home,self).dispatch(request,*args,**kwargs)
        print('after')
        return res

    def get(self,request):
        print(request.method)
        return render(request,'home.html')
        pass

    def post(self,request):
        print(request.method)
        return render(request,'home.html')
        pass