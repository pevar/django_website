# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BusinessUnit'
        db.create_table(u'business_unit_businessunit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('slug', self.gf('pleiadi.base.fields.AutoSlugField')(max_length=50, blank=True)),
            ('code', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('pleiadi.base.fields.HtmlTextField')()),
        ))
        db.send_create_signal(u'business_unit', ['BusinessUnit'])


    def backwards(self, orm):
        # Deleting model 'BusinessUnit'
        db.delete_table(u'business_unit_businessunit')


    models = {
        u'business_unit.businessunit': {
            'Meta': {'object_name': 'BusinessUnit'},
            'code': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'description': ('pleiadi.base.fields.HtmlTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('pleiadi.base.fields.AutoSlugField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['business_unit']