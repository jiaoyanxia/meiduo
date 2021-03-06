from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from .view.admin_views import AdminView, AdminSimpleAPIView
from .view.count_views import UserDailyActiveCountView, \
    UserDailyOrderCountView, UserDayCountView, UserMonthCountView
from .view.group_views import GroupView, GroupAddView
from .view.permission_view import PermissionView, ContentTypeView
from .view.sku_view import SKUModelViewSet, SKUCategoriesView, GoodsSimpleView, GoodsSpecView
from .view.user_view import UserListView
from .view.image_view import ImageView, SKUView

urlpatterns = [
    # 用于返回 token
    path('authorizations/', obtain_jwt_token),
    # 用于返回 当日活跃人数
    path('statistical/day_active/', UserDailyActiveCountView.as_view()),
    # 用于返回 当日下单人数
    path('statistical/day_orders/', UserDailyOrderCountView.as_view()),
    # 用于返回 当日新增人数
    path('statistical/day_increment/', UserDayCountView.as_view()),
    # 用于返回 当月新增人数
    path('statistical/month_increment/', UserMonthCountView.as_view()),
    # 用于返回 用户总人数
    path('users/', UserListView.as_view()),
    # 用于返回SPU表名称数据
    path('skus/simple/', SKUView.as_view()),
    # 用于获取所有三级类别数据
    path('skus/categories/', SKUCategoriesView.as_view()),
    # 用于获取简单的SPU数据
    path('goods/simple/', GoodsSimpleView.as_view()),
    # 用于获取规格
    path('goods/<int:pk>/specs/', GoodsSpecView.as_view()),
    # 保存用户权限
    path('permission/content_types/', ContentTypeView.as_view()),
    # 新增用户组数据
    path('permission/simple/', GroupAddView.as_view()),
    # 获取分组表数据
    path('permission/groups/simple/', AdminSimpleAPIView.as_view()),
]

# ----- 使用默认实例
router = DefaultRouter()
# ----- 注册路由
router.register(r'skus/images', ImageView, basename='imagesku')
# 获取所有SKU数据
router.register(r'skus', SKUModelViewSet, basename='SKU')
# 获取权限数据
router.register(r'permission/perms', PermissionView, basename='Permission')
# 获取用户组数据
router.register(r'permission/groups', GroupView, basename='Group')
# 获取管理员用户列表数据
router.register(r'permission/admins', AdminView, basename='Admin')

# ----- 追加到 urlpatterns 中
urlpatterns += router.urls
