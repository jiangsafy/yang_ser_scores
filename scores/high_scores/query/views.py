from django.core.paginator import Paginator
from django.http import response, HttpResponse
from query.models import Hign_scores
from interface.resp import User_response
from django.views import View
import redis
from django_redis import get_redis_connection


# pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
# r = redis.Redis(connection_pool=pool)
# pipe = r.pipeline()


def get_top_n_users(request):
    # http://127.0.0.1:8000/v1/ranking_list/link/?client_name=client_1&page=1&count=10&begin=1&end=10
    if request.method == 'GET':
        request_params = request.GET
        print(f"request_params:{request_params}")
        if not request_params:
            return response.JsonResponse(User_response.User_Response.error(400, "no data"))
        client_name = request_params.get("client_name")
        if not client_name:
            return response.JsonResponse(User_response.User_Response.error(400, "no client_name"))
        begin = request_params.get("begin")
        # 查询范围
        begin = request_params.get("begin")
        if not begin:
            return response.JsonResponse(User_response.User_Response.error(400, "no begin"))
        end = int(request_params.get("end", 1))
        if not end:
            return response.JsonResponse(User_response.User_Response.error(400, "no end"))
        ##
        current_page = int(request_params.get("page", 1))
        count = request_params.get("count", 10)
        # 用redis有序集合(废)
        # fraction_list = pipe.zrange('fraction', 0, count + 1, withscores=True)
        # hign_scores = Hign_scores.objects.filter(fraction__in=range_client)

        # 用mysql
        hign_scores = Hign_scores.objects.all().order_by("fraction")
        print(f"+++++++++hign_scores:{type(hign_scores)}+++++++")
        try:
            # 分页对象
            paginator = Paginator(hign_scores, count)
            num_pages = paginator.num_pages
            print(num_pages)
            if current_page > num_pages:
                current_page = 1
        except:
            return response.JsonResponse(User_response.User_Response.error(400, "Create a failure:paginator"))
        start_index = (current_page - 1) * 10 + 1
        page = paginator.page(current_page)
        total = paginator.count
        fraction_array_data = []
        current_o = None
        if not current_o:
            current_o = Hign_scores.objects.filter(client_name=client_name)
        if current_o:
            fraction_array_data.append({
                "index": 1,
                "id": current_o.id,
                "client_name": current_o.client_name,
                "fraction": current_o.fraction,
            })

        for index, hign_o in enumerate(page):
            fraction_array_data.append(
                {"index": start_index + index, "id": hign_o.id, "client_name": hign_o.client_name,
                 "fraction": hign_o.fraction})
        interval = []
        for index, hign_o in enumerate(hign_scores):
            interval.append({"index": index, "id": hign_o.id, "client_name": hign_o.client_name,
                             "fraction": hign_o.fraction})
        if len(interval) >= int(begin):
            interval_data = {
                "begin": begin,
                "end": end,
                "data": interval[int(begin) - 1:int(end)]
            }
        else:
            interval_data = {
                "begin": begin,
                "end": end,
                "data": "Not ranked"
            }
        query_data = {
            "page": current_page,
            "count": count,
            "total": total,
            "fraction_array_data": fraction_array_data,
            "interval_data": interval_data
        }
        record = User_response.User_Response.success(200, query_data)
        return response.JsonResponse(data=record)
    elif request.method == 'POST':
        pass


# def get_top_interval(request):
#     # http://127.0.0.1:8000/v1/ranking_list/interval/?begin=1&end=10
#     if request.method == 'GET':
#         request_params = request.GET
#         if not request_params:
#             return response.JsonResponse(User_response.User_Response.error(400, "no data"))
#         begin = request_params.get("begin")
#         if not begin:
#             return response.JsonResponse(User_response.User_Response.error(400, "no begin"))
#         end = int(request_params.get("end", 1))
#         if not end:
#             return response.JsonResponse(User_response.User_Response.error(400, "no end"))
#         hign_scores = Hign_scores.objects.all().order_by("fraction")
#         fraction_array_data = []
#         for index, hign_o in enumerate(hign_scores):
#             fraction_array_data.append({"index": index, "id": hign_o.id, "client_name": hign_o.client_name,
#                                      "fraction": hign_o.fraction})
#         data = {
#             "begin": begin,
#             "end": end,
#             "data": fraction_array_data[int(begin):int(end) + 1]
#         }
#         record = User_response.User_Response.success(200, data)
#
#         print(f"record:{record}")
#         return response.JsonResponse(data=record)
