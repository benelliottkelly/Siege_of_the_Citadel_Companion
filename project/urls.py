from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/battle_reports/', include('battle_reports.urls')),
    path('api/experience/', include('experience.urls')),
    path('api/corporations/', include('corporations.urls')),
    path('api/doomtroopers/', include('doomtroopers.urls')),
    path('api/specialist_types/', include('specialist_types.urls')),
    path('api/levels/', include('levels.urls')),
    path('api/entrance_points/', include('entrance_points.urls')),
    path('api/dark_legion/', include('dark_legion.urls')),
    path('api/events/', include('events.urls')),
    path('api/games/', include('games.urls')),
]
