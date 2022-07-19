from django.urls import path
from . import views


urlpatterns = [
    path('',views.OrderCreateListView.as_view(),name="orders_creations"),
    path('<int:order_id>/',views.OrderDetailView.as_view(),name="orderdetails"),
    path('update-status/<int:order_id>/',views.UpdatedOrderStatus.as_view(),name="UdpateOrderStatus"),
    path('user/<int:user_id>/orders',views.UserOrderView.as_view(),name="UsersOrder"),
    path('user/<int:user_id>/orders/<int:order_id>',views.UserOrderDetailView.as_view(),name="UserOrderDetailView"),
]
