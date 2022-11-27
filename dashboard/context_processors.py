from .models import Notification

def global_var(request):
    notifications = None
    unreadNotifications = 0
    if request.user.is_authenticated:
        if not request.user.role == '1':
            notifications = Notification.objects.filter(
                user=request.user).order_by('-createdAt')
            unreadNotifications = notifications.filter(userRead=False).count()
        else:
            notifications = Notification.objects.all().order_by('-createdAt')
            unreadNotifications = notifications.filter(adminRead=False).count()
            
    context = {'notifications': notifications,
               'unreadNotifications': unreadNotifications}
    return context
