from flask import current_app
from flask import g
from flask import render_template
from flask import session

from info import constants
from info.models import News, User
from info.utils.common import user_login_data
from . import news_blu


@news_blu.route('/<int:news_id>')
@user_login_data
def news_detail(news_id):
    """
    新闻详情
    :param news_id:
    :return:
    """
    # 采用装饰器和g变量获取用户登入的信息
    user =  g.user

    # :右侧的新闻排行的逻辑
    news_list = []
    try:
        # 搜索数据库 : 按照最高点记率,排序6个
        news_list = News.query.order_by(News.clicks.desc()).limit(constants.CLICK_RANK_MAX_NEWS).all()
    except Exception as e:
        current_app.logger.error(e)

    # 因为news_list是模型对象
    news_dict_li = []
    # 遍历对象列表,将对象的字典添加到字典列表中
    for news in news_list:
        news_dict_li.append(news.to_basic_dict())

    data = {
        "new_dict_li" : news_dict_li
    }

    return render_template('news/detail.html', data=data)