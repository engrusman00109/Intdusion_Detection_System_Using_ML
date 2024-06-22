from django import forms
from .models import Section, CodeSnippet, ProjectOutput, Prediction


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = "__all__"


class CodeSnippetForm(forms.ModelForm):
    class Meta:
        model = CodeSnippet
        fields = "__all__"


class ProjectOutputForm(forms.ModelForm):
    class Meta:
        model = ProjectOutput
        fields = "__all__"


class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        fields = [
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
            "dttl",  # Multi-class specific field
            "ct_dst_ltm",  # Multi-class specific field
            "ct_src_ltm",  # Multi-class specific field
        ]
        widgets = {
            "state": forms.NumberInput(attrs={"type": "range", "min": 0, "max": 9}),
            "rate": forms.NumberInput(
                attrs={
                    "type": "range",
                    "min": 0,
                    "max": 111111.107200,
                    "step": 0.01,
                }
            ),
            "sttl": forms.NumberInput(attrs={"type": "range", "min": 0, "max": 255}),
            "dload": forms.NumberInput(
                attrs={"type": "range", "min": 0, "max": 22422730.0, "step": 1}
            ),
            "swin": forms.NumberInput(attrs={"type": "range", "min": 0, "max": 255}),
            "stcpb": forms.NumberInput(
                attrs={"type": "range", "min": 0, "max": 4294958913}
            ),
            "dtcpb": forms.NumberInput(
                attrs={"type": "range", "min": 0, "max": 4294881924}
            ),
            "dwin": forms.NumberInput(attrs={"type": "range", "min": 0, "max": 255}),
            "ct_srv_src": forms.NumberInput(
                attrs={"type": "range", "min": 0, "max": 63}
            ),
            "ct_state_ttl": forms.NumberInput(
                attrs={"type": "range", "min": 0, "max": 6}
            ),
            "ct_src_dport_ltm": forms.NumberInput(
                attrs={"type": "range", "min": 1, "max": 51}
            ),
            "ct_dst_sport_ltm": forms.NumberInput(
                attrs={"type": "range", "min": 1, "max": 46}
            ),
            "ct_dst_src_ltm": forms.NumberInput(
                attrs={"type": "range", "min": 1, "max": 65}
            ),
            "ct_srv_dst": forms.NumberInput(
                attrs={"type": "range", "min": 1, "max": 62}
            ),
            "dttl": forms.NumberInput(attrs={"type": "range", "min": 0, "max": 255}),
            "ct_dst_ltm": forms.NumberInput(
                attrs={"type": "range", "min": 1, "max": 51}
            ),
            "ct_src_ltm": forms.NumberInput(
                attrs={"type": "range", "min": 1, "max": 60}
            ),
        }
