# The world is a prison for the believer.

from django.dispatch import Signal

## This event is fired before foxitiPanel core load template for create backup page.
preBackupSite = Signal()

## This event is fired after foxitiPanel core load template for create backup page.
postBackupSite = Signal()

## This event is fired before foxitiPanel core load template for restore backup page.
preRestoreSite = Signal()

## This event is fired after foxitiPanel core load template for restore backup page.
postRestoreSite = Signal()

## This event is fired before foxitiPanel core start creating backup of a website
preSubmitBackupCreation = Signal()

## This event is fired before foxitiPanel core starts to load status of backup started earlier througb submitBackupCreation
preBackupStatus = Signal()

## This event is fired after foxitiPanel core has loaded backup status
postBackupStatus = Signal()

## This event is fired before foxitiPanel core start deletion of a backup
preDeleteBackup = Signal()

## This event is fired after foxitiPanel core finished the backup deletion
postDeleteBackup = Signal()

## This event is fired before foxitiPanel core start restoring a backup.
preSubmitRestore = Signal()

## This event is fired before foxitiPanel core starts to add a remote backup destination
preSubmitDestinationCreation = Signal()

## This event is fired after foxitiPanel core is finished adding remote backup destination
postSubmitDestinationCreation = Signal()

## This event is fired before foxitiPanel core starts to delete a backup destination
preDeleteDestination = Signal()

## This event is fired after foxitiPanel core finished deleting a backup destination
postDeleteDestination = Signal()

## This event is fired before foxitiPanel core start adding a backup schedule
preSubmitBackupSchedule = Signal()

## This event is fired after foxitiPanel core finished adding a backup schedule
postSubmitBackupSchedule = Signal()

## This event is fired before foxitiPanel core start the deletion of backup schedule
preScheduleDelete = Signal()

## This event is fired after foxitiPanel core finished the deletion of backup schedule
postScheduleDelete = Signal()

## This event is fired before foxitiPanel core star the remote backup process
preSubmitRemoteBackups = Signal()

## This event is fired after foxitiPanel core finished remote backup process
postSubmitRemoteBackups = Signal()

## This event is fired before foxitiPanel core star the remote backup process
preStarRemoteTransfer = Signal()

## This event is fired after foxitiPanel core finished remote backup process
postStarRemoteTransfer = Signal()

## This event is fired before foxitiPanel core start restore of remote backups
preRemoteBackupRestore = Signal()

## This event is fired after foxitiPanel core finished restoring remote backups in local server
postRemoteBackupRestore = Signal()
