from tastypie.resources import ModelResource
from api.models import prescriber, overdoses, docdrugqty, dangerscore

class PrescriberResource(ModelResource):
    class Meta:
        queryset = prescriber.objects.all()
        resource_name = 'prescriber'

class OverdosesResource(ModelResource):
    class Meta:
        queryset = overdoses.objects.all()
        resource_name = 'overdoses'

class DocDrugQtyResource(ModelResource):
    class Meta:
        queryset = docdrugqty.objects.all()
        resource_name = 'docdrugqty'

class DangerScoreResource(ModelResource):
    class Meta:
        queryset = dangerscore.objects.all()
        resource_name = 'dangerscore'