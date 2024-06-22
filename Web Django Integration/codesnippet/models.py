from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=200)  # Corrected 'max_lenght' to 'max_length'

    def __str__(self):
        return self.name


class CodeSnippet(models.Model):
    title = models.CharField(max_length=100)
    code = models.TextField()
    explanation = models.TextField()
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE
    )  # Added correct ForeignKey argument

    def __str__(self):
        return self.title


class ProjectOutput(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    output_name = models.CharField(max_length=100)
    output_image = models.ImageField(upload_to="project_images/")
    output_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.output_name


class Supervisor(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="supervisor_images/")
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="student_images/")
    roll_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Team(models.Model):
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    student1 = models.ForeignKey(
        Student, related_name="student1", on_delete=models.CASCADE
    )
    student2 = models.ForeignKey(
        Student, related_name="student2", on_delete=models.CASCADE
    )
    student3 = models.ForeignKey(
        Student, related_name="student3", on_delete=models.CASCADE, null=True
    )
    project_title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"Team {self.project_title}"


class ResearchPaper(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    publication_date = models.DateField()
    authors = models.ManyToManyField(Student, related_name="authored_papers")
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    document = models.FileField(upload_to="research_papers/")

    def __str__(self):
        return self.title


"state", "rate", "sttl", "dload", "swin",
"stcpb", "dtcpb", "dwin", "ct_srv_src",
"ct_state_ttl", "ct_src_dport_ltm", "ct_dst_sport_ltm",
"ct_dst_src_ltm", "ct_srv_dst"


class Prediction(models.Model):
    # Common fields for both binary and multi-class classification
    state = models.IntegerField(null=True, blank=True, default=0)
    rate = models.FloatField(null=True, blank=True, default=0.0)
    sttl = models.IntegerField(null=True, blank=True, default=0)
    swin = models.IntegerField(null=True, blank=True, default=0)
    stcpb = models.BigIntegerField(null=True, blank=True, default=0)
    dtcpb = models.BigIntegerField(null=True, blank=True, default=0)
    dwin = models.IntegerField(null=True, blank=True, default=0)
    ct_srv_src = models.IntegerField(null=True, blank=True, default=0)
    ct_src_dport_ltm = models.IntegerField(null=True, blank=True, default=0)
    ct_dst_sport_ltm = models.IntegerField(null=True, blank=True, default=0)
    ct_dst_src_ltm = models.IntegerField(null=True, blank=True, default=0)
    ct_srv_dst = models.IntegerField(null=True, blank=True, default=0)

    # Multi-class classification fields
    ct_state_ttl = models.IntegerField(null=True, blank=True, default=0)
    ct_dst_ltm = models.IntegerField(null=True, blank=True, default=0)
    ct_src_ltm = models.IntegerField(null=True, blank=True, default=0)

    # Fields to store model predictions
    prediction_gn_binary = models.FloatField(null=True, blank=True, default=0.0)
    prediction_gn_multiclass = models.FloatField(null=True, blank=True, default=0.0)
    prediction_gb_binary = models.FloatField(null=True, blank=True, default=0.0)
    prediction_gb_multiclass = models.FloatField(null=True, blank=True, default=0.0)
    prediction_lr_binary = models.FloatField(null=True, blank=True, default=0.0)
    prediction_lr_multiclass = models.FloatField(null=True, blank=True, default=0.0)
    prediction_lr_l1_binary = models.FloatField(null=True, blank=True, default=0.0)
    prediction_lr_l1_multiclass = models.FloatField(null=True, blank=True, default=0.0)
    prediction_lr_l2_binary = models.FloatField(null=True, blank=True, default=0.0)
    prediction_lr_l2_multiclass = models.FloatField(null=True, blank=True, default=0.0)
    prediction_gb_gscv_binary = models.FloatField(null=True, blank=True, default=0.0)
    prediction_gb_gscv_multiclass = models.FloatField(
        null=True, blank=True, default=0.0
    )

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Prediction {self.id}"


class Prediction(models.Model):
    # Common fields for both binary and multi-class classification
    state = models.IntegerField(null=True, blank=True, default=0)
    rate = models.FloatField(null=True, blank=True, default=0.0)
    sttl = models.IntegerField(null=True, blank=True, default=0)
    dload = models.FloatField(null=True, blank=True, default=0.0)
    swin = models.IntegerField(null=True, blank=True, default=0)
    stcpb = models.BigIntegerField(null=True, blank=True, default=0)
    dtcpb = models.BigIntegerField(null=True, blank=True, default=0)
    dwin = models.IntegerField(null=True, blank=True, default=0)
    ct_srv_src = models.IntegerField(null=True, blank=True, default=0)
    ct_state_ttl = models.IntegerField(null=True, blank=True, default=0)
    ct_src_dport_ltm = models.IntegerField(null=True, blank=True, default=0)
    ct_dst_sport_ltm = models.IntegerField(null=True, blank=True, default=0)
    ct_dst_src_ltm = models.IntegerField(null=True, blank=True, default=0)
    ct_srv_dst = models.IntegerField(null=True, blank=True, default=0)

    # Fields for multi-class classification
    dttl = models.IntegerField(null=True, blank=True, default=0)
    ct_dst_ltm = models.IntegerField(null=True, blank=True, default=0)
    ct_src_ltm = models.IntegerField(null=True, blank=True, default=0)

    # Fields to store model predictions
    prediction_gn_binary = models.FloatField(null=True, blank=True, default=0.0)
    prediction_gn_multiclass = models.FloatField(null=True, blank=True, default=0.0)
    prediction_gb_binary = models.FloatField(null=True, blank=True, default=0.0)
    prediction_gb_multiclass = models.FloatField(null=True, blank=True, default=0.0)
    prediction_lr_binary = models.FloatField(null=True, blank=True, default=0.0)
    prediction_lr_multiclass = models.FloatField(null=True, blank=True, default=0.0)
    prediction_lr_l1_binary = models.FloatField(null=True, blank=True, default=0.0)
    prediction_lr_l1_multiclass = models.FloatField(null=True, blank=True, default=0.0)
    prediction_lr_l2_binary = models.FloatField(null=True, blank=True, default=0.0)
    prediction_lr_l2_multiclass = models.FloatField(null=True, blank=True, default=0.0)
    prediction_gb_gscv_binary = models.FloatField(null=True, blank=True, default=0.0)
    prediction_gb_gscv_multiclass = models.FloatField(
        null=True, blank=True, default=0.0
    )

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Prediction {self.id}"
