import json

import tornado.ioloop
import tornado.web

# 定义处理类型
tool_bar = {}


# tool_bar = {
#     "id": "toolbar_____",
#     "title": "\u4e66\u7b7e\u5de5\u5177\u680f",
#     "index": 1,
#     "dateAdded": 1608713447670,
#     "type": "folder",
#     "dateGroupModified": 1608776773455,
#     "children": [
#         {
#             "id": "xF9itG_HqSrZ",
#             "title": "1",
#             "index": 0,
#             "dateAdded": 1608714538000,
#             "type": "bookmark",
#             "url": "http://baidu/",
#             "parentId": "toolbar_____"
#         },
#         {
#             "id": "Dfb5dsHYe0mo",
#             "title": "2",
#             "index": 1,
#             "dateAdded": 1608714632935,
#             "type": "folder",
#             "parentId": "toolbar_____",
#             "dateGroupModified": 1608714723372,
#             "children": [
#                 {
#                     "id": "4I4zts_zo3n_",
#                     "title": "3",
#                     "index": 0,
#                     "dateAdded": 1608714637848,
#                     "type": "bookmark",
#                     "url": "http://0.0.0.2/",
#                     "parentId": "Dfb5dsHYe0mo"
#                 }
#             ]
#         },
#         {
#             "id": "NvywRHNPhNcP",
#             "title": " 4",
#             "index": 2,
#             "dateAdded": 1608773643556,
#             "type": "folder",
#             "parentId": "toolbar_____",
#             "dateGroupModified": 1608773643556,
#             "children": []
#         }
#     ],
#     "parentId": "root________"
# }


class GetBookMark(tornado.web.RequestHandler):
    # 添加一个处理get请求方式的方法
    async def post(self):
        all_bookmark = self.get_body_argument("allBookMark")
        all_bookmark = json.loads(all_bookmark)
        global tool_bar
        tool_bar = all_bookmark
        print(json.dumps(all_bookmark, indent=2))
        await self.finish("succ")

    async def get(self):
        global tool_bar
        await self.finish(json.dumps(tool_bar))

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")  # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')


if __name__ == '__main__':
    # 创建一个应用对象
    app = tornado.web.Application([(r'/', GetBookMark)])
    # 绑定一个监听端口
    app.listen(9000)
    # 启动web程序，开始监听端口的连接
    tornado.ioloop.IOLoop.current().start()
