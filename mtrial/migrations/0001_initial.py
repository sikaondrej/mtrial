# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subject'
        db.create_table('mtrial_subject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url_key', self.gf('django.db.models.fields.SlugField')(max_length=8)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal('mtrial', ['Subject'])

        # Adding model 'Category'
        db.create_table('mtrial_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url_key', self.gf('django.db.models.fields.SlugField')(max_length=8)),
            ('parrent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mtrial.Category'], null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal('mtrial', ['Category'])

        # Adding model 'Example'
        db.create_table('mtrial_example', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mtrial.Category'])),
            ('entering', self.gf('django.db.models.fields.TextField')()),
            ('procedure', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('result', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('mtrial', ['Example'])


    def backwards(self, orm):
        # Deleting model 'Subject'
        db.delete_table('mtrial_subject')

        # Deleting model 'Category'
        db.delete_table('mtrial_category')

        # Deleting model 'Example'
        db.delete_table('mtrial_example')


    models = {
        'mtrial.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'parrent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mtrial.Category']", 'null': 'True', 'blank': 'True'}),
            'url_key': ('django.db.models.fields.SlugField', [], {'max_length': '8'})
        },
        'mtrial.example': {
            'Meta': {'object_name': 'Example'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mtrial.Category']"}),
            'entering': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'procedure': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'result': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'mtrial.subject': {
            'Meta': {'object_name': 'Subject'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'url_key': ('django.db.models.fields.SlugField', [], {'max_length': '8'})
        }
    }

    complete_apps = ['mtrial']