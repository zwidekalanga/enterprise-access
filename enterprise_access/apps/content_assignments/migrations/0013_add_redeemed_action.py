# Generated by Django 4.2.6 on 2023-12-12 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_assignments', '0012_assignmentaction_add_automatic_cancellation_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallearnercontentassignmentaction',
            name='action_type',
            field=models.CharField(choices=[('learner_linked', 'Learner linked to customer'), ('notified', 'Learner notified of assignment'), ('reminded', 'Learner reminded about assignment'), ('redeemed', 'Learner redeemed the assigned content'), ('cancelled', 'Learner assignment cancelled'), ('automatic_cancellation', 'Learner assignment cancelled automatically')], db_index=True, help_text='The type of action take on the related assignment record.', max_length=255),
        ),
        migrations.AlterField(
            model_name='historicallearnercontentassignmentaction',
            name='error_reason',
            field=models.CharField(blank=True, choices=[('email_error', 'Email error'), ('internal_api_error', 'Internal API error'), ('enrollment_error', 'Enrollment error')], db_index=True, help_text='The type of error that occurred during the action, if any.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='learnercontentassignmentaction',
            name='action_type',
            field=models.CharField(choices=[('learner_linked', 'Learner linked to customer'), ('notified', 'Learner notified of assignment'), ('reminded', 'Learner reminded about assignment'), ('redeemed', 'Learner redeemed the assigned content'), ('cancelled', 'Learner assignment cancelled'), ('automatic_cancellation', 'Learner assignment cancelled automatically')], db_index=True, help_text='The type of action take on the related assignment record.', max_length=255),
        ),
        migrations.AlterField(
            model_name='learnercontentassignmentaction',
            name='error_reason',
            field=models.CharField(blank=True, choices=[('email_error', 'Email error'), ('internal_api_error', 'Internal API error'), ('enrollment_error', 'Enrollment error')], db_index=True, help_text='The type of error that occurred during the action, if any.', max_length=255, null=True),
        ),
    ]