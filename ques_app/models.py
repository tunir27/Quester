from django.db import models

# Create your models here.
class Question_Details(models.Model):
    question=models.CharField(max_length=1000, help_text="Enter the Question",verbose_name="Question")
    choice_1=models.CharField(max_length=500, help_text="Enter the Answer Choice 1",verbose_name="Choice1")
    choice_2=models.CharField(max_length=500, help_text="Enter the Answer Choice 2",verbose_name="Choice2")
    choice_3=models.CharField(max_length=500, help_text="Enter the Answer Choice 3",verbose_name="Choice3")
    choice_4=models.CharField(max_length=500, help_text="Enter the Answer Choice 4",verbose_name="Choice4")
    correct_ans=models.CharField(max_length=1, help_text="Enter the Correct Answer in A,B,C,D",verbose_name="Answer")

    def __str__(self):
        return str(self.id)

class Answer_Details(models.Model):
    ans_right=models.CharField(max_length=20, help_text="Enter the Total no of Right Answers ",verbose_name="Total no of Answers Right")
    avg_time=models.CharField(max_length=20, help_text="Enter the Average Time for Solve the Exam",verbose_name="Avg Time")
    avg_clicks=models.CharField(max_length=20, help_text="Enter the Average Clicks",verbose_name="Avg Clicks")
    avg_marked=models.CharField(max_length=20, help_text="Enter the Average no of questions marked for review",verbose_name="No of Questions Marked for Review")
    stu_class=models.CharField(max_length=20, help_text="Enter the Classification of Student",verbose_name="Classification",blank=True,null=True)

    def __str__(self):
        return str(self.id)
