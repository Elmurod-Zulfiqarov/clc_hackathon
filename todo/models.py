from django.utils import timezone
from django.db import models
from accounts.models import Account


class TodoList(models.Model):
    title = models.CharField(max_length=512, unique=True)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="todo_list")


    def __str__(self) -> str:
        return f"{self.title} by {self.owner}"

    
class TodoItem(models.Model):
    title = models.CharField(max_length=512, unique=True)
    description = models.TextField(max_length=10000)

    created_at = models.DateField(auto_now_add=True)
    due_date = models.DateField(default=timezone.now().year)

    is_success = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name="todo_item")

    def __str__(self) -> str:
        return f"{self.title}, ({self.is_success}) due: ({self.due_date})"
