from pytube import YouTube
print("Enter number: ")
n=int(input())
filename='links.txt'
outfile=open(filename,"w")
for i in range(0,n):
    print("Enter link for the video: ")
    link=str(input())
    # link = "https://www.youtube.com/watch?v=giXco2jaZ_4"
    
    yt = YouTube(link)  
    outfile.write(str(i+1)+"\t")
    outfile.write(str(link)+"\t")
    outfile.write(str("F:\programming\python mini project"+"\n"))
    try:
        yt.streams.filter(progressive = True, 
    file_extension = "mp4").first().download(output_path = "F:\programming\python mini project", 
    filename = "video")
    except:
        print("Some Error!")
    print('Task Completed!')
outfile.close()

#DontthinkJustdo
# fvar=open("inputlinks.txt",'r')
# r_file=fvar.read()

# yt = YouTube(r_file)
# print(r_file)
# try:
#     yt.streams.filter(progressive = True, 
# file_extension = "mp4").first().download(output_path = "F:\programming\python mini project", 
# filename = "video")
# except:
#     print("Some Error!")
# print('Task Completed!')