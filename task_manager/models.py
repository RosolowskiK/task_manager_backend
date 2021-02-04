from django.db import models


class TaskRoot(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128, blank=True)  # blank ustawia columne na wymaganą w formularzu

    def __str__(self):
        return f'{self.name} {self.description}'


class TaskChild(models.Model):
    task_root = models.ForeignKey(TaskRoot, related_name='task_children',
                                  on_delete=models.CASCADE, blank=True)  # klucz obcy na rodzica i dodatkowo usuwanie zadań razem z rootem (cascade)
    name = models.CharField(max_length=128, blank=True)
    done = models.BooleanField(default=False)
