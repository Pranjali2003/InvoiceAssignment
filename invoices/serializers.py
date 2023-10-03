from rest_framework import serializers

from invoices.models import Invoice,InvoiceDetail

class InvoiceSerializer(serializers.Serializer):
    class Meta:
        model = Invoice
        fields = '__all__'
        

class InvoiceDetail(serializers.Serializer):
    class Meta:
        model = InvoiceDetail
        fields = '__all__'
    