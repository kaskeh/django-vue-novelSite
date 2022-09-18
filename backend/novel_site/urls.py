from django.urls import path, re_path
# 只改变了请求token返回的，刷新token依旧保持不动
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from . import views

app_name = 'novel_site'

urlpatterns = [
    path('books_cates/', views.books_cates, name="books_cates"),
    path('<int:id>/', views.accounts, name="accounts"),
    path('aa/', views.Aa.as_view(), name="login_Aa"),
    path('register/', views.register, name="register_account"),
    path('regisToken/', views.token, name="regisToken"),
    # 验证用户并生成token
    path('login/', views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    # 刷新token
    path('loginToken/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # 获取令牌并指示它是否有效。此视图不提供关于令牌适用于特定用途的信息
    path('loginToken/verrify/', TokenVerifyView.as_view(), name='token_verrify'),
]