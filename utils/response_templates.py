from datetime import datetime

BY_MSISDN_TEMPLATE = {
  "code": 0,
  "description": "string",
  "is_person_in_white_list": True,
  "is_person_in_stop_list": False,
  "is_person_in_alarm_list": False,
  "is_person_in_mdw_list": False,
  "is_person_in_terror_list": False
}

BY_PASSPORT_TEMPLATE = {
  "code": 0,
  "description": "string",
  "is_person_in_terror_list": False,
  "is_passport_expired": False,
  "smev_check_date": "string",
  "smev_code": 0,
  "smev_subcode": 0,
  "smev_invalidity_date": "string"
}

SIMPLE_CHECK_TEMPLATE = {
  "code": 0,
  "description": "string",
  "is_person_in_white_list": True,
  "is_person_in_stop_list": False,
  "is_person_in_alarm_list": False,
  "is_person_in_mdw_list": False,
  "is_passport_expired": False,
  "is_person_in_terror_list": False,
  "smev_check_date": datetime.now().strftime('%Y-%m-%d'),
  "smev_code": 0,
  "smev_subcode": 0,
  "smev_invalidity_date": "string"
}

SIMPLE_CHECK_LAZY_TEMPLATE = {
  "code": 8,
  "description": "Success",
  "accepted": True,
  "version": "0.0.2",
  "status": "finished"
}

FULL_CHECK_TEMPLATE = {
  "code": 0,
  "description": "string",
  "is_person_in_white_list": True,
  "is_person_in_stop_list": False,
  "is_person_in_alarm_list": False,
  "is_person_in_mdw_list": False,
  "is_passport_expired": False,
  "is_person_in_terror_list": False,
  "smev_check_date": datetime.now().strftime('%Y-%m-%d'),
  "smev_code": 0,
  "smev_subcode": 0,
  "smev_invalidity_date": "string",
  "task_id": "string"
}

FULL_CHECK_LAZY_TEMPLATE = {
  "code": 8,
  "description": "Success",
  "accepted": True,
  "version": "0.0.2",
  "status": "finished",
  "task_id": "string"
}