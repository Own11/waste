from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
# pyrefly: ignore [missing-import]
from rest_framework_simplejwt.views import TokenRefreshView
from api import views

urlpatterns = [
    # Serve index.html template from root URL
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('admin/', admin.site.urls),
    
    # Auth endpoints
    path('api/auth/login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Shared resource endpoints (available to all authenticated users)
    path('api/products/', views.ProductsListView.as_view(), name='products_list'),
    path('api/branches/', views.BranchesListView.as_view(), name='branches_list'),
    
    # Worker endpoints
    path('api/worker/profile/', views.WorkerProfileView.as_view(), name='worker_profile'),
    path('api/worker/write-off/scan/', views.WorkerScanView.as_view(), name='worker_write_off_scan'),
    path('api/worker/write-off/create/', views.WorkerWriteOffCreateView.as_view(), name='worker_write_off_create'),
    
    # Manager endpoints
    path('api/manager/requests/', views.ManagerRequestsListView.as_view(), name='manager_requests'),
    path('api/manager/requests/<int:pk>/review/', views.ManagerReviewView.as_view(), name='manager_review'),
    path('api/manager/supply/check/', views.ManagerSupplyCheckView.as_view(), name='manager_supply_check'),
    path('api/manager/suppliers/', views.ManagerSuppliersListView.as_view(), name='manager_suppliers'),
    
    # Analytics / Executive endpoints
    path('api/analytics/dashboard/', views.AnalyticsDashboardView.as_view(), name='analytics_dashboard'),
    path('api/analytics/heatmap/', views.AnalyticsHeatmapView.as_view(), name='analytics_heatmap'),
    path('api/analytics/export/google-sheets/', views.AnalyticsExportSheetsView.as_view(), name='analytics_export_sheets'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
