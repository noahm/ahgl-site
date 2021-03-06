# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Game.home_race'
        db.delete_column('tournaments_game', 'home_race')

        # Deleting field 'Game.away_race'
        db.delete_column('tournaments_game', 'away_race')

        # Adding M2M table for field home_race on 'Game'
        db.create_table('tournaments_game_home_race', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game', models.ForeignKey(orm['tournaments.game'], null=False)),
            ('character', models.ForeignKey(orm['api.character'], null=False))
        ))
        db.create_unique('tournaments_game_home_race', ['game_id', 'character_id'])

        # Adding M2M table for field away_race on 'Game'
        db.create_table('tournaments_game_away_race', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('game', models.ForeignKey(orm['tournaments.game'], null=False)),
            ('character', models.ForeignKey(orm['api.character'], null=False))
        ))
        db.create_unique('tournaments_game_away_race', ['game_id', 'character_id'])


    def backwards(self, orm):
        # Adding field 'Game.home_race'
        db.add_column('tournaments_game', 'home_race',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1, blank=True),
                      keep_default=False)

        # Adding field 'Game.away_race'
        db.add_column('tournaments_game', 'away_race',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1, blank=True),
                      keep_default=False)

        # Removing M2M table for field home_race on 'Game'
        db.delete_table('tournaments_game_home_race')

        # Removing M2M table for field away_race on 'Game'
        db.delete_table('tournaments_game_away_race')


    models = {
        'api.character': {
            'Meta': {'object_name': 'Character'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'options'", 'to': "orm['api.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'api.game': {
            'Meta': {'object_name': 'Game'},
            'article_section_image_url': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'away_character_diplay_name': ('django.db.models.fields.CharField', [], {'default': "'Away Race'", 'max_length': '2048'}),
            'background_match_image_url': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'character_number': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'header_image_glow_hex_color': ('api.fields.ColourField', [], {'max_length': '7'}),
            'header_image_url': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'home_character_diplay_name': ('django.db.models.fields.CharField', [], {'default': "'Home Race'", 'max_length': '2048'}),
            'icon_image_url': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'live_stream_section_image_url': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'match_section_image_url': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'questions': ('profiles.fields.HTMLField', [], {'default': "'<ol><li>\\n<p>Why did you choose this race/champion?</p>\\n<p>-</p>\\n</li>\\n<li>\\n<p>What do you do for a living?  What do you love about your job?</p>\\n<p>-</p>\\n</li>\\n<li>\\n<p>What other hobbies do you have?</p>\\n<p>-</p>\\n</li>\\n<li>\\n<p>Why do you play StarCraft/League of Legends?</p>\\n<p>-</p>\\n</li>\\n<li>\\n<p>How long have you been playing?</p>\\n<p>-</p>\\n</li>\\n<li>\\n<p>What have you done to prepare for the momentous challenge that is the AHGL Tournament?</p>\\n<p>-</p>\\n</li>\\n<li>\\n<p>Why is your team going to win?</p>\\n<p>-</p>\\n</li>\\n<li>\\n<p>Who is the best player on your team?  Why?</p>\\n<p>-</p>\\n</li>\\n<li>\\n<p>Whom do you fear most amongst the competition and why?</p>\\n<p>-</p>\\n</li>\\n</ol>'", 'attributes': "{'blockquote': ['cite'], 'th': ['colspan'], 'table': ['class'], 'td': ['colspan'], 'a': ['href', 'rel', 'target', 'title', 'data-toggle', 'class'], 'span': ['class'], 'img': ['src', 'alt', 'title', 'style'], 'ul': ['class'], 'li': ['class'], 'q': ['cite'], 'p': ['style'], 'iframe': ['src', 'width', 'height', 'frameborder', 'allowfullscreen'], 'div': ['class', 'id', 'style']}", 'blank': 'True', 'tags': "['ol', 'ul', 'li', 'strong', 'em', 'p']"}),
            'small_game_thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '2048'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 6, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'profiles.charity': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Charity'},
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'logo': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'profiles.profile': {
            'Meta': {'object_name': 'Profile'},
            'autosubscribe': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'avatar': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'custom_thumb': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'en'", 'max_length': '10', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'photo': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'post_count': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'show_signatures': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'signature': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'blank': 'True'}),
            'signature_html': ('django.db.models.fields.TextField', [], {'max_length': '1054', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'time_zone': ('django.db.models.fields.FloatField', [], {'default': '3.0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profile'", 'to': "orm['auth.User']"}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'profiles.team': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('name', 'tournament'), ('slug', 'tournament'))", 'object_name': 'Team'},
            'approval': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'charity': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'teams'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['profiles.Charity']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'karma': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'losses': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'teams'", 'to': "orm['profiles.Profile']", 'through': "orm['profiles.TeamMembership']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'motto': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'photo': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'seed': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'R'", 'max_length': '1'}),
            'tiebreaker': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teams'", 'to': "orm['tournaments.Tournament']"}),
            'wins': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'profiles.teammembership': {
            'Meta': {'ordering': "('-active', '-captain', 'char_name')", 'unique_together': "(('team', 'profile'),)", 'object_name': 'TeamMembership', 'db_table': "'profiles_team_members'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'captain': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'champion': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'char_code': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'char_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'game_profile': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team_membership'", 'to': "orm['profiles.Profile']"}),
            'questions_answers': ('profiles.fields.HTMLField', [], {'attributes': "{'blockquote': ['cite'], 'th': ['colspan'], 'table': ['class'], 'td': ['colspan'], 'a': ['href', 'rel', 'target', 'title', 'data-toggle', 'class'], 'span': ['class'], 'img': ['src', 'alt', 'title', 'style'], 'ul': ['class'], 'li': ['class'], 'q': ['cite'], 'p': ['style'], 'iframe': ['src', 'width', 'height', 'frameborder', 'allowfullscreen'], 'div': ['class', 'id', 'style']}", 'blank': 'True', 'tags': "['ol', 'ul', 'li', 'strong', 'em', 'p']"}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '1'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team_membership'", 'to': "orm['profiles.Team']"})
        },
        'tournaments.article': {
            'Meta': {'object_name': 'Article'},
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publish_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'summary': ('tinymce.models.HTMLField', [], {'max_length': '4000', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'tournaments': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'articles'", 'symmetrical': 'False', 'to': "orm['tournaments.Tournament']"})
        },
        'tournaments.articlepluginmodel': {
            'Meta': {'object_name': 'ArticlePluginModel', 'db_table': "'cmsplugin_articlepluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cms_plugin'", 'unique': 'True', 'to': "orm['tournaments.Article']"}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        },
        'tournaments.game': {
            'Meta': {'ordering': "('order',)", 'unique_together': "(('order', 'match'),)", 'object_name': 'Game'},
            'away_player': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'away_games'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['profiles.TeamMembership']"}),
            'away_race': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'match_away_games'", 'blank': 'True', 'to': "orm['api.Character']"}),
            'forfeit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'home_player': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'home_games'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['profiles.TeamMembership']"}),
            'home_race': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'match_home_games'", 'blank': 'True', 'to': "orm['api.Character']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ace': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'loser': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'game_losses'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['profiles.TeamMembership']"}),
            'loser_team': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'game_losses'", 'null': 'True', 'to': "orm['profiles.Team']"}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournaments.Map']"}),
            'match': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'games'", 'to': "orm['tournaments.Match']"}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'replay': ('django.db.models.fields.files.FileField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'victory_screen': ('django.db.models.fields.files.ImageField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'vod': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'game_wins'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': "orm['profiles.TeamMembership']"}),
            'winner_team': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'game_wins'", 'null': 'True', 'to': "orm['profiles.Team']"})
        },
        'tournaments.gamepluginmodel': {
            'Meta': {'object_name': 'GamePluginModel', 'db_table': "'cmsplugin_gamepluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournaments.Game']", 'null': 'True', 'blank': 'True'}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournaments.Tournament']"})
        },
        'tournaments.map': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Map'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'photo': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'tournaments.match': {
            'Meta': {'object_name': 'Match'},
            'away_submission_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'away_submitted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'away_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'away_matches'", 'to': "orm['profiles.Team']"}),
            'creation_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'home_submission_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'home_submitted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'home_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home_matches'", 'to': "orm['profiles.Team']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loser': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'match_losses'", 'null': 'True', 'to': "orm['profiles.Team']"}),
            'publish_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'referee': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.Profile']", 'null': 'True', 'blank': 'True'}),
            'structure': ('django.db.models.fields.CharField', [], {'default': "'I'", 'max_length': '1'}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'matches'", 'to': "orm['tournaments.Tournament']"}),
            'tournament_round': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'matches'", 'to': "orm['tournaments.TournamentRound']"}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'match_wins'", 'null': 'True', 'to': "orm['profiles.Team']"})
        },
        'tournaments.tournament': {
            'Meta': {'object_name': 'Tournament'},
            'game': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['api.Game']", 'unique': 'True', 'null': 'True'}),
            'games_per_match': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '5'}),
            'map_pool': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['tournaments.Map']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1', 'db_index': 'True'}),
            'structure': ('django.db.models.fields.CharField', [], {'default': "'I'", 'max_length': '1'})
        },
        'tournaments.tournamentpluginmodel': {
            'Meta': {'object_name': 'TournamentPluginModel', 'db_table': "'cmsplugin_tournamentpluginmodel'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tournaments.Tournament']"})
        },
        'tournaments.tournamentround': {
            'Meta': {'ordering': "('-stage_order', 'order')", 'object_name': 'TournamentRound'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stage_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'stage_order': ('django.db.models.fields.IntegerField', [], {}),
            'structure': ('django.db.models.fields.CharField', [], {'default': "'G'", 'max_length': '1'}),
            'teams': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'rounds'", 'symmetrical': 'False', 'to': "orm['profiles.Team']"}),
            'tournament': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rounds'", 'to': "orm['tournaments.Tournament']"})
        }
    }

    complete_apps = ['tournaments']