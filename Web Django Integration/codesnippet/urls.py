from django.urls import path
from .views import (
    CodeSnippetView,
    ProjectOutputListView,
    TeamListView,
    ResearchPaperPDFView,
    ResearchPaperTemplateView,
    NotebookView,
    ModelPredictionView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("project-code/", CodeSnippetView.as_view(), name="project-code"),
    path(
        "project-outputs/", ProjectOutputListView.as_view(), name="project_output_list"
    ),
    path("teams/", TeamListView.as_view(), name="team_members"),
    path(
        "research_paper/",
        ResearchPaperTemplateView.as_view(),
        name="research_paper_detail",
    ),
    path(
        "research_paper/pdf/", ResearchPaperPDFView.as_view(), name="research_paper_pdf"
    ),
    path("notebook/", NotebookView.as_view(), name="notebook_view"),
    path("predictions/", ModelPredictionView.as_view(), name="model_predictions"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
