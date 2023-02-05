# TODO здесь производится настройка пермишенов для нашего проекта
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "You are not the owner!"

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user