from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("api/get_customer_locations", views.get_customer_locations),
    path("api/delete_customer_locations", views.delete_customer_locations),
    path("api/add_modify_locations", views.add_or_modify_location),
    path("api/get_delivery_agent_orders/", views.get_delivery_agent_orders),
    # Use custom login view instead of the default one
    path("login/", views.CustomLoginView.as_view(), name="login"),
    # Include other auth URLs (logout, password reset, etc.)
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("signup/", views.sign_up, name="signup"),
    path("customer/", views.customer, name="Customer Page"),
]
