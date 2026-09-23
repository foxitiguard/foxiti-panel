# The world is a prison for the believer.
## https://www.youtube.com/watch?v=DWfNYztUM1U

from django.dispatch import Signal

## This event is fired before foxitiPanel core load the create package template, this special event is used
## to create a beautiful names official plugin. Actual package creation happes with event named preSubmitPackage and postSubmitPackage.
preCreatePacakge = Signal()

## See info for preCreatePacakge
postCreatePacakge = Signal()

## This event is fired before foxitiPanel core start creation a package.
preSubmitPackage = Signal()

## This event is fired after foxitiPanel core finished creation of a package.
postSubmitPackage = Signal()

## This event is fired before foxitiPanel core start deletion of a package.
preSubmitDelete = Signal()

## This event is fired after foxitiPanel core finished deletion of a package.
postSubmitDelete = Signal()

## This event is fired before foxitiPanel core start to modify a package.
preSaveChanges = Signal()

## This event is fired after foxitiPanel core finished modifying a package.
postSaveChanges = Signal()