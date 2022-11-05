from django.urls import path
from .views import CuotaView, AyerView

urlpatterns=[ 
    path('cuotas/', CuotaView.as_view(), name='cuota_list' ),
    path('cuotas/<int:id>', CuotaView.as_view(), name='cuotas_process' ),

    path('ayers/', AyerView.as_view(), name='ayer_list' ),
    path('ayers/<int:id>', AyerView.as_view(), name='ayer_process' ),

]