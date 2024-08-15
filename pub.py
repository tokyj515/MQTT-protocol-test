import paho.mqtt.client as mqtt

# MQTT 브로커 설정
broker_address = "ip"  # EC2 인스턴스의 공인 IP 주소
topic = "test/topic"

# MQTT 클라이언트 생성
client = mqtt.Client()

# 브로커에 연결
client.connect(broker_address, 1883, 60)

# 메시지 발행
message = "Hello from EC2!"
client.publish(topic, message)

# 연결 종료
client.disconnect()

print(f"Message '{message}' published to topic '{topic}'")
