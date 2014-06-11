# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from base.form_utils import RequiredFieldForm

from .models import (
    Product,
    ProductBundle,
)


class BundleForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(BundleForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'pure-input-2-3'}
        )

    class Meta:
        model = ProductBundle
        fields = (
            'name',
            'slug',
            'product',
            'price',
        )


class ProductForm(RequiredFieldForm):

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for name in ('name', 'description'):
            self.fields[name].widget.attrs.update(
                {'class': 'pure-input-2-3'}
            )

    class Meta:
        model = Product
        fields = (
            'name',
            'slug',
            'category',
            'description',
            'price',
            'legacy',
        )
