import time

import django_filters
from celery.result import AsyncResult
from django.db import IntegrityError
from django.db.models.aggregates import Count
from django.db.models.fields import IntegerField
from django.db.models.functions import Cast
from django.utils import timezone
from rest_framework import viewsets, mixins, serializers
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from store.models import Seller, ProductVariant, Brand
from store.models.sales import Sales
from store.serializers import AnalyticsSerializer, AnalyticsSalesSerializer, SellerSerializer, AnalyticsChartSerializer, \
    ProductVariantSerializer, ProductBrandSerializer, TaskResult
from django.db.models import Sum, F, When, Value, Case

