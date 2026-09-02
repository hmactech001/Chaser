from client.ChaserClient import ChaserClient


def main():
    client = ChaserClient("192.168.xx.x", 2009, "test")
    client.connect()

    while True:
        # 制御コードとマップ情報を得る
        control_code, map_info = client.receive()
        # 制御コードが'0'の場合ループを抜ける
        if control_code == '0':
            break


        client.get_ready()
        if control_code == '1':
            client.walk_up()
        elif control_code == '2':
            client.put_right()     
        elif control_code == '3':
            client.search_down()
        else :
            client.look_left()
        client.turn_end()
     
    client.close()


if __name__ == "__main__":
    main()
