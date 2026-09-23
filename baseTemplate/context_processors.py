# -*- coding: utf-8 -*-
from foxitipanel_version import BUILD, FULL_VERSION, VERSION

def version_context(request):
    """Add version information to all templates"""
    return {
        'FOXITIPANEL_VERSION': VERSION,
        'FOXITIPANEL_BUILD': BUILD,
        'FOXITIPANEL_FULL_VERSION': FULL_VERSION
    }

def cosmetic_context(request):
    """Add cosmetic data (custom CSS) to all templates"""
    try:
        from .models import foxitiPanelCosmetic
        cosmetic = foxitiPanelCosmetic.objects.get(pk=1)
        return {
            'cosmetic': cosmetic
        }
    except:
        from .models import foxitiPanelCosmetic
        cosmetic = foxitiPanelCosmetic()
        cosmetic.save()
        return {
            'cosmetic': cosmetic
        }
