from restapi import api
from .models import *


@api
def add_logactivity(user_id, type_id, title, poster, start_time, end_time, address, people_num, details):

	log_activity = LogActivity.add_logactivity(user_id, type_id, title, poster, start_time, end_time, address, people_num, details)
	
	print(log_activity)

	return {"id":log_activity.id}

@api
def add_logticket(activity_id, nickname, price, amount, audit, status, explain, one_buy, less, more, order_start, order_end, valid_start, valid_end):
	
	logticket = LogTicket.add_logticket(activity_id, nickname, price, amount, audit, status, explain, one_buy, less, more, order_start, order_end, valid_start, valid_end)

	return {'id':logticket.id}


@api
def add_activity(user_id, log_activity_id, logticket_id, logapplyform_id=None):
	
	activity = Activity.add_activity(user_id, log_activity_id, logticket_id, logapplyform_id)

	print(activity)