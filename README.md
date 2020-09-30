# Audio Converter

The tool depends on FFmpeg to convert audio format

## Setup

1. Add executable permisssion for `start.sh`, `install.sh`
   - `chmod a+x start.sh`
   - `chmod a+x install.sh`
1. Run `install.sh`
1. Activite Virtual Env
   1. Mac: `source venv/bin/activate`
   1. Or Win32: `source venv/Scripts/activate`

## To get audio property

```bash
python3 demo.py
```

## Convert audio to .mp3

```bash
ffmpeg -i input/filename.arm output/filename-output.mp3
```

## [`brew`, `ffmpeg` install, `raw.githubusercontent.com port 443`](https://github.com/Jaylee89/installation-issues/blob/master/python.project.md)

## [ffmpeg doc](http://ffmpeg.org/ffmpeg.html) or https://ld246.com/article/1595480295489

or https://www.cnblogs.com/chen1987lei/archive/2010/12/03/1895242.html

## [learning courses from CSDN audio](https://edu.csdn.net/course/detail/2314)