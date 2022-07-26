import copy

from django.utils.safestring import mark_safe
from django.http.request import QueryDict


# 分页组件
class Pagination(object):

    def __init__(self, request, query_set, page_param="page", page_size=10, width=5):
        # 全局预处理量
        self.data_count = query_set.count()  # 总数据条数
        self.total_page_count = int(self.data_count / page_size) + 1  # 总页码数
        self.query_dict = copy.deepcopy(request.GET)
        self.page_param = page_param

        # 获取当前页
        current_page = request.GET.get(page_param, "1")
        if current_page.isdecimal():
            current_page = int(current_page)
        else:
            current_page = 1

        # 校验当前页码
        if current_page < 1:
            current_page = 1
        if current_page > self.total_page_count:
            current_page = self.total_page_count

        # 当前的页码
        self.current_page = current_page
        # 每一页展示的数据量和范围
        self.page_size = page_size
        # 需要展示的数据部分
        self.page_query_set = query_set[(self.current_page - 1) * self.page_size: min(
            self.current_page * self.page_size, self.data_count)]
        # 需要展示的页码范围宽度
        self.width = width

    def html(self):
        """生成html"""
        # 添加上一页的代码
        self.query_dict.setlist(self.page_param, [max(1, self.current_page - 1)])
        page_nav_string = ['<li>'
                           '<a href="?{}" aria-label="Previous">'
                           '<span aria-hidden="true">上一页</span>'
                           '</a>'
                           '</li>'.format(self.query_dict.urlencode())]
        # 页码横向列表
        for i in range(1, self.total_page_count + 1):
            if abs(i - self.current_page) > self.width:
                # 如果在当前页面周围6页以外则不生成
                continue
            self.query_dict.setlist(self.page_param, [i])
            if i == self.current_page:
                # 如果是当前页就添加active
                page_nav_string.append(
                    '<li class="active"><a href="/pretty/number/list/?{}">{}</a></li>'.format(
                        self.query_dict.urlencode(), i))
            else:
                page_nav_string.append(
                    '<li><a href="/pretty/number/list/?{}">{}</a></li>'.format(self.query_dict.urlencode(), i))
        # 添加下一页的代码
        self.query_dict.setlist(self.page_param, [min(self.total_page_count, self.current_page + 1)])
        page_nav_string.append('<li>'
                               '<a href="?{}" aria-label="Next">'
                               '<span aria-hidden="true">下一页</span>'
                               '</a>'
                               '</li>'.format(self.query_dict.urlencode()))
        # 添加一行搜索框
        page_nav_string.append('<div style="float: right;width: 300px;">'
                               '<form method="get">'
                               '<div class="input-group">'
                               '<input type="text" class="form-control" placeholder="页码"'
                               ' name="page">'
                               '<span class="input-group-btn">'
                               '<button class="btn btn-default" type="submit">'
                               '<span class="glyphicon glyphicon-search" aria-hidden="true"></span>'
                               '</button>'
                               '</span>'
                               '</div><!-- /input-group -->'
                               '</form>'
                               '</div>'.format())
        return mark_safe("".join(page_nav_string))
