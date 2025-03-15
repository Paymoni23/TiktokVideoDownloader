import yt_dlp

def download_tiktok_video(urls, output_path='downloads/%(title)s.%(ext)s'):
    options = {
        'format': 'best',  # Get the best available quality
        'outtmpl': output_path,  # Save with the video title
    }
    
    success = []
    failed = []
    
    with yt_dlp.YoutubeDL(options) as ydl:
        for url in urls:
            try:
                ydl.download([url])
                success.append(url)
            except Exception as e:
                print(f"Failed to download: {url}\nError: {e}")
                failed.append(url)
    
    print("\nSummary:")
    print(f"Successfully downloaded: {len(success)} videos")
    for vid in success:
        print(f" - {vid}")
    print(f"Failed to download: {len(failed)} videos")
    for vid in failed:
        print(f" - {vid}")

def read_links_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines() if line.strip()]

if __name__ == "__main__":
    file_path = input("Enter the path to the .txt file with TikTok links: ")
    video_urls = read_links_from_file(file_path)
    if video_urls:
        download_tiktok_video(video_urls)
        print("\nDownload process completed!")
    else:
        print("No valid URLs found in the file.")
