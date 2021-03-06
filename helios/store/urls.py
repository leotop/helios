# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.views.generic import TemplateView, ListView
from helios.store.models import Product, ProductImage
from helios.conf import settings
from helios.store.views import CollectionList, ProductDetail, ProductList


urlpatterns = patterns('helios.store.views',
    (r'^cart/clear/$', 'cart_clear'),
    (r'^cart/debug/$', 'cart_debug'),

    url(r'^cart/set/(?P<product_id>\d+)/$',
        'cart_set_quantity',
        name='store_cart_set_quantity'),
    url(r'^checkout/$',
        'checkout',
        name='store_checkout'),
    url(r'^success/$', 'success',
        name='store_success'),
    #url(r'^submit-order/$',
        #'submit_order',
        #name='store_submit_order'),
    url(r'^products/(?P<slug>[-\w]+)/add/$',
        'product_add',
        name='store_product_add'),
    url(r'^products/(?P<slug>[-\w]+)/remove/$',
        'product_remove',
        name='store_product_remove'),
    url(r'^unshippable/$',
        'unshippable',
        name='store_unshippable'),
)

urlpatterns += patterns('',
    url(r'^cart/$',
        TemplateView.as_view(
            template_name='cart.html'
        ),
        name='store_cart'
    ),
    url(r'^products/(?P<slug>[-\w]+)/$',
        ProductDetail.as_view(),
        name='store_product_detail'
    ),
    url(r'^products/$',
        ListView.as_view(
            queryset=Product.objects.filter(is_active__exact=True),
            context_object_name='product_list'
        ),
        name='store_product_list'
    ),
    url(r'^collections/(?P<collection>[-\w]+)/$',
        CollectionList.as_view(),
        name='store_collection_list'
    ),
    url(r'^(?P<category>[-\w]+)/$',
        ProductList.as_view(),
        name='store_category_list'
    ),
)
