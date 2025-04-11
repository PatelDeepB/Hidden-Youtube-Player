# YouTube Headless Script Controller

This Python script uses Selenium and Undetected ChromeDriver to control YouTube video playback in a headless browser. It allows you to play videos, skip ads, search and download videos, interact with the player, and control subtitles — all from the terminal.

## 🚀 Features

- Launches a headless, incognito YouTube session
- Automatically plays the first video from search results
- Interactive command menu:
  - Play/Pause, Next, Previous
  - Toggle Autoplay
  - Skip Ads, Search videos
  - Retrieve video URL, title, and length
  - Increase/Decrease playback speed
  - Take screenshot of currently playing video
  - Download video using pytube
  - Subtitle fetcher (WIP)
- Saves and loads Selenium session (optional)
- Multi-threaded video downloads

## 📦 Requirements

Install dependencies using the included `requirements.txt`:

```bash
pip install -r requirements.txt
```

You also need to have Chrome installed.

🛠 Usage

```bash
python3 play_headless.py
```

The script will search and play a predefined YouTube query. You can edit the `query` variable in the script to customize the search.

Once the video starts playing, a terminal prompt will offer you various commands to control playback and other features.

## 📁 Notes
- Default download location: `/home/pragnakalpl40/Downloads/`
- Make sure you have the correct permissions or change the path if needed
- Video download and subtitles rely on `pytube`, which might break due to YouTube changes
- ChromeDriver is managed using `undetected_chromedriver`

## ⚠️ Disclaimer
This tool is for educational purposes only. Use responsibly and respect YouTube's terms of service.

---

### 📦 `requirements.txt`

```txt
selenium
undetected-chromedriver
pytube
```