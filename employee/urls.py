from rest_framework.routers import DefaultRouter
from employee.views import CompanyViewSet, EmployeeViewSet

router = DefaultRouter()
router.register('companies', CompanyViewSet)
router.register('employees', EmployeeViewSet)

urlpatterns = router.urls