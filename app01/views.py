from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
# 建议两个都用
# 类的方式 和 函数
# USER_DICT = {
#     '1': {'name' : 'root', 'email' : 'root@live.com'},
#     '2': {'name' : 'root', 'email' : 'root@live.com'},
#     '3': {'name' : 'root', 'email' : 'root@live.com'},
#     '4': {'name' : 'root', 'email' : 'root@live.com'},
#     '5': {'name' : 'root', 'email' : 'root@live.com'},
#     '6': {'name' : 'root', 'email' : 'root@live.com'},
# }
USER_DICT = {
    '1': 'ROOT1',
    '2': 'ROOT2',
    '3': 'ROOT3',
    '4': 'ROOT4',
    '5': 'ROOT5',
}

def index(request):
    return render(request,'index.html',{'user_dict':USER_DICT})


def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    if request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('passwd')
        # checkbox
        # request.POST.getlist()
        if u == 'alex' and p == '123':
            return redirect('/index/')
        else:
            return  render(request,'login.html')
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