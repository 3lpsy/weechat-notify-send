import gi

gi.require_version("Notify", "0.7")

from gi.repository import Notify

Notify.init("App Name")
n = Notify.Notification.new("Hi")
n.set_timeout(1000)
n.show()
Notify.uninit()

from notify_send_tests import new_notification
from notify_send import send_notification


import warnings

# import sys
# import traceback


# def warn_with_traceback(message, category, filename, lineno, file=None, line=None):

#     log = file if hasattr(file, "write") else sys.stderr
#     traceback.print_stack(file=log)
#     log.write(warnings.formatwarning(message, category, filename, lineno, line))


# warnings.showwarning = warn_with_traceback


notification = new_notification()
send_notification(notification)

notification = new_notification(message="second", transient=False)
send_notification(notification)

notification = new_notification(message="third", urgency="low")
send_notification(notification)

notification = new_notification(message="third", urgency="critical")
send_notification(notification)
notification = new_notification(message="a" * 2000, urgency="critical")
send_notification(notification)
