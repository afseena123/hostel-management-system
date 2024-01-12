

from django.urls import path
from . import views

urlpatterns = [
   path('adminpage/',views.adminpage,name='adminpage'),
   path('get_hostel_list/', views.get_hostel_list, name='get_hostel_list'),
   path('HostelSubmission/',views.HostelSubmission,name='HostelSubmission'),
   path('AdminApproval/',views.AdminApproval,name='AdminApproval'),
   path('approve_hostel/<int:hostel_id>/', views.approve_hostel, name='approve_hostel'),
   path('view_students/', views.view_students, name='view_students'),
   path('add_student/',views.add_student,name='add_student'),
   path('edit_student/<int:student_id>',views.edit_student,name='edit_student'),
   
   path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
]



