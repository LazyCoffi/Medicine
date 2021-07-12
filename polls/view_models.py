from django.db import models

class WorkerView(models.Model):
    员工编号 = models.CharField(max_length=10, db_collation='utf8_general_ci', primary_key=True)
    员工姓名 = models.CharField(max_length=6, db_collation='utf8_general_ci')
    员工性别 = models.CharField(max_length=2, db_collation='utf8_general_ci')
    员工职位 = models.CharField(max_length=20, db_collation='utf8_general_ci')

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = '员工视图'

class CustomerView(models.Model):
    客户编号 = models.CharField(max_length=10, db_collation='utf8_general_ci', primary_key=True)
    客户姓名 = models.CharField(max_length=10, db_collation='utf8_general_ci')
    客户性别 = models.CharField(max_length=2, db_collation='utf8_general_ci')

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = '客户视图'

class IndustryView(models.Model):
    厂家注册号 = models.CharField(max_length=10, db_collation='utf8_general_ci', primary_key=True)
    厂家名字 = models.CharField(max_length=20, db_collation='utf8_general_ci')
    厂家地址 = models.CharField(max_length=20, db_collation='utf8_general_ci')
    厂家登记机关 = models.CharField(max_length=45, db_collation='utf8_general_ci')

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = '生产厂家视图'

class MediniceInfoView(models.Model):
    药品编号 = models.CharField(max_length=10, db_collation='utf8_general_ci', primary_key=True)
    药品名称 = models.CharField(max_length=20, db_collation='utf8_general_ci')
    零售价 = models.DecimalField(max_digits=20, decimal_places=4)
    批发价 = models.DecimalField(max_digits=20, decimal_places=4)
    厂家注册号 = models.CharField(max_length=10, db_collation='utf8_general_ci')
    药品条码 = models.CharField(max_length=20, db_collation='utf8_general_ci')
    通用码 = models.CharField(max_length=20, db_collation='utf8_general_ci')
    拼音码 = models.CharField(max_length=20, db_collation='utf8_general_ci')
    单位 = models.CharField(max_length=20, db_collation='utf8_general_ci')
    规格码 = models.CharField(max_length=20, db_collation='utf8_general_ci')
    剂型 = models.CharField(max_length=20, db_collation='utf8_general_ci')
    产地 = models.CharField(max_length=20, db_collation='utf8_general_ci')
    包装数量 = models.IntegerField()
    有效期 = models.DateField()
    质量标准 = models.CharField(max_length=20, db_collation='utf8_general_ci')
    医疗编号 = models.CharField(max_length=20, db_collation='utf8_general_ci')
    药品类别 = models.CharField(max_length=45, db_collation='utf8_general_ci')

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = '药品信息视图'

class MediniceStoreView(models.Model):
    药品编号 = models.CharField(max_length=10, db_collation='utf8_general_ci')
    药品名称 = models.CharField(max_length=20, db_collation='utf8_general_ci')
    库存量 = models.IntegerField()

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = '药品库存视图'

class PurchaseView(models.Model):
    进货单号 = models.CharField(max_length=10, db_collation='utf8_general_ci', primary_key=True)
    厂家注册号 = models.CharField(max_length=45, db_collation='utf8_general_ci')
    进货日期 = models.DateField()
    员工编号 = models.CharField(max_length=45, db_collation='utf8_general_ci')
    品种数量 = models.IntegerField()
    进货总量 = models.IntegerField(blank=True, null=True)
    进货金额 = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = '药品进货视图'

class SellView(models.Model):
    销售单号 = models.CharField(max_length=10, db_collation='utf8_general_ci', primary_key=True)
    销售日期 = models.CharField(max_length=10, db_collation='utf8_general_ci')
    员工编号 = models.CharField(max_length=10, db_collation='utf8_general_ci')
    客户编号 = models.CharField(max_length=10, db_collation='utf8_general_ci')
    品种数量 = models.IntegerField()
    销售总量 = models.IntegerField()
    销售金额 = models.DecimalField(max_digits=20, decimal_places=4)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = '药品销售视图'

class PurchaseInfoView(models.Model):
    进货单号 = models.CharField(max_length=10, db_collation='utf8_general_ci', primary_key=True)
    药品编号 = models.CharField(max_length=45, db_collation='utf8_general_ci')
    进货量 = models.IntegerField()
    进货单价 = models.DecimalField(max_digits=20, decimal_places=4)
    进货金额 = models.DecimalField(max_digits=20, decimal_places=4)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = '进货明细视图'

class SellInfoView(models.Model):
    销售单号 = models.CharField(max_length=10, db_collation='utf8_general_ci', primary_key=True)
    药品编号 = models.CharField(max_length=10, db_collation='utf8_general_ci')
    销售量 = models.IntegerField()
    销售单价 = models.DecimalField(max_digits=20, decimal_places=4)
    销售金额 = models.DecimalField(max_digits=20, decimal_places=4)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = '销售明细视图'