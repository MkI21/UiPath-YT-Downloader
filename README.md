# YouTube Audio Downloader – UiPath RPA Project

## Overview

This project is an RPA solution built with **UiPath** using the **REFramework** architecture.
It automates the process of retrieving music requests and downloading the corresponding audio files from YouTube as MP3s.

The solution is composed of three main parts:

1. **Dispatcher** – Collects and queues music requests.
2. **Performer (REFramework)** – Processes each request.
3. **Python Downloader** – Searches and downloads the audio using `yt-dlp`.

---

## Architecture

```
[Data Source]
      ↓
  Dispatcher
      ↓
   Orchestrator Queue
      ↓
 Performer (REFramework)
      ↓
 Python Downloader
      ↓
  C:\Music\Artist\Song.mp3
```

---

## Components

### 1. Dispatcher

The Dispatcher is responsible for:

* Retrieving data (Artist and Song).
* Creating queue items in **UiPath Orchestrator**.
* Each queue item contains:

  * `Artist`
  * `Song`

This ensures:

* Scalability.
* Centralized data management.
* Easy retry and monitoring.

---

### 2. Performer (REFramework)

The Performer is built using **UiPath REFramework**.

Its responsibilities:

* Retrieves queue items from Orchestrator.
* Extracts:

  * `Artist`
  * `Song`
* Calls the Python script using **Start Process**.
* Monitors execution.
* Marks the transaction as:

  * **Successful** if download completes.
  * **Failed** if an error occurs.

REFramework provides:

* Automatic retry logic.
* Structured exception handling.
* Logging and reporting.

---

### 3. Python Downloader

The Python script performs the actual download.

#### Responsibilities:

* Receives arguments:

  ```
  python script.py "Artist" "Song"
  ```
* Normalizes and sanitizes folder and file names.
* Checks if the artist folder already exists.
* Creates it if necessary.
* Searches YouTube using `yt-dlp`.
* Downloads the best audio.
* Converts it to MP3 using FFmpeg.

#### Output structure:

```
C:\Music\
   └── Artist Name\
         └── Song Name.mp3
```

---

## Technologies Used

* **UiPath Studio**
* **REFramework**
* **UiPath Orchestrator**
* **Python 3.13**
* **yt-dlp**
* **FFmpeg**

---

## Python Script Behavior

The script:

1. Reads command-line arguments (`Artist`, `Song`).
2. Sanitizes names to avoid invalid characters.
3. Checks for an existing artist folder.
4. Downloads audio from YouTube.
5. Converts it to MP3.
6. Saves it in the correct folder.

---

## UiPath Start Process Configuration

**FileName:**

```
C:\Program Files\Python313\python.exe
```

**Arguments:**

```vbnet
"""C:\Path\To\script.py"" """ & Artist & """ """ & Song & """"
```

This ensures:

* Proper handling of spaces in names.
* Correct argument passing to Python.

---

## Error Handling

Handled by REFramework:

* System exceptions (Python failure, process errors).
* Application exceptions (invalid data, download errors).
* Automatic retries for failed transactions.

---

## Prerequisites

Before running the project:

1. Install Python.
2. Install dependencies:

```
pip install yt-dlp
```

3. Download FFmpeg and note its path.
4. Update the `ffmpeg_location` in the Python script.
5. Ensure the `C:\Music` folder is accessible.

---

## How to Run

1. Run the **Dispatcher** to populate the queue.
2. Start the **Performer** (REFramework).
3. The robot will:

   * Process each queue item.
   * Download the corresponding song.
   * Store it in the correct artist folder.

---

## Example

Queue item:

```
Artist: Kendrick Lamar
Song: HUMBLE
```

Result:

```
C:\Music\Kendrick Lamar\HUMBLE.mp3
```

---

## Benefits of This Architecture

* Scalable and queue-based.
* Fault-tolerant with retries.
* Clean separation between data retrieval and processing.
* Easy to maintain and extend.

---

## Future Improvements

* Metadata tagging (ID3 tags).
* Duplicate song detection.
* Parallel processing with multiple robots.
* Support for playlists.


### about REFrameWork Template ###
**Robotic Enterprise Framework**

* Built on top of *Transactional Business Process* template
* Uses *State Machine* layout for the phases of automation project
* Offers high level logging, exception handling and recovery
* Keeps external settings in *Config.xlsx* file and Orchestrator assets
* Pulls credentials from Orchestrator assets and *Windows Credential Manager*
* Gets transaction data from Orchestrator queue and updates back status
* Takes screenshots in case of system exceptions

