import speedtest 
import time
from playsound3 import playsound 

def play_alert():
    playsound('Sound\\alert.mp3')

def check_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000
    return download_speed, upload_speed

def main():
    while True:
        download, upload = check_speed()
        print(f"Download speed: {download: .2f} Mbps, Upload speed: {upload: .2f} Mbps")
        if download < 5:
            print("Внимание! Скорость загрузки меньше 5 Мбит/с!")
            play_alert()
        if upload < 5:
            print("Внимание! Скорость отдачи меньше 5 Мбит/с!")
            play_alert()
        time.sleep(60)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


