import datetime

x = datetime.datetime.now()

epoch = datetime.datetime(1970, 1, 1)
current_time = datetime.datetime.now()
time_difference = current_time - epoch
seconds_since_epoch = time_difference.total_seconds()

print(f"Seconds since January 1, 1970: {seconds_since_epoch:,.4f} or {seconds_since_epoch:.2e} in scientific notation")
print(x.strftime("%b %d %Y"))
