from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
gender_choices = [
    ('male', '男'),
    ('female', '女')
]

weekday_choices = [
    ('Monday', '周一'),
    ('Tuesday', '周二'),
    ('Wednesday', '周三'),
    ('Thursday', '周四'),
    ('Friday', '周五'),
    ('Saturday', '周六'),
    ('Sunday', '周天')
]

# 基础模型
class BaseModel(models.Model):
    # 创建时间
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # 更新时间
    updated_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        abstract = True

# 班次
class PeriodClass(BaseModel):
    # 名称
    name = models.CharField(verbose_name='名称', max_length=32)
    # 年级
    grade = models.IntegerField(verbose_name='年级')
    # 上课次数
    number_of_classes = models.IntegerField(verbose_name='上课次数', default=0)
    # 开始时间
    start_time = models.DateField(verbose_name='开始时间')
    # 结束时间
    end_time = models.DateField(verbose_name='结束时间')
    # 价格
    price = models.DecimalField(verbose_name='价格', max_digits=8, decimal_places=2)
    # 描述
    description = models.CharField(verbose_name='描述', max_length=128, blank=True)
    # 备注
    remark = models.CharField(verbose_name='备注', max_length=128, blank=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '班次'
        verbose_name_plural = '班次'

# 科目
class Subject(BaseModel):
    name = models.CharField(verbose_name='名称', max_length=16)
    # 备注
    remark = models.CharField(verbose_name='备注', max_length=128, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '科目'
        verbose_name_plural = '科目'

# 老师
class Teacher(BaseModel):
    # 姓名
    name = models.CharField(verbose_name='姓名', max_length=32)
    # 性别
    gender = models.CharField(verbose_name='性别', max_length=16, choices=gender_choices, default='male')
    # 手机号
    phone_number = models.CharField(verbose_name='电话号码', max_length=32, blank=True)
    # 科目
    subjects = models.ManyToManyField(Subject, verbose_name='科目')
    # 地址
    address = models.CharField(verbose_name='地址', max_length=128, blank=True)
    # 备注
    remark = models.CharField(verbose_name='备注', max_length=128, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '老师'
        verbose_name_plural = '老师'

# 考试期次
class ExamPeriod(BaseModel):
    description = models.CharField(verbose_name='描述', max_length=128)
    # 备注
    remark = models.CharField(verbose_name='备注', max_length=128, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = '考试期次'
        verbose_name_plural = '考试期次'

# 课表
class Curriculum(BaseModel):
    # 班次
    period_class = models.ForeignKey(PeriodClass, verbose_name='班次', null=True, on_delete=models.SET_NULL)
    # 上课时间
    class_time = models.CharField(verbose_name='上课时间', max_length=16, choices=weekday_choices)
    # 备注
    remark = models.CharField(verbose_name='备注', max_length=128, blank=True)

    def __str__(self):
        if self.period_class:
            return self.period_class.name
        else:
            return self.class_time

    class Meta:
        verbose_name = '课表'
        verbose_name_plural = '课表'

# 课节
class Course(BaseModel):
    # 科目
    subject = models.ForeignKey(Subject, verbose_name='科目', null=True, on_delete=models.SET_NULL)
    # 老师
    teacher = models.ForeignKey(Teacher, verbose_name='老师', null=True, on_delete=models.SET_NULL)
    # 开始时间
    start_time = models.TimeField(verbose_name='开始时间')
    # 结束时间
    end_time = models.TimeField(verbose_name='结束时间')
    # 课表
    curriculum = models.ForeignKey(Curriculum, verbose_name='课表', null=True, on_delete=models.SET_NULL)
    # 备注
    remark = models.CharField(verbose_name='备注', max_length=128, blank=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = '课节'
        verbose_name_plural = '课节'

# 考试
class Exam(BaseModel):
    # 期次(用来筛选同一期全部考试)
    period = models.ForeignKey(ExamPeriod, verbose_name='考试期次', null=True, on_delete=models.SET_NULL)
    # 描述
    description = models.CharField(verbose_name='描述', max_length=128, blank=True)
    # 科目
    subject = models.ForeignKey(Subject, verbose_name='科目', null=True, on_delete=models.SET_NULL)
    # 满分
    full_score = models.FloatField(verbose_name='满分', default=100)
    # 班次
    period_class = models.ForeignKey(PeriodClass, verbose_name='班次', null=True, on_delete=models.SET_NULL)
    # 开始时间
    start_time = models.DateTimeField(verbose_name='开始时间')
    # 结束时间
    end_time = models.DateTimeField(verbose_name='结束时间')
    # 备注
    remark = models.CharField(verbose_name='备注', max_length=128, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = '考试'
        verbose_name_plural = '考试'


# 家长
class Parent(BaseModel):
    # 名字
    name = models.CharField(verbose_name='姓名', max_length=32)
    # 性别
    gender = models.CharField(verbose_name='性别', max_length=16, choices=gender_choices, default='male')
    # 手机号码
    phone_number = models.CharField(verbose_name='电话号码', max_length=32, blank=True)
    # 地址
    address = models.CharField(verbose_name='地址', max_length=128, blank=True)
    # 备注
    remark = models.CharField(verbose_name='备注', max_length=128, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '家长'
        verbose_name_plural = '家长'

# 学生模型
class Student(BaseModel):
    # 姓名
    name = models.CharField(verbose_name='姓名', max_length=32)
    # 出生日期
    birthday = models.DateField(verbose_name='出生日期')
    # 性别
    gender = models.CharField(verbose_name='性别', max_length=16, choices=gender_choices, default='male')
    # 就读学校
    school = models.CharField(verbose_name='就读学校', max_length=32, blank=True)
    # 年级
    grade = models.IntegerField(verbose_name='年级')
    # 手机号
    phone_number = models.CharField(verbose_name='电话号码', max_length=32, blank=True)
    # 地址
    address = models.CharField(verbose_name='地址', max_length=128, blank=True)
    # 报名信息
    register_information = models.ManyToManyField(PeriodClass, verbose_name='报名信息', through='RegisterInformation')
    # 家长
    parent = models.ManyToManyField(Parent, verbose_name='家长')
    # 备注
    remark = models.CharField(verbose_name='备注', max_length=128, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = '学生'

# 成绩单
class Transcript(BaseModel):
    # 期次(用来筛选同一期全部考试)
    period = models.ForeignKey(ExamPeriod, verbose_name='考试期次', on_delete=models.CASCADE)
    # 科目
    subject = models.ForeignKey(Subject, verbose_name='科目', on_delete=models.CASCADE)
    # 满分
    full_score = models.FloatField(verbose_name='满分', default=100)
    # 得分
    score = models.FloatField(verbose_name='得分', default=0)
    # 学生
    student = models.ForeignKey(Student, verbose_name='学生', on_delete=models.CASCADE)
    # 备注
    remark = models.CharField(verbose_name='备注', max_length=128, blank=True)

    def __str__(self):
        if self.period:
            return self.subject + '_' + self.period
        else:
            return self.subject

    class Meta:
        verbose_name = '成绩单'
        verbose_name_plural = '成绩单'


# 报名信息
class RegisterInformation(BaseModel):
    # 班次
    period_class = models.ForeignKey(PeriodClass, verbose_name='班次', on_delete=models.CASCADE)
    # 学生
    student = models.ForeignKey(Student, verbose_name='学生', on_delete=models.CASCADE)
    # 已缴金额
    amount_paid = models.DecimalField(verbose_name='已付款', max_digits=8, decimal_places=2, default=0)
    # 备注
    remark = models.CharField(verbose_name='备注', max_length=128, blank=True)

    def __str__(self):
        return self.student.name + '-->' + self.period_class.name

    class Meta:
        verbose_name = '报名信息'
        verbose_name_plural = '报名信息'

# 推荐信息
class SpreadInformation(BaseModel):
    # 推荐人
    promoter = models.ForeignKey(Student, verbose_name='推荐人', on_delete=models.CASCADE, related_name='promoter')
    # 被荐人
    customer = models.OneToOneField(Student, verbose_name='被荐人', on_delete=models.CASCADE, primary_key=False)
    # 优惠金额
    discount = models.DecimalField(verbose_name='优惠金额', max_digits=8, decimal_places=2)
    # 备注
    remark = models.CharField(verbose_name='备注', max_length=128, blank=True)

    def clean(self):
        if self.promoter == self.customer:
            raise ValidationError('推荐人和被推荐人不能为同一人')

    def __str__(self):
        return self.customer.name

    class Meta:
        verbose_name = '推荐信息'
        verbose_name_plural = '推荐信息'
