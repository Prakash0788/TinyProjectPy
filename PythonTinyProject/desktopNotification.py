from plyer import notification

title = input("Notification title: ")
msg = input("Notification message: ")

notification.notify(
    title = title,
    message = msg,
    timeout = 5
)