from django.db import models

# Create your models here.

class User(models.Model):
	class Meta:
		verbose_name = verbose_name_plural = '用户'
		db_table = "user"

	openid = models.CharField(max_length=200, verbose_name='openid')
	user_focus = models.ManyToManyField('User',null=True, blank=True, verbose_name='关注的用户', related_name='many_user')
	activity = models.ManyToManyField('Activity', null=True, blank=True, verbose_name='关注的活动', related_name='many_activity')
	nickname = models.CharField(max_length=200, verbose_name='昵称')
	sex = models.IntegerField(choices=[(0,'男'), (1,'女')], verbose_name='性别')
	status = models.IntegerField(default=0, verbose_name='状态')
	address = models.CharField(max_length=200, verbose_name='地址')
	real_name = models.CharField(null=True, blank=True,max_length=200, verbose_name='真实姓名')
	iphone = models.CharField(null=True, blank=True, max_length=200, verbose_name='电话')
	email = models.CharField(null=True, blank=True, max_length=200, verbose_name='邮箱')

	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)


class Activity(models.Model):
	class Meta:
		verbose_name = verbose_name_plural = '活动'
		db_table = 'activity'

	user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='用户', related_name='create_user')
	type = models.ForeignKey('Type', on_delete=models.CASCADE, verbose_name='活动类型') 
	title = models.CharField(max_length=200, verbose_name='标题')
	poster = models.ImageField(upload_to='poster/', verbose_name='海报')
	start_time = models.CharField(max_length=200, verbose_name='举办开始时间')
	end_time = models.CharField(max_length=200, verbose_name='举办结束时间')
	address = models.CharField(max_length=200, verbose_name='地址')
	hot = models.IntegerField(verbose_name='热度')
	people_num = models.CharField(max_length=200, verbose_name='活动人数')
	details = models.TextField(verbose_name='活动详情')
	status = models.IntegerField(verbose_name='状态')

	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)

	@staticmethod
	def add_activity(user_id, type_id, title, poster, start_time, end_time, address, people_num, details, logticket_id, logapplyform_id=None):
		
		logticket = LogTicket.objects.filter(id__in=logticket_id)
		type = Type.objects.filter(id=type_id).first()
		if logapplyform_id:
			logapplyform = LogApplyForm.objects.filter(id=logapplyform_id).first()
		user = User.objects.filter(id=user_id).first()

		activity = Activity.objects.create(
			user = user,
			type = type,
			title = title,
			poster = poster,
			start_time = start_time,
			end_time = end_time,
			address = address,
			people_num = people_num,
			details = details,
			status = status
		)

		for i in logticket:
			Ticket.objects.create(
				activity = activity,
				nickname = i.nickname,
				price = i.price,
				amount = i.amount,
				audit = i.audit,
				status = i.status,
				explain = i.explain,
				one_buy = i.one_buy,
				less = i.less,
				more = i.more,
				order_start = i.order_start,
				order_end = i.order_end,
				valid_start = i.valid_start,
				valid_end = i.valid_end
			)

		if logapplyform_id:
			ApplyForm.objects.create(
				activity = activity,
				more = logapplyform
			)
		else:
			ApplyForm.objects.create(
				activity = activity
			)

		return '111'


class Type(models.Model):
	class Meta:
		verbose_name = verbose_name_plural = '活动类型'
		db_table = 'type'

	nickname = models.CharField(max_length=200, verbose_name='类型名称')

	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)


class Ticket(models.Model):
	class Meta:
		verbose_name = verbose_name_plural = '票种'
		db_table = 'ticket'

	activity = models.ForeignKey('Activity', on_delete=models.CASCADE, verbose_name='活动')
	nickname = models.CharField(max_length=200, verbose_name='票种名称')
	price = models.FloatField(verbose_name='价格')
	amount = models.IntegerField(verbose_name='张数')
	audit = models.IntegerField(choices=[(0,'无需审核'),(1,'需我审核')], verbose_name='审核')
	status = models.IntegerField(verbose_name='状态')
	explain = models.CharField(null=True, blank=True, max_length=200, verbose_name='票种说明')
	one_buy = models.IntegerField(null=True, blank=True, verbose_name='单次购买')
	less = models.IntegerField(null=True, blank=True, verbose_name='最少购买张数')
	more = models.IntegerField(null=True, blank=True, verbose_name='最多购买张数')
	order_start = models.CharField(max_length=200, verbose_name='购票开始时间')
	order_end = models.CharField(max_length=200, verbose_name='购票结束时间')
	valid_start = models.CharField(max_length=200, verbose_name='有效时间开始')
	valid_end = models.CharField(max_length=200, verbose_name='有效时间结束')

	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)

	# @staticmethod
	# def add_ticket(activity_id, ):
	# 	pass


class ApplyForm(models.Model):
	class Meta:
		 verbose_name = verbose_name_plural = '报名表单'
		 db_table = 'applyfrom'

	activity = models.ForeignKey('Activity', on_delete=models.CASCADE, verbose_name='活动')
	
	more = models.TextField(null=True, verbose_name='更多项',default='')


	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)	 


class LogActivity(models.Model):
	class Meta:
		verbose_name = verbose_name_plural = '活动临时表'
		db_table = 'logactivity'

	user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='用户', related_name='log_create_user')
	type = models.ForeignKey('Type', on_delete=models.CASCADE, verbose_name='活动类型') 
	title = models.CharField(max_length=200, verbose_name='标题')
	poster = models.ImageField(upload_to='poster/', verbose_name='海报')
	start_time = models.CharField(max_length=200, verbose_name='举办开始时间')
	end_time = models.CharField(max_length=200, verbose_name='举办结束时间')
	address = models.CharField(max_length=200, verbose_name='地址')
	people_num = models.CharField(max_length=200, verbose_name='活动人数')
	details = models.TextField(verbose_name='活动详情')
	status = models.IntegerField(verbose_name='状态')

	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)

	@staticmethod
	def add_logactivity(user_id, type_id, title, poster, start_time, end_time, address, people_num, details):
		''' 添加活动临时表 '''

		user = User.objects.filter(id=user_id).first()

		type = Type.objects.filter(id=type_id).first()

		log_activity = LogActivity.objects.create(
			user = user,
			type = type,
			title = title,
			poster = poster,
			start_time = start_time,
			end_time = end_time,
			address = address,
			people_num = people_num,
			details = details,
			status = 0
		)

		return log_activity


class LogTicket(models.Model):
	class Meta:
		verbose_name = verbose_name_plural = '票种临时表'
		db_table = 'logticket'

	activity = models.ForeignKey('LogActivity', on_delete=models.CASCADE, verbose_name='活动')
	nickname = models.CharField(max_length=200, verbose_name='票种名称')
	price = models.CharField(max_length=200, verbose_name='价格')
	amount = models.IntegerField(verbose_name='张数')
	audit = models.IntegerField(choices=[(0,'无需审核'),(1,'需我审核')], verbose_name='审核')
	status = models.IntegerField(verbose_name='状态')
	explain = models.CharField(null=True, blank=True, max_length=200, verbose_name='票种说明')
	one_buy = models.IntegerField(null=True, blank=True, verbose_name='单次购买')
	less = models.IntegerField(null=True, blank=True, verbose_name='最少购买张数')
	more = models.IntegerField(null=True, blank=True, verbose_name='最多购买张数')
	order_start = models.CharField(max_length=200, verbose_name='购票开始时间')
	order_end = models.CharField(max_length=200, verbose_name='购票结束时间')
	valid_start = models.CharField(max_length=200, verbose_name='有效时间开始')
	valid_end = models.CharField(max_length=200, verbose_name='有效时间结束')

	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)


	@staticmethod
	def add_logticket(activity_id, nickname, price, amount, audit, status, explain, one_buy, less, more, order_start, order_end, valid_start, valid_end):
		
		logactivity = LogActivity.objects.filter(id=activity_id).first()

		logticket = LogTicket.objects.create(
			activity = logactivity,
			nickname = nickname,
			price = price,
			amount = amount,
			audit = audit,
			status = status,
			explain = explain,
			one_buy = one_buy,
			less = less,
			more = more,
			order_start = order_start,
			order_end = order_end,
			valid_start = valid_start,
			valid_end = valid_end,
		)

		return logticket


	def del_logticket(logtid):
		''' 删除临时表 '''

		logticket = LogTicket.objects.filter(id=logtid).first().delete()

		return logticket


class LogApplyForm(models.Model):
	class Meta:
		 verbose_name = verbose_name_plural = '报名表单临时表'
		 db_table = 'logapplyform'

	activity = models.ForeignKey('LogActivity', on_delete=models.CASCADE, verbose_name='活动')
	more = models.TextField(verbose_name='更多项', default='')

	@staticmethod
	def logapply_more(activity, more):
		
		logapplyform = LogApplyForm.objects.create(
			activity = activity,
			more = more
		)

		return logapplyform


class Apply(models.Model):
	class Meta:
		verbose_name = verbose_name_plural = '报名'
		db_table = 'apply'

	user = models.ForeignKey('User', null=True, on_delete=models.CASCADE, verbose_name='用户')
	activity = models.ForeignKey('Activity', null=True, on_delete=models.CASCADE, verbose_name='活动')
	ticket = models.ForeignKey('Ticket',null=True, on_delete=models.CASCADE, verbose_name='票种')
	name = models.CharField(max_length=200, verbose_name='姓名')
	phone = models.CharField(max_length=200, verbose_name='手机号')
	email = models.CharField(max_length=200, verbose_name='邮箱')
	more = models.TextField(null=True,verbose_name='更多')


class Video(models.Model):
	class Meta:
		verbose_name = verbose_name = '视频'
		db_table = 'video'

	activity = models.ForeignKey('Activity', null=True, blank=True, on_delete=models.CASCADE, verbose_name='活动')
	user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='用户')
	introduce = models.CharField(max_length=200, verbose_name='介绍')
	activity_name = models.CharField(max_length=200, verbose_name='活动名称')
	activity_address = models.CharField(max_length=200, verbose_name='活动地址')
	file_path = models.FileField(upload_to='file_path/', verbose_name='视频文件')
	status = models.IntegerField(default=0, verbose_name='状态')
	# look_num = models.IntegerField(default=0, verbose_name='观看量')
	comments_num = models.IntegerField(default=0, verbose_name='评论数')
	ups_num = models.IntegerField(default=0, verbose_name='点赞数')
	transpond_num = models.IntegerField(default=0, verbose_name='转发数')

	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)


class Ups(models.Model):
	class Meta:
		verbose_name = verbose_name_plural = '点赞'
		db_table = 'ups'

	video = models.ForeignKey('Video', on_delete=models.CASCADE, verbose_name='视频')
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
	isups = models.IntegerField(default=1, verbose_name='点赞')

	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)


class Comments(models.Model):
	class Meta:
		verbose_name = verbose_name_plural = '评论'
		db_table = 'comments'

	video = models.ForeignKey('Video', on_delete=models.CASCADE, verbose_name='视频')
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
	content = models.TextField(verbose_name='内容')
	status = models.IntegerField(default=0, verbose_name='状态')
	ups_num = models.IntegerField(default=0, verbose_name='点赞数')
	parent = models.ForeignKey('Comments', null=True, blank=True, on_delete=models.CASCADE, verbose_name='父评论', related_name='bor_parent')
	big_parent = models.ForeignKey('Comments', null=True, blank=True, on_delete=models.CASCADE, verbose_name='最大评论', related_name='fu_parent')

	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)


class TranSpond(models.Model):
	class Meta:
		 verbose_name = verbose_name_plural = '转发'
		 db_table = 'transpond'

	video = models.ForeignKey('Video', on_delete=models.CASCADE, verbose_name='视频')
	user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='用户')

	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)


# class Order(models.Model):
# 	class Meta:
# 		verbose_name = verbose_name_plural = '订单'
# 		db_table = 'order'


# 	activity = models.ForeignKey('Activity', null=True, blank=True, on_delete=models.CASCADE, verbose_name='活动')
# 	ticket = models.ForeignKey('Ticket',null=True, on_delete=models.CASCADE, verbose_name='票种')
# 	user = models.ForeignKey('User', null=True, on_delete=models.CASCADE, verbose_name='用户')
# 	order_num = models.CharField(max_length=200, verbose_name='订单号')
# 	order_money = models.FloatField(verbose_name='订单金额')
# 	pay = models.IntegerField(verbose_name='支付方式')

# 	create_time = models.DateTimeField(auto_now_add=True)
# 	update_time = models.DateTimeField(auto_now=True)












