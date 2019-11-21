# Generated by Django 2.1.13 on 2019-11-15 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.CharField(blank=True, max_length=128, verbose_name='备注')),
                ('start_time', models.TimeField(verbose_name='开始时间')),
                ('end_time', models.TimeField(verbose_name='结束时间')),
            ],
            options={
                'verbose_name': '课节',
                'verbose_name_plural': '课节',
            },
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.CharField(blank=True, max_length=128, verbose_name='备注')),
                ('class_time', models.CharField(choices=[('Monday', '周一'), ('Tuesday', '周二'), ('Wednesday', '周三'), ('Thursday', '周四'), ('Friday', '周五'), ('Saturday', '周六'), ('Sunday', '周天')], max_length=16, verbose_name='上课时间')),
            ],
            options={
                'verbose_name': '课表',
                'verbose_name_plural': '课表',
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.CharField(blank=True, max_length=128, verbose_name='备注')),
                ('description', models.CharField(blank=True, max_length=128, verbose_name='描述')),
                ('full_score', models.FloatField(default=100, verbose_name='满分')),
                ('start_time', models.DateTimeField(verbose_name='开始时间')),
                ('end_time', models.DateTimeField(verbose_name='结束时间')),
            ],
            options={
                'verbose_name': '考试',
                'verbose_name_plural': '考试',
            },
        ),
        migrations.CreateModel(
            name='ExamPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.CharField(blank=True, max_length=128, verbose_name='备注')),
                ('description', models.CharField(max_length=128, verbose_name='描述')),
            ],
            options={
                'verbose_name': '考试期次',
                'verbose_name_plural': '考试期次',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.CharField(blank=True, max_length=128, verbose_name='备注')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=16, verbose_name='性别')),
                ('phone_number', models.CharField(blank=True, max_length=32, verbose_name='电话号码')),
                ('address', models.CharField(blank=True, max_length=128, verbose_name='地址')),
            ],
            options={
                'verbose_name': '家长',
                'verbose_name_plural': '家长',
            },
        ),
        migrations.CreateModel(
            name='PeriodClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.CharField(blank=True, max_length=128, verbose_name='备注')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('grade', models.IntegerField(verbose_name='年级')),
                ('number_of_classes', models.IntegerField(default=0, verbose_name='上课次数')),
                ('start_time', models.DateField(verbose_name='开始时间')),
                ('end_time', models.DateField(verbose_name='结束时间')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='价格')),
                ('description', models.CharField(blank=True, max_length=128, verbose_name='描述')),
            ],
            options={
                'verbose_name': '班次',
                'verbose_name_plural': '班次',
            },
        ),
        migrations.CreateModel(
            name='RegisterInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.CharField(blank=True, max_length=128, verbose_name='备注')),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='已付款')),
                ('period_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galaxy.PeriodClass', verbose_name='班次')),
            ],
            options={
                'verbose_name': '报名信息',
                'verbose_name_plural': '报名信息',
            },
        ),
        migrations.CreateModel(
            name='SpreadInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.CharField(blank=True, max_length=128, verbose_name='备注')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='优惠金额')),
            ],
            options={
                'verbose_name': '推荐信息',
                'verbose_name_plural': '推荐信息',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.CharField(blank=True, max_length=128, verbose_name='备注')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('birthday', models.DateField(verbose_name='出生日期')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=16, verbose_name='性别')),
                ('school', models.CharField(blank=True, max_length=32, verbose_name='就读学校')),
                ('grade', models.IntegerField(verbose_name='年级')),
                ('phone_number', models.CharField(blank=True, max_length=32, verbose_name='电话号码')),
                ('address', models.CharField(blank=True, max_length=128, verbose_name='地址')),
                ('parent', models.ManyToManyField(to='galaxy.Parent', verbose_name='家长')),
                ('register_information', models.ManyToManyField(through='galaxy.RegisterInformation', to='galaxy.PeriodClass', verbose_name='报名信息')),
            ],
            options={
                'verbose_name': '学生',
                'verbose_name_plural': '学生',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.CharField(blank=True, max_length=128, verbose_name='备注')),
                ('name', models.CharField(max_length=16, verbose_name='名称')),
            ],
            options={
                'verbose_name': '科目',
                'verbose_name_plural': '科目',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.CharField(blank=True, max_length=128, verbose_name='备注')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=16, verbose_name='性别')),
                ('phone_number', models.CharField(blank=True, max_length=32, verbose_name='电话号码')),
                ('address', models.CharField(blank=True, max_length=128, verbose_name='地址')),
            ],
            options={
                'verbose_name': '老师',
                'verbose_name_plural': '老师',
            },
        ),
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('remark', models.CharField(blank=True, max_length=128, verbose_name='备注')),
                ('full_score', models.FloatField(default=100, verbose_name='满分')),
                ('score', models.FloatField(default=0, verbose_name='得分')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galaxy.ExamPeriod', verbose_name='考试期次')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galaxy.Student', verbose_name='学生')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galaxy.Subject', verbose_name='科目')),
            ],
            options={
                'verbose_name': '成绩单',
                'verbose_name_plural': '成绩单',
            },
        ),
        migrations.AddField(
            model_name='spreadinformation',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='galaxy.Student', verbose_name='被荐人'),
        ),
        migrations.AddField(
            model_name='spreadinformation',
            name='promoter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='promoter', to='galaxy.Student', verbose_name='推荐人'),
        ),
        migrations.AddField(
            model_name='registerinformation',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galaxy.Student', verbose_name='学生'),
        ),
        migrations.AddField(
            model_name='exam',
            name='period',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='galaxy.ExamPeriod', verbose_name='考试期次'),
        ),
        migrations.AddField(
            model_name='exam',
            name='period_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='galaxy.PeriodClass', verbose_name='班次'),
        ),
        migrations.AddField(
            model_name='exam',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='galaxy.Subject', verbose_name='科目'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='period_class',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='galaxy.PeriodClass', verbose_name='班次'),
        ),
        migrations.AddField(
            model_name='course',
            name='curriculum',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='galaxy.Curriculum', verbose_name='课表'),
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='galaxy.Subject', verbose_name='科目'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='galaxy.Teacher', verbose_name='老师'),
        ),
    ]
