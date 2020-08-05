# pi-tools
Small services done with Rapsberry Pi hardware such as people counter with video detection, ....

## Control Panel

This django app will containt all the data sent from the raspberry pi services, and will display them in a human readable and relevant way.

To start this server, run the following command

```
python3 manage.py runserver
```

## People Counter

This is a service running on the Pi, and requiring a camera. It will counter (or counter down) the number of people passing the line and sent it to the Control Panel.

To simulate the sent data, the following curl can be used

```
curl --header "Content-Type: application/json" --request POST  --data '{"count":-2}' http://localhost:8000/api/counter/
```

```
python people_counter.py --prototxt config/MobileNetSSD_deploy.prototxt --model config/MobileNetSSD_deploy.caffemodel --server-config config/server_config.json
```
