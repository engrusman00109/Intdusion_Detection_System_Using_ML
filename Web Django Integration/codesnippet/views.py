from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import CodeSnippet, ProjectOutput, Team, ResearchPaper, Section, Prediction
from django.db.models import Q
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from nbconvert import HTMLExporter
from .forms import PredictionForm
import joblib
import pandas as pd


class NotebookView(TemplateView):
    template_name = "notebook.html"
    notebook_file_path_binary = r"c:\Users\SAEED COMPUTERS\Desktop\fydp\Classification Notebooks\FYDP_Binary_Classification_NUSW-NB-15_Dataset.ipynb"
    notebook_file_path_multi = r"c:\Users\SAEED COMPUTERS\Desktop\fydp\Classification Notebooks\FYDP_Multi_Classification_NUSW-NB-15_Dataset.ipynb"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        html_exporter_binary = HTMLExporter()
        html_exporter_multi = HTMLExporter()
        (body_binary, resources) = html_exporter_binary.from_filename(
            self.notebook_file_path_binary
        )
        (body_multi, resources) = html_exporter_multi.from_filename(
            self.notebook_file_path_multi
        )

        context["html_content_binary"] = body_binary
        context["html_content_multi"] = body_multi
        return context


class CodeSnippetView(LoginRequiredMixin, TemplateView):
    template_name = "project-code.html"
    login_url = "/accounts/login/"  # Update with your login URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        snippets = CodeSnippet.objects.all()

        # Filter snippets based on search query
        query = self.request.GET.get("q")
        if query:
            snippets = snippets.filter(
                Q(title__icontains=query) | Q(section__name__icontains=query)
            )

        paginator = Paginator(snippets, 3)  # Show 3 snippets per page
        page_number = self.request.GET.get("page")

        try:
            snippets = paginator.page(page_number)
        except PageNotAnInteger:
            snippets = paginator.page(1)
        except EmptyPage:
            snippets = paginator.page(paginator.num_pages)

        context["snippets"] = snippets
        return context


class ProjectOutputListView(LoginRequiredMixin, ListView):
    model = ProjectOutput
    template_name = "project_output_list.html"  # Update with your template name
    context_object_name = "outputs"
    paginate_by = 10
    login_url = "/accounts/login/"  # Update with your login URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sections = Section.objects.all()
        section_outputs = {
            section: ProjectOutput.objects.filter(section=section)
            for section in sections
        }
        context["section_outputs"] = section_outputs
        return context


class TeamListView(LoginRequiredMixin, ListView):
    model = Team
    template_name = "team_list.html"
    context_object_name = "teams"
    login_url = "/accounts/login/"  # Update with your login URL


class ResearchPaperTemplateView(TemplateView):
    template_name = "research_paper_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["research_paper"] = get_object_or_404(ResearchPaper)
        return context


class ResearchPaperPDFView(TemplateView):

    def get(self, request, *args, **kwargs):
        research_paper = get_object_or_404(ResearchPaper)
        response = FileResponse(
            research_paper.document.open(), content_type="application/pdf"
        )
        response["Content-Disposition"] = (
            f'inline; filename="{research_paper.document.name}"'
        )
        return response


class ModelPredictionView(CreateView):
    form_class = PredictionForm
    template_name = "template/prediction_form.html"
    success_url = reverse_lazy("model_predictions")

    def form_valid(self, form):
        # Extract data from the form
        form_data = form.cleaned_data

        # Define the columns for binary and multi-class models
        binary_columns = [
            "state",
            "rate",
            "sttl",
            "dload",
            "swin",
            "stcpb",
            "dtcpb",
            "dwin",
            "ct_srv_src",
            "ct_state_ttl",
            "ct_src_dport_ltm",
            "ct_dst_sport_ltm",
            "ct_dst_src_ltm",
            "ct_srv_dst",
        ]

        multi_columns = [
            "state",
            "rate",
            "sttl",
            "dttl",
            "swin",
            "stcpb",
            "dwin",
            "ct_srv_src",
            "ct_dst_ltm",
            "ct_src_dport_ltm",
            "ct_dst_sport_ltm",
            "ct_dst_src_ltm",
            "ct_src_ltm",
            "ct_srv_dst",
        ]

        # Create DataFrames for binary and multi-class predictions
        binary_data = {col: [form_data[col]] for col in binary_columns}
        multi_data = {col: [form_data.get(col, 0)] for col in multi_columns}

        df_binary = pd.DataFrame(binary_data)
        df_multi = pd.DataFrame(multi_data)

        # List of binary model filenames
        binary_models = [
            r"c:\Users\SAEED COMPUTERS\Desktop\fydp\Classification Models\ANOVA-B-GN.pkl",
            r"c:\Users\SAEED COMPUTERS\Desktop\fydp\Classification Models\ANOVA-B-GB.pkl",
            r"c:\Users\SAEED COMPUTERS\Desktop\fydp\Classification Models\ANOVA-B-LR.pkl",
            r"c:\Users\SAEED COMPUTERS\Desktop\fydp\Classification Models\ANOVA-B-LR-L1.pkl",
            r"c:\Users\SAEED COMPUTERS\Desktop\fydp\Classification Models\ANOVA-B-LR-L2.pkl",
            r"c:\Users\SAEED COMPUTERS\Desktop\fydp\Classification Models\ANOVA-B-GB-GSCV.pkl",
        ]

        # List of multi-class model filenames
        multi_models = [
            r"c:\Users\SAEED COMPUTERS\Desktop\fydp\Classification Models\ANOVA-M-GN.pkl",
            r"c:\Users\SAEED COMPUTERS\Desktop\fydp\Classification Models\ANOVA-M-GB.pkl",
            r"c:\Users\SAEED COMPUTERS\Desktop\fydp\Classification Models\ANOVA-M-LR.pkl",
            r"c:\Users\SAEED COMPUTERS\Desktop\fydp\Classification Models\ANOVA-M-LR-L1.pkl",
            r"c:\Users\SAEED COMPUTERS\Desktop\fydp\Classification Models\ANOVA-M-LR-L2.pkl",
            r"c:\Users\SAEED COMPUTERS\Desktop\fydp\Classification Models\ANOVA-M-GB-GSCV.pkl",
        ]

        # Dictionary to store predictions from each model
        binary_predictions = {}
        multi_predictions = {}

        # Iterate over each binary model, load it, and make predictions
        for model_filename in binary_models:
            model = joblib.load(model_filename)
            prediction = model.predict(df_binary)
            binary_predictions[model_filename] = prediction[0]

        # Iterate over each multi-class model, load it, and make predictions
        for model_filename in multi_models:
            model = joblib.load(model_filename)
            prediction = model.predict(df_multi)
            multi_predictions[model_filename] = prediction[0]

        # Pass the predictions to the context
        context = self.get_context_data(
            binary_predictions=binary_predictions,
            multi_predictions=multi_predictions,
            form=form,
        )
        return self.render_to_response(context)
