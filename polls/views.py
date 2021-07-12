from django.shortcuts import render
from django.http import HttpResponse
from django.db import OperationalError
from django.db import IntegrityError
from django.db import DataError
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection

from polls.models import MediniceInfo
from polls.models import Industry
from polls.models import Worker
from polls.models import Customer
from polls.models import MediniceStore
from polls.models import User
from polls.models import Purchase
from polls.models import PurchaseInfo
from polls.models import Sell
from polls.models import SellInfo

from polls.view_models import MediniceInfoView
from polls.view_models import IndustryView
from polls.view_models import WorkerView
from polls.view_models import CustomerView
from polls.view_models import MediniceStoreView
from polls.view_models import PurchaseView
from polls.view_models import PurchaseInfoView
from polls.view_models import SellView
from polls.view_models import SellInfoView


class InputError(Exception):
    pass


def insert_text(request):
    for i in range(5):
        index = Industry()
        index.厂家注册号 = '00000' + str(i)
        index.厂家名字 = '安徽第' + str(i)
        index.厂家地址 = 'home'
        index.厂家登记机关 = 'China'
        index.save()
    return HttpResponse('数据插入完毕')


def index(request):
    return render(request, 'polls/table.html')


def table(request):
    return render(request, 'polls/table.html')


def toSell(request):
    return render(request, 'polls/sell.html')


def toError(request):
    return render(request, 'polls/Error.html')

def toLr(request):
    return render(request, 'polls/lr.html')

# def view(request):
#     if request.name == 'update':
#         id = request.POST['ID']
#         name = request.POST['name']
#         address = request.POST['address']
#         department = request.POST['department']
#
#         index = Industry()
#         index.厂家注册号 = id
#         index.厂家名字 = name
#         index.厂家地址 = address
#         index.厂家登记机关 = department
#         index.save()
#         return render(request, 'polls/table.html')
#     if request.name == 'query':
#         name = request.GET.get('name')
#         if name is not '':
#             index = Industry.objects.filter(厂家地址=name)
#         else:
#             index = Industry.objects.all()
#         return render(request, 'polls/table.html', {"result": index})


# ------------------------Medinice-------------------------#

def industryOp(request):  # url not set
    try:
        if request.method == 'POST':  # 表单提供type用于对增查改进行判断
            type = request.POST.get('type')
            id = request.POST.get('id')
            name = request.POST.get('name')
            addr = request.POST.get('addr')
            department = request.POST.get('department')

            if type == 'add':  # 提供所有属性并插入，html中使用require保证属性都非空
                index = Industry()
                index.厂家注册号 = id
                index.厂家名字 = name
                index.厂家地址 = addr
                index.厂家登记机关 = department
                index.save()

            if type == 'update':  # 提供主键，修改其他属性
                index = Industry.objects.get(厂家注册号=id)
                index.厂家名字 = name
                index.厂家地址 = addr
                index.厂家登记机关 = department
                index.save()
            if type == 'delete':  # 提供任意数量属性，只要任意一条满足则删除
                Industry.objects.filter(厂家注册号=id).delete()
                Industry.objects.filter(厂家名字=name).delete()
                Industry.objects.filter(厂家地址=addr).delete()
                Industry.objects.filter(厂家登记机关=department).delete()

            return render(request, 'polls/table.html')  # template not set yet

        if request.method == 'GET':  # 提供任意数量属性，输出全部满足项，若都未输入则全部输出
            id = request.GET.get('id')
            name = request.GET.get('name')
            addr = request.GET.get('addr')
            department = request.GET.get('department')
            qSet = IndustryView.objects.all()

            if id != '':
                qSet = qSet.filter(厂家注册号=id)
            if name != '':
                qSet = qSet.filter(厂家名字=name)
            if addr != '':
                qSet = qSet.filter(厂家地址=addr)
            if department != '':
                qSet = qSet.filter(厂家登记机关=department)

            return render(request, '', {"result": qSet})  # template not set yet
    except OperationalError as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})
    except ObjectDoesNotExist as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except IntegrityError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except DataError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "输入出现异常"})
    except Exception as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})


def workerOp(request):
    try:
        if request.method == 'POST':  # 表单提供type用于对增查改进行判断
            type = request.POST.get('type')
            id = request.POST.get('id')  # 员工编号
            name = request.POST.get('name')
            gender = request.POST.get('gender')  # 性别
            job = request.POST.get('job')  # 职位
            age = request.POST.get('age')
            wage = request.POST.get('wage')  # 工资
            tid = request.POST.get('tid')  # 身份证号
            birth = request.POST.get('birth')  # 出生日期

            if type == 'add':  # 提供所有属性并插入，html中使用require保证属性都非空
                index = Worker()
                index.员工编号 = id
                index.员工姓名 = name
                index.员工性别 = gender
                index.员工出生日期 = birth
                index.员工工资 = wage
                index.员工职位 = job
                index.员工年龄 = age
                index.员工身份证号 = tid
                index.save()

            if type == 'update':  # 提供主键，修改其他属性
                index = Worker.objects.get(员工编号=id)
                index.员工姓名 = name
                index.员工性别 = gender
                index.员工出生日期 = birth
                index.员工工资 = wage
                index.员工职位 = job
                index.员工年龄 = age
                index.员工身份证号 = tid
                index.save()
            if type == 'delete':  # 提供任意数量属性，只要任意一条满足则删除
                Worker.objects.filter(员工编号=id).delete()
                Worker.objects.filter(员工姓名=name).delete()
                Worker.objects.filter(员工性别=gender).delete()
                Worker.objects.filter(员工职位=job).delete()

            return render(request, '')  # template not set yet

        if request.method == 'GET':  # 提供任意数量属性，输出全部满足项，若都未输入则全部输出
            id = request.GET.get('id')
            name = request.GET.get('name')
            gender = request.GET.get('gender')
            job = request.GET.get('job')
            qSet = WorkerView.objects.all()

            if id != '':
                qSet = qSet.filter(员工编号=id)
            if name != '':
                qSet = qSet.filter(员工姓名=name)
            if gender != '':
                qSet = qSet.filter(员工性别=gender)
            if job != '':
                qSet = qSet.filter(员工职位=job)

            return render(request, '', {"result": qSet})  # template not set yet
    except OperationalError as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})
    except ObjectDoesNotExist as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except IntegrityError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except DataError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "输入出现异常"})
    except Exception as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})


def custumerOp(request):
    try:
        if request.method == 'POST':  # 表单提供type用于对增查改进行判断
            type = request.POST.get('type')
            id = request.POST.get('id')  # 客户编号
            name = request.POST.get('name')
            gender = request.POST.get('gender')  # 性别
            age = request.POST.get('age')
            tid = request.POST.get('tid')  # 身份证号
            birth = request.POST.get('birth')  # 出生日期

            if type == 'add':  # 提供所有属性并插入，html中使用require保证属性都非空
                index = Customer()
                index.客户编号 = id
                index.客户姓名 = name
                index.客户性别 = gender
                index.客户出生日期 = birth
                index.客户年龄 = age
                index.客户身份证号 = tid
                index.save()

            if type == 'update':  # 提供主键，修改其他属性
                index = Customer.objects.get(客户编号=id)
                index.客户姓名 = name
                index.客户性别 = gender
                index.客户出生日期 = birth
                index.客户年龄 = age
                index.客户身份证号 = tid
                index.save()
            if type == 'delete':  # 提供任意数量属性，只要任意一条满足则删除
                Customer.objects.filter(客户编号=id).delete()
                Customer.objects.filter(客户姓名=name).delete()
                Customer.objects.filter(客户性别=gender).delete()

            return render(request, '')  # template not set yet

        if request.method == 'GET':  # 提供任意数量属性，输出全部满足项，若都未输入则全部输出
            id = request.GET.get('id')
            name = request.GET.get('name')
            gender = request.GET.get('gender')
            job = request.GET.get('job')
            qSet = CustomerView.objects.all()

            if id != '':
                qSet = qSet.filter(客户编号=id)
            if name != '':
                qSet = qSet.filter(客户姓名=name)
            if gender != '':
                qSet = qSet.filter(客户性别=gender)

            return render(request, '', {"result": qSet})  # template not set yet
    except OperationalError as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})
    except ObjectDoesNotExist as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except IntegrityError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except DataError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "输入出现异常"})
    except Exception as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})


def mediniceInfoOp(request):
    try:
        if request.method == 'POST':  # 表单提供type用于对增查改进行判断
            type = request.POST.get('type')
            id = request.POST.get('id')
            name = request.POST.get('name')
            iprice = request.POST.get('iprice')  # 零售价
            nprice = request.POST.get('nprice')  # 批发价
            iid = request.POST.get('iid')  # 厂家注册号
            medid = request.POST.get('medid')  # 药品条码
            comid = request.POST.get('comid')  # 通用码
            unit = request.POST.get('unit')  # 单位
            stiid = request.POST.get('stiid')  # 规格码
            mev = request.POST.get("mev")  # 剂型
            addr = request.POST.get('addr')  # 产地
            pnum = request.POST.get('pnum')  # 包装数量
            gp = request.POST.get('gp')  # 质量标准
            hid = request.POST.get('hid')  # 医疗编号
            med = request.POST.get('med')  # 药品类别
            indE = Industry.objects.get(厂家注册号=iid)

            if type == 'add':  # 提供所有属性并插入，html中使用require保证属性都非空
                index = MediniceInfo()
                index.药品编号 = id
                index.药品名称 = name
                index.零售价 = iprice
                index.批发价 = nprice
                index.厂家注册号 = indE
                index.药品条码 = medid
                index.通用码 = comid
                index.单位 = unit
                index.规格码 = stiid
                index.剂型 = mev
                index.产地 = addr
                index.包装数量 = pnum
                index.质量标准 = gp
                index.医疗编号 = hid
                index.药品类别 = med
                index.save()

            if type == 'update':  # 提供主键，修改其他属性
                index = MediniceInfo.objects.get(药品编号=id)
                index.药品名称 = name
                index.零售价 = iprice
                index.批发价 = nprice
                index.厂家注册号 = indE
                index.药品条码 = medid
                index.通用码 = comid
                index.单位 = unit
                index.规格码 = stiid
                index.剂型 = mev
                index.产地 = addr
                index.包装数量 = pnum
                index.质量标准 = gp
                index.医疗编号 = hid
                index.药品类别 = med
                index.save()
            if type == 'delete':  # 提供任意数量属性，只要任意一条满足则删除
                MediniceInfo.objects.filter(药品编号=id).delete()
                MediniceInfo.objects.filter(药品名称=name).delete()
                MediniceInfo.objects.filter(零售价=iprice).delete()
                MediniceInfo.objects.filter(批发价=nprice).delete()
                MediniceInfo.objects.filter(厂家注册号=iid).delete()
                MediniceInfo.objects.filter(药品条码=medid).delete()
                MediniceInfo.objects.filter(通用码=comid).delete()
                MediniceInfo.objects.filter(单位=unit).delete()
                MediniceInfo.objects.filter(规格码=stiid).delete()
                MediniceInfo.objects.filter(剂型=mev).delete()
                MediniceInfo.objects.filter(产地=addr).delete()
                MediniceInfo.objects.filter(包装数量=pnum).delete()
                MediniceInfo.objects.filter(质量标准=gp).delete()
                MediniceInfo.objects.filter(医疗编号=hid).delete()
                MediniceInfo.objects.filter(药品类别=med).delete()

            return render(request, '')  # template not set yet

        if request.method == 'GET':  # 提供任意数量属性，输出全部满足项，若都未输入则全部输出
            type = request.GET.get('type')
            id = request.GET.get('id')
            name = request.GET.get('name')
            iprice = request.GET.get('iprice')  # 零售价
            nprice = request.GET.get('nprice')  # 批发价
            iid = request.GET.get('iid')  # 厂家注册号
            medid = request.GET.get('medid')  # 药品条码
            comid = request.GET.get('comid')  # 通用码
            unit = request.GET.get('unit')  # 单位
            stiid = request.GET.get('stiid')  # 规格码
            mev = request.GET.get("mev")  # 剂型
            addr = request.GET.get('addr')  # 产地
            pnum = request.GET.get('pnum')  # 包装数量
            gp = request.GET.get('gp')  # 质量标准
            hid = request.GET.get('hid')  # 医疗编号
            med = request.GET.get('med')  # 药品类别
            qSet = MediniceInfoView.objects.all()

            if id != '':
                qSet = qSet.filter(药品编号=id)
            if name != '':
                qSet = qSet.filter(药品名称=name)
            if iprice != '':
                qSet = qSet.filter(零售价=iprice)
            if nprice != '':
                qSet = qSet.filter(批发价=nprice)
            if iid != '':
                qSet = qSet.filter(厂家注册号=iid)
            if medid != '':
                qSet = qSet.filter(药品条码=medid)
            if comid != '':
                qSet = qSet.filter(通用码=comid)
            if unit != '':
                qSet = qSet.filter(单位=unit)
            if stiid != '':
                qSet = qSet.filter(规格码=stiid)
            if mev != '':
                qSet = qSet.filter(剂型=mev)
            if addr != '':
                qSet = qSet.filter(产地=addr)
            if pnum != '':
                qSet = qSet.filter(包装数量=pnum)
            if gp != '':
                qSet = qSet.filter(质量标准=gp)
            if hid != '':
                qSet = qSet.filter(医疗编号=hid)
            if med != '':
                qSet = qSet.filter(药品类别=med)

            return render(request, '', {"result": qSet})  # template not set yet
    except OperationalError as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})
    except ObjectDoesNotExist as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except IntegrityError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except DataError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "输入出现异常"})
    except Exception as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})


def mediniceStoreOp(request):  # url not set
    try:
        if request.method == 'GET':  # 提供任意数量属性，输出全部满足项，若都未输入则全部输出
            id = request.GET.get('id')
            num = request.GET.get('num')
            qSet = MediniceStoreView.objects.all()

            if id != '':
                qSet = qSet.filter(药品编号=id)
            if num != '':
                qSet = qSet.filter(库存量=num)

        return render(request, '', {"result": qSet})  # template not set yet
    except OperationalError as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})
    except ObjectDoesNotExist as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except IntegrityError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except DataError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "输入出现异常"})
    except Exception as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})


def purchaseOp(request):
    try:
        if request.method == 'POST':  # 表单提供type用于对增查改进行判断
            type = request.POST.get('type')
            id = request.POST.get('id')
            iid = request.POST.get('iid')  # 厂家注册号
            date = request.POST.get('date')  # 进货日期
            wid = request.POST.get('wid')  # 员工编号
            num = 0  # 品种数量,插入时总为0
            total = 0  # 进货总量,插入时总为0
            price = 0  # 进货金额,插入时总为0
            indE = Industry.objects.get(厂家注册号=iid)

            if type == 'add':  # 提供所有属性并插入，html中使用require保证属性都非空
                index = Purchase()
                index.进货单号 = id
                index.厂家注册号 = indE
                index.进货日期 = date
                index.员工编号 = wid
                index.品种数量 = num
                index.进货总量 = total
                index.进货金额 = price
                index.save()

            if type == 'update':  # 提供主键，修改其他属性
                index = Purchase.objects.get(进货单号=id)
                index.厂家注册号 = indE
                index.进货日期 = date
                index.员工编号 = wid
                index.save()

            if type == 'delete':  # 提供任意数量属性，只要任意一条满足则删除
                Purchase.objects.filter(进货单号=id).delete()
                Purchase.objects.filter(厂家注册号=iid).delete()
                Purchase.objects.filter(进货日期=date).delete()
                Purchase.objects.filter(员工编号=wid).delete()

            return render(request, '')  # template not set yet

        if request.method == 'GET':  # 提供任意数量属性，输出全部满足项，若都未输入则全部输出
            id = request.GET.get('id')
            iid = request.GET.get('iid')
            date = request.GET.get('date')
            wid = request.GET.get('wid')
            qSet = PurchaseView.objects.all()

            if id != '':
                qSet = qSet.filter(进货单号=id)
            if iid != '':
                qSet = qSet.filter(厂家注册号=iid)
            if date != '':
                qSet = qSet.filter(进货日期=date)
            if wid != '':
                qSet = qSet.filter(员工编号=wid)

            return render(request, 'polls/sell.html', {"result": qSet})  # template not set yet
    except OperationalError as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})
    except ObjectDoesNotExist as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except IntegrityError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except DataError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "输入出现异常"})
    except Exception as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})


def sellOp(request):
    try:
        if request.method == 'POST':  # 表单提供type用于对增查改进行判断
            type = request.POST.get('type')
            id = request.POST.get('id')
            cid = request.POST.get('cid')  # 客户编号
            date = request.POST.get('date')  # 销售日期
            wid = request.POST.get('wid')  # 员工编号
            workE = Worker.objects.get(员工编号=wid)
            cusE = Customer.objects.get(客户编号=cid)
            num = 0  # 品种数量,插入时总为0
            total = 0  # 销售总量,插入时总为0
            price = 0  # 销售金额,插入时总为0

            if type == 'add':  # 提供所有属性并插入，html中使用require保证属性都非空
                index = Sell()
                index.销售单号 = id
                index.客户编号 = cusE
                index.销售日期 = date
                index.员工编号 = workE
                index.品种数量 = num
                index.销售总量 = total
                price.销售金额 = price
                index.save()

            if type == 'update':  # 提供主键，修改其他属性
                index = Sell.objects.get(进货单号=id)
                index.客户编号 = cusE
                index.销售日期 = date
                index.员工编号 = workE
                index.save()

            if type == 'delete':  # 提供任意数量属性，只要任意一条满足则删除
                Sell.objects.filter(销售单号=id).delete()
                Sell.objects.filter(客户编号=cid).delete()
                Sell.objects.filter(销售日期=date).delete()
                Sell.objects.filter(员工编号=wid).delete()

            return render(request, '')  # template not set yet

        if request.method == 'GET':  # 提供任意数量属性，输出全部满足项，若都未输入则全部输出
            id = request.GET.get('id')
            cid = request.GET.get('cid')
            date = request.GET.get('date')
            wid = request.GET.get('wid')
            qSet = SellView.objects.all()

            if id != '':
                qSet = qSet.filter(销售单号=id)
            if cid != '':
                qSet = qSet.filter(客户编号=cid)
            if date != '':
                qSet = qSet.filter(销售日期=date)
            if wid != '':
                qSet = qSet.filter(员工编号=wid)

            return render(request, '', {"result": qSet})  # template not set yet

    except OperationalError as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})
    except ObjectDoesNotExist as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except IntegrityError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except DataError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "输入出现异常"})
    except Exception as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})


def purchaseInfoOp(request):
    try:
        if request.method == 'POST':  # 表单提供type用于对增查改进行判断
            type = request.POST.get('type')
            id = request.POST.get('id')
            mid = request.POST.get('mid')  # 药品编号
            num = request.POST.get('num')  # 进货量
            iprice = request.POST.get('iprice')  # 进货单价
            purE = Purchase.objects.get(进货单号=id)
            medE = MediniceInfo.objects.get(药品编号=mid)
            price = eval(num) * eval(iprice)  # 进货金额,自动计算，不必输入

            if eval(num) < 0 or eval(iprice) < 0:
                raise DataError

            if type == 'add':  # 提供所有属性并插入，html中使用require保证属性都非空
                index = PurchaseInfo()
                index.进货单号 = purE
                index.药品编号 = medE
                index.进货量 = num
                index.进货单价 = iprice
                index.进货金额 = price
                index.save()

            return render(request, '')  # template not set yet

        if request.method == 'GET':  # 提供任意数量属性，输出全部满足项，若都未输入则全部输出
            id = request.GET.get('id')
            mid = request.GET.get('mid')
            num = request.GET.get('num')
            iprice = request.GET.get('iprice')
            price = request.GET.get('price')
            qSet = PurchaseInfoView.objects.all()

            if id != '':
                qSet = qSet.filter(进货单号=id)
            if mid != '':
                qSet = qSet.filter(药品编号=mid)
            if num != '':
                qSet = qSet.filter(进货量=num)
            if iprice != '':
                qSet = qSet.filter(进货单价=iprice)
            if price != '':
                qSet = qSet.filter(进货金额=price)

            return render(request, '', {"result": qSet})  # template not set yet

    except OperationalError as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})
    except ObjectDoesNotExist as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except IntegrityError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except DataError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "输入出现异常"})
    except Exception as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})


def sellInfoOp(request):
    try:
        if request.method == 'POST':  # 表单提供type用于对增查改进行判断
            type = request.POST.get('type')
            id = request.POST.get('id')
            sellE = Sell.objects.get(销售单号=id)
            mid = request.POST.get('mid')  # 药品编号
            medE = MediniceInfo.objects.get(药品编号=id)
            num = request.POST.get('num')  # 销售量
            iprice = request.POST.get('iprice')  # 销售单价
            price = eval(num) * eval(iprice)  # 销售金额,自动计算，不必输入

            if eval(num) < 0 or eval(iprice) < 0:
                raise DataError

            if type == 'add':  # 提供所有属性并插入，html中使用require保证属性都非空

                index = SellInfo()
                index.销售单号 = sellE
                index.药品编号 = medE
                index.销售量 = num
                index.销售单价 = iprice
                index.销售金额 = price
                index.save()
                return render(request, 'polls/sell.html')  # template not set yet

        if request.method == 'GET':  # 提供任意数量属性，输出全部满足项，若都未输入则全部输出
            id = request.GET.get('id')
            mid = request.GET.get('mid')
            num = request.GET.get('num')
            iprice = request.GET.get('iprice')
            price = request.GET.get('price')
            qSet = SellInfoView.objects.all()

            if id != '':
                qSet = qSet.filter(销售单号=id)
            if mid != '':
                qSet = qSet.filter(药品编号=mid)
            if num != '':
                qSet = qSet.filter(销售量=num)
            if iprice != '':
                qSet = qSet.filter(销售单价=iprice)
            if price != '':
                qSet = qSet.filter(销售金额=price)

        return render(request, 'polls/sell.html', {"result": qSet})  # template not set yet

    except OperationalError as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})
    except ObjectDoesNotExist as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except IntegrityError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except DataError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "输入出现异常"})
    except Exception as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})


def userOP(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            privilege = request.POST.get('privilege')
            with connection.cursor() as cursor:
                cursor.callproc('register', (username, password, privilege))
            return render(request, 'polls/lr.html')

        if request.method == 'GET':
            username = request.GET.get('username')
            password = request.GET.get('password')
            privilege = request.GET.get('privilege')
            with connection.cursor() as cursor:
                cursor.callproc('login', [username, password, privilege])
            return render(request, 'polls/lr.html')

    except OperationalError as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})
    except ObjectDoesNotExist as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except IntegrityError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "不满足完整性约束"})
    except DataError as e:
        return render(request, 'polls/Error.html', {"errorMessage": "输入出现异常"})
    except Exception as e:
        return render(request, 'polls/Error.html', {"errorMessage": e})
