## **测试结果：**

**客户端上传客户端号和分数**
	URL：http://127.0.0.1:8000/v1/ranking_list/upload
**客户端查询排行榜**
	URL：http://127.0.0.1:8000/v1/ranking_list/link/?client_name=client_1&page=1&count=10&begin=1&end=10

```python
data = {
    message: "ok",
    code: "200",
    data: {
        page: 1,
        count: "10",
        total: 11,
        fraction_array_data: [],
        interval_data: {
            begin: "1",
            end: 10,
            data: [
                {
                    index: 0,
                    id: 39,
                    client_name: "client6",
                    fraction: 123564
                },
                {
                    index: 1,
                    id: 42,
                    client_name: "client9",
                    fraction: 432111
                },
                {
                    index: 2,
                    id: 44,
                    client_name: "client11",
                    fraction: 534323
                },
                {
                    index: 3,
                    id: 35,
                    client_name: "client2",
                    fraction: 542412
                },
                {
                    index: 4,
                    id: 38,
                    client_name: "client5",
                    fraction: 642456
                },
                {
                    index: 5,
                    id: 43,
                    client_name: "client10",
                    fraction: 666666
                },
                {
                    index: 6,
                    id: 37,
                    client_name: "client4",
                    fraction: 676423
                },
                {
                    index: 7,
                    id: 41,
                    client_name: "client8",
                    fraction: 756422
                },
                {
                    index: 8,
                    id: 40,
                    client_name: "client7",
                    fraction: 875453
                },
                {
                    index: 9,
                    id: 36,
                    client_name: "client3",
                    fraction: 875531
                }
            ]
        }
    }
}
```
