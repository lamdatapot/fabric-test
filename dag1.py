import json
import pendulum
from airflow.models import DAG
from airflow.operators.empty import EmptyOperator
from airflow.timetables.trigger import CronTriggerTimetable
from airflow.utils.trigger_rule import TriggerRule


DAG_NAME = "facebook_ads_daily"
SCHEDULE_INTERVAL = CronTriggerTimetable("30 05,10,13,17 * * *", timezone="Asia/Ho_Chi_Minh")