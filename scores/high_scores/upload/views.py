from django.shortcuts import render

import redis
# Create your views here.
from django.http import response, HttpResponse
from query.models import Hign_scores
from interface.resp import User_response

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
pipe = r.pipeline()


# # pipe.zadd("cheshi",{65:1,91:1,32:1,87:1,54:1,43:1})
# pipe.execute()
# range_client = r.zrevrange('cheshi', 0, 3, withscores=True)[:4]
# print(range_client)

def post_top_n_users(request):
    if request.method == "GET":
        html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <form method='post' action="http://127.0.0.1:8000/v1/ranking_list/upload">
    玩家姓名:<input type="text" name="client_name">
    成绩:<input type="text" name="fraction">
    <input type='submit' value='提交'>
</form>
</body>
</html>"""
        return HttpResponse(html)
    if request.method == 'POST':
        request_data = request.POST
        print(f"POST内容:{request_data}")
        client_name = request_data.get("client_name")
        fraction = request_data.get("fraction")
        if not client_name and not fraction:
            return response.JsonResponse(User_response.User_Response.error(400, "not params client_name, fraction"))
        print(f"client_name:{client_name}, fraction:{fraction}")
        # 放redis有序集合(废)
        score = 1
        fraction_list = r.zrange("fraction", 0, -1)
        if int(fraction) not in fraction_list:
            pipe.zadd("fraction", {int(fraction): score})
            pipe.execute()

        current_client = Hign_scores.objects.filter(client_name=client_name)

        print(f"current_client:{current_client}")
        if current_client:
            Hign_scores.objects.filter(client_name=client_name).update(fraction=int(fraction))
        else:
            try:
                Hign_scores_obj = Hign_scores.objects.create(client_name=client_name, fraction=int(fraction))
                Hign_scores_obj.save()
            except Exception as e:
                return response.JsonResponse(User_response.User_Response.error(400, "not params"))
        upload_data = {}
        upload_data["client_name"] = client_name
        upload_data["fraction"] = fraction
        record = User_response.User_Response.success(200, upload_data)
        return response.JsonResponse(data=record)
