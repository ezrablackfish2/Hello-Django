import freezegun

with freezegun.freeze(datetime(2023, 6, 30, 12, 0, 0, tzinfo=timezone.utc)):
    pip3 freeze > requirements.txt
