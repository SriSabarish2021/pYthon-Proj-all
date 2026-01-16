from plyer import battery
from plyer import notification
print("This is a Plyer Project".center(50,"-"))
print("")

print(battery.status)

notification.notify(
    title="Jarvis",
    message="Task completed successfully",
    timeout=5
)
