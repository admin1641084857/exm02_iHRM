"""
    封装员工的增删改查请求实现
"""
import app


class EmpCRUD:

    # 函数1:增
    def add(self, session, username, mobile, workNumber):
        # return session对象.post("新增的URL",json=提交的数据)
        myAddEmp = {"username": username,
                    "mobile": mobile,
                    "workNumber": workNumber
                    }
        return session.post(app.BASE_URL + "user",
                            json=myAddEmp,
                            headers={"Authorization": "Bearer " + app.TOKEN})

    # 函数2:改
    def update(self, session, userId, username):
        # session对象.put("修改的URL,后缀ID",json={"username":账号})
        return session.put(app.BASE_URL + "user/" + userId,
                           json={"username": username},
                           headers={"Authorization": "Bearer " + app.TOKEN})

    # 函数3:查
    def get(self, session, userId):
        return session.get(app.BASE_URL + "user/" + userId,
                           headers={"Authorization": "Bearer " + app.TOKEN})

    # 函数4:删
    def delete(self, session, userId):
        return session.delete(app.BASE_URL + "user/" + userId,
                              headers={"Authorization": "Bearer " + app.TOKEN})
