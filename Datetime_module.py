import datetime
import pytz

d=datetime.date.today()
print(d)
dt=datetime.timedelta(days=8,hours=12)
print(dt)
print(d-dt)

ti=datetime.time(23,12,56,1000)
print(ti)

print(datetime.datetime.today())
print(datetime.datetime.now(tz=pytz.utc))
print(datetime.datetime.utcnow().replace(tzinfo=pytz.utc))

#print(pytz.all_timezones)
now_utc=datetime.datetime.now(tz=pytz.utc)
print(now_utc.astimezone((pytz.timezone("Poland"))))

det=datetime.datetime.now()
det_tz=pytz.timezone("Indian/Reunion")
det=det_tz.localize(det)
print(det)