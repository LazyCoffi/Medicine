# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PollsTestModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'polls_test_model'


class Worker(models.Model):
    员工编号 = models.CharField(primary_key=True, max_length=10)
    员工姓名 = models.CharField(max_length=6)
    员工出生日期 = models.DateField()
    员工年龄 = models.IntegerField()
    员工身份证号 = models.CharField(max_length=20)
    员工职位 = models.CharField(max_length=20)
    员工工资 = models.DecimalField(max_digits=20, decimal_places=4)
    员工性别 = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = '员工表'


class Customer(models.Model):
    客户编号 = models.CharField(primary_key=True, max_length=10)
    客户姓名 = models.CharField(max_length=10)
    客户出生日期 = models.DateField()
    客户年龄 = models.IntegerField()
    客户身份证号 = models.CharField(max_length=20)
    客户性别 = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = '客户表'


class Industry(models.Model):
    厂家注册号 = models.CharField(primary_key=True, max_length=10)
    厂家名字 = models.CharField(max_length=20)
    厂家地址 = models.CharField(max_length=20)
    厂家登记机关 = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = '生产厂家表'


class User(models.Model):
    用户编号 = models.AutoField(primary_key=True)
    用户名 = models.CharField(max_length=20)
    密码 = models.CharField(max_length=20)
    用户权限 = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = '用户表'


class MediniceInfo(models.Model):
    药品编号 = models.CharField(primary_key=True, max_length=10)
    药品名称 = models.CharField(max_length=20)
    零售价 = models.DecimalField(max_digits=20, decimal_places=4)
    批发价 = models.DecimalField(max_digits=20, decimal_places=4)
    厂家注册号 = models.ForeignKey(Industry, models.DO_NOTHING, db_column='厂家注册号')
    药品条码 = models.CharField(max_length=20)
    通用码 = models.CharField(max_length=20)
    拼音码 = models.CharField(max_length=20)
    单位 = models.CharField(max_length=20)
    规格码 = models.CharField(max_length=20)
    剂型 = models.CharField(max_length=20)
    产地 = models.CharField(max_length=20)
    包装数量 = models.IntegerField()
    有效期 = models.DateField()
    质量标准 = models.CharField(max_length=20)
    医疗编号 = models.CharField(max_length=20)
    药品类别 = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = '药品信息表'


class MediniceStore(models.Model):
    药品编号 = models.OneToOneField(MediniceInfo, models.DO_NOTHING, db_column = '药品编号', primary_key = True)
    库存量 = models.IntegerField()

    class Meta:
        managed = False
        db_table = '药品库存表'


class Purchase(models.Model):
    进货单号 = models.CharField(primary_key=True, max_length=10)
    厂家注册号 = models.ForeignKey(Industry, models.DO_NOTHING, db_column='厂家注册号')
    进货日期 = models.DateField()
    员工编号 = models.ForeignKey(Worker, models.DO_NOTHING, db_column='员工编号')
    品种数量 = models.IntegerField()
    进货总量 = models.IntegerField(blank=True, null=True)
    进货金额 = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '药品进货表'


class Sell(models.Model):
    销售单号 = models.CharField(primary_key=True, max_length=10)
    销售日期 = models.CharField(max_length=10)
    员工编号 = models.ForeignKey(Worker, models.DO_NOTHING, db_column='员工编号')
    客户编号 = models.ForeignKey(Customer, models.DO_NOTHING, db_column='客户编号')
    品种数量 = models.IntegerField()
    销售总量 = models.IntegerField()
    销售金额 = models.DecimalField(max_digits=20, decimal_places=4)

    class Meta:
        managed = False
        db_table = '药品销售表'


class PurchaseInfo(models.Model):
    进货单号 = models.OneToOneField(Purchase, models.DO_NOTHING, db_column='进货单号', primary_key=True)
    药品编号 = models.ForeignKey(MediniceInfo, models.DO_NOTHING, db_column='药品编号')
    进货量 = models.IntegerField()
    进货单价 = models.DecimalField(max_digits=20, decimal_places=4)
    进货金额 = models.DecimalField(max_digits=20, decimal_places=4)

    class Meta:
        managed = False
        db_table = '进货明细表'
        unique_together = (('进货单号', '药品编号'),)


class SellInfo(models.Model):
    销售单号 = models.OneToOneField(Sell, models.DO_NOTHING, db_column='销售单号', primary_key=True)
    药品编号 = models.ForeignKey(MediniceInfo, models.DO_NOTHING, db_column='药品编号')
    销售量 = models.IntegerField()
    销售单价 = models.DecimalField(max_digits=20, decimal_places=4)
    销售金额 = models.DecimalField(max_digits=20, decimal_places=4)

    class Meta:
        managed = False
        db_table = '销售明细表'
        unique_together = (('销售单号', '药品编号'),)