from django.db import models

class CourseGroup(models.Model):
    course_unit_id = models.IntegerField()
    group_number = models.IntegerField()
    submit_count = models.IntegerField()
