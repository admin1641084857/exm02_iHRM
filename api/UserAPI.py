"""
    封装登录请求
"""
import app
import logging


class UserLogin:

    # 登录请求
    def login(self, session, mobile, password):
        # return session对象.post("登录URL",json={"mobile":账号, "password":密码})
        logging.info("执行登录操作")
        return session.post(app.BASE_URL + "login",
                            json={"mobile": mobile, "password": password})
