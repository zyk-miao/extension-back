import json

import tornado.ioloop
import tornado.web


# 定义处理类型


class GetBookMark(tornado.web.RequestHandler):
    # 添加一个处理get请求方式的方法

    async def post(self):
        all_bookmark = self.get_body_argument("allBookMark")
        all_bookmark = json.loads(all_bookmark)
        # chrome
        # bookmark_bar_list = all_bookmark[0]['children'][0]['children']
        # firefox
        bookmark_bar_list = all_bookmark[0]['children']
        print(json.dumps(bookmark_bar_list, indent=2))
        await self.finish("bbb")

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")  # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')


if __name__ == '__main__':
    # 创建一个应用对象
    app = tornado.web.Application([(r'/', GetBookMark)])
    # 绑定一个监听端口
    app.listen(8002)
    # 启动web程序，开始监听端口的连接
    tornado.ioloop.IOLoop.current().start()
