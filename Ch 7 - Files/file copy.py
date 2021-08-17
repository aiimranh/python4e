# copy text file.
rhandle = open('mbox-short.txt', 'r')
whandle = open('mbox-write.txt', 'w')
for line in rhandle:
    whandle.write(line)
whandle.close()
rhandle.close()

# copy image file.
rhandle = open('Screenshot.png', 'rb')
whandle = open('Screenshot2.png', 'wb')
for line in rhandle:
    whandle.write(line)
whandle.close()
rhandle.close()

# copy video file.
rhandle = open('demo_video.mp4', 'rb')
whandle = open('demo_video2.mp4', 'wb')
for line in rhandle:
    whandle.write(line)
whandle.close()
rhandle.close()
