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
	company = models.CharField(default='', max_length=200, verbose_name='所属单位')
	introduce = models.TextField(default='', verbose_name='介绍')
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
	start_time = models.DateTimeField(verbose_name='举办开始时间')
	end_time = models.DateTimeField(verbose_name='举办结束时间')
	address = models.CharField(max_length=200, verbose_name='地址')
	hot = models.IntegerField(verbose_name='热度')
	people_num = models.CharField(max_length=200, verbose_name='活动人数')
	details = models.TextField(verbose_name='活动详情')
	status = models.IntegerField(verbose_name='状态')

	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)


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
	order_start = models.DateTimeField(verbose_name='购票开始时间')
	order_end = models.DateTimeField(verbose_name='购票结束时间')
	valid_start = models.DateTimeField(verbose_name='有效时间开始')
	valid_end = models.DateTimeField(verbose_name='有效时间结束')

	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)



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
	start_time = models.DateTimeField(verbose_name='举办开始时间')
	end_time = models.DateTimeField(verbose_name='举办结束时间')
	address = models.CharField(max_length=200, verbose_name='地址')
	people_num = models.CharField(max_length=200, verbose_name='活动人数')
	details = models.TextField(verbose_name='活动详情')
	status = models.IntegerField(verbose_name='状态')

	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)


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
	order_start = models.DateTimeField(verbose_name='购票开始时间')
	order_end = models.DateTimeField(verbose_name='购票结束时间')
	valid_start = models.DateTimeField(verbose_name='有效时间开始')
	valid_end = models.DateTimeField(verbose_name='有效时间结束')

	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)


class LogApplyForm(models.Model):
	class Meta:
		 verbose_name = verbose_name_plural = '报名表单临时表'
		 db_table = 'logapplyform'

	activity = models.ForeignKey('LogActivity', on_delete=models.CASCADE, verbose_name='活动')
	more = models.TextField(verbose_name='更多项', default='')


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


class Order(models.Model):
	class Meta:
		verbose_name = verbose_name_plural = '订单'
		db_table = 'order'

	activity = models.ForeignKey('Activity', null=True, blank=True, on_delete=models.CASCADE, verbose_name='活动')
	ticket = models.ForeignKey('Ticket',null=True, on_delete=models.CASCADE, verbose_name='票种')
	user = models.ForeignKey('User', null=True, on_delete=models.CASCADE, verbose_name='用户')
	order_num = models.CharField(max_length=200, verbose_name='订单号')
	status = models.IntegerField(choices=[(0,'未支付'),(1,'已支付')])
	order_money = models.FloatField(verbose_name='订单金额')
	pay = models.IntegerField(verbose_name='支付方式')

	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)


class ReFund(models.Model):
	class Meta:
		verbose_name = verbose_name_plural = '退款'

	order = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name='订单')
	transaction = models.CharField(max_length=200, verbose_name='退款交易号')
	money = models.FloatField(verbose_name='退款金额')
	status = models.IntegerField(choices=[(0,'退款中'),(1,'退款成功'),(2,'退款失败')],verbose_name='退款状态')
	cause = models.TextField(verbose_name='退款原因')

	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)










