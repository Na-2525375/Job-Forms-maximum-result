from django.db import models
from django.contrib.auth.models import AbstractUser


class customUser(AbstractUser):
    USER=[
        ('recruiter','Recruiter'),('jobseeker','JobSeeker')
    ]
    profile_pic=models.ImageField(upload_to='media/profile_pic',null=True)
    user_type=models.CharField(choices=USER,max_length=120,null=True)
    city=models.CharField(max_length=120,null=True)

    def __str__(self) -> str:
        return self.username
    

class addJobModel(models.Model):
    Job_Title=models.CharField(max_length=120)
    Job_Description=models.CharField(max_length=500)
    Job_Requirements=models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.Job_Title
    
class jobApplyModel(models.Model):
    
    job=models.ForeignKey(addJobModel,on_delete=models.CASCADE,related_name='applications')
    applicant=models.ForeignKey(customUser,on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.applicant.display_name} applied for {self.job.job_title}"




