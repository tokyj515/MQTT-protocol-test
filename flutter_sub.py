import paho.mqtt.client as mqtt

# 브로커 주소 및 토픽 설정
broker_address = "3.35.30.20"  # EC2 인스턴스의 공인 IP 주소
topic = "obd/topic"

# 메시지를 수신할 때 호출되는 콜백 함수
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode('utf-8')}")

# MQTT 클라이언트 생성
client = mqtt.Client()

# 메시지 수신 콜백 함수 설정
client.on_message = on_message

# 브로커에 연결
client.connect(broker_address, 1883, 60)

# 토픽 구독
client.subscribe(topic)

print(f"Subscribed to topic '{topic}' on broker '{broker_address}'")

# 메시지 수신 대기 (blocking)
client.loop_forever()
