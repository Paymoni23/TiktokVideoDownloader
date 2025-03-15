### Installation

1. Install `yt-dlp` by running the following command:

   ```bash
   pip install yt-dlp
   ```
2. Make sure Python is installed on your system.
## Usage

1. Create a `.txt` file containing TikTok video URLs (one URL per line).

2. Run the Python script:

   ```bash
   python code.py
   ```

3. The script will prompt you to enter the path to the `.txt` file containing the TikTok links. Also remove **""**

4. Once the file is provided, the script will attempt to download the videos to the specified directory. By default, the videos will be saved to a folder named `downloads/` in the same location as the script. The filename will be the title of the video with the appropriate file extension.

5. After the download process completes, the script will print a summary, showing how many videos were successfully downloaded and which failed.
