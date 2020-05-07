class User_Response(object):
    @classmethod
    def success(cls,code,data):
        return {
            "message": "ok",
            "code": f"{code}",
            "data": data or {},
        }

    @classmethod
    def error(cls,code, msg=None):
        return {
            "message": msg,
            "code": str(code),
            "data": {},
        }
