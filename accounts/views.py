from django.shortcuts import render
from django.views import View
from .models import Account
from todo.models import TodoList, TodoItem

class AccountListView(View):
    def get(self, request, *args, **kwargs):
        accounts = Account.objects.all()
        todo_list = TodoList.objects.all()
        context = {
            "accounts": accounts,
            "todo_list": todo_list
        }
        return render(request, 'accounts/accounts.html', context=context)
        