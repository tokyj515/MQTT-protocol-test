import paho.mqtt.client as mqtt

# MQTT 브로커 설정
mqtt_broker = "3.35.30.20"  # MQTT 브로커 주소
mqtt_port = 1883  # MQTT 기본 포트
mqtt_topic = "pedal/topic"  # 퍼블리시할 토픽

# MQTT 클라이언트 생성
client = mqtt.Client()

# MQTT 연결 콜백 함수
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("MQTT 연결 성공")
    else:
        print("MQTT 연결 실패, 코드:", rc)

# MQTT 퍼블리시 함수
def publish_message(message):
    try:
        result = client.publish(mqtt_topic, message)
        status = result[0]
        if status == 0:
            print(f"메시지 전송 성공: {message}")
        else:
            print(f"메시지 전송 실패: {message}")
    except Exception as e:
        print(f"메시지 전송 중 오류 발생: {e}")

# 연결 시도
client.on_connect = on_connect
client.connect(mqtt_broker, mqtt_port, 60)

# 메시지 퍼블리시 반복
client.loop_start()
try:
    while True:
        # 사용자로부터 메시지 입력 받기
        user_message = input("보낼 메시지를 입력하세요 (종료하려면 'exit' 입력): ")

        if user_message.lower() == 'exit':
            print("MQTT 퍼블리셔 종료")
            break

        # 입력받은 메시지 퍼블리시
        publish_message(user_message)

except KeyboardInterrupt:
    print("MQTT 퍼블리셔 강제 종료")
finally:
    client.loop_stop()
    client.disconnect()
