# Generated by Django 1.11.29 on 2021-07-07 19:03

from django.db import migrations

import sentry.db.models.fields.bounded


class Migration(migrations.Migration):
    # This flag is used to mark that a migration shouldn't be automatically run in
    # production. We set this to True for operations that we think are risky and want
    # someone from ops to run manually and monitor.
    # General advice is that if in doubt, mark your migration as `is_dangerous`.
    # Some things you should always mark as dangerous:
    # - Large data migrations. Typically we want these to be run manually by ops so that
    #   they can be monitored. Since data migrations will now hold a transaction open
    #   this is even more important.
    # - Adding columns to highly active tables, even ones that are NULL.
    is_dangerous = False

    # This flag is used to decide whether to run this migration in a transaction or not.
    # By default we prefer to run in a transaction, but for migrations where you want
    # to `CREATE INDEX CONCURRENTLY` this needs to be set to False. Typically you'll
    # want to create an index concurrently when adding one to an existing table.
    # You'll also usually want to set this to `False` if you're writing a data
    # migration, since we don't want the entire migration to run in one long-running
    # transaction.
    atomic = True

    dependencies = [
        ("sentry", "0218_releasefile_remove_fks"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.RemoveField(
                    model_name="exporteddata",
                    name="file",
                ),
                migrations.AddField(
                    model_name="exporteddata",
                    name="file_id",
                    field=sentry.db.models.fields.bounded.BoundedBigIntegerField(null=True),
                ),
                migrations.AddField(
                    model_name="exporteddatablob",
                    name="blob_id",
                    field=sentry.db.models.fields.bounded.BoundedBigIntegerField(default=0),
                    preserve_default=False,
                ),
                migrations.RemoveField(
                    model_name="exporteddatablob",
                    name="blob",
                ),
                migrations.AlterUniqueTogether(
                    name="exporteddatablob",
                    unique_together={("data_export", "blob_id", "offset")},
                ),
            ],
        )
    ]
