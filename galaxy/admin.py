from django.contrib import admin
from . import models
from datetime import date

# Register your models here.

admin.site.site_header = 'AAA教育'
admin.site.site_title = 'AAA教育'
admin.site.empty_value_display = '无'

admin.site.register(models.Subject)
admin.site.register(models.ExamPeriod)
admin.site.register(models.Exam)
# admin.site.register(models.Teacher)
# admin.site.register(models.Curriculum)
admin.site.register(models.Course)
admin.site.register(models.Transcript)

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'gender', 'grade', 'class_name', 'remark')
    filter_horizontal = ('parent',)
    def class_name(self, obj):
        now = date.today()
        my_class = models.PeriodClass.objects.get(student=obj, end_time__gte=now)
        return my_class.name
    class_name.short_description = '班次'

@admin.register(models.PeriodClass)
class PeriodClassAdmin(admin.ModelAdmin):
    ordering = ('-start_time',)
    list_display = ('name', 'number_of_classes', 'is_processing', 'start_time', 'end_time', 'description', 'remark')

    def is_processing(self, obj):
        now = date.today()
        return obj.start_time <= now <= obj.end_time
    is_processing.boolean = True
    is_processing.short_description = '正在开课'

@admin.register(models.Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'phone_number', 'children_name', 'address', 'remark')

    def children_name(self, obj):
        children = models.Student.objects.filter(parent=obj)
        names = ''
        for child in children:
            names += (child.name + '，')
        return names[:-1]
    children_name.short_description = '孩子'


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'subjects_name', 'remark')
    filter_horizontal = ('subjects',)
    def subjects_name(self, obj):
        name = ''
        for sub in obj.subjects.all():
            name += (sub.name + ',')
        return name[:-1]
    subjects_name.short_description = '科目'

@admin.register(models.RegisterInformation)
class RegisterInformationAdmin(admin.ModelAdmin):
    list_display = ('student', 'period_class', 'class_price', 'promotion_number', 'discounted_price', 'amount_to_be_paid', 'amount_paid')

    def class_price(self, obj):
        return obj.period_class.price
    class_price.short_description = '报名费'

    # 推广信息
    def spread_information(self, obj):
        student = obj.student
        spread_information = models.SpreadInformation.objects.filter(promoter=student)
        return spread_information

    # 推广人数
    def promotion_number(self, obj):
        spread_information = self.spread_information(obj)
        return spread_information.count()
    promotion_number.short_description = '推荐人数'

    # 优惠总金额
    def discounted_price(self, obj):
        spread_information = self.spread_information(obj)
        amount = 0
        for info in spread_information:
            amount += info.discount
        return amount
    discounted_price.short_description = '总优惠'

    # 还需支付金额
    def amount_to_be_paid(self, obj):
        amount = self.discounted_price(obj)
        return obj.period_class.price - amount
    amount_to_be_paid.short_description = '应付款'


class CourseInline(admin.TabularInline):
    model = models.Course

@admin.register(models.Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = ('period_class', 'class_time')
    inlines = [CourseInline]

@admin.register(models.SpreadInformation)
class SpreadInformationAdmin(admin.ModelAdmin):
    list_display = ('promoter', 'customer', 'discount')
