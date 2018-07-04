# -*- coding: utf-8 -*-
# 配置数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 修改数据库为MySQL，并进行配置
        'NAME': 'my_blog',
        'USER': 'develop',
        'PASSWORD': 'project123',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4', }
    }
}
# 邮箱配置
EMAIL_HOST = 'smtp.163.com'
EMAIL_HOST_USER = 'qian_chen_jin@163.com'
EMAIL_HOST_PASSWORD = 'yeakofan2617'  # 这个不是邮箱密码，而是授权码
EMAIL_PORT = 465  # 由于阿里云的25端口打不开，所以必须使用SSL然后改用465端口
# 是否使用了SSL 或者TLS，为了用465端口，要使用这个
EMAIL_USE_SSL = True
# 默认发件人，不设置的话django默认使用的webmaster@localhost，所以要设置成自己可用的邮箱
DEFAULT_FROM_EMAIL = 'Yeakofan <qian_chen_jin@163.com>'

# 网站默认设置和上下文信息
SITE_END_TITLE = '秋叶成林,孤灯夜话'
SITE_DESCRIPTION = '谈谈技术,写写生活,聊聊人生,吹吹牛逼'
SITE_KEYWORDS = '秋城夜话'