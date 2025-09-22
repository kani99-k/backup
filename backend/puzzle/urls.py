from django.urls import path
from .views import PuzzlePageView, StartPuzzleView, CompletePuzzleView, SessionDetailView

urlpatterns = [
    path('puzzle/', PuzzlePageView.as_view(), name='puzzle-page'),
    path('start/', StartPuzzleView.as_view(), name='puzzle-start'),
    path('complete/', CompletePuzzleView.as_view(), name='puzzle-complete'),
    path('sessions/<int:pk>/', SessionDetailView.as_view(), name='puzzle-session-detail'),
]
