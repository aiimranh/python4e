# copy text file.
with open('mbox-short.txt', 'r') as rf:
    with open('mbox-write2.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# copy image file.
with open('Screenshot.png', 'rb') as rf:
    with open('Screenshot2.png', 'wb') as wf:
        for line in rf:
            wf.write(line)

# copy video file.
with open('demo_video.mp4', 'rb') as rf:
    with open('demo_video2.mp4', 'wb') as wf:
        for line in rf:
            wf.write(line)
