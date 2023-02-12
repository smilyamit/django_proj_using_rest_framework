from django.urls import path, include
from . import views
from . import genericViews
from api_app.rf_views.rf_fun_views import blog_view
from api_app.rf_views.rf_cls_views import BlogAPIView
from api_app.rf_views.rf_generic_api_views import BlogPostListCreateApiView, BlogPostRetrieveUpdateDestroyAPIView
from api_app.rf_views.rf_viewsets_api_views import BlogViewSets, BlogModelViewSets
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('rf_modelviewsets', BlogModelViewSets)

#for BlogViewSets,
blog_list = BlogViewSets.as_view(
    {'get': 'list'}
)

blog_detail = BlogViewSets.as_view(
    {'get': 'retrieve'}
)

#for BlogModelViewSets  # alternative methods
# blog_list_models = BlogModelViewSets.as_view(
#     {'get': 'list'}
# )
#
# blog_detail_models = BlogModelViewSets.as_view(
#     {'get': 'retrieve'}
# )


# rf => rest framework
urlpatterns = [
    path('', views.index, name='index'),
    # path('car_name/<int:pk>/', views.add_car, name='car_name'),
    path('car_name/', views.add_car, name='car_name'),
    path('car_class/', views.CarView.as_view()),
    path('bike_list/', genericViews.BikeListView.as_view(), name="bike_related"),

    #From here all below path are for rest_framework
    path('motor_bike_list/', genericViews.MotorBikeListView.as_view(), name="motor_bike_related"),

    path('rf_fn_blog_post/', blog_view, name='rf_fn_blog_view'),

    path('rf_cls_blog_post/', BlogAPIView.as_view()),

    path('rf_generics/', BlogPostListCreateApiView.as_view()),
    path('rf_generics/<int:pk>/', BlogPostRetrieveUpdateDestroyAPIView.as_view()),

    path('rf_viewsets/', blog_list, name="blog-list"),
    path('rf_viewsets/<int:pk>/', blog_detail, name="blog-details"),

    # path('rf_modelviewsets/', blog_list_models, name="blog-list-models"),
    # path('rf_modelviewsets/<int:pk>/', blog_detail_models, name="blog-details-models"),

    path('api/', include(router.urls)),
]
