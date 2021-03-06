# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 09:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20171126_1244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlesource',
            options={'verbose_name': '文章来源', 'verbose_name_plural': '文章来源'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': '课程', 'verbose_name_plural': '课程'},
        ),
        migrations.AlterModelOptions(
            name='coursechapter',
            options={'verbose_name': '课程章节', 'verbose_name_plural': '课程章节'},
        ),
        migrations.AlterModelOptions(
            name='coursedetail',
            options={'verbose_name': '课程详情页内容', 'verbose_name_plural': '课程详情页内容'},
        ),
        migrations.AlterModelOptions(
            name='courseoutline',
            options={'verbose_name': '课程大纲', 'verbose_name_plural': '课程大纲'},
        ),
        migrations.AlterModelOptions(
            name='coursesection',
            options={'verbose_name': '课时目录', 'verbose_name_plural': '课时目录'},
        ),
        migrations.AlterModelOptions(
            name='degreecourse',
            options={'verbose_name': '学位课程', 'verbose_name_plural': '学位课程'},
        ),
        migrations.AlterModelOptions(
            name='degreecoursereview',
            options={'verbose_name': '学位课程评价', 'verbose_name_plural': '学位课程评价'},
        ),
        migrations.AlterModelOptions(
            name='homework',
            options={'verbose_name': '家庭作业', 'verbose_name_plural': '家庭作业'},
        ),
        migrations.AlterModelOptions(
            name='oftenaskedquestion',
            options={'verbose_name': '常见问题', 'verbose_name_plural': '常见问题'},
        ),
        migrations.AlterModelOptions(
            name='pricepolicy',
            options={'verbose_name': '价格与有课程效期表', 'verbose_name_plural': '价格与有课程效期表'},
        ),
        migrations.AlterModelOptions(
            name='scholarship',
            options={'verbose_name': '学位课程奖学金', 'verbose_name_plural': '学位课程奖学金'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': '讲师、导师表', 'verbose_name_plural': '讲师、导师表'},
        ),
        migrations.RenameField(
            model_name='coursedetail',
            old_name='recommend_courses',
            new_name='recommend_coursesy',
        ),
        migrations.AddField(
            model_name='account',
            name='balance',
            field=models.PositiveIntegerField(default=0, verbose_name='可提现余额'),
        ),
    ]
