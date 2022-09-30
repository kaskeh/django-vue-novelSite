# 设置任务队列的url 地址
broker_url = "redis://127.0.0.1:6379/14"
# 设置结果队列url队列 地址
result_backend = "redis://127.0.0.1:6379/15"
worker_concurrency = 2  # 并发worker数