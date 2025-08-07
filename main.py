   from picamera2 import Picamera2
   from picamera2.encoders import H264Encoder
   from picamera2.outputs import FileOutput

   picam2 = Picamera2()
   video_config = picam2.create_video_configuration()
   picam2.configure(video_config)

   encoder = H264Encoder(10000000)  # 10 Mbps bitrate
   output = FileOutput("test.h264")
   picam2.start_recording(encoder, output)
   picam2.start()
   time.sleep(10)  # Record for 10 seconds
   picam2.stop_recording()
   picam2.stop()
