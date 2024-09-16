# Music Player

## Description
This is an open-source music player built using CustomTkinter and Pygame. It allows users to play, pause, and navigate through a small playlist of songs. The player also displays album art for the songs being played.

## Features
- **Custom UI**: Built using CustomTkinter for a modern look and feel.
- **Play/Pause Support**: Allows you to play and pause songs.
- **Album Art Display**: Displays the album art of the current song.
- **Progress Bar**: Shows the progress of the song.
- **Multi-threading**: Uses threading to keep the UI responsive during song playback.

## Requirements
- Python 3.x
- Pygame: For handling audio playback.
- Pillow: For displaying images (album art).
- CustomTkinter: For building the custom user interface.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/music-player.git
    ```

2. Install the required libraries:

    ```bash
    pip install pygame pillow customtkinter
    ```

3. Add your audio files:

    - Place your `.mp3` files in a `songs` directory within the project folder.
    - Ensure that corresponding album art images are placed in an `img` folder.

## Usage
Run the script:

```bash
python mp.py
```
## Project Alocation Structure

```bash
.
├── img/
│   ├── unravel.png
│   ├── ssimg.jpg
│   ├── unlasting.jpeg
│   └── Call of Silence.jpeg
├── songs/
│   ├── Unravel Piano(Version).mp3
│   ├── Sudden Shower.mp3
│   ├── Unlasting.mp3
│   └── Call of Silence.mp3
└── mp.py
```
## Customization

You can modify the songs and playlist in mp.py to include your own songs and corresponding album art.

## License
This project is open-source and available under the MIT License.

## Contribution
Feel free to open issues or submit pull requests for any improvements or additional features.
