# Generated by Django 2.1.2 on 2018-12-28 10:29

from django.db import migrations, models
import django.db.models.deletion


def updateTransactions(apps, schema_editor):
    Transaction = apps.get_model('silverstrike', 'Transaction')
    db_alias = schema_editor.connection.alias
    for t in Transaction.objects.using(db_alias).all():
        if t.transaction_type == 1:
            # deposit
            for s in t.splits.filter(amount__gt=0):
                t.amount += s.amount
                t.src = s.opposing_account
                t.dst = s.account
        elif t.transaction_type == 2:
            # withdraw
            for s in t.splits.filter(amount__gt=0):
                t.amount += s.amount
                t.src = s.opposing_account
                t.dst = s.account
        elif t.transaction_type == 3:
            # transfer
            for s in t.splits.filter(amount__gt=0):
                t.amount += s.amount
                t.src = s.opposing_account
                t.dst = s.account
        elif t.transaction_type == 4:
            # system/reconcile
            for s in t.splits.filter(amount__gt=0):
                t.amount += s.amount
                t.src = s.opposing_account
                t.dst = s.account
        t.save()


class Migration(migrations.Migration):

    dependencies = [
        ('silverstrike', '0005_auto_20180929_1451'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='transaction',
            name='dst',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='credits', to='silverstrike.Account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='src',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='debits', to='silverstrike.Account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(default=0, decimal_places=2, max_digits=10),
        ),
        migrations.RunPython(
            updateTransactions
        )
    ]
