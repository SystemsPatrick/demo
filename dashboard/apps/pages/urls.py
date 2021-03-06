from django.urls import path

import  dashboard.apps.pages.facebook.views as facebookViews
import  dashboard.apps.pages.instagram.views as instagramViews
import  dashboard.apps.pages.twitter.views as twitterViews
import  dashboard.apps.pages.mercadolibre.views as mercadoLibreViews
import  dashboard.apps.pages.olx.views as olxViews 
import  dashboard.apps.pages.youtube.views as youtubeViews
import dashboard.apps.pages.google.views as googleViews
 
import dashboard.apps.frontend.views as mainViews 



app_name = 'pages'


urlpatterns = [
    path('', mainViews.IndexView.as_view(), name='index'),
    path('facebook',facebookViews.IndexView.as_view(),	name='facebook'),
    path('instagram', instagramViews.IndexView.as_view(), name='instagram'),
    path('twitter', twitterViews.IndexView.as_view(), name='twitter'),
    path('mercadolibre',mercadoLibreViews.IndexView.as_view(),	name='mercadolibre'),
    path('youtube', youtubeViews.YoutubeParametros.as_view(), name='youtube'),
    path('youtube-resultados/', youtubeViews.YoutubeVideo.as_view(), name='youtube_resultados'),
    path('youtube-resultados-comentarios/', youtubeViews.YoutubeComentarios.as_view(), name='youtube_resultados_comentarios'),
    path('olx', olxViews.IndexView.as_view(), name='olx'),
    path('google', googleViews.IndexView.as_view(), name='google'),
]
