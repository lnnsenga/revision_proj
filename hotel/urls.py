from django.urls import path

from .import views


urlpatterns = [
    path('', views.homepage, name = "index"),
    path('login',views.user_login,name="login"),
    path('rooms',views.list_room,name="rooms"),
    path('rooms/<uuid:room_id>',views.single_room,name="single room"),
    path('rooms/<uuid:room_id>/booking',views.book_room,name="book room"),
    path('rooms/<uuid:room_id>/booking/payment',views.pay_for_booking,name="pay booking"),
    path('rooms/<uuid:room_id>/checkin',views.checkin_room,name="checkin"),
    path('rooms/<uuid:room_id>/checkout',views.checkout_room,name="checkout"),
    
    path('customer-dashboard',views.customer_dashboard,name="customer-dashboard"),
    path('admin-dashboard',views.admin_dashboard,name="admin-dashboard"),
    path('admin',views.list_admin,name="list admin"),
    path('admin/create',views.create_admin,name="create admin"),
    path('admin/<uuid:staff_id>',views.show_admin,name="show admin"),
    path('admin/<uuid:staff_id>/edit',views.edit_admin,name="edit admin"),
    path('admin/<uuid:staff_id>/delete',views.delete_admin,name="delete admin"),
    path('admin/logs',views.logs,name="logs"),
    
    
    
    
    
    

    
    
    
    
  
    
]