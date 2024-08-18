import paho.mqtt.client as mqtt

# MQTT 브로커 설정
broker_address = "3.35.30.20"  # EC2 인스턴스의 공인 IP 주소
topic = "test/topic"

# MQTT 클라이언트 생성
client = mqtt.Client()

# 브로커에 연결
client.connect(broker_address, 1883, 60)

# 메시지 발행
message = "우아"
client.publish(topic, message)

# 연결 종료
client.disconnect()

print(f"Message '{message}' published to topic '{topic}'")
