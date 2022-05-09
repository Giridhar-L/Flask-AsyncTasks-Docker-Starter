# Flask-AsyncTasks-Docker-Starter

This is starter project to implent a web app with ability to process tasks asynchronously.
Using Celery, background tasks can be created and tracked.
RabbitMQ acts as message broker
MongoDB acts as results backend

This starter project has following code examples
 - Task creation : /task
 - Check Task status: /status/<task_id> 


To start the application run the following command from project root directory
```
docker compose up --build
```


if you launched rabbitmq by using somthing like:
```
docker run -d --name some-rabbit -p 4369:4369 -p 5671:5671 -p 5672:5672 -p 15672:15672 rabbitmq
```
then you can enable its management plugins while that container runs using the following command:
```
docker container exec -it some-rabbit rabbitmq-plugins enable rabbitmq_management
```
and the management GUI is running on http://localhost:15672 For management GUI
